"""
    Defines Global SDK Configurations
"""

from flask import Flask

class Configurations:
    """Defines SDK Configurations"""

    SERVER_URL = None
    ACCESS_TOKEN = None

sdk = Flask('fyleplatformsdk')
sdk.config.from_object(Configurations)
