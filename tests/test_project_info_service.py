import unittest
from unittest.mock import Mock, patch
from uuid import uuid4
from src.ProjectInfo.ProjectInfoRepository import ProjectInfoRepository
from src.ProjectInfoServiceException import ProjectInfoServiceException
from src.ProjectInfo.ProjectInfoService import ProjectInfoService
from src.ProjectInfo.models.ProjectInfoPersistCommand import ProjectInfoPersistCommand

class TestProjectInfoService(unittest.TestCase):
    """Unit tests for the ProjectInfoService class."""

    def setUp(self):
        """Set up test fixtures."""
        self.mock_repository = Mock(spec=ProjectInfoRepository)
        self.config = Mock()
        self.config.logger = None
        self.core_service = ProjectInfoService(self.config, self.mock_repository)

    def test_init_with_no_repository(self):
        """Test that the constructor raises an exception when no repository is provided."""
        with self.assertRaises(ProjectInfoServiceException):
            ProjectInfoService(self.config, None)

    def test_get_basic_project_info(self):
        """Test the get_basic_project_info method."""
        mock_project_id = uuid4()
        self.mock_repository.get_project_info.return_value = None
        result = self.core_service.get_basic_project_info(mock_project_id)
        self.assertIsNone(result)

    def test_get_detailed_project_info(self):
        """Test the get_detailed_project_info method."""
        mock_project_id = uuid4()
        self.mock_repository.get_project_info.return_value = None
        result = self.core_service.get_detailed_project_info(mock_project_id)
        self.assertIsNone(result)

    def test_get_all_projects_info(self):
        """Test the get_all_projects_info method."""
        self.mock_repository.get_all_project_info.return_value = None
        result = self.core_service.get_all_projects_info()
        self.assertIsNone(result)

    @patch('src.ProjectInfoService.ProjectInfoService.persist_command_to_project_info')
    def test_add_project_info(self, mock_persist_command_to_project_info):
        """Test the add_project_info method."""
        mock_command = Mock(spec=ProjectInfoPersistCommand)
        mock_persist_command_to_project_info.return_value = None
        self.core_service.add_project_info(mock_command)
        self.mock_repository.add_project_info.assert_called_once()

    @patch('src.ProjectInfoService.ProjectInfoService.persist_command_to_project_info')
    def test_update_project_info(self, mock_persist_command_to_project_info):
        """Test the update_project_info method."""
        mock_command = Mock(spec=ProjectInfoPersistCommand)
        mock_persist_command_to_project_info.return_value = None
        self.mock_repository.get_project_info.return_value = None
        with self.assertRaises(ProjectInfoServiceException):
            self.core_service.update_project_info(mock_command)

if __name__ == '__main__':
    unittest.main()