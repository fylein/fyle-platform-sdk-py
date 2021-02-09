"""
    Defines Delete resource class.
"""

from .api_base import ApiBase


class DeleteResources(ApiBase):
    """Delete Resource Class"""

    def __init__(self, version, role, endpoint):
        self.version = version
        self.role = role
        self.endpoint = endpoint

        api = super().__init__(self.version, self.role)
        self.make_get_request = api.make_get_request

    def delete(self, id_: str):
        """
        Deletes the resource object
        :param id_: resource object id
        :return: Status
        """
        return self.make_delete_request(
            api_url='{endpoint}/{id}'.format(endpoint=self.endpoint, id=id_)
        )
