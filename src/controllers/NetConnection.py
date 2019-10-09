from entities.Token import Token
from entities.Group import Group
from entities.Challenge import Challenge

class NetConnection():
    '''
    This class connects the application to the web service running the actual
    competition.
    '''
    
    _instance: NetConnection = None
    
    def __init__(self):
        if NetConnection._instance:
            self.get_instance()
    
    @classmethod
    def get_instance(cls):
        '''
        Use this class method to get an instance of this class.
        '''
        if cls._instance is None:
            cls._instance = NetConnection()
        
        return cls._instance
    
    def signup(self, group: Group, token: Token) -> bool:
        '''
        This method signs you up for the competition. The group is identified
        by a token.
        '''
        pass
    
    def start_timer(self, token: Token) -> bool:
        '''
        Starts a timer, visible for all to see.
        '''
        pass
    
    def stop_timer(self, token: Token) -> bool:
        '''
        Stops the aforementioned timer.
        '''
        pass
    
    def request_challenge(self, token: Token) -> Challenge:
        '''
        Asks for the challenge that you'll have to solve.
        '''
        pass
    
    def submit_response(self, token: Token, challenge: Challenge) -> bool:
        '''
        Submits the response to the challenge.
        '''
        pass
    
    def claim_prize(self, token: Token) -> bool:
        '''
        There can be only one. Use this method to claim your prize, but be
        careful: you only get one try!
        '''
        pass