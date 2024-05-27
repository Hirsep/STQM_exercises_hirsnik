import datetime
from enums import TicketPriority, OperatingSystems
from tickets import Ticket
from teams import Team, Assignments


if __name__ == "__main__":

    software_ticket = Ticket.create(
        ticket_type='software',
        description='App crashes on startup',
        priority=TicketPriority.SEVERE,
        error_message='Null pointer exception',
        operating_systems=[OperatingSystems.WINDOWS, OperatingSystems.MACOS]
    )
    software_ticket.add_comment("terrible app", "Peter", datetime.datetime.now())

    hardware_ticket = Ticket.create(
        ticket_type='hardware',
        description='Printer not working',
        priority=TicketPriority.SIGNIFICANT,
        component='Printer',
        serial_number=12345678,
        error_code='E404'
    )
    hardware_ticket.add_comment("printers never work", "Georg", datetime.datetime.now())

    software_ticket2 = Ticket.create(
        ticket_type='software',
        description='App crashes on startup',
        priority=TicketPriority.SEVERE,
        error_message='Null pointer exception',
        operating_systems=[OperatingSystems.WINDOWS, OperatingSystems.MACOS]
    )

    team1 = Team("Team 1", "Peter", "Petar")
    team2 = Team("Team 2", "Oliver", "Hooman")
    assignments = Assignments()
    assignments.add(team1, software_ticket)
    assignments.add(team1, hardware_ticket)
    assignments.add(team2, software_ticket2)
    print(f"All assignments:\n\n{assignments}")
