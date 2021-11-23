"""
V1 Beta Common Places
"""

from typing import Dict
from ....internals.get_resources import GetResources
from ....internals.list_resources import ListResources
from .... import exceptions


class Places(GetResources):
    """Class for Places APIs."""

    PLACES = "/places"

    def __init__(self, version, role):
        super().__init__(version, role, Places.PLACES)

    def get_by_id(self, id_) -> Dict:
        api_url = self.endpoint

        if not id_:
            raise exceptions.WrongParamsError("Invalid Parameters")

        query_params = {"id": id_}
        response = self.api.make_get_request(
            api_url=api_url,
            query_params=query_params,
        )

        if id_ and response["count"] < 1:
            raise exceptions.NotFoundItemError("Not found item with ID")
        elif id_ and response["count"] > 1:
            raise exceptions.MultipleObjectReturned("Multiple Objects returned")

        return response.get("data")[0]

class PlacesAutocomplete(ListResources):
    """Class for Places autocomplete APIs."""

    PLACESAUTOCOMPLETE = "/places/autocomplete"

    def __init__(self, version, role):
        super().__init__(version, role, PlacesAutocomplete.PLACESAUTOCOMPLETE)

    def list(self, q, types=None, location=None) -> Dict:
        """
        Get Resources
        :param query_params:
        :return: List of Places Objects
        """
        if not q:
            raise exceptions.WrongParamsError("Invalid Parameters")
        query_params = { 
            'q': q
        }

        if types:
            query_params['types'] = types

        if location:
            query_params['location'] = location

        return self.api.make_get_request(
            api_url=self.endpoint,
            query_params=query_params
        )
