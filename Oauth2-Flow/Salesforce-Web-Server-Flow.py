# _author_ = "Jean-Claude Tissier"
# _github_ = "https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples"

import requests
from urllib.parse import quote


class SalesforceOAuth2(object):
    """
        Salesforce Web Server Oauth Authentication Flow
    """
    _authorization_url = '/services/oauth2/authorize'
    _token_url = '/services/oauth2/token'

    def __init__(self, client_id, client_secret, redirect_uri, sandbox):
        """
        Create SalesforceOauth2 object
        :param client_id: Connected App's Consumer Key
        :param client_secret: Connected App's Consumer Secret
        :param redirect_uri: Callback URL once logged in
        :param sandbox: Boolean flag to determine authentication site
        """
        if sandbox:
            self.auth_site = 'https://test.salesforce.com'
        else:
            self.auth_site = 'https://login.salesforce.com'
        self.redirect_uri = redirect_uri
        self._client_id = client_id
        self._client_secret = client_secret

    def authorize_login_url(self):
        """
        URL to login through Salesforce
        :return: Redirect URL for Oauth2 authentication
        """

        return "{site}{authorize_url}" \
               "?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&prompt=login".format(
                    site=self.auth_site,
                    authorize_url=self._authorization_url,
                    client_id=self._client_id,
                    redirect_uri=quote(self.redirect_uri)
                )

    def get_access_token(self, code):
        """
        Sets the body of the POST request
        :return: POST response
        """
        body = {
            'grant_type': 'authorization_code',
            'redirect_uri': self.redirect_uri,
            'code': code,
            'client_id': self._client_id,
            'client_secret': self._client_secret
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
            "{site}{token_url}".format(
                site=self.auth_site,
                token_url=self._token_url
            ),
            data=data,
            headers=headers
        )

        return response
    
    
"""
Testing data

import webbrowser
import urllib.parse as urlparse

oauth = SalesforceOAuth2(
    client_id='your_client_id',
    client_secret='your_client_secret',
    redirect_uri='https://www.enter-url-here.com/',
    sandbox=True
)

oauth_redirect = oauth.authorize_login_url()
webbrowser.open(oauth_redirect)
# Fill in your credentials and Login, you will be redirected to your app's callback URL, Copy the URL Link (with the parameters)

# https://www.enter-url-here.com/?code=aPrxILdoIUt7J4zOidrhMRBqhwgwsTAh7expE53Qeh2KhelBXIzspDZ8nPV8t7uADsOHeWXz5g%3D%3D
callback_url = input('Copy-Paste your callback URL and press ENTER')

# Extract the code from the URL
extract_code = urlparse.urlparse(url)
code = urlparse.parse_qs(extract_code.query)['code'][0]
print(code)
# aPrxILdoIUt7J4zOidrhMRBqhwgwsTAh7expE53Qeh2KhelBXIzspDZ8nPV8t7uADsOHeWXz5g==

# Retrieve access_token from Salesforce by sending authenticated code
sf_authentication = oauth.get_access_token(code)
print(sf_authentication.json())                 # Print the JSON response
"""
