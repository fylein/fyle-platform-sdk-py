"""
V1 Admin Expense Fields
"""
from typing import Iterable
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources
from ....internals.get_resources import GetResources
from .... import exceptions


class DependentExpenseFieldValues(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Dependent Expense Field Values APIs."""

    DEPENDENT_FIELD_VALUES = '/dependent_expense_field_values'
    BULK_CREATE_DEPENDENT_EXPENSE_FIELDS_VALUES = '/dependent_expense_field_values/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, DependentExpenseFieldValues.DEPENDENT_FIELD_VALUES)

    def list_all(self, query_params=None) -> Iterable:
        query_params = {} if query_params is None else query_params
        if 'expense_field_id' not in query_params:
            raise exceptions.WrongParamsError('expense_field_id is a mandatory query param.')
        if 'parent_expense_field_id' not in query_params:
            raise exceptions.WrongParamsError('parent_expense_field_id is a mandatory query param.')
        return super().list_all(query_params)

    def bulk_post_dependent_expense_field_values(self, payload):
        return self.api.make_post_request(
            api_url=DependentExpenseFieldValues.BULK_CREATE_DEPENDENT_EXPENSE_FIELDS_VALUES,
            payload=payload
        )
