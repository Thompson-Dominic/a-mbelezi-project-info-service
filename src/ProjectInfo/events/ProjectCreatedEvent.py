import uuid
from ...SeedWork.DomainEvent import DomainEvent


class ProjectCreatedEvent(DomainEvent):
    """Event for when a project is created."""
    def __init__(self, project_id: uuid, project_name: str):
        self.project_id = project_id
        self.project_name = project_name

    def __str__(self):
        return f"ProjectCreatedEvent(project_id={self.project_id}, project_name={self.project_name}"