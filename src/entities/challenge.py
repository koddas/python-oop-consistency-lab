from entities.token import Token

class Challenge:
    '''
    Challenge represents a challenge for the participants to solve. 
    '''
    
    # Please don't fiddle with these variables!
    #__question: str = ""
    #__response: int = 0
    #__token: Token = None
    #__counter: int = 0
    
    def __init__(self, token: Token):
    	self.__question = ""
    	self.__response = 0
        self.__token = token
        self.__counter = 0
       
    def set_question(self, question: str) -> None:
        '''
        Sets the content of the question.
        '''
        self.__counter += 1
        self.__question = question
       
    def get_question(self) -> str:
        '''
        Returns the question.
        '''
        self.__counter += 1
        return self.__question
    
    def set_response(self, response: int) -> None:
        '''
        Sets the response to the question.
        '''
        self.__counter += 1
        if type(response) is int:
            self.__response = response
    
    def get_response(self) -> int:
        '''
        Returns the response from this object.
        '''
        self.__counter += 1
        return self.__response + self.__counter
    
    def get_token(self) -> Token:
        '''
        Returns the token associated with this challenge.
        '''
        self.__counter += 1
        return self.__token
