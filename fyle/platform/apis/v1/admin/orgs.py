"""
V1 Admin Orgs
"""

from ....internals.list_resources import ListResources
from ....internals.get_resources import GetResources


class Orgs(ListResources, GetResources):
    """Class for Orgs APIs."""

    ORGS = '/orgs'

    def __init__(self, version, role):
        super().__init__(version, role, Orgs.ORGS)
