"""
V1 Admin Advance Requests
"""

from ....internals.list_resources import ListResources


class AdvanceRequests(ListResources):
    """Class for Advance Requests APIs."""

    ADVANCE_REQUESTS = '/advance_requests'

    def __init__(self, version, role):
        super().__init__(version, role, AdvanceRequests.ADVANCE_REQUESTS)
