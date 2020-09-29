class Person:
    '''
    Person represents a physical person, e.g. you!
    '''
    
    __first_name: str
    __last_name: str
    
    def __init__(self):
        self.__first_name = ""
        self.__last_name = ""
    
    def set_first_name(self, name: str) -> None:
        '''
        Sets the first name of this person.
        '''
        self.__first_name = name
    
    def get_first_name(self) -> str:
        '''
        Returns the first name of this person.
        '''
        return self.__first_name
    
    def set_last_name(self, name: str) -> None:
        '''
        Sets the last name of this person.
        '''
        self.__last_name = name
    
    def get_last_name(self) -> str:
        '''
        Returns the last name of this person.
        '''
        return self.__last_name
    
    def get_full_name(self) -> str:
        '''
        Returns the full name of this person.
        '''
        return self.__first_name + " " + self.__last_name
