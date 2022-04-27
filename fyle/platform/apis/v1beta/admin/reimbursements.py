"""
V1 Beta Admin Reimbursements
"""

from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Reimbursements(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Reimbursements APIs."""

    REIMBURSEMENTS = '/reimbursements'
    BULK_POST_REIMBURSEMENTS = '/reimbursements/mark_paid/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, Reimbursements.REIMBURSEMENTS)
    
    def bulk_post_reimbursements(self, payload):
        return self.api.make_post_request(
            api_url=Reimbursements.BULK_POST_REIMBURSEMENTS,
            payload=payload
        )
