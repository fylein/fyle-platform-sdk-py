"""
V1 Fyler Cost Center
"""

from typing import Dict

from ...api_base import ApiBase


class CostCenters(ApiBase):
    """Class for Cost Center APIs."""

    LIST_COST_CENTERS = '/cost_centers'
    GET_COST_CENTERS = '/cost_centers/{id}'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, created_at=None, updated_at=None, only_enabled=None,
             limit=None, offset=None, order=None, **kwargs) -> Dict:
        """
        Get Cost Center
        :param created_at:
        :param updated_at:
        :param only_enabled:
        :param limit: No. of Cost Centers to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of Cost Centers Objects
        """
        return self.make_get_request(
            api_url=CostCenters.LIST_COST_CENTERS,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'only_enabled': only_enabled,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )

    def get(self, id) -> Dict:
        """
        Get Single Project by ID
        :param id: Project ID
        :return: Project Object
        """
        return self.make_get_request(
            api_url=CostCenters.GET_COST_CENTERS.format(id)
        )
