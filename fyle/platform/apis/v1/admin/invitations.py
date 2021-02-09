"""
V1 Admin Employees
"""

from ....internals.post_resources import PostResources


class InvitationsBulk(PostResources):
    """Class for Invitations APIs."""

    INVITATIONS_BULK = '/invitations/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, InvitationsBulk.INVITATIONS_BULK)
