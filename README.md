# Fyle

Python SDK for accessing Fyle Platform APIs. [Fyle](https://www.fylehq.com/) is an expense management system.

## Installation

This project requires [Python 3+](https://www.python.org/downloads/) and [Requests](https://pypi.org/project/requests/) library (pip install requests).

1. Download this project and use it (copy it in your project, etc).
2. Install it from [pip](https://pypi.org).
        
        $ pip install fyle

## Usage

To use this SDK you'll need these Fyle credentials used for OAuth2 authentication: **client ID**, **client secret** and **refresh token**. You can follow the steps on this [Article](https://help.fylehq.com/en/articles/3045578-integrating-with-fyle) or reach out to support@fylehq.com.

This SDK is very easy to use.
* First you'll need to create a connection using the main class Platform.
```python
from fyle.platform import Platform

fyle = Platform(
    server_url='FYLE SERVER URL',
    token_url='FYLE TOKEN URL',
    refresh_token='FYLE REFRESH TOKEN',
    client_id='FYLE CLIENT ID',
    client_secret='FYLE CLIENT SECRET'
)
```

*  You can access the V1beta version of the APIs as follows:
```python
"""
USAGE: <Platform INSTANCE>.<VERSION: eg. v1beta>.<FYLE ROLE: eg. admin>.<API_NAME: eg. expenses>.<API_METHOD: eg. get>(<PARAMETERS>)
"""

# Get a list of all Expenses in a paginated manner and add to a list
expenses = []

query_params = {
    'order': 'created_at.desc'
}

expenses_generator = fyle.v1beta.admin.expenses.list_all(query_params=query_params)

for response in expenses_generator:
    if response.get('data'):
        expenses.extend(response['data'])

```

## Integration Tests

1. Install [pytest](https://pypi.org/project/pytest/) package using pip as follows:

```
pip install pytest
```

2. Add the following environment variables to test_credentials.sh file

```
    export SERVER_URL=<FYLE SERVER URL>
    export TOKEN_URL=<FYLE TOKEN URL>
    export REFRESH_TOKEN=<FYLE REFRESH TOKEN>
    export CLIENT_ID=<FYLE CLIENT ID>
    export CLIENT_SECRET=<FYLE CLIENT SECRET>
```
##### NOTE: The credentials used should have required roles assigned to them

3. Apply secrets and Run integration tests as follows:

```
source test_credentials.sh  && python -m pytest test/integration
```
4. To get the code coverage execute the following:

```
pytest test/ --cov
```
Currently the code coverage is at 95%

## Release latest version to [PyPi](https://pypi.org/project/fyle/)

* Open the releases section on GitHub and [Draft a new release](https://github.com/fylein/fyle-platform-sdk-py/releases/new).
* Check the version in setup.py, make sure you update that version along with your changes.
* Add the version and description and click ok `Publish Release` button.
* This will trigger the github action and automatically push the SDK to PyPi

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
