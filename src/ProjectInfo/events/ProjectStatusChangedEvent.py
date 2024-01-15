from ...SeedWork.DomainEvent import DomainEvent


class ProjectStatusChangedEvent(DomainEvent):
    """Event for when a project's status is changed."""
    def __init__(self, project_id, status):
        self.project_id = project_id
        self.status = status