"""
V1 Admin Invitations
"""
from fyle.platform.internals.post_bulk_resources import PostBulkResources


class Invitations(PostBulkResources):
    """Class for Invitations APIs."""

    INVITATIONS_BULK = '/invitations/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, Invitations.INVITATIONS_BULK)
