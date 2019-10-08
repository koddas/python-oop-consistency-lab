from uuid import uuid4

class Token:
    '''
    Token represents a token, used to identify your group through the system. A
    token is really just a UUID-formatted string.
    '''
    _token: str
    
    def __init__(self):
        self._token = uuid4()
    
    def getValue(self) -> str:
        '''
        Returns the value of this token.
        '''
        return self._token