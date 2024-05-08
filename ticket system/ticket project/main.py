import create_ticket
from tabulate import tabulate

creator = create_ticket.CreateTicket()
tickets = []

num_tickets = int(input("How many tickets do you want to create? "))

for _ in range(num_tickets):
    ticket = creator.create_ticket()
    tickets.append(ticket)

tickets_data = []
for ticket in tickets:
    tickets_data.append([ticket.ticket_id, ticket.ticket_title, ticket.ticket_status, ticket.ticket_agent, ticket.ticket_priority, ticket.ticket_date])

headers = ["ID", "Title", "Status", "Agent", "Priority", "Creation Date"]

table = tabulate(tickets_data, headers=headers, tablefmt="fancy_grid")

print(table)
