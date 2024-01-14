import unittest
from src.ProjectSection.ProjectSection import ProjectSection
from uuid import uuid4

class TestProjectSection(unittest.TestCase):
    def setUp(self):
        """Set up a ProjectSection instance for testing."""
        self.project_section = ProjectSection("Section1", 1, "Details of section 1")

    def test_sectionName(self):
        """Test the getter, setter, and deleter for sectionName."""
        self.assertEqual(self.project_section.sectionName, "Section1")
        self.project_section.sectionName = "Section2"
        self.assertEqual(self.project_section.sectionName, "Section2")
        del self.project_section.sectionName
        with self.assertRaises(AttributeError):
            self.project_section.sectionName

    def test_project_id(self):
        """Test the getter, setter, and deleter for project_id."""
        new_uuid = uuid4()
        self.project_section.project_id = new_uuid
        self.assertEqual(self.project_section.project_id, new_uuid)
        del self.project_section.project_id
        with self.assertRaises(AttributeError):
            self.project_section.project_id

    def test_details(self):
        """Test the getter, setter, and deleter for details."""
        self.assertEqual(self.project_section.details, "Details of section 1")
        self.project_section.details = "Details of section 2"
        self.assertEqual(self.project_section.details, "Details of section 2")
        del self.project_section.details
        with self.assertRaises(AttributeError):
            self.project_section.details

if __name__ == '__main__':
    unittest.main()