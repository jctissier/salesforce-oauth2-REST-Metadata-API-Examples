# _author_ = "Jean-Claude Tissier"
# _github_ = "https://github.com/jctissier/Salesforce-Oauth2-REST-Metadata-API-Python-Examples"

import requests


class SalesforceOAuth2(object):
    """
        Salesforce Username-Password Oauth Authentication Flow
        https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_username_password_oauth_flow.htm
    """

    _token_url = '/services/oauth2/token'

    def __init__(self, client_id, client_secret, username, password, token, sandbox):
        """
        Create SalesforceOauth2 object
        :param client_id: Connected App's Consumer Key
        :param client_secret: Connected App's Consumer Secret
        :param username: Org's username
        :param password: Org's password
        :param token: Org's token, request a new one: My Settings > Personal > Reset My Security Token
        :param sandbox: Boolean flag to determine authentication site
        """
        if sandbox:
            self.auth_site = 'https://test.salesforce.com'
        else:
            self.auth_site = 'https://login.salesforce.com'

        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.token = token

    def get_access_token(self):
        """
        Sets the body of the POST request
        :return: POST response
        """
        body = {
            'grant_type': 'password',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'username': self.username,
            'password': self.password + self.token
        }
        response = self._request_token(body)

        return response

    def _request_token(self, data):
        """
        Sends a POST request to Salesforce to authenticate credentials
        :param data: body of the POST request
        :return: POST response
        """
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(
            "{site}{token}".format(
                site=self.auth_site,
                token=self._token_url
            ),
            data=data,
            headers=headers
        )

        return response

    
    
"""
Testing data

oauth = SalesforceOAuth2(
    client_id='your_client_id',
    client_secret='your_client_secret',
    username='your_username',
    password='your_password',
    token='your_token',
    sandbox=True                        # True = test.salesforce.com, False = login.salesforce.com
)
sf_authentication = oauth.get_access_token()
response = sf_authentication.json()
print(response)
"""
