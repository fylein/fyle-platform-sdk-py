from ....internals.post_resources import PostResources


class Reports(PostResources):

    REPORTS = '/reports'
    MARK_AS_PAID = '/reports/mark_paid/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, Reports.REPORTS)

    def bulk_mark_as_paid(self, payload):
        return self.api.make_post_request(
            api_url=Reports.MARK_AS_PAID,
            payload=payload
        )
