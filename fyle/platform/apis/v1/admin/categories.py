"""
V1 Beta Admin Categories
"""

from ....internals.list_resources import ListResources
from ....internals.list_all_resources import ListAllResources
from ....internals.post_resources import PostResources


class Categories(ListResources, ListAllResources, PostResources):
    """Class for Categories APIs."""

    CATEGORIES = '/categories'

    def __init__(self, version, role):
        super().__init__(version, role, Categories.CATEGORIES)
