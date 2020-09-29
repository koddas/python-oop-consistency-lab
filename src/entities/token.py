from uuid import uuid4, UUID
from entities.serializable import Serializable

class Token(Serializable):
    '''
    Token represents a token, used to identify your group through the system. A
    token is really just an encapsulated UUID.
    '''
    __token: UUID
    
    def __init__(self):
        self.__token = uuid4()
    
    def get_value(self) -> UUID:
        '''
        Returns the value of this token.
        '''
        return self.__token
    
    def serialize(self) -> str:
        '''
        Converts the contents of this object into a string.
        '''
        return self.__token.__str__()
    
    @staticmethod
    def deserialize(raw:str) -> object:
        '''
        Creates an object of the class based on serialized data.
        '''
        token = Token()
        token.__token = UUID(raw)
        
        return token
