from boundaries.UserInterface import UserInterface
from entities.Challenge import Challenge

class TextUI(UserInterface):
    '''
    TextUI represents a text-based user interface.
    '''
    
    def __init__(self):
        pass
    
    def choose_step(self) -> int:
        '''
        Presents the user with a menu, from which the user can choose a task to
        run.
        '''
        print("Welcome to the game!")
        print("--------------------")
        print("What would you like to do?")
        print("1. Register for game")
        print("2. Play the game")
        print("3. Claim the prize")
        choice: int = int(self.ask_user("Please, pick a number"))
        
        return choice
    
    def prompt_user(self, message: str) -> None:
        '''
        Prompts the user with a message.
        '''
        print(message)
    
    def ask_user(self, message: str) -> str:
        '''
        Asks the user for some input
        '''
        return input(message + "\n> ")
    
    def request_filename(self) -> str:
        '''
        Asks the user for a file name
        '''
        return self.ask_user("What's the name of the file?")
    
    def present_challenge(self, challenge: Challenge) -> None:
        '''
        Presents a challenge to the user
        '''
        pass