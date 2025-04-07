# dbTxOutput
Working code for exporting an database transaction audit table to JSON object for import into a log aggregation tool

# Oracle Driver for Python
This will use oracleDB module for connectivity (more info here:  https://oracle.github.io/python-oracledb/samples/tutorial/Python-and-Oracle-Database-The-New-Wave-of-Scripting.html )

# Use Case
Oracle Cloud Integration platform that writes transaction details to an Oracle database in near-real-time.  We need to export this data rapidly to .json format in order for NewRelic infrastructure agent to pick up the data as a log file.  This enables dashboarding and alerting based on transaction activity and success/error codes in the log.

# Requirements
The current implementation is written in Linux Bash shell.  Due to some issues with atomic writes and instability we want to do a proof of concept of basic functionality using Python with the OracleDB Module.
