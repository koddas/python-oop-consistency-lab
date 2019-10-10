from entities.serializable import Serializable

class Storage:
    '''
    Storage represents a file storage that stores and retrieves objects
    '''
    
    def __init__(self):
        pass
    
    def save(self, filename: str, data: Serializable) -> bool:
        '''
        Stores a serializable object. If the object isn't explicitly marked as
        being serializable, this method will fail.
        '''
        if not issubclass(data.__class__, Serializable):
            return False
        
        f = open(filename, "w")
        f.write(data.serialize())
        f.close()
        
        return True
    
    def read(self, filename: str, class_name: type) -> Serializable:
        '''
        Retrieves a serialized object. You specify the type of he object to
        deserialize by passing the class (as a type, not a string) as the
        second parameter.
        '''
        if not issubclass(class_name, Serializable):
            return None
        
        f = open(filename, "r")
        data = f.read()
        f.close()
        
        deserialized = class_name.deserialize(data)
        
        return deserialized