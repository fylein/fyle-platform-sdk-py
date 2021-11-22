"""
V1 Beta Common Places
"""

from typing import Dict
from ....internals.get_resources import GetResources
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

        count = len(response["data"])
        if id_ and count < 1:
            raise exceptions.NotFoundItemError("Not found item with ID")
        elif id_ and count > 1:
            raise exceptions.MultipleObjectReturned("Multiple Objects returned")

        return response.get("data")[0]
