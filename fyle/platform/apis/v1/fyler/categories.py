"""
V1 Fyler Categories
"""

from typing import Dict

from ....internals.list_resources import ListResources


class Categories(ListResources):
    """Class for Categories APIs."""

    CATEGORIES = '/categories'

    def __init__(self, version, role):
        super().__init__(version, role, Categories.CATEGORIES)
