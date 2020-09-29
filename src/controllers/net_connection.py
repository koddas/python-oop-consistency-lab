import requests
import json
import inspect
from entities.token import Token
from entities.group import Group
from entities.challenge import Challenge

class NetConnection():
    '''
    This class connects the application to the web service running the actual
    competition.
    '''
    
    __instance = None
    __URL = "http://antontibblin.se/oop-labb/api.php"
    
    def __init__(self):
        if NetConnection.__instance:
            self.get_instance()
    
    @classmethod
    def get_instance(cls):
        '''
        Use this class method to get an instance of this class.
        '''
        if cls.__instance is None:
            cls.__instance = NetConnection()
        
        return cls.__instance
    
    def signup(self, group: Group, token: Token) -> bool:
        '''
        This method signs you up for the competition. The group is identified
        by a token.
        '''
        if group.get_nbr_of_members() < 2:
            return False
        
        token_value = token.get_value()
        people = []
        for person in group.get_all_members():
            people.append(person.get_full_name())

        response = requests.post(self.__URL + '?signup', data={
            'name': json.dumps(group.get_name()),
            'people': json.dumps(people),
            'token': token_value
        })
        json_response = response.json()

        if json_response['success']:
            return True

        return False

    
    def start_timer(self, token: Token) -> bool:
        '''
        Starts a timer, visible for all to see.
        '''
        print(inspect.stack()[1][3])
        if inspect.stack()[1][3] != "start_timer":
            return False
        token_value = token.get_value()
        response = requests.post(self.__URL + '?start', data={
            'token': token_value
        })
        json_response = response.json()

        if json_response['success']:
            return True

        return False
    
    def stop_timer(self, token: Token) -> bool:
        '''
        Stops the aforementioned timer.
        '''
        if inspect.stack()[1][3] != "stop_timer":
            return False
        token_value = token.get_value()
        response = requests.post(self.__URL + '?stop', data={
            'token': token_value
        })
        json_response = response.json()

        if json_response['success']:
            return True

        return False
    
    def request_challenge(self, token: Token) -> Challenge:
        '''
        Asks for the challenge that you'll have to solve.
        '''
        token_value = token.get_value()
        response = requests.post(self.__URL + '?get-challenge', data={
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
        response = requests.post(self.__URL + '?check-challenge', data={
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
        if inspect.stack()[1][3] != "finish_game":
            return False
        token_value = token.get_value()
        response = requests.post(self.__URL + '?price', data={
            'token': token_value
        })
        json_response = response.json()

        if json_response['success']:
            print(json_response['message'])
            return True

        return False
