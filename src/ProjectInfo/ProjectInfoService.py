"""Core service for project info."""
import uuid
import logging

from src.ProjectInfo.ProjectInfo import ProjectInfo
from src.ProjectInfo.ProjectInfoRepository import ProjectInfoRepository
from src.ProjectInfo.models.BasicProjectInfoModels import ProjectInfoBasicModel, ProjectInfoDetailModel
from src.ProjectInfo.models.ProjectInfoPersistCommand import ProjectInfoPersistCommand
from src.ProjectInfoServiceException import ProjectInfoServiceException


class ProjectInfoService:
    """ Core service for project info."""
    # __dispatcher = None
    __repository = None
    __logger = None

    def __init__(self, config, repository:ProjectInfoRepository):
        """ Initialize a new instance of CoreService class."""
        # self.config = config
        if repository is None:
            raise ProjectInfoServiceException("Project Info Repository is required.")
        # default configurations
        self.__repository = repository
        
        if config is None:
            self.__logger = logging.getLogger() if config.logger is None else config.logger

    def get_basic_project_info(self, project_id: uuid):
        """Get the basic project info."""
        try:
            self.__logger.info("Get the basic project info- %s", project_id)
            project_info = self.__repository.get_project_info(project_id)
            if project_info is None:
                self.__logger.info("Project not found- %s", project_id)
                return None
            self.__logger.info("Project found-%s", project_id)
            return ProjectInfoService.project_info_to_basic(project_info).to_dict()
        except Exception as e:
            self.__logger.error("Project not found-%s", e)
            raise e
    
    def get_detailed_project_info(self, projectid: uuid):
        """Get the detailed project info."""
        try:
            self.__logger.info("Get the detailed project info- %s", projectid)
            project_info = self.__repository.get_project_info(projectid)
            if project_info is None:
                self.__logger.info("Project not found- %s", projectid)
                return None
            self.__logger.info("Project found-%s", projectid)
            return ProjectInfoService.project_info_to_details(project_info).to_dict()
        except Exception as e:
            self.__logger.error("Project not found- %s", e)
            raise e

    def get_all_projects_info(self):
        """Get all the projects info."""
        
        try:
            self.__logger.info("Get all the project info")
            project_infos = self.__repository.get_all_project_info()
            if project_infos is None:
                self.__logger.info("Projects not found")
                return None
            self.__logger.info("Projects found")
            return [ ProjectInfoService.project_info_to_basic(project).to_dict() for project in project_infos]
        except Exception as e:
            self.__logger.error("Projects not found-%s", e)
            raise e
    
    def add_project_info(self, command: ProjectInfoPersistCommand):
        """Add a new project info."""
        
        try:
            self.__logger.info("Add a new project info")
            project_info = self.persist_command_to_project_info(command)
            self.__repository.add_project_info(project_info)
            self.__logger.info("Project %s added", project_info.get_id())
        except Exception as e:
            self.__logger.error("Project not added- %s", e)
            raise e
    
    def update_project_info(self, command: ProjectInfoPersistCommand):
        """Update the project info."""
        try:
            self.__logger.info("Update the project info %s", command.id)
            project_info = self.__repository.get_project_info(command.id)
            if project_info is None:
                self.__logger.info("Project not found-%s", command.id)
                raise ProjectInfoServiceException("Project not found.")
            self.__repository.update_project_info(project_info)
            self.__logger.info("Project %s updated", command.id)
        except Exception as e:
            self.__logger.error("Project not updated-%s", e)
            raise e
        
    @classmethod
    def project_info_to_basic(cls, project_info: ProjectInfo):
        """ Convert project info to basic project info."""
        return  ProjectInfoBasicModel(project_id= project_info.get_id(), **project_info)

    @classmethod
    def project_info_to_details(cls, project_info: ProjectInfo):
        """ Convert project info to detailed project info."""
        return  ProjectInfoDetailModel(project_id= project_info.get_id(), **project_info)
    
    def persist_command_to_project_info(self, project_info: ProjectInfoPersistCommand):
        """ Convert project info to project info model."""
        return ProjectInfo(**project_info)