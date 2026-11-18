from ....internals.post_resources import PostResources
from ....internals.list_all_resources import ListAllResources


class Reports(ListAllResources, PostResources):

    REPORTS = '/reports'
    MARK_AS_PAID = '/reports/mark_paid/bulk'
    RESET_ACCOUNTING_EXPORT_SUMMARY = '/reports/reset_accounting_export_summary/bulk'


    def __init__(self, version, role):
        super().__init__(version, role, Reports.REPORTS)

    def bulk_mark_as_paid(self, payload):
        return self.api.make_post_request(
            api_url=Reports.MARK_AS_PAID,
            payload=payload
        )

    def bulk_reset_accounting_export_summary(self, payload):
        return self.api.make_post_request(
            api_url=Reports.RESET_ACCOUNTING_EXPORT_SUMMARY,
            payload=payload
        )
