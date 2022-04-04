"""
V1 Beta Spender Files
"""
import requests

from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Files(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Files APIs."""

    FILES = '/files'
    GENERATE_FILE_URLS = '/files/generate_urls'

    def __init__(self, version, role):
        super().__init__(version, role, Files.FILES)

    def create_file(self, payload):
        return self.api.make_post_request(
            api_url=Files.FILES,
            payload=payload
        )

    def put_file_to_url(self, content_type, data, url):
        """Create an File.

        Parameters:
            content_type (str): Content type of file. Example application/json for JSON
            data (file): File data as binary string.
            url (str): AWS S3 upload URL.

        Returns:
            AWS S3 upload url.
        """

        headers = {"Content-Type": content_type}
        requests.put(url=url, data=data, headers=headers)
        return True

    def generate_file_urls(self, payload):
        return self.api.make_post_request(
            api_url=Files.GENERATE_FILE_URLS,
            payload=payload
        )
