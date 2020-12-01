"""
	Initializing Common API's
"""

from .places import Places
from .data_extraction import DataExtraction

from ..version import version

role = 'common'

places = Places(version, role)
data_extraction = DataExtraction(version, role)
