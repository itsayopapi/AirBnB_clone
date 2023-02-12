#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """
        The BaseModel class defines the common attributes/methods for other classes.

        Public instance attributes:
	    - id : string - assign with an uuid when an instance is created. The
	        uuid must be unique for every instance.
	    - created_at: datetime - assign with the current datetime when an instace
                is created.
	    - updated_at: datetime - assign with the current datetime when an instance 
                is created and it will be updated every time you change your object.

        Public instance methods: save(), to_dict()
     """

    def __init__(self, *args, **kwargs):
        """
         The init method is the constructor for the base model
        """

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """returns the string representation of the base model object in the form:
           [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance object
            - only instance attributes set will be returned
            - a key __class__ is added with the class name of the object
            - created_at and updated_at must be converted to string object in ISO format object
		
	* Running the __dict__ method on the object helps understand this task * 
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                obj_dict = self.__dict__[key].isoformat()
        return obj_dict
