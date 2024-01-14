from datetime import datetime

from src.SeedWork.BaseDomain import BaseDomain
from . import ProjectStatus

class ProjectInfo(BaseDomain):
    """ This class models basic information about a project"""

    __name = None
    __description = None
    __timeline_in_weeks = None
    __budget = None
    __budget_currency = None
    __approved_date = None
    __project_classification_id = None
    __locality_id = None
    __community = None
    __projectStatus = None

    def __init__(self, name: str, description: str, timeline_in_weeks: int, budget: float, 
                 budget_currency: str, approved_date: datetime, project_classification_id: int = None, 
                 locality_id: int = None, community: str = None):
        self.__name = name
        self.__description = description
        self.__timeline_in_weeks = timeline_in_weeks
        self.__budget = budget
        self.__budget_currency = budget_currency
        self.__approved_date = approved_date
        self.__project_classification_id = project_classification_id
        self.__locality_id = locality_id
        self.__community = community
        self.__projectStatus = ProjectStatus.ProjectStatus.NOT_STARTED

    # Getter, Setter and Deleter for name
    @property
    def name(self) -> str:
        """Get the name of the project."""
        if self.__name is None:
            raise AttributeError("name is not defined.")
        return self.__name

    @name.setter
    def name(self, name: str):
        """Set the name of the project."""
        self.__name = name

    @name.deleter
    def name(self):
        """Delete the name of the project."""
        del self.__name
    
        # Getter, Setter and Deleter for description
    @property
    def description(self) -> str:
        """Get the description of the project."""
        if self.__description is None:
            raise AttributeError("description is not defined.")
        return self.__description

    @description.setter
    def description(self, description: str):
        """Set the description of the project."""
        self.__description = description

    @description.deleter
    def description(self):
        """Delete the description of the project."""
        del self.__description

    # Getter, Setter and Deleter for timeline_in_weeks
    @property
    def timeline_in_weeks(self) -> int:
        """Get the timeline of the project in weeks."""
        if self.__timeline_in_weeks is None:
            raise AttributeError("timeline_in_weeks is not defined.")
        return self.__timeline_in_weeks

    @timeline_in_weeks.setter
    def timeline_in_weeks(self, timeline_in_weeks: int):
        """Set the timeline of the project in weeks."""
        self.__timeline_in_weeks = timeline_in_weeks

    @timeline_in_weeks.deleter
    def timeline_in_weeks(self):
        """Delete the timeline of the project."""  
        del self.__timeline_in_weeks
    
    # Getter, Setter and Deleter for budget
    @property
    def budget(self) -> float:
        """Get the budget of the project."""
        if self.__budget is None:
            raise AttributeError("budget is not defined.")
        return self.__budget

    @budget.setter
    def budget(self, budget: float):
        """Set the budget of the project."""
        self.__budget = budget

    @budget.deleter
    def budget(self):
        """Delete the budget of the project."""
        del self.__budget

    # Getter, Setter and Deleter for budget_currency
    @property
    def budget_currency(self) -> str:
        """Get the currency of the project's budget."""
        if self.__budget_currency is None:
            raise AttributeError("budget_currency is not defined.")
        return self.__budget_currency

    @budget_currency.setter
    def budget_currency(self, budget_currency: str):
        """Set the currency of the project's budget."""
        self.__budget_currency = budget_currency

    @budget_currency.deleter
    def budget_currency(self):
        """Delete the currency of the project's budget."""
        del self.__budget_currency

    # Getter, Setter and Deleter for approved_date
    @property
    def approved_date(self) -> datetime:
        """Get the approved date of the project."""
        if self.__approved_date is None:
            raise AttributeError("approved_date is not defined.")
        return self.__approved_date

    @approved_date.setter
    def approved_date(self, approved_date: datetime):
        """Set the approved date of the project."""
        self.__approved_date = approved_date

    @approved_date.deleter
    def approved_date(self):
        """Delete the approved date of the project."""
        del self.__approved_date

    # Getter, Setter and Deleter for project_classification_id
    @property
    def project_classification_id(self) -> int:
        """Get the classification id of the project."""
        if self.__project_classification_id is None:
            raise AttributeError("project_classification_id is not defined.")
        return self.__project_classification_id

    @project_classification_id.setter
    def project_classification_id(self, project_classification_id: int):
        """Set the classification id of the project."""
        self.__project_classification_id = project_classification_id

    @project_classification_id.deleter
    def project_classification_id(self):
        """Delete the classification id of the project."""
        del self.__project_classification_id

    # Getter, Setter and Deleter for locality_id
    @property
    def locality_id(self) -> int:
        """Get the locality id of the project."""
        if self.__locality_id is None:
            raise AttributeError("locality_id is not defined.")
        return self.__locality_id

    @locality_id.setter
    def locality_id(self, locality_id: int):
        """Set the locality id of the project."""
        self.__locality_id = locality_id

    @locality_id.deleter
    def locality_id(self):
        """Delete the locality id of the project."""
        del self.__locality_id

    # Getter, Setter and Deleter for community
    @property
    def community(self) -> str:
        """Get the community of the project."""
        if self.__community is None:
            raise AttributeError("community is not defined.")
        return self.__community

    @community.setter
    def community(self, community: str):
        """Set the community of the project."""
        self.__community = community

    @community.deleter
    def community(self):
        """Delete the community of the project."""
        del self.__community
        
    
    # Getter and Setter for projectStatus
    @property
    def projectStatus(self) -> ProjectStatus:
        """Get the status of the project."""
        return self.__projectStatus

    @projectStatus.setter
    def projectStatus(self, projectStatus: ProjectStatus):
        """Set the status of the project."""
        self.__projectStatus = projectStatus