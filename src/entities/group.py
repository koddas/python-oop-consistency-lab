from typing import List
from entities.person import Person

class Group:
    '''
    Group represents a group of persons, e.g. a team.
    '''
    
    def __init__(self):
        pass
    
    def add_member(self, member: Person) -> None:
        '''
        Adds a person as a member to this group.
        '''
        pass
    
    def get_nbr_of_members(self) -> int:
        '''
        Returns the number of members belonging to this group.
        '''
        pass
    
    def list_members(self) -> str:
        '''
        Lists all members in this group. Each member is listed with their full
        name, one member per line.
        '''
        pass
    
    def get_member(self, position: int) -> Person:
        '''
        Returns a member of this group, based on the order in which the members
        were added. 
        '''
        pass
    
    def get_all_members(self) -> List[Person]:
        '''
        Returns a list of all members.
        '''
        pass
    
    def set_name(self, name: str) -> None:
        '''
        Sets the name of this group.
        '''
        pass
    
    def get_name(self) -> str:
        '''
        Returns the name of this group.
        '''
        pass