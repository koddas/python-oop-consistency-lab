from boundaries.UserInterface import UserInterface
from entities.Group import Group
from entities.Person import Person

class EntityFactory:
    '''
    This class is used to create entities. It communicates with the user using
    a boundary class. Obviously.
    '''
    
    _ui: UserInterface = None
    
    def __init__(self):
        pass
    
    def set_UI(self, ui: UserInterface):
        '''
        Sets the boundary class used by this factory
        '''
        self._ui = ui
    
    def create_group(self) -> Group:
        '''
        Asks the user for input to create a new group.
        '''
        self._ui.prompt_user("Creating a new group")
        name = self._ui.ask_user("What's the name of the group?")
        
        group = Group()
        group.set_name(name)
        
        return group
    
    def create_person(self) -> Person:
        '''
        Asks the user for input in order to create a new person.
        '''
        self._ui.prompt_user("Adding a new person")
        first_name = self._ui.ask_user("What's the first name of this person?")
        last_name = self._ui.ask_user("What's the last name of this person?")
        
        person = Person()
        person.set_first_name(first_name)
        person.set_last_name(last_name)
        
        return person