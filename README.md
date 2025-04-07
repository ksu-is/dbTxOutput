# dbTxOutput
Working code for exporting an database transaction audit table to JSON object for import into a log aggregation tool

# Oracle Driver for Python
This will use oracleDB module for connectivity (more info here:  https://oracle.github.io/python-oracledb/samples/tutorial/Python-and-Oracle-Database-The-New-Wave-of-Scripting.html )

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

