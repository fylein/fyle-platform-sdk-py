"""
V1 Admin Advances
"""

from ....internals.list_resources import ListResources


class Advances(ListResources):
    """Class for Advances APIs."""

    ADVANCES = '/advances'

    def __init__(self, version, role):
        super().__init__(version, role, Advances.ADVANCES)
