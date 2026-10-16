"""
V1 Admin Categories
"""

from ....internals.list_resources import ListResources
from ....internals.list_all_resources import ListAllResources
from ....internals.post_resources import PostResources
from ....internals.post_bulk_resources import PostBulkResources

class Categories(ListResources, ListAllResources, PostResources, PostBulkResources):
    """Class for Categories APIs."""

    CATEGORIES = '/categories'
    CATEGORIES_DELETE_BULK = '/categories/delete/bulk'
    CATEGORIES_DELETE_SUMMARY_BULK = '/categories/delete_summary/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, Categories.CATEGORIES)

    def delete_summary_bulk(self, data):
        return self.post(Categories.CATEGORIES_DELETE_SUMMARY_BULK, data)

    def delete_bulk(self, data):
        return self.post(Categories.CATEGORIES_DELETE_BULK, data)
