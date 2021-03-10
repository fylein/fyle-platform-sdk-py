import os

from fyle.platform import Platform


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
