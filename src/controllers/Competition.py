from entities.Token import Token
from boundaries.UserInterface import UserInterface
from controllers.NetConnection import NetConnection
from controllers.Scoreboard import Scoreboard
from controllers.Storage import Storage
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
        self._conn = NetConnection.get_instance()()
        self._board = Scoreboard()
        self._storage = Storage()
        self._factory = EntityFactory()
        
        self._board.set_connection(self._conn)
    
    def run_game(self) -> None:
        choice: int = self._ui.choose_step()
        
        if choice == 1:
            self.start_game()
        elif choice == 2:
            self.perform_challenge()
        elif choice == 3:
            self.finish_game()
        else:
            self._ui.prompt_user("That's not how we play. Try again.")
            sys.exit(0)
    
    def start_game(self) -> None:
        self._ui.prompt_user("Ok. Let's start by creating a group.")
        
        group = self._factory.create_group()
        
        self._ui.prompt_user("Now, let's add our first member.")
        group.add_member(self._ui.create_person())
        while self._ui.ask_user("Add another member? (y/n)\n") == 'y':
            group.add_member(self._factory.create_person())
        
        token = Token()
        
        name = self._ui.request_filename()
        if self._storage.save(Competition.FILE_PREFIX + name, token):
            if self._conn.signup(group, token):
                self._board.start_timer(token)
                self._ui.prompt_user("Thank you. You're now registered.")
            else:
                self._ui.prompt_user("Couldn't register.")
        else:
            self._ui.prompt_user("Couldn't save token.")
        sys.exit(0)
    
    def perform_challenge(self) -> None:
        self._ui.prompt_user("Cool. Let's play!")
        name = self._ui.request_filename() 
        token = self._storage.read(Competition.FILE_PREFIX + name, Token)
        
        sys.exit(0)
    
    def finish_game(self) -> None:
        sys.exit(0)