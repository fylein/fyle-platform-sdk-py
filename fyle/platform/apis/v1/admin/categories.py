"""
V1 Admin Categories
"""

from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Categories(ListResources, PostResources):
    """Class for Categories APIs."""

    CATEGORIES = '/categories'

    def __init__(self, version, role):
        super().__init__(version, role, Categories.CATEGORIES)
