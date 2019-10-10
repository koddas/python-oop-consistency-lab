'''
This is from where we run the program. Yay!
'''
from controllers.competition import Competition
from boundaries.text_ui import TextUI

competition = Competition(TextUI())
competition.run_game()