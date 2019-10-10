from boundaries.user_interface import UserInterface
from entities.group import Group
from entities.person import Person

class EntityFactory:
    '''
    This class is used to create entities. It communicates with the user using
    a boundary class. Obviously.
    '''
    
    def __init__(self):
        pass
    
    def set_ui(self, ui: UserInterface) -> None:
        '''
        Sets the boundary class used by this factory
        '''
        pass
    
    def create_group(self) -> Group:
        '''
        Asks the user for input to create a new group.
        '''
        pass
    
    def create_person(self) -> Person:
        '''
        Asks the user for input in order to create a new person.
        '''
        pass