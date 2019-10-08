from abc import ABC, abstractmethod
from entities.Group import Group
from entities.Person import Person

class UserInterface(ABC):
    
    @abstractmethod
    def create_group(self) -> Group:
        pass
    
    @abstractmethod
    def create_person(self) -> Person:
        pass