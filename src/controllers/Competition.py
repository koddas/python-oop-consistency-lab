from entities.Token import Token
from entities.Group import Group
from boundaries.NetConnection import NetConnection
from boundaries.UserInterface import UserInterface
from controllers.Scoreboard import Scoreboard
from controllers.Storage import Storage
from fileinput import filename
from controllers.EntityFactory import EntityFactory
import sys

class Competition():
    '''
    Competition represents a competition, in which you, dear player, gets to
    partake.
    '''
    
    # The following fields are not to be touched.
    _ui: UserInterface      = None
    _conn: NetConnection    = None
    _board: Scoreboard      = None
    _storage: Storagee      = None
    _factory: EntityFactory = None
    
    # You may fiddle around with the following fields
    FILE_PREFIX: str     = "competition_"
    
    def __init__(self, ui: UserInterface):
        self._ui = ui
        self._conn = NetConnection()
        self._board = Scoreboard()
        self._storage = Storage()
        self._factory = EntityFactory()
        
        self._board.set_connection(self._conn)
    
    def start_game(self) -> None:
        self._ui.prompt_user("Welcome to the game!")
        self._ui.prompt_user("--------------------")
        
        group = self._factory.create_group()
        
        self._ui.prompt_user("Now, let's add our first member.")
        group.add_member(self._ui.create_person())
        while self._ui.ask_user("Add another member? (y/n)\n") == 'y':
            group.add_member(self._factory.create_person())
        
        token = Token()
        
        filename = self._ui.request_filename()
        if self._storage.save(Competition.FILE_PREFIX + filename, token):
            if self._conn.signup(group, token):
                self._board.start_timer(token)
                self._ui.prompt_user("Thank you. You're now registered.")
            else:
                self._ui.prompt_user("Couldn't register.")
        else:
            self._ui.prompt_user("Couldn't save token.")
        sys.exit(0)
    
    def perform_challenge(self) -> None:
        sys.exit(0)
    
    def finish_game(self, token: Token) -> None:
        sys.exit(0)