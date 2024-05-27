import json
from tickets import Ticket


def save_tickets(tickets, filename="ticket-log.json"):
    ticket_dict = [ticket.to_dict() for ticket in tickets]
    with open(filename, "w") as file:
        json.dump(ticket_dict, file, indent=4)
