"""
V1 Approver Reports
"""

from ....internals.get_resources import GetResources
from ....internals.list_resources import ListResources


class Reports(ListResources, GetResources):
    """Class for Reports APIs."""

    REPORTS = '/reports'
    PARTIALLY_APPROVE_REPORT = '/reports/partially_approve'

    def __init__(self, version, role):
        super().__init__(version, role, Reports.REPORTS)

    def approve(self, id_, comment):
        """
        To approve the report
        :param id_: id of report to be approved
        :param comment: comment to be added along with approve action
        :return: partially_approved_report
        """
        partially_approve_report_url = Reports.PARTIALLY_APPROVE_REPORT
        return self.api.make_post_request(
            api_url=partially_approve_report_url,
            payload={
                'id': id_,
                'comment': comment
            }
        )
