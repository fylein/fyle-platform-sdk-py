"""
V1 Admin Reimbursements
"""

from typing import Dict

from ....internals.list_resources import ListResources


class Reimbursements(ListResources):
    """Class for Reimbursements APIs."""

    REIMBURSEMENTS = '/reimbursements'

    def __init__(self, version, role):
        super().__init__(version, role, Reimbursements.REIMBURSEMENTS)
