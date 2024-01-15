""" ProjectInfoPersistCommand module."""
import datetime
import uuid


class ProjectInfoPersistCommand:
    """Command for persisting a project info."""
    def __init__(self, name: str, description: str, timeline_in_weeks: int, budget: float, 
                 budget_currency: str, approved_date: datetime, project_classification_id: int = None, 
                 locality_id: int = None, community: str = None, project_id:uuid = None):
        """ Initialize a new instance of the ProjectInfoPersistCommand class.
        
        Args:
        
            name (str): The name of the project.
            description (str): The description of the project.
            timeline_in_weeks (int): The timeline of the project in weeks.
            budget (float): The budget of the project.
            budget_currency (str): The currency of the project's budget.   
            approved_date (datetime): The approved date of the project.
            project_classification_id (int): The classification id of the project.
            locality_id (int): The locality id of the project.
            community (str): The community of the project.
            id (uuid): The id of the project.
                
        """
        self.name = name
        self.description = description
        self.timeline_in_weeks = timeline_in_weeks
        self.budget = budget
        self.budget_currency = budget_currency
        self.approved_date = approved_date
        self.project_classification_id = project_classification_id
        self.locality_id = locality_id
        self.community = community
        self.project_id = project_id