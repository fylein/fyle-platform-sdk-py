"""
    Contains general serializers
"""

import enum
import json
from datetime import date, datetime

from requests import Response


class GeneralObject:
    """Class for General Object"""

    def __init__(self, object_as_dict):
        self.__dict__ = object_as_dict

    def to_json(self):
        """Class method to convert dict to json"""
        return json.loads(serialize(self))

    def get(self, item, default=None):
        """Class method for get item"""
        return self.__dict__.get(item, default)

    def __getattr__(self, item):
        return None

    def __repr__(self):
        return self.__dict__.__str__()


def deserialize(dictionary):
    """General JSON deserializer method"""
    if not isinstance(dictionary, dict):
        return dictionary

    for key, value in dictionary.items():
        if isinstance(value, dict):
            deserialized_value = deserialize(value)
            dictionary[key] = deserialized_value
        elif isinstance(value, list):
            for index, item in enumerate(value):
                deserialized_item = deserialize(item)
                value[index] = deserialized_item
            dictionary[key] = value
    deserialized_object = GeneralObject(dictionary)
    return deserialized_object


class ComplexEncoder(json.JSONEncoder):
    """Class for Custom JSON Encoder"""

    def default(self, o):
        if isinstance(o, Response):
            try:
                encoded_obj = o.json()
            except Exception:
                encoded_obj = {}
        elif isinstance(o, date):
            encoded_obj = o.isoformat()
        elif isinstance(o, datetime):
            encoded_obj = o.isoformat() + "Z"
        elif isinstance(o, enum.Enum):
            encoded_obj = o.value
        elif isinstance(o, GeneralObject):
            encoded_obj = o.__dict__
        elif hasattr(o, '__class__'):
            if hasattr(o, 'serialize'):
                encoded_obj = o.serialize()
            else:
                return None
        elif isinstance(o, Exception):
            encoded_obj = {
                "error": o.__class__.__name__,
                "args": o.args,
            }
        else:
            encoded_obj = json.JSONEncoder.default(self, o)

        return encoded_obj


def serialize(instance, **kwargs):
    """JSON serializer method"""
    return json.dumps(instance, cls=ComplexEncoder, **kwargs)
