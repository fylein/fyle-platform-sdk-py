"""
V1 Admin Advance Requests
"""

from typing import Dict

from ...api_base import ApiBase


class AdvanceRequests(ApiBase):
    """Class for Advance Requests APIs."""

    GET_ADVANCE_REQUESTS = '/advance_requests'

    def __init__(self, version, role):
        super().__init__(version, role)
