"""
V1 Beta Admin Files
"""
import base64

import requests

from fyle.platform import exceptions
from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Files(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Files APIs."""

    FILES = '/files'
    BULK_GENERATE_FILES_URLS = '/files/generate_urls/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, Files.FILES)
        super().__init__(version, role, Files.BULK_GENERATE_FILES_URLS)

    def create_file(self, payload):
        return self.api.make_post_request(
            api_url=Files.FILES,
            payload=payload
        )

    def upload_file_to_aws(self, content_type, data, url):
        """Create an File.

        Parameters:
            content_type (str): Content type of file. Example application/json for JSON
            data (file): File data as Base64 string.
            url (str): AWS S3 upload URL.

        Returns:
            True
        """
        try:
            base64.b64decode(data)
        except Exception:
            raise exceptions.WrongParamsError('Invalid base64')

        headers = {"Content-Type": content_type}
        requests.put(url=url, data=base64.b64decode(data), headers=headers)
        return True

    def bulk_generate_file_urls(self, payload):
        return self.api.make_post_request(
            api_url=Files.BULK_GENERATE_FILES_URLS,
            payload=payload
        )
