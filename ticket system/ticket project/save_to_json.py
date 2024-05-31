import json


def write_json(tickets, filename="ticket-log.json"):
    ticket_dict = [ticket.as_dict() for ticket in tickets]
    with open(filename, "w") as file:
        json.dump(ticket_dict, file, indent=4)


def read_json(file_name="ticket-log.json"):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data
