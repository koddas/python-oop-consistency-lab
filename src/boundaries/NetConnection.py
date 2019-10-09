from entities.Token import Token
from entities.Group import Group

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
        if cls._instance is None:
            cls._instance = NetConnection()
        
        return cls._instance
    
    def signup(self, group: Group, token: Token) -> bool:
        pass
    
    def start_timer(self, Token) -> bool:
        pass
    
    def stop_timer(self, Token) -> bool:
        pass