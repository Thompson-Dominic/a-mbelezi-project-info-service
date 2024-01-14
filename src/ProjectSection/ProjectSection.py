import uuid
from src.SeedWork.BaseDomain import BaseDomain


class ProjectSection(BaseDomain):
    __sectionName = None
    __project_id = None
    __details = None


    def __init__(self, sectionName: str, project_id: uuid, details: str):
        """
        Initialize a new instance of the ProjectSection class.

        Args:
            sectionName (str): The name of the project section.
            project_id (int): The id of the project.
            details (str): The details of the project section.
        """
        self.__sectionName = sectionName
        self.__project_id = project_id
        self.__details = details

    # Getter, Setter and Deleter for sectionName
    @property
    def sectionName(self) -> str:
        """Get the section name of the project."""
        if self.__sectionName is None:
            raise AttributeError("section Name is not defined.")
        return self.__sectionName

    @sectionName.setter
    def sectionName(self, sectionName: str):
        """Set the section name of the project."""
        self.__sectionName = sectionName

    @sectionName.deleter
    def sectionName(self):
        """Delete the section name of the project."""
        del self.__sectionName
        


    # Getter, Setter and Deleter for project_id
    @property
    def project_id(self) -> uuid:
        """Get the project id."""
        if self.__project_id is None:
            raise AttributeError("project_id is not defined.")
        return self.__project_id

    @project_id.setter
    def project_id(self, project_id: uuid):
        """Set the project id."""
        self.__project_id = project_id

    @project_id.deleter
    def project_id(self):
        """Delete the project id."""
        del self.__project_id
 

    # Getter, Setter and Deleter for detials
    @property
    def details(self) -> str:
        """Get the details of the project section."""
        if self.__details is None:
            raise AttributeError("details is not defined.")
        return self.__details

    @details.setter
    def details(self, details: str):
        """Set the details of the project section."""
        self.__details = details

    @details.deleter
    def details(self):
        """Delete the details of the project section."""
        del self.__details