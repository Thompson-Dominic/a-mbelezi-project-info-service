import unittest
from src.ProjectInfo.ProjectInfo import ProjectInfo
from src.ProjectInfo.ProjectStatus import ProjectStatus
from datetime import datetime

class TestProjectInfo(unittest.TestCase):
    def setUp(self):
        """Set up a ProjectInfo instance for testing."""
        self.project_info = ProjectInfo("Project1", "This is a test project", 4, 1000.0, "USD", datetime.now())

    def test_name(self):
        """Test the getter, setter, and deleter for name."""
        self.project_info.name = "Project1"
        self.assertEqual(self.project_info.name, "Project1")
        del self.project_info.name
        with self.assertRaises(AttributeError):
            self.project_info.name

    def test_description(self):
        """Test the getter, setter, and deleter for description."""
        self.project_info.description = "This is a test project"
        self.assertEqual(self.project_info.description, "This is a test project")
        del self.project_info.description
        with self.assertRaises(AttributeError):
            self.project_info.description

    def test_timeline_in_weeks(self):
        """Test the getter, setter, and deleter for timeline_in_weeks."""
        self.project_info.timeline_in_weeks = 4
        self.assertEqual(self.project_info.timeline_in_weeks, 4)
        del self.project_info.timeline_in_weeks
        with self.assertRaises(AttributeError):
            self.project_info.timeline_in_weeks

    def test_budget(self):
        """Test the getter, setter, and deleter for budget."""
        self.project_info.budget = 1000.0
        self.assertEqual(self.project_info.budget, 1000.0)
        del self.project_info.budget
        with self.assertRaises(AttributeError):
            self.project_info.budget

    def test_budget_currency(self):
        """Test the getter, setter, and deleter for budget_currency."""
        self.project_info.budget_currency = "USD"
        self.assertEqual(self.project_info.budget_currency, "USD")
        del self.project_info.budget_currency
        with self.assertRaises(AttributeError):
            self.project_info.budget_currency

    def test_approved_date(self):
        """Test the getter, setter, and deleter for approved_date."""
        date = datetime.now()
        self.project_info.approved_date = date
        self.assertEqual(self.project_info.approved_date, date)
        del self.project_info.approved_date
        with self.assertRaises(AttributeError):
            self.project_info.approved_date

    def test_project_classification_id(self):
        """Test the getter, setter, and deleter for project_classification_id."""
        self.project_info.project_classification_id = 1
        self.assertEqual(self.project_info.project_classification_id, 1)
        del self.project_info.project_classification_id
        with self.assertRaises(AttributeError):
            self.project_info.project_classification_id

    def test_locality_id(self):
        """Test the getter, setter, and deleter for locality_id."""
        self.project_info.locality_id = 1
        self.assertEqual(self.project_info.locality_id, 1)
        del self.project_info.locality_id
        with self.assertRaises(AttributeError):
            self.project_info.locality_id

    def test_community(self):
        """Test the getter, setter, and deleter for community."""
        self.project_info.community = "Community1"
        self.assertEqual(self.project_info.community, "Community1")
        del self.project_info.community
        with self.assertRaises(AttributeError):
            self.project_info.community

    def test_projectStatus(self):
        """Test the getter and setter for projectStatus."""
        self.project_info.projectStatus = ProjectStatus.IN_PROGRESS
        self.assertEqual(self.project_info.projectStatus, ProjectStatus.IN_PROGRESS)

if __name__ == '__main__':
    unittest.main()