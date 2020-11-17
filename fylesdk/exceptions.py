class FylePlatformSDKError(Exception):
    """The base exception class for FyleSDK.

    Parameters:
        msg (str): Short description of the error.
        response: Error response from the API call.
    """

    def __init__(self, msg, response=None):
        super(FylePlatformSDKError, self).__init__(msg)
        self.message = msg
        self.response = response

    def __str__(self):
        if isinstance(self.response, dict):
            return repr(self.response)
        return repr(self.message)


class NotFoundClientError(FylePlatformSDKError):
    """Client not found OAuth2 authorization, 404 error."""
    pass


class UnauthorizedClientError(FylePlatformSDKError):
    """Wrong client secret and/or refresh token, 401 error."""
    pass


class ExpiredTokenError(FylePlatformSDKError):
    """Expired (old) access token, 498 error."""
    pass


class InvalidTokenError(FylePlatformSDKError):
    """Wrong/non-existing access token, 401 error."""
    pass


class NoPrivilegeError(FylePlatformSDKError):
    """The user has insufficient privilege, 403 error."""
    pass


class WrongParamsError(FylePlatformSDKError):
    """Some of the parameters (HTTP params or request body) are wrong, 400 error."""
    pass


class NotFoundItemError(FylePlatformSDKError):
    """Not found the item from URL, 404 error."""
    pass
    

class InternalServerError(FylePlatformSDKError):
    """The rest FyleSDK errors, 500 error."""
    pass