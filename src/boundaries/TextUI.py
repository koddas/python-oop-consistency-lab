from boundaries.UserInterface import UserInterface
from entities.Challenge import Challenge

class TextUI(UserInterface):
    '''
    TextUI represents a text-based user interface.
    '''
    
    def __init__(self):
        pass
    
    def prompt_user(self, message: str) -> None:
        print(message)
    
    def ask_user(self, message: str) -> str:
        return input(message + "\n> ")
    
    def request_filename(self) -> str:
        '''
        Asks the user for a file name
        '''
        return self.ask_user("What's the name of the file?")
    
    def present_challenge(self, challenge: Challenge) -> None:
        pass