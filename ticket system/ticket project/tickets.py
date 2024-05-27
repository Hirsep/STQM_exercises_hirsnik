from datetime import datetime
from enums import TicketPriority, TicketStatus


class Ticket:

    tickets = []

    def __init__(self, description: str, priority: TicketPriority, status: TicketStatus = TicketStatus.CREATED):
        self.description = description
        self.priority = priority
        self.status = status
        self.time = datetime.now().strftime("%d/%m/%y")
        self.comments = []
        Ticket.tickets.append(self)

    def __str__(self):
        return f"Description: {self.description} \
                 Priority: {self.priority} \
                 Status: {self.status} \
                 Time: {self.time} \
                 Comments: {self.comments}"

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            'description': self.description,
            'priority': self.priority.name,
            'status': self.status.value,
            'time': self.time,
            'comments': [
                {'text': comment[0], 'user': comment[1], 'timestamp': comment[2].strftime('%d/%m/%y %H:%M:%S')}
                for comment in self.comments
            ]
        }

    def add_comment(self, text: str, user: str, timestamp: datetime):
        self.comments.append((text, user, timestamp))

    @classmethod
    def create(cls, ticket_type: str, description: str, priority: TicketPriority, **kwargs):
        if ticket_type.lower() == 'software':
            error_message = kwargs.get('error_message')
            operating_systems = kwargs.get('operating_systems')
            if not error_message or not operating_systems:
                raise ValueError("Error message and operating systems are required for software tickets.")
            return SoftwareTicket(description, priority, error_message, operating_systems)
        elif ticket_type.lower() == 'hardware':
            component = kwargs.get('component')
            serial_number = kwargs.get('serial_number')
            error_code = kwargs.get('error_code')
            if not component or serial_number is None:
                raise ValueError("Component and serial number are required for hardware tickets.")
            return HardwareTicket(description, priority, component, serial_number, error_code)
        else:
            raise ValueError("Invalid ticket type. Choose 'software' or 'hardware'.")


class HardwareTicket(Ticket):
    hardware_ticket_id_counter = 200000

    def __init__(self, description: str, priority: TicketPriority, component: str, serial_number: int, error_code: str):
        super().__init__(description, priority)
        self.id = HardwareTicket.hardware_ticket_id_counter
        HardwareTicket.hardware_ticket_id_counter += 1
        self.component = component
        self.serial_number = serial_number
        self.error_code = error_code

    def __str__(self):
        error_code_str = self.error_code if self.error_code else "N/A"
        comments_str = "\n".join(
            [f"{comment[1]}, {comment[2].strftime('%m/%d/%y %H:%M:%S')}: {comment[0]}" for comment in self.comments])
        hardware_info = (
            f"Hardware Ticket ID - {self.id}: {self.description}\n"
            f"Created {self.time} - {self.priority.name}\n"
            f"Component: {self.component}, s/n: {self.serial_number}, error code: {error_code_str}\n" 
            f"Comments: {comments_str if comments_str else 'No comments'}\n"
        )
        return f"{hardware_info}"

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        ticket_dict = super().to_dict()
        ticket_dict.update({
            'hardware_ticket_id': self.id,
            'component': self.component,
            'serial_number': self.serial_number,
            'error_code': self.error_code
        })
        return ticket_dict


class SoftwareTicket(Ticket):
    software_ticket_id_counter = 100000

    def __init__(self, description: str, priority: TicketPriority, error_message: str, operating_systems: list):
        super().__init__(description, priority)
        self.id = SoftwareTicket.software_ticket_id_counter
        SoftwareTicket.software_ticket_id_counter += 1
        self.error_message = error_message
        self.operating_systems = operating_systems

    def __str__(self):
        os_str = ", ".join([os.value for os in self.operating_systems])
        comments_str = "\n".join(
            [f"{comment[1]}, {comment[2].strftime('%m/%d/%y %H:%M:%S')}: {comment[0]}" for comment in self.comments])
        software_info = (
            f"Software Ticket ID - {self.id}: {self.description}\n"
            f"Created {self.time} - {self.priority.name}\n"
            f"Error message: {self.error_message}, Affected OSs: {os_str}\n"
            f"Comments: {comments_str if comments_str else 'No comments'}\n"
        )
        return f"{software_info}"

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        ticket_dict = super().to_dict()
        ticket_dict.update({
            'software_ticket_id': self.id,
            'error_message': self.error_message,
            'operating_systems': [os.value for os in self.operating_systems]
        })
        return ticket_dict
