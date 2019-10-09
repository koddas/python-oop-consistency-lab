from abc import ABC, abstractmethod

class Serializable(ABC):
	'''
	This abstract class describes an interface for serializable classes.
	'''
	
	@abstractmethod	
	def serialize(self) -> str:
		pass
	
	@staticmethod
	@abstractmethod
	def deserialize(raw: str) -> object:
		pass