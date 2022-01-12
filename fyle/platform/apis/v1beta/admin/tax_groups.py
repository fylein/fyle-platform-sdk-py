"""
V1 Beta Admin Tax Groups
"""

from typing import Dict, List
from fyle.platform.internals.post_bulk_resources import PostBulkResources
from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class TaxGroups(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Tax Groups APIs."""

    TAX_GROUPS = '/tax_groups'
    BULK_TAX_GROUPS = '/tax_groups/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, TaxGroups.TAX_GROUPS)

    def post_bulk(self, payload: List[Dict]):

        return self.api.make_post_request(
            api_url=TaxGroups.BULK_TAX_GROUPS,
            payload=payload
        )
