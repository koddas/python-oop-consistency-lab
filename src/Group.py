from typing import List
from Person import Person
from _ctypes import sizeof

class Group:
    _members: List[Person]
    _name: str
    
    def __init__(self):
        self._members = []
        self._name = ""
    
    def add_member(self, member: Person) -> None:
        self._members.append(member)
    
    def get_nbr_of_members(self) -> int:
        return len(self._members)
    
    def list_members(self) -> str:
        members: List[str] = list(map(lambda member: member.get_full_name(), self._members))
        return '\n'.join(members)
    
    def get_member(self, position: int) -> Person:
        return List[position]
    
    def get_all_members(self) -> List[Person]:
        return self._members
    
    def set_name(self, name: str) -> None:
        self._name = name
    
    def get_name(self) -> str:
        return self._name