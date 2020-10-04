from typing import List
from entities.person import Person

class Group:
    '''
    Group represents a group of persons, e.g. a team.
    '''
    
    #__members: List[Person]
    #__name: str
    
    def __init__(self):
        self.__members = []
        self.__name = ""
    
    def add_member(self, member: Person) -> None:
        '''
        Adds a person as a member to this group.
        '''
        self.__members.append(member)
    
    def get_nbr_of_members(self) -> int:
        '''
        Returns the number of members belonging to this group.
        '''
        return len(self.__members)
    
    def list_members(self) -> str:
        '''
        Lists all members in this group. Each member is listed with their full
        name, one member per line.
        '''
        members: List[str] = list(map(lambda member: member.get_full_name(), self.__members))
        return '\n'.join(members)
    
    def get_member(self, position: int) -> Person:
        '''
        Returns a member of this group, based on the order in which the members
        were added. 
        '''
        return self.__members[position]
    
    def get_all_members(self) -> List[Person]:
        '''
        Returns a list of all members.
        '''
        return self.__members
    
    def set_name(self, name: str) -> None:
        '''
        Sets the name of this group.
        '''
        self.__name = name
    
    def get_name(self) -> str:
        '''
        Returns the name of this group.
        '''
        return self.__name
