from boundaries.user_interface import UserInterface
from entities.group import Group
from entities.person import Person

class EntityFactory:
    '''
    This class is used to create entities. It communicates with the user using
    a boundary class. Obviously.
    '''
    
    __ui: UserInterface = None
    
    def __init__(self):
        pass
    
    def set_ui(self, ui: UserInterface) -> None:
        '''
        Sets the boundary class used by this factory
        '''
        self.__ui = ui
    
    def create_group(self) -> Group:
        '''
        Asks the user for input to create a new group.
        '''
        self.__ui.prompt_user("Creating a new group")
        name = self.__ui.ask_user("What's the name of the group?")
        
        group = Group()
        group.set_name(name)
        
        return group
    
    def create_person(self) -> Person:
        '''
        Asks the user for input in order to create a new person.
        '''
        self.__ui.prompt_user("Adding a new person")
        first_name = self.__ui.ask_user("What's the first name of this person?")
        last_name = self.__ui.ask_user("What's the last name of this person?")
        
        person = Person()
        person.set_first_name(first_name)
        person.set_last_name(last_name)
        
        return person
