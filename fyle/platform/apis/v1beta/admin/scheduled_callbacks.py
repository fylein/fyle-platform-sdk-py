"""
V1 Admin Scheduled Callbacks
"""

from ....internals.list_resources import ListResources
from ....internals.list_all_resources import ListAllResources
from ....internals.post_resources import PostResources


class ScheduledCallbacks(ListResources, ListAllResources, PostResources):
    """Class for Scheduled Callbacks APIs."""

    SCHEDULED_CALLBACKS = '/scheduled_callbacks'

    def __init__(self, version, role):
        super().__init__(version, role, ScheduledCallbacks.SCHEDULED_CALLBACKS)
