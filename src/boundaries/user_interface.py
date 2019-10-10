from abc import ABC, abstractmethod
from entities.challenge import Challenge

class UserInterface(ABC):
    
    @abstractmethod
    def choose_step(self) -> int:
        '''
        Presents the user with a menu, from which the user can choose a task to
        run.
        '''
        pass
    
    @abstractmethod
    def prompt_user(self, message: str) -> None:
        '''
        Prompts the user with a message.
        '''
        pass
    
    @abstractmethod
    def ask_user(self, message: str) -> str:
        '''
        Asks the user for some input
        '''
        pass
    
    @abstractmethod
    def request_filename(self) -> str:
        '''
        Asks the user for a file name
        '''
        pass
    
    @abstractmethod
    def present_challenge(self, challenge: Challenge) -> None:
        '''
        Presents a challenge to the user
        '''
        pass