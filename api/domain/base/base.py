import uuid
from datetime import datetime
from api.util.regex import regex


class Base():
    def __init__(self):
        self.id = uuid.uuid4().hex
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        self.updatedAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        self.isActive = True
        self.deletedAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        
    def get_String(self, value:str, name:str)->str:
      
        if regex.match(value) is None:
            raise ValueError(f'{name} is required')
        return value