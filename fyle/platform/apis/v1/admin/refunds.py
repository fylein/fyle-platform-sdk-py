"""
V1 Admin Refunds
"""

from ....internals.list_resources import ListResources


class Refunds(ListResources):
    """Class for Refunds APIs."""

    REFUNDS = '/refunds'

    def __init__(self, version, role):
        super().__init__(version, role, Refunds.REFUNDS)
