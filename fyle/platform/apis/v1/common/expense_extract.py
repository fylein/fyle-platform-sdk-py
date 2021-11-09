"""
V1 Common Expense Extract
"""

from fyle.platform import exceptions
from ....internals.post_resources import PostResources


class ExpenseExtract(PostResources):
    """Class for Expense Extract APIs"""

    EXPENSE_EXTRACT = "/expense_extract/v1"

    def __init__(self, version, role) -> None:
        super().__init__(version, role, ExpenseExtract.EXPENSE_EXTRACT)

    def extract(self, params_object):
        """
        To extract the expenses from images
        :param params_object
        :return extracted expense
        """
        params_object = {} if params_object is None else params_object
        if not params_object.get('file_name') or not params_object.get('b64_content'):
            raise exceptions.WrongParamsError(
                "Mandatory query params missing: file_name, b64_content are mandatory query params.")

        if not len(params_object.get('file_name').split('.')) > 1:
            raise exceptions.WrongParamsError(
                "Invalid Filename: Please add file extension")

        return self.post({
            "data": {
                "files": [{
                    "name": params_object['file_name'],
                    'content': params_object['b64_content']
                }]
            }
        })
