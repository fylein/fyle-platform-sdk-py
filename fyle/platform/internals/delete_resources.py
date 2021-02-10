"""
    Defines Delete resource class.
"""

from .api_base import ApiBase


class DeleteResources:
    """Delete Resource Class"""

    def __init__(self, version, role, endpoint):
        self.version = version
        self.role = role
        self.endpoint = endpoint

        self.api = ApiBase(self.version, self.role)

    def delete(self, id_: str):
        """
        Deletes the resource object
        :param id_: resource object id
        :return: Status
        """
        return self.api.make_delete_request(
            api_url='{endpoint}/{id}'.format(endpoint=self.endpoint, id=id_)
        )
