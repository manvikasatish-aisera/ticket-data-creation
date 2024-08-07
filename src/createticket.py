from generatecontent import *
import csv
from io import StringIO

def read_tickets():
    ticket_info = generate_ticket_content()
    csv_file = StringIO(ticket_info)
    reader = csv.DictReader(csv_file)

    tickets = list(reader)

    for ticket in tickets:
        print("_______________________________")
        print(ticket)

read_tickets()