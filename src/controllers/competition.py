from entities.token import Token
from boundaries.user_interface import UserInterface
from controllers.net_connection import NetConnection
from controllers.scoreboard import Scoreboard
from controllers.storage import Storage
from controllers.entity_factory import EntityFactory
import sys

class Competition():
    '''
    Competition represents a competition, in which you, dear player, gets to
    partake.
    '''
    
    # The following fields are not to be touched.
    __ui: UserInterface      = None
    __conn: NetConnection    = None
    __board: Scoreboard      = None
    __storage: Storage       = None
    __factory: EntityFactory = None
    
    # You may fiddle around with the following fields
    FILE_PREFIX: str     = "competition_"
    
    def __init__(self, ui: UserInterface):
        pass
    
    def run_game(self) -> None:
        '''
        Presents the user with a menu and runs the chosen action.
        '''
        pass
    
    def start_game(self) -> None:
        '''
        Initializes the game by asking the user to create a group of eager
        players.
        '''
        pass
    
    def perform_challenge(self) -> None:
        '''
        Runs the challenge part of the game.
        '''
        pass
    
    def finish_game(self) -> None:
        '''
        Finishes the game. If you're fast enough, you get the prize!
        '''
        pass
