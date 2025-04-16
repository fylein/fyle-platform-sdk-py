"""
V1 Admin Subscriptions
"""

from ....internals.list_resources import ListResources
from ....internals.list_all_resources import ListAllResources
from ....internals.post_resources import PostResources

class Subscriptions(ListResources, ListAllResources, PostResources):
    """Class for Subscriptions APIs."""

    SUBSCRIPTIONS = '/subscriptions'

    def __init__(self, version, role):
        super().__init__(version, role, Subscriptions.SUBSCRIPTIONS)
