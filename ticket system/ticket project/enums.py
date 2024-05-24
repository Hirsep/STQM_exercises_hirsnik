from enum import IntEnum
from enum import Enum


class TicketPriority(IntEnum):
    SEVERE = 1
    SIGNIFICANT = 2
    AFFECTING = 3
    NON_CRITICAL = 4
    ROUTINE = 5


class TicketStatus(Enum):
    CREATED = "Created"
    IN_PROGRESS = "In progress"
    TESTING = "Testing"
    CLOSED = "Closed"


class OperatingSystems(Enum):
    WINDOWS = "Windows"
    MACOS = "macOS"
    LINUX = "Linux"
    ANDROID = "Android"
    IOS = "iOS"
