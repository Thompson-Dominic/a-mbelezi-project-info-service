""" This module contains the basic models for the project info """

class ProjectInfoBasicModel:
    """ This class models basic information about a project """
    def __init__(self, project_id, name, description, approved_date):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.approved_date = approved_date
    
    def to_dict(self):
        """ Returns a dictionary representation of the project info"""
        return {
            "project_id": self.project_id,
            "name": self.name,
            "description": self.description,
            "approved_date": self.approved_date
        }


class ProjectInfoDetailModel(ProjectInfoBasicModel):
    """ This class models detailed information about a project"""
    def __init__(self, project_id, name, description, approved_date, timeline_in_weeks, budget, 
                 budget_currency, project_classification_id, 
                 locality_id, community):
        super().__init__(project_id, name, description, approved_date)
        self.timeline_in_weeks = timeline_in_weeks
        self.budget = budget
        self.budget_currency = budget_currency
        self.approved_date = approved_date
        self.project_classification_id = project_classification_id
        self.locality_id = locality_id
        self.community = community 
    
    def to_dict(self):
        """ Returns a dictionary representation of the project info"""
        return super().to_dict() | {
            "timeline_in_weeks": self.timeline_in_weeks,
            "budget": self.budget,
            "budget_currency": self.budget_currency,
            "approved_date": self.approved_date,
            "project_classification_id": self.project_classification_id,
            "locality_id": self.locality_id,
            "community": self.community
        }