from entities.Group import Group
from entities.Person import Person
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
    
    def create_group(self) -> Group:
        '''
        Asks the user for input to create a new group.
        '''
        print("Creating a new group")
        name = self.ask_user("What's the name of the group?")
        
        group = Group()
        group.set_name(name)
        
        return group
    
    def create_person(self) -> Person:
        '''
        Asks the user for input in order to create a new person.
        '''
        print("Adding a new person")
        first_name = self.ask_user("What's the first name of this person?")
        last_name = self.ask_user("What's the last name of this person?")
        
        person = Person()
        person.set_first_name(first_name)
        person.set_last_name(last_name)
        
        return person
    
    def request_filename(self) -> str:
        '''
        Asks the user for a file name
        '''
        return self.ask_user("What's the name of the file?")
    
    def present_challenge(self, challenge: Challenge) -> None:
        pass