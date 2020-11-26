"""
V1 Admin Advance Requests
"""

from typing import Dict

from ....internals.get_resources import GetResources


class AdvanceRequests(GetResources):
    """Class for Advance Requests APIs."""

    ADVANCE_REQUESTS = '/advance_requests'

    def __init__(self, version, role):
        super().__init__(version, role, AdvanceRequests.ADVANCE_REQUESTS)
