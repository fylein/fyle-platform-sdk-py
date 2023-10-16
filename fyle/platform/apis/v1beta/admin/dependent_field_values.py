"""
V1 Beta Admin Expense Fields
"""
from typing import Iterable
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources
from ....internals.get_resources import GetResources
from .... import exceptions


class DependentFieldValues(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Expense Fields APIs."""

    DEPENDENT_FIELD_VALUES = '/dependent_expense_field_values'
    BULK_CREATE_DEPENDENT_EXPENSE_FIELDS_VALUES = '/dependent_expense_field_values/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, DependentFieldValues.DEPENDENT_FIELD_VALUES)

    def list_all(self, query_params=None) -> Iterable:
        query_params = {} if query_params is None else query_params
        if 'expense_field_id' not in query_params:
            raise exceptions.WrongParamsError('expense_field_id and limit are not supported query params.')
        if 'parent_expense_field_id' not in query_params:
            raise exceptions.WrongParamsError('parent_expense_field_id and limit are not supported query params.')
        return super().list_all(query_params)

    def bulk_post_dependent_expense_field_values(self, payload):
        return self.api.make_post_request(
            api_url=DependentFieldValues.BULK_CREATE_DEPENDENT_EXPENSE_FIELDS_VALUES,
            payload=payload
        )
