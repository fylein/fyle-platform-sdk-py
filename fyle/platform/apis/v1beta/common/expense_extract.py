"""
V1 Beta Common Expense Extract
"""

from fyle.platform import exceptions
from ....internals.post_resources import PostResources


class ExpenseExtract(PostResources):
    """Class for Expense Extract APIs"""

    EXPENSE_EXTRACT = "/expense_extract/v1"

    def __init__(self, version, role) -> None:
        super().__init__(version, role, ExpenseExtract.EXPENSE_EXTRACT)

    def extract(self, file_name, b64_content):
        """
        To extract the expenses from images
        :param file_name: name of the file with extension
        :param b64_content: base64 encoded string of the file_object
        :return: extracted expense
        """
        if not file_name or not b64_content:
            raise exceptions.WrongParamsError(
                "Mandatory arguments missing: file_name, b64_content are mandatory arguments.")

        if not len(file_name.split('.')) > 1:
            raise exceptions.WrongParamsError(
                "Invalid Filename: Please add file extension")

        return self.post({
            "data": {
                "files": [{
                    "name": file_name,
                    'content': b64_content
                }]
            }
        })
