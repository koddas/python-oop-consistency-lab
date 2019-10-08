from entities.Group import Group
from entities.Person import Person

class TextUI:
    '''
    TextUI represents a text-based user interface.
    '''
    
    def __init__(self):
        pass
    
    def create_group(self) -> Group:
        '''
        Asks the user for input to create a new group.
        '''
        print("Creating a new group")
        name = input("What's the name of the group?\n")
        
        group = Group()
        group.set_name(name)
        
        print("Now, let's add our first member.")
        group.add_member(self.create_person())
        while input("Add another member? (y/n)\n") == 'y':
            group.add_member(self.create_person())
        
        return group
    
    def create_person(self) -> Person:
        '''
        Asks the user for input in order to create a new person.
        '''
        print("Adding a new person")
        first_name = input("What's the first name of this person?\n")
        last_name = input("What's the last name of this person?\n")
        
        person = Person()
        person.set_first_name(first_name)
        person.set_last_name(last_name)
        
        return person