"""
V1 Admin Cost Center
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources
from ....internals.post_bulk_resources import PostBulkResources

class CostCenters(ListResources, ListAllResources, PostResources, PostBulkResources):
    """Class for Cost Center APIs."""

    COST_CENTERS = '/cost_centers'
    COST_CENTERS_DELETE_BULK = '/cost_centers/delete/bulk'
    COST_CENTERS_DELETE_SUMMARY_BULK = '/cost_centers/delete_summary/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, CostCenters.COST_CENTERS)

    def delete_summary_bulk(self, data):
        return self.api.make_post_request(
            api_url=CostCenters.COST_CENTERS_DELETE_SUMMARY_BULK,
            payload=data
        )

    def delete_bulk(self, data):
        return self.api.make_post_request(
            api_url=CostCenters.COST_CENTERS_DELETE_BULK,
            payload=data
        )
