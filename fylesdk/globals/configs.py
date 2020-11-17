"""
    Defines Global SDK Configurations
"""

import configparser

configurations = {
    'FYLE': {
        'TOKEN_URL': None,
        'SERVER_URL': None
    },
    'AUTH': {
        'REFRESH_TOKEN': None,
        'ACCESS_TOKEN': None
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
