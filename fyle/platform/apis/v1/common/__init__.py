"""
	Initializing Common API's
"""

from .data_extraction import DataExtraction
from .places import Places
from ..version import version

role = 'common'

places = Places(version, role)
data_extraction = DataExtraction(version, role)
