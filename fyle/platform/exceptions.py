"""
    Contains SDK exceptions
"""


class PlatformError(Exception):
    """The base exception class for FyleSDK.

    Parameters:
        msg (str): Short description of the error.
        response: Error response from the API call.
    """

    def __init__(self, msg, response=None):
        super(PlatformError, self).__init__(msg)
        self.message = msg
        self.response = response

    def __str__(self):
        if isinstance(self.response, dict):
            return repr(self.response)
        return repr(self.message)


class NotFoundClientError(PlatformError):
    """Client not found OAuth2 authorization, 404 error."""
    pass


class UnauthorizedClientError(PlatformError):
    """Wrong client secret and/or refresh token, 401 error."""
    pass


class ExpiredTokenError(PlatformError):
    """Expired (old) access token, 498 error."""
    pass


class InvalidTokenError(PlatformError):
    """Wrong/non-existing access token, 401 error."""
    pass


class NoPrivilegeError(PlatformError):
    """The user has insufficient privilege, 403 error."""
    pass


class WrongParamsError(PlatformError):
    """Some of the parameters (HTTP params or request body) are wrong, 400 error."""
    pass


class NotFoundItemError(PlatformError):
    """Not found the item from URL, 404 error."""
    pass


class InternalServerError(PlatformError):
    """The rest FyleSDK errors, 500 error."""
    pass


class RetryException(Exception):
    pass
