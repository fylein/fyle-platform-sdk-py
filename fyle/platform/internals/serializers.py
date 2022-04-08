"""
    Contains general serializers
"""

import json

class GeneralObject:
    """Class for General Object"""

    def __init__(self, object_as_dict):
        self.__dict__ = object_as_dict


def deserialize(dictionary):
    """General JSON deserializer method"""
    deserialized_object = GeneralObject(dictionary)
    return deserialized_object


def serialize(instance):
    """JSON serializer method"""
    return json.dumps(instance)
