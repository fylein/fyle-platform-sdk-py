"""
    Defining Network related operations
"""

from fylePyLibs import assertions, exceptions, http

class Network:
    """Class for making GET, POST requests"""

    def _assert_response(self, response):
        if response.status_code == 400:
            assertions.assert_valid(
                False,
                'Some of the parameters are wrong, Response: {}'.format(response.text)
            )
        elif response.status_code == 401:
            assertions.assert_auth(
                None,
                'Invalid token, try to refresh it, Response: {}'.format(response.text)
            )
        elif response.status_code == 403:
            assertions.assert_true(
                False,
                'Forbidden, the user has insufficient privilege, Response: {}'.format(response.text)
            )
        elif response.status_code == 404:
            assertions.assert_found(
                False,
                'Not found item with ID, Response: {}'.format(response.text)
            )
        elif response.status_code == 498:
            assertions.assert_auth(
                False,
                'Expired token, try to refresh it, Response: {}'.format(response.text)
            )
        elif response.status_code == 500:
            assertions.assert_good(
                False,
                'Internal server error, Response: {}'.format(response.text)
            )
        else:
            raise exceptions.InvalidUsage(response.text, response.status_code)


    def _get_request(self, url, *args, **kwargs):
        """Create a HTTP GET request.

        Parameters:
            params (dict): HTTP GET parameters for the wanted API.
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """

        return http.get(url, *args, **kwargs)


    def _post_request(self, url, **kwargs):
        """Create a HTTP post request.

        Parameters:
            data (dict): HTTP POST body data for the wanted API.
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """
        return http.post(url, **kwargs)
