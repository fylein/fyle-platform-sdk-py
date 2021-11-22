"""
V1 Beta Admin Employees
"""

from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Employees(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Employees APIs."""

    EMPLOYEES = '/employees'

    def __init__(self, version, role):
        super().__init__(version, role, Employees.EMPLOYEES)

    def invite_bulk(self, payload):
        invite_bulk_api = '{}/{}'.format(self.endpoint, 'invite/bulk')
        return self.api.make_post_request(
            api_url=invite_bulk_api,
            payload=payload
        )
