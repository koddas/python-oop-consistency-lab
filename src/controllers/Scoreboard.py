from entities.Token import Token
from controllers.NetConnection import NetConnection

class Scoreboard:
	'''
	Scoreboard represents a scoreboard, on which you, dear player, gets to
	publish your group's progress.
	'''
	
	# The following fields are not to be touched.
	_conn: NetConnection = None
	_state: int          = 0
	
	def __init__(self):
		pass
	
	def start_timer(self, token: Token) -> None:
		self._conn.start_timer(token)
	
	def stop_timer(self, token: Token) -> None:
		self._conn.stop_timer(token)
	
	def set_connection(self, conn: NetConnection) -> None:
		self._conn = conn