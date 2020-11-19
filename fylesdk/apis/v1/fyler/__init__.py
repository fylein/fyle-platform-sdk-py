"""
	Initializing Fyler API's
"""

from .expense_comments import ExpenseComments

from ..version import version

role = 'fyler'

expense_comments = ExpenseComments(version, role)
