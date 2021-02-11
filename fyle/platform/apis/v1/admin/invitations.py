"""
V1 Admin Employees
"""
from ....internals.bulk_post_resources import BulkPostResources


class Invitations(BulkPostResources):
    """Class for Invitations APIs."""

    INVITATIONS_BULK = '/invitations/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, Invitations.INVITATIONS_BULK)
