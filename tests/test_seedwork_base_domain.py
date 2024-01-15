import unittest
import uuid
from src.SeedWork.BaseDomain import BaseDomain
from src.SeedWork.DomainEvent import DomainEvent

class TestBaseDomain(unittest.TestCase):
    def setUp(self):
        """Set up a BaseDomain instance for testing."""
        self.base_domain = BaseDomain(None)

    def test_is_transient(self):
        """Test the is_transient method."""
        self.assertTrue(self.base_domain.is_transient())
        self.base_domain.generate_id()
        self.assertFalse(self.base_domain.is_transient())

    def test_assign_id(self):
        """Test the assign_id method."""
        new_id = uuid.uuid4()
        self.base_domain.assign_id(new_id)
        self.assertEqual(self.base_domain.get_id(), new_id)

    def test_generate_id(self):
        """Test the generate_id method."""
        self.base_domain.generate_id()
        self.assertIsInstance(self.base_domain.get_id(), uuid.UUID)

    def test_get_id(self):
        """Test the get_id method."""
        with self.assertRaises(AttributeError):
            self.base_domain.get_id()
        self.base_domain.generate_id()
        self.assertIsInstance(self.base_domain.get_id(), uuid.UUID)

    def test_add_event(self):
        """Test the add_event method."""
        event = DomainEvent()
        self.base_domain.add_event(event)
        self.assertEqual(self.base_domain.get_events(), [event])

    def test_get_events(self):
        """Test the get_events method."""
        self.assertEqual(self.base_domain.get_events(), [])
        event = DomainEvent()
        self.base_domain.add_event(event)
        self.assertEqual(self.base_domain.get_events(), [event])

if __name__ == '__main__':
    unittest.main()