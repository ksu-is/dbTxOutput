#!/usr/bin/env python3
## OIC Audit Export Script
## Basic structure for Oracle Integration Cloud audit data export.

import oracledb

# Oracle DB Connection Parameters
# TODO: Replace these placeholders with actual connection details
DB_USERNAME = "your_username"
DB_PASSWORD = "your_password"
DB_DSN = "localhost:1521/XEPDB1"  # Format: host:port/service_name

def get_checkpoint():
    ## Read the last checkpoint ID from file (this will be manual at start then we add
    ## logic to read subsequent checkpoints from the last record in either the fetch_audit_data
    ## or export_data function
    ## Returns:
        ## int: The last processed ID or 0 if no checkpoint exists
    try:
        with open("checkpoint_py", "r") as checkpoint_file:
            last_id = checkpoint_file.read().strip()
            return int(last_id) if last_id else 0
    except FileNotFoundError:
        print("Checkpoint file not found. Starting from ID 0.")
        return 0
    except (ValueError, IOError) as e:
        print(f"Error reading checkpoint file: {e}")
        return 0

def fetch_audit_data(last_id):
    ##Fetch audit data from database using original query with timestamp logic.
    ##Args:
    ##last_id (int): ID to start fetching from
    ##Returns:
    ##list: List of JSON strings representing records
    
    # The query to fetch audit data with JSON formatting directly from the database
    query = """
    SELECT json_object (
        'checkpoint_id' VALUE ID, 
        'timestamp' VALUE TO_CHAR((CAST(FROM_TZ(TO_TIMESTAMP(INSERT_TIMESTAMP, 'DD-MON-RR HH.MI.SSXFF AM'), 'America/New_York') AT TIME ZONE 'UTC' AS DATE) - TO_DATE('1970-01-01', 'YYYY-MM-DD')) * 86400 * 1000 + TO_NUMBER(TO_CHAR(TO_TIMESTAMP(INSERT_TIMESTAMP, 'DD-MON-RR HH.MI.SSXFF AM'), 'FF3'))), 
        'insert_timestamp' VALUE INSERT_TIMESTAMP, 
        'source' VALUE SOURCE, 
        'target' VALUE TARGET, 
        'interface_name' VALUE INTERFACE_NAME, 
        'status' VALUE STATUS, 
        'resp_code' VALUE RESP_CODE, 
        'resp_msg' VALUE RESP_MSG,
        'env' VALUE 'pythondev'
    ) AS formatted_values 
    FROM audit 
    WHERE INSERT_TIMESTAMP IS NOT null 
    AND ID > :last_id
    """
    
    try:
        # Establish connection to Oracle database
        connection = oracledb.connect(
            user=DB_USERNAME,
            password=DB_PASSWORD,
            dsn=DB_DSN
        )
        
        # Create a cursor
        cursor = connection.cursor()
        
        # Execute the query with the last_id parameter
        cursor.execute(query, last_id=last_id)
        
        # Fetch all results
        results = cursor.fetchall()
        
        # Extract the JSON strings from the results
        records = [row[0] for row in results]
        
        print(f"Retrieved {len(records)} records from the database")
        
        # Close cursor and connection
        cursor.close()
        connection.close()
        
        return records
        
    except oracledb.Error as error:
        print(f"Oracle Database Error: {error}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def export_data(records):
    ##Export JSON records to file.
    ## records (list): List of JSON strings to export
    if not records:
        print("No records to export")
        return False
    
    import os
    import json
    import tempfile
    
    output_file = "outputfile.json"
    
    try:
        # Create a temporary file in the same directory
        temp_dir = os.path.dirname(os.path.abspath(output_file)) or "."
        fd, temp_path = tempfile.mkstemp(dir=temp_dir)
        
        # Write records to the temporary file
        with os.fdopen(fd, 'w') as temp_file:
            for record in records:
                # Write each record as a separate line in the JSON file
                temp_file.write(record + '\n')
        
        # Atomically replace the output file with the temporary file
        # This prevents file corruption if the process is interrupted
        os.replace(temp_path, output_file)
        
        print(f"Successfully exported {len(records)} records to {output_file}")
        return True
        
    except Exception as e:
        print(f"Error exporting data: {e}")
        # Clean up the temporary file if it exists
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.remove(temp_path)
        return False

def set_new_checkpoint(records):
    ## read the LAST ID from the records export list (if exists) and write to checkpoint file
    ### IMPORTANT this is completed AFTER records export is successful
    if not records:
        print("No records to update checkpoint")
        return None
    
    import os
    import json
    import tempfile
    
    try:
        # Get the last record
        last_record = records[-1]
        
        # Parse the JSON string to extract the checkpoint_id
        record_data = json.loads(last_record)
        new_id = record_data.get('checkpoint_id')
        
        if not new_id:
            print("Could not find checkpoint_id in the last record")
            return None
        
        # Atomic write to checkpoint file
        checkpoint_file = "checkpoint_py"
        
        # Create a temporary file in the same directory
        temp_dir = os.path.dirname(os.path.abspath(checkpoint_file)) or "."
        fd, temp_path = tempfile.mkstemp(dir=temp_dir)
        
        # Write the new checkpoint ID to the temporary file
        with os.fdopen(fd, 'w') as temp_file:
            temp_file.write(str(new_id))
        
        # Atomically replace the checkpoint file with the temporary file
        os.replace(temp_path, checkpoint_file)
        
        print(f"Updated checkpoint to ID: {new_id}")
        return new_id
        
    except Exception as e:
        print(f"Error updating checkpoint: {e}")
        # Clean up the temporary file if it exists
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.remove(temp_path)
        return None

def main():
    ## Main execution flow.
    print("Starting OIC Audit Export")
    
    # 1. Read checkpoint
    last_id = get_checkpoint()
    print(f"Using checkpoint: {last_id}")
    
    # 2. Fetch data
    records = fetch_audit_data(last_id)
    
    # 3. Export data
    if records:
        export_data(records)
        set_new_checkpoint(records) ## this may not work if the list is empty ##
        print(f"Exported {len(records)} records")
    else:
        print("No records to export")
    
    print("Export completed")

# guard to allow code to be imported without running in another script
if __name__ == "__main__":
    main()
