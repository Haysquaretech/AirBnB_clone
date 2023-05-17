#!/usr/bin/python3
""" BaseModel Class encapsulating all services """
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ BaseModel Class Abstraction """
    def __init__(self, *args, **kwargs):
        """
            Class constructor with attributes:
            id: uuid unique identifier string
            created_at: datatime
            updated_at: datetime
        """
        if kwargs:
            del(kwargs['__class__'])
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            return self.__dict__.update(kwargs)

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ print string """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates updated_at """
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """ dictionary representation """
        new_dict = {}
        new_dict.update(self.__dict__)
        new_dict.update({'__class__': type(self).__name__})
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict