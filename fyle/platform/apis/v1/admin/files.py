"""
V1 Admin Files
"""

from ....internals.post_resources import PostResources
from ....internals.get_resources import GetResources


class Files(PostResources, GetResources):
    """Class for Files APIs."""

    FILES = '/files'

    def __init__(self, version, role):
        super().__init__(version, role, Files.FILES)
