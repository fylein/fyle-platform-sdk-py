"""
V1 Beta Admin Expense Fields
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources
from ....internals.get_resources import GetResources
from .... import exceptions


class ExpenseFields(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Expense Fields APIs."""

    EXPENSE_FIELDS = '/expense_fields'

    def __init__(self, version, role):
        super().__init__(version, role, ExpenseFields.EXPENSE_FIELDS)

    def get(self, query_params=None):
        """
        Get Expense Fields
        :return: expense-fields list
        """
        query_params = {} if query_params is None else query_params

        response = self.api.make_get_request(
            api_url=self.endpoint,
            query_params=query_params,
        )

        if response is None or response['data'] is None or response['data'] == []:
            raise exceptions.NotFoundItemError('Not found item with ID')

        return response
