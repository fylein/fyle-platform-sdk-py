"""
V1 Common Data Extraction
"""

from typing import Dict

from ...api_base import ApiBase


class DataExtraction(ApiBase):
    """Class for Data Extraction APIs."""

    GET_EXPENSE_EXTRACT = '/expense_extract'

    def __init__(self, version, role):
        super().__init__(version, role)

    def extract_expense(self, payload) -> Dict:
        """
        Extracts the expense details from a reciept
        :param payload: Expense object
        :return: expenses Object
        """
        return self.make_post_request(
            api_url=DataExtraction.GET_EXPENSE_EXTRACT,
            payload=payload
        )
