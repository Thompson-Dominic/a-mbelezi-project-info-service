"""Provides the BaseDomain class for objects in the domain model."""
import uuid

from . import DomainEvent

class BaseDomain:
    """Base class for objects in the domain model"""
    _id = None
    _events = None
    
    def __init__(self, domain_id:uuid=None):
        """
        Initialize a new instance of BaseDomain.
        
        :param id: The unique identifier for this object. Defaults to None.
        """
        self._id = domain_id

    def is_transient(self):
        """Returns True if the object is not persisted yet, False otherwise"""
        return self._id is None
    
    def assign_id(self, domain_id:uuid):
        """Assigns an id to the object"""
        self._id = domain_id
    
    def generate_id(self):
        """Generates an id for the object"""
        self._id = uuid.uuid4()
        
    def get_id(self):
        """Returns the object's id"""
        if self._id is None:
            raise AttributeError("id is not defined.")
        
        return self._id

    def add_event(self, event:DomainEvent):
        """Adds an event to the object"""
        if self._events is None:
            self._events = []
        self._events.append(event)
    
    def get_events(self):
        """Returns the object's events"""
        if self._events is None:
            self._events = []
        return self._events


    def __eq__(self, other):
        return self._id == other.id

    def __hash__(self):
        return hash(self._id)