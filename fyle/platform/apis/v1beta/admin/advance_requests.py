"""
V1 Beta Admin Advance Requests
"""

from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class AdvanceRequests(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Advance Requests APIs."""

    ADVANCE_REQUESTS = '/advance_requests'

    def __init__(self, version, role):
        super().__init__(version, role, AdvanceRequests.ADVANCE_REQUESTS)
