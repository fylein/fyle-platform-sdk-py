"""
V1 Common Data Extraction
"""

from typing import Dict

from ....internals.api_base import ApiBase


class DataExtraction:
    """Class for Data Extraction APIs."""

    GET_EXPENSE_EXTRACT = '/expense_extract'

    def __init__(self, version, role):
        self.version = version
        self.role = role

    def extract_expense(self, payload) -> Dict:
        """
        Extracts the expense details from a reciept
        :param payload: Expense object
        :return: expenses Object
        """
        api = ApiBase(self.version, self.role)

        return api.make_post_request(
            api_url=DataExtraction.GET_EXPENSE_EXTRACT,
            payload=payload
        )
