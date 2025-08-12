from ....internals.list_resources import ListResources
from ....internals.list_all_resources import ListAllResources


class OrgSettings(ListResources, ListAllResources):
    """Class for Org Settings APIs."""

    ORG_SETTINGS = "/org_settings"

    def __init__(self, version, role):
        super().__init__(version, role, OrgSettings.ORG_SETTINGS)
