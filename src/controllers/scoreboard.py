from entities.token import Token
from controllers.net_connection import NetConnection

class Scoreboard:
	'''
	Scoreboard represents a scoreboard, on which you, dear player, gets to
	publish your group's progress.
	'''
	
	# The following fields are not to be touched.
	#__conn: NetConnection = None
	#__state: int          = 0
	
	def __init__(self):
		self.__state = 0
		self.__conn = NetConnection.get_instance()
	
	def start_timer(self, token: Token) -> None:
		'''
        Starts a timer, visible for all to see.
        '''
		self.__state = 1
		self.__conn.start_timer(token)
	
	def stop_timer(self, token: Token) -> None:
		'''
        Stops the aforementioned timer.
        '''
		if self.__state == 0:
			self.__conn.stop_timer(token)
