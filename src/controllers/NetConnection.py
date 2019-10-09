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
    
    _instance = None
    _URL = "http://antontibblin.se/oop-labb/api.php"
    
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
        for person in group.get_all_members():
            people.append(person.get_full_name())

        response = requests.post(self._URL + '?signup', data={
            'name': json.dumps(group.get_name()),
            'people': json.dumps(people),
            'token': token_value
        })
        json_response = response.json()

        if json_response['success']:
            return True

        print(json_response['message'])
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

        if json_response['success']:
            return True

        print(json_response['message'])
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

        if json_response['success']:
            return True

        print(json_response['message'])
        return False
    
    def request_challenge(self, token: Token) -> Challenge:
        '''
        Asks for the challenge that you'll have to solve.
        '''
        token_value = token.get_value()
        response = requests.post(self._URL + '?get-challenge', data={
            'token': token_value
        })
        challenge = Challenge(token)
        challenge.set_question(response.content.decode("utf-8"))
        
        return challenge
    
    def submit_response(self, challenge: Challenge) -> bool:
        '''
        Submits the response to the challenge.
        '''
        token_value = challenge.get_token().get_value()
        response = requests.post(self._URL + '?check-challenge', data={
            'token': token_value,
            'guess': challenge.get_response()
        })
        json_response = response.json()

        if json_response['success']:
            return True

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

        if json_response['success']:
            print(json_response['message'])
            return True

        print(json_response['message'])
        return False