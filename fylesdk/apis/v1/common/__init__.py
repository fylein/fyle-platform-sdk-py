"""
	Initializing Common API's
"""

from .places import Places

from ..version import version

role = 'common'

places = Places(version, role)
