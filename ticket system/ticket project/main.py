import datetime
from enums import TicketPriority, OperatingSystems
from tickets import Ticket


if __name__ == "__main__":

    software_ticket = Ticket.create(
        ticket_type='software',
        description='App crashes on startup',
        priority=TicketPriority.SEVERE,
        error_message='Null pointer exception',
        operating_systems=[OperatingSystems.WINDOWS, OperatingSystems.MACOS]
    )
    software_ticket.add_comment("terrible app", "Peter", datetime.datetime.now())
    print(software_ticket, "\n")

    hardware_ticket = Ticket.create(
        ticket_type='hardware',
        description='Printer not working',
        priority=TicketPriority.SIGNIFICANT,
        component='Printer',
        serial_number=12345678,
        error_code='E404'
    )
    print(hardware_ticket, "\n")

    software_ticket2 = Ticket.create(
        ticket_type='software',
        description='App crashes on startup',
        priority=TicketPriority.SEVERE,
        error_message='Null pointer exception',
        operating_systems=[OperatingSystems.WINDOWS, OperatingSystems.MACOS]
    )
    print(software_ticket2, "\n")
