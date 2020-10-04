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
    #__ui: UserInterface      = None
    #__conn: NetConnection    = None
    #__board: Scoreboard      = None
    #__storage: Storage       = None
    #__factory: EntityFactory = None
    
    # You may fiddle around with the following fields
    FILE_PREFIX: str     = "competition_"
    
    def __init__(self, ui: UserInterface):
        self.__ui = ui
        self.__board = Scoreboard()
        self.__storage = Storage()
        self.__factory = EntityFactory()
        self.__conn = NetConnection.get_instance()
        
        self.__factory.set_ui(ui)
    
    def run_game(self) -> None:
        '''
        Presents the user with a menu and runs the chosen action.
        '''
        choice: int = self.__ui.choose_step()
        
        if choice == 1:
            self.start_game()
        elif choice == 2:
            self.perform_challenge()
        elif choice == 3:
            self.finish_game()
        else:
            self.__ui.prompt_user("That's not how we play. Try again.")
            sys.exit(0)
    
    def start_game(self) -> None:
        '''
        Initializes the game by asking the user to create a group of eager
        players.
        '''
        self.__ui.prompt_user("Ok. Let's start by creating a group.")
        
        group = self.__factory.create_group()
        
        self.__ui.prompt_user("Now, let's add our first member.")
        group.add_member(self.__factory.create_person())
        while self.__ui.ask_user("Add another member? (y/n)") == 'y':
            group.add_member(self.__factory.create_person())
        
        token = Token()
        
        name = self.__ui.request_filename()
        if self.__storage.save(Competition.FILE_PREFIX + name, token):
            if self.__conn.signup(group, token):
                self.__board.start_timer(token)
                self.__ui.prompt_user("Thank you. You're now registered.")
            else:
                self.__ui.prompt_user("Couldn't register.")
        else:
            self.__ui.prompt_user("Couldn't save token.")
        sys.exit(0)
    
    def perform_challenge(self) -> None:
        '''
        Runs the challenge part of the game.
        '''
        self.__ui.prompt_user("Cool. Let's play!")
        name = self.__ui.request_filename() 
        token = self.__storage.read(Competition.FILE_PREFIX + name, Token)
        
        if token is None:
            self.__ui.prompt_user("Couldn't read your token")
            sys.exit(0)
        
        challenge = self.__conn.request_challenge(token)
        self.__ui.present_challenge(challenge)
        answer = int(self.__ui.ask_user("Your answer, please"))
        challenge.set_response(answer)
        
        self.__ui.prompt_user("Thank you. Submitting your answer.")
        if self.__conn.submit_response(challenge):
            self.__board.stop_timer(token)
            self.__ui.prompt_user("Good going! Now, go and claim your prize!")
        else:
            self.__ui.prompt_user("No, that's not the correct answer.")
        
        sys.exit(0)
    
    def finish_game(self) -> None:
        '''
        Finishes the game. If you're fast enough, you get the prize!
        '''
        self.__ui.prompt_user("Claim your prize! First, let's get that token.")
        name = self.__ui.request_filename()
        token = self.__storage.read(Competition.FILE_PREFIX + name, Token)
        
        if token is None:
            self.__ui.prompt_user("Couldn't read your token")
            sys.exit(0)
            
        if self.__conn.claim_prize(token):
            self.__ui.prompt_user("Yay! You won!")
        else:
            self.__ui.prompt_user("Close, but no cigar. Better luck next time.")
        
        sys.exit(0)
