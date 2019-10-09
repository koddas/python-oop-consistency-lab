from abc import ABC, abstractmethod
from entities.Group import Group
from entities.Person import Person
from entities.Challenge import Challenge

class UserInterface(ABC):
    
    @abstractmethod
    def prompt_user(self, message: str) -> None:
        pass
    
    @abstractmethod
    def ask_user(self, message: str) -> str:
        pass
    
    @abstractmethod
    def create_group(self) -> Group:
        pass
    
    @abstractmethod
    def create_person(self) -> Person:
        pass
    
    @abstractmethod
    def request_filename(self) -> str:
        pass
    
    @abstractmethod
    def present_challenge(self, challenge: Challenge) -> None:
        pass