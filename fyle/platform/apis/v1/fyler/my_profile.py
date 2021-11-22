"""
V1 Beta Spender My Profile
"""
from typing import Dict

from .... import exceptions
from ....internals.get_resources import GetResources


class MyProfile(GetResources):
    """Class for My Profile API."""

    MY_PROFILE = '/my_profile'

    def __init__(self, version, role):
        super().__init__(version, role, MyProfile.MY_PROFILE)

    def get_by_id(self, id_: str) -> Dict:
        raise NotImplementedError()

    def get(self) -> Dict:
        """
        Get Single Resource object by ID
        :return: Resource Object
        """
        query_params = {}

        response = self.api.make_get_request(
            api_url=self.endpoint,
            query_params=query_params,
        )

        if response is None or response['data'] is None or response['data'] == {}:
            raise exceptions.NotFoundItemError('Not found item with ID')

        return response
