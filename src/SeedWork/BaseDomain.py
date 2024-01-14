from abc import ABC, abstractmethod

class BaseDomain:
    _id = None
    
    # def __init__(self, id: str):
    #     self.id = id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)