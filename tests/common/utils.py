import json
import os


def get_admin_schema():
    with open('tests/schema/admin.json') as f:
        schema = json.load(f)
    return schema


def get_approver_schema():
    with open('tests/schema/approver.json') as f:
        schema = json.load(f)
    return schema


def get_fyler_schema():
    with open('tests/schema/fyler.json') as f:
        schema = json.load(f)
    return schema


def get_common_schema():
    with open('tests/schema/common.json') as f:
        schema = json.load(f)
    return schema


def fyle_connect():
    """
    Fyle platform SDK connector
    Returns:
        FylePlatformSDK class instance
    """
    assert os.getenv('SERVER_URL') is not None, 'SERVER_URL is not set'
    assert os.getenv('TOKEN_URL') is not None, 'TOKEN_URL is not set'
    assert os.getenv('CLIENT_ID') is not None, 'CLIENT_ID is not set'
    assert os.getenv('CLIENT_SECRET') is not None, 'CLIENT_SECRET is not set'
    assert os.getenv('REFRESH_TOKEN') is not None, 'REFRESH_TOKEN is not set'

    connection = Platform(
        server_url=os.environ['SERVER_URL'],
        token_url=os.environ['TOKEN_URL'],
        client_id=os.environ['CLIENT_ID'],
        client_secret=os.environ['CLIENT_SECRET'],
        refresh_token=os.environ['REFRESH_TOKEN']
    )
    return connection
