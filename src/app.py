'''
This is from where we run the program. Yay!
'''
from controllers.Competition import Competition
from boundaries.TextUI import TextUI

competition = Competition(TextUI())
competition.run_game()