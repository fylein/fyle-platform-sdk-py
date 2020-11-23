import logging

import jsonschema

logger = logging.getLogger(__name__)


def test_post_report_approvals(fyle, approver_schema):
    """
    Test Fyle report approvals post call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    payload = {'data': [{'id': 'rphs782hj245'}]}

    report_approvals = fyle.v1.approver.report_approvals.post(payload=payload)
    url = report_approvals.get('url')
    print(url)

    report_approvals_schema = approver_schema.get(url).get('post').get('responses').get('200')
    jsonschema.validate(instance=report_approvals, schema=report_approvals_schema)
