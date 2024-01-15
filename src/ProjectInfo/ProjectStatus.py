from enum import Enum

class ProjectStatus(Enum):
    """Enumeration of the status of a project."""
    NOT_STARTED = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    ON_HOLD = 4