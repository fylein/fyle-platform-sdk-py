"""
V1 Beta Approver Reports
"""

from ....internals.get_resources import GetResources
from ....internals.list_resources import ListResources


class Reports(ListResources, GetResources):
    """Class for Reports APIs."""

    REPORTS = '/reports'
    PARTIALLY_APPROVE_REPORT = '/reports/partially_approve'

    def __init__(self, version, role):
        super().__init__(version, role, Reports.REPORTS)

    def approve(self, id_):
        """
        To approve the report
        :param id_: id of report to be approved
        :return: partially_approved_report
        """
        partially_approve_report_url = Reports.PARTIALLY_APPROVE_REPORT
        return self.api.make_post_request(
            api_url=partially_approve_report_url,
            payload={
                'data': {
                    'id': id_
                }
            }
        )
