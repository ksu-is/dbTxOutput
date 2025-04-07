# dbTxOutput
Working code for exporting an database transaction audit table to JSON object for import into a log aggregation tool

## Project Overview
This project is a Python-based rewrite of a Bash script used to export transaction audit data from an Oracle database and convert it into JSON logs. These logs are picked up by the NewRelic Infrastructure Agent (`logging.d`) to enable real-time monitoring and alerting on Oracle Integration Cloud (OIC) activity.

# Oracle Driver for Python
This will use oracleDB module for connectivity (more info here:  https://oracle.github.io/python-oracledb/samples/tutorial/Python-and-Oracle-Database-The-New-Wave-of-Scripting.html )

## Oracle Database Version used for testing
- https://www.oracle.com/database/technologies/xe-downloads.html
- Installed locally on Development Machine
- After project completion will migrate to corp environment for testing against 'real' dev env
- Will mock up test data to be obfuscated from anything 'real'

# Use Case
Oracle Cloud Integration platform that writes transaction details to an Oracle database in near-real-time.  We need to export this data rapidly to .json format in order for NewRelic infrastructure agent to pick up the data as a log file.  This enables dashboarding and alerting based on transaction activity and success/error codes in the log. The current implementation is written in Linux Bash shell.  Due to some issues with atomic writes and instability we want to do a proof of concept of basic functionality using Python with the OracleDB Module.

## Required JSON Output Data Format
### Note the timestamp format is EPOCH in Milliseconds
Sample output format:
```json
{
    "checkpoint_id": 59565369,
    "timestamp": "1731509692413",
    "insert_timestamp": "2024-11-13T09:54:52.413000",
    "source": "SRCAPP",
    "target": "EBS",
    "interface_name": "OrderCreateService",
    "interface_id": "00505511",
    "instance_id": "oIFJoek5HPEe-EQr8eLLWoFg",
    "clientTransactionId": "ac8afa8-2defd-26f7-8d43-13fd7ac4b55c",
    "status": "EBS_RESPONSE",
    "future_use1": null,
    "future_use2": null,
    "resp_code": "200",
    "resp_msg": "SUCCESS",
    "msg_source": "EBS SQL query"
}
```
Note: DB headers all match, except instance_id2, which is being sent as "clientTransactionId". This correlates to the clientTransactionId being sent from CCI for Wireless Integrations.

### Oracle Query to embed in the script (this logic has already been worked out, no need to re-engineer)
QUERY="SELECT json_object ('checkpoint_id' VALUE ID, 'timestamp' VALUE TO_CHAR((CAST(FROM_TZ(TO_TIMESTAMP(INSERT_TIMESTAMP, 'DD-MON-RR HH.MI.SSXFF AM'), 'America/New_York') AT TIME ZONE 'UTC' AS DATE) - TO_DATE('1970-01-01', 'YYYY-MM-DD')) * 86400 * 1000 + TO_NUMBER(TO_CHAR(TO_TIMESTAMP(INSERT_TIMESTAMP, 'DD-MON-RR HH.MI.SSXFF AM'), 'FF3'))), 'insert_timestamp' VALUE INSERT_TIMESTAMP, 'source' VALUE SOURCE, 'target' VALUE TARGET, 'interface_name' VALUE INTERFACE_NAME, 'interface_id' VALUE INTERFACE_ID, 'instance_id' VALUE INSTANCE_ID, 'clientTransactionId' VALUE INSTANCE_ID2, 'status' VALUE STATUS, 'future_use1' VALUE FUTURE_USE1, 'future_use2' VALUE FUTURE_USE2, 'resp_code' VALUE RESP_CODE, 'resp_msg' VALUE RESP_MSG, 'msg_source' VALUE MSG_SOURCE) AS formatted_values FROM ksu_custom.oic_tx WHERE INSERT_TIMESTAMP IS NOT null AND ID > $LAST_ID;"

# Requirements
## 1. Original Bash Implementation
Two bash scripts that orchestrate data retrieval and formatting from OIC Audit (in CEIPODS) to JSON format. NewRelic logging agent picks up this data and publishes to NewRelic logs as oicdbimportjson.log for production and staging.  (NOTE:  THIS IS WORKING)

### Directory Structure
- Json Data and checkpoint_id: `/home/<user>/nr_import/`
- Scripts: `/home/<user>/nr_import/scripts/`
- Logs: `/home/<user>/nr_import/scripts/log/`

### Scripts
- `oic_db_import_json.sh`: Retrieves and formats data from OIC Audit
- `run_table_import_json.sh`: Orchestrates the data export process

### Cron Setup
```bash
* * * * * /home/<user>/nr_import/scripts/run_table_import_json.sh
```
### Important Files
- `checkpoint_id`: Tracks the most recent record pulled from OIC Audit table
- `outputfile.json`: Contains the exported data, should be rotated hourly

## Python POC Alternative

