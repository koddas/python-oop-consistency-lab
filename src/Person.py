class Person:
    _first_name: str
    _last_name: str
    
    def __init__(self):
        self._first_name = ""
        self._last_name = ""
    
    def set_first_name(self, name: str) -> None:
        self._first_name = name
    
    def get_first_name(self) -> str:
        return self._first_name
    
    def set_last_name(self, name: str) -> None:
        self._last_name = name
    
    def get_last_name(self) -> str:
        return self._last_name
    
    def get_full_name(self) -> str:
        return self._first_name + " " + self._last_name