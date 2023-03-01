"""
V1 Beta Admin Expense Fields
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources
from ....internals.get_resources import GetResources


class ExpenseFields(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Expense Fields APIs."""

    EXPENSE_FIELDS = '/expense_fields'
    DEPENDENT_EXPENSE_FIELDS_VALUES = '/dependent_expense_field_values'
    BULK_CREATE_DEPENDENT_EXPENSE_FIELDS_VALUES = '/dependent_expense_field_values/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, ExpenseFields.EXPENSE_FIELDS)


    def get_dependent_expense_field_values(self):
        return self.api.make_get_request(
            api_url=ExpenseFields.DEPENDENT_EXPENSE_FIELDS_VALUES
        )

    def bulk_post_dependent_expense_field_values(self, payload):
        return self.api.make_post_request(
            api_url=ExpenseFields.BULK_CREATE_DEPENDENT_EXPENSE_FIELDS_VALUES,
            payload=payload
        )
