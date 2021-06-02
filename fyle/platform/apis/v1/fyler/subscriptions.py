"""
V1 Fyler Subscriptions
"""

from ....internals.post_resources import PostResources


class Subscriptions(PostResources):
    """Class for Reports APIs."""

    SUBSCRIPTIONS = '/subscriptions'

    def __init__(self, version, role):
        super().__init__(version, role, Subscriptions.SUBSCRIPTIONS)
