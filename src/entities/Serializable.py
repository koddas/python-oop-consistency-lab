from abc import ABC, abstractmethod

class Serializable(ABC):
	'''
	This abstract class describes an interface for serializable classes.
	'''
	
	@abstractmethod	
	def serialize(self) -> str:
		'''
		Converts the contents of this object into a string.
		'''
		pass
	
	@staticmethod
	@abstractmethod
	def deserialize(raw: str) -> object:
		'''
		Creates an object of the class based on serialized data.
		'''
		pass