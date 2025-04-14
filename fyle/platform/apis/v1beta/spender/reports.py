"""
V1 Spender Reports
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Reports(ListResources, ListAllResources, PostResources):
    """Class for Report APIs."""

    REPORTS = '/reports'
    ADD_EXPENSE_TO_REPORT = '/reports/add_expenses'
    SUBMIT_REPORT = '/reports/submit'

    def __init__(self, version, role):
        super().__init__(version, role, Reports.REPORTS)
 
    
    def add_expense_to_report(self, payload):
        return self.api.make_post_request(
            api_url=Reports.ADD_EXPENSE_TO_REPORT,
            payload=payload
        )


    def submit_report(self, payload):
        return self.api.make_post_request(
            api_url=Reports.SUBMIT_REPORT,
            payload=payload
        )
