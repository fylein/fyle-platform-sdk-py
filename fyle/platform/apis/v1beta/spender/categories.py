"""
V1 Beta Spender Categories
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class Categories(ListResources, ListAllResources):
    """Class for Category APIs."""

    CATEGORIES = '/categories'

    def __init__(self, version, role):
        super().__init__(version, role, Categories.CATEGORIES)
