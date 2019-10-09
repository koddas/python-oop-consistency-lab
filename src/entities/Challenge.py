from entities.Token import Token

class Challenge:
    '''
    Challenge represents a challenge for the participants to solve. 
    '''
    
    # Please don't fiddle with these variables!
    _question: str = ""
    _response: int = 0
    _token: Token = None
    _counter: int = 0
    
    def __init__(self, token: Token):
        self._token = token
       
    def set_question(self, question: str) -> None:
        self._counter =+ 1
        self._question = question
       
    def get_question(self) -> str:
        self._counter =+ 1
        return self._question
    
    def set_response(self, response: int) -> None:
        self._counter =+ 1
        self._response = response
    
    def get_response(self) -> int:
        self._counter =+ 1
        return self._response + self._counter
    
    def get_token(self) -> Token:
        self._counter =+ 1
        return self._token