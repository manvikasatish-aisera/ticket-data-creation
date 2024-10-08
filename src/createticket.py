import os
import csv
from urllib.parse import urlparse

from io import StringIO
from salesforce_bulk import SalesforceBulk
from salesforce_bulk import CsvDictsAdapter
from generatecontent import *

def read_tickets():
    ticket_info = generate_ticket_content()
    csv_file = StringIO(ticket_info)

    # Ensure the destination directory exists
    destination_directory = 'bulkupload'
    os.makedirs(destination_directory, exist_ok=True)

    # Save the CSV content to a file in the 'bulkupload' directory
    csv_file_path = os.path.join(destination_directory, 'ticket_info.csv')
    with open(csv_file_path, 'w') as file:
        file.write(csv_file.getvalue())

def bulk_upload():
    session_id = os.getenv("SESSION_ID")

    # session id and host work   
    bulk = SalesforceBulk(sessionId=session_id, host=urlparse('https://staging0-ticketai-dev-ed.lightning.force.com/').hostname)
    print("got here.")
    job = bulk.create_insert_job("ticket_info", contentType='CSV', concurrency='Parallel')
    
    # Read the CSV file from the 'bulkupload' directory
    csv_file_path = os.path.join('bulkupload', 'ticket_info.csv')

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        disbursals = [row for row in reader]

    csv_iter = CsvDictsAdapter(iter(disbursals))
    batch = bulk.post_bulk_batch(job, csv_iter)

    bulk.wait_for_batch(job, batch)
    bulk.close_job(job)
    print("Data successfully uploaded!")

# uncomment line below for full functionality, right now commented to test bulk upload login. 
#read_tickets()
bulk_upload()
