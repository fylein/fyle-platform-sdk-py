"""
V1 Beta Admin Reimbursements
"""

from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources
from ....internals.post_bulk_resources import PostBulkResources



class Reimbursements(ListResources, ListAllResources, PostResources, GetResources, PostBulkResources):
    """Class for Reimbursements APIs."""

    REIMBURSEMENTS = '/reimbursements'

    def __init__(self, version, role):
        super().__init__(version, role, Reimbursements.REIMBURSEMENTS)
