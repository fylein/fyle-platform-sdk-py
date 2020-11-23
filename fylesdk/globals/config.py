"""
    Defines Global SDK Configurations
"""

import configparser

configurations = {
    'FYLE': {
        'TOKEN_URL': '',
        'SERVER_URL': ''
    },
    'AUTH': {
        'REFRESH_TOKEN': '',
        'ACCESS_TOKEN': ''
    }
}

config = configparser.ConfigParser()
config.read_dict(configurations)

# from flask import Flask

# class Configurations:
#     """Defines SDK Configurations"""

#     SERVER_URL = None
#     ACCESS_TOKEN = None

# sdk = Flask('fyleplatformsdk')
# sdk.config.from_object(Configurations)
