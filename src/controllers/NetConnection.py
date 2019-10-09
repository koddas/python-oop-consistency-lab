import requests
import json
from entities.Token import Token
from entities.Group import Group
from entities.Challenge import Challenge

class NetConnection():
    '''
    This class connects the application to the web service running the actual
    competition.
    '''
    
    _instance: NetConnection = None
    _URL = "127.0.0.1:8050"
    
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
        token_value = token.get_value()
        people = []
        for person in Group.get_all_members():
            people.append(person.get_full_name())

        response = requests.post(self._URL + '?signup', data={
            'people': json.encoder(people),
            'token': token_value
        })
        json_response = response.json()

        if json_response.success:
            return True

        print(json_response.message)
        return False

    
    def start_timer(self, token: Token) -> bool:
        '''
        Starts a timer, visible for all to see.
        '''
        token_value = token.get_value()
        response = requests.post(self._URL + '?start', data={
            'token': token_value
        })
        json_response = response.json()

        if json_response.success:
            return True

        print(json_response.message)
        return False
    
    def stop_timer(self, token: Token) -> bool:
        '''
        Stops the aforementioned timer.
        '''
        token_value = token.get_value()
        response = requests.post(self._URL + '?stop', data={
            'token': token_value
        })
        json_response = response.json()

        if json_response.success:
            return True

        print(json_response.message)
        return False
    
    def request_challenge(self, token: Token) -> Challenge:
        '''
        Asks for the challenge that you'll have to solve.
        '''
        token_value = token.get_value()
        response = requests.post(self._URL + '?challenge', data={
            'token': token_value
        })
        json_response = response.json()

        if json_response.success:
            return True

        print(json_response.message)
        return False
    
    def submit_response(self, token: Token, challenge: Challenge) -> bool:
        '''
        Submits the response to the challenge.
        '''
        token_value = token.get_value()
        response = requests.post(self._URL + '?response', data={
            'token': token_value
        })
        json_response = response.json()

        if json_response.success:
            return True

        print(json_response.message)
        return False
    
    def claim_prize(self, token: Token) -> bool:
        '''
        There can be only one. Use this method to claim your prize, but be
        careful: you only get one try!
        '''
        token_value = token.get_value()
        response = requests.post(self._URL + '?price', data={
            'token': token_value
        })
        json_response = response.json()

        if json_response.success:
            return True

        print(json_response.message)
        return False