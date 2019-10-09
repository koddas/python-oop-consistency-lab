from typing import List
from entities.Person import Person

class Group:
    '''
    Group represents a group of persons, e.g. a team.
    '''
    
    _members: List[Person]
    _name: str
    
    def __init__(self):
        self._members = []
        self._name = ""
    
    def add_member(self, member: Person) -> None:
        '''
        Adds a person as a member to this group.
        '''
        self._members.append(member)
    
    def get_nbr_of_members(self) -> int:
        '''
        Returns the number of members belonging to this group.
        '''
        return len(self._members)
    
    def list_members(self) -> str:
        '''
        Lists all members in this group. Each member is listed with their full
        name, one member per line.
        '''
        members: List[str] = list(map(lambda member: member.get_full_name(), self._members))
        return '\n'.join(members)
    
    def get_member(self, position: int) -> Person:
        '''
        Returns a member of this group, based on the order in which the members
        were added. 
        '''
        return List[position]
    
    def get_all_members(self) -> List[Person]:
        '''
        Returns a list of all members.
        '''
        return self._members
    
    def set_name(self, name: str) -> None:
        '''
        Sets the name of this group.
        '''
        self._name = name
    
    def get_name(self) -> str:
        '''
        Returns the name of this group.
        '''
        return self._name