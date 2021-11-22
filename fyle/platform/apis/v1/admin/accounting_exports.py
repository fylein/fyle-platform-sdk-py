"""
V1 Beta Admin Accounting Exports
"""
from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class AccountingExports(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Accounting Exports APIs."""

    ACCOUNTING_EXPORTS = '/accounting_exports'
    ACCOUNTING_EXPORT_LINEITEMS = '/accounting_export_lineitems'
    BULK_CREATE_ACCOUNTING_EXPORT_LINEITEMS = '/accounting_export_lineitems/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, AccountingExports.ACCOUNTING_EXPORTS)
        super().__init__(version, role, AccountingExports.ACCOUNTING_EXPORT_LINEITEMS)

    def create_accounting_exports(self, payload):
        return self.api.make_post_request(
            api_url=AccountingExports.ACCOUNTING_EXPORTS,
            payload=payload
        )

    def create_accounting_export_lineitems(self, payload):
        return self.api.make_post_request(
            api_url=AccountingExports.ACCOUNTING_EXPORT_LINEITEMS,
            payload=payload
        )

    def bulk_create_accounting_export_lineitems(self, payload):
        return self.api.make_post_request(
            api_url=AccountingExports.BULK_CREATE_ACCOUNTING_EXPORT_LINEITEMS,
            payload=payload
        )
