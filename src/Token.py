from uuid import uuid4

class Token:
    _token: str
    
    def __init__(self):
        self._token = uuid4()
    
    def getValue(self) -> str:
        return self._token