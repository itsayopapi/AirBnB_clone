#!/usr/bin/python3
"""
base model
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
defines all common attributes from other classes:
Public instance attributes:
id: string - assign with an uuid when an instance is created:
you can use uuid.uuid4() to generate unique id but don’t forget to
 convert to a string
the goal is to have unique id for each BaseModel
created_at: datetime - assign with the current datetime when an instance
 is created
updated_at: datetime - assign with the current datetime when an 
instance is created and it will be updated every time you change your object
__str__: should print: [<class name>] (<self.id>) <self.__dict__>
Public instance methods:
save(self): updates the public instance attribute updated_at
 with the current datetime
to_dict(self): returns a dictionary containing all keys/values
 of __dict__ of the instance:
by using self.__dict__, only instance attributes set will be returned
a key __class__ must be added to this dictionary with the class
 name of the object
created_at and updated_at must be converted to string object in ISO format:
format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
you can use isoformat() of datetime object

    """

    def __init__(self, *args, **kwargs):
        """
        Initlizes the public attributes of the instance after creation
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """

        TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, TIME_FORMAT)
                elif key == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        returns the string representation of a class
        """        
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """
        updates the public instance attribute with current datetime
        """
        self.update_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict_repr["__class__"] = type(self).__name__
        return dict_repr
