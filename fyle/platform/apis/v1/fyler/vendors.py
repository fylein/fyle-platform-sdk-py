"""
V1 Fyler Vendors
"""

from ....internals.list_resources import ListResources


class Vendors(ListResources):
    """Class for Vendors APIs."""

    VENDORS = '/vendors'

    def __init__(self, version, role):
        super().__init__(version, role, Vendors.VENDORS)
