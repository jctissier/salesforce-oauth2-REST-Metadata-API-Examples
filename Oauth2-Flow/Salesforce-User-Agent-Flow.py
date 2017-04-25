# _author_ = "Jean-Claude Tissier"
# _github_ = "https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples"

import requests


class SalesforceOAuth2(object):
    """
        Salesforce User-Agent Oauth Authentication Flow
    """

    _authorize_url = '/services/oauth2/authorize'

    def __init__(self, client_id, redirect_uri, sandbox):
        """
        Create SalesforceOauth2 object
        :param client_id: Connected App's Consumer Key
        :param redirect_uri: Callback URL once logged in
        :param sandbox: Boolean flag to determine authentication site
        """
        if sandbox:
            self.auth_site = 'https://test.salesforce.com'
        else:
            self.auth_site = 'https://login.salesforce.com'

        self.client_id = client_id
        self.redirect_uri = redirect_uri

    def get_access_token(self):
        """
        Sets the body of the POST request
        :return: POST response
        """
        body = {
            'response_type': 'token',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri
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
                token=self._authorize_url
            ),
            data=data,
            headers=headers
        )

        return response
