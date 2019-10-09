from entities.Token import Token
from entities.Group import Group
from boundaries.NetConnection import NetConnection
from controllers.Scoreboard import Scoreboard
from boundaries.UserInterface import UserInterface

class Competition():
    '''
    Competition represents a competition, in which you, dear player, gets to
    partake.
    '''
    
    # The following fields are not to be touched.
    _ui: UserInterface = None
    _conn: NetConnection = None
    _board: Scoreboard = None
    
    # You may fiddle around with the following fields
    FILE_PREFIX: str     = "competition_"
    
    def __init__(self, ui: UserInterface):
        self._ui = ui
        self._conn = NetConnection()
        self._board = Scoreboard()
        
        self._board.set_connection(self._conn)
    
    def start_game(self, group: Group) -> Token:
        token = Token()
        
        self._conn.signup(group, token)
        
        return token
    
    def finish_game(self, token: Token) -> None:
        pass