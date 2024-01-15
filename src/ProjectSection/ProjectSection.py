""" This module contains the basic models for the project info """
import uuid
from src.SeedWork.BaseDomain import BaseDomain


class ProjectSection(BaseDomain):
    """ This class models basic information about a project section"""
    __section_name = None
    __project_id = None
    __details = None


    def __init__(self, section_name: str, project_id: uuid, details: str, project_section_id: uuid = None):
        """
        Initialize a new instance of the ProjectSection class.

        Args:
            section_name (str): The name of the project section.
            project_id (int): The id of the project.
            details (str): The details of the project section.
        """
        self.__section_name = section_name
        self.__project_id = project_id
        self.__details = details
        super().__init__(project_section_id)
        if self.is_transient():
            self.generate_id()

    # Getter, Setter and Deleter for section_name
    @property
    def section_name(self) -> str:
        """Get the section name of the project."""
        if self.__section_name is None:
            raise AttributeError("section Name is not defined.")
        return self.__section_name

    @section_name.setter
    def section_name(self, section_name: str):
        """Set the section name of the project."""
        self.__section_name = section_name

    @section_name.deleter
    def section_name(self):
        """Delete the section name of the project."""
        del self.__section_name
        


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