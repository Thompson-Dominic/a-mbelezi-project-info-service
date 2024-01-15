""" Interface for ProjectInfoRepository """

from abc import ABC, abstractmethod
from typing import List
import uuid
from .ProjectInfo import ProjectInfo

class ProjectInfoRepository(ABC):
    """ Interface for ProjectInfoRepository"""
    @abstractmethod
    def get_project_info(self, project_id: str) -> ProjectInfo:
        """Get the project info of the project."""

    @abstractmethod
    def get_all_project_info(self) -> List[ProjectInfo]:
        """Get all the project info."""

    @abstractmethod
    def create_project_info(self, project_info: ProjectInfo) -> uuid:
        """Create the project info."""

    @abstractmethod
    def update_project_info(self, project_id: str, project_info: ProjectInfo) -> bool:
        """ Update the project info."""

    @abstractmethod
    def delete_project_info(self, project_id: str) -> bool:
        """ Delete the project info."""
