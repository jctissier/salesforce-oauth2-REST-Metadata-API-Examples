# _author_ = "Jean-Claude Tissier"
# _github_ = "https://github.com/jctissier/Salesforce-Oauth2-REST-Metadata-API-Python-Examples"

import requests
import salesforce_username_password_flow as oauth


class RESTApi(object):
    """
        Salesforce REST API Class
            -Include HTTP Methods:      (Working)           GET, POST, HEAD
            -Remaining methods:         (Not Tested)        PUT, PATCH, DELETE
            -Authenticated headers are required to call Salesforce's REST API
                -example for authenticated headers
                {
                    'Content-Type': 'application/json',
                    'X-PrettyPrint': '1',
                    'Authorization': 'Bearer "access_token"'
                }
    """

    def __init__(self, access_token, instance_url):
        """
        Constructor for RESTApi Class
        :param rest_url: particular API method that needs to be called,
                   ex: sobjects in ==> org_instance/services/data/v39.0/sobjects
        :param body: used for the body of API calls (ex: POST)
        :param version: Salesforce API version (ex: current is '39.0')
        """
        self.instance = instance_url
        self.sf_headers = {
                    'Content-Type': 'application/json',
                    'X-PrettyPrint': '1',
                    'Authorization': 'Bearer ' + access_token
                }

    def rest_api_get(self, rest_url, api_version):
        """
        GET request to the REST API
        :return: JSON string of the GET response
        """
        response = requests.get(
            "{org_instance}/services/data/v{api_version}/{rest_url}".format(
                org_instance=self.instance, api_version=api_version, rest_url=rest_url
            ),
            headers=self.sf_headers
        )

        return response

    def rest_api_head(self, rest_url, api_version):
        """
        HEAD request to the REST API
        :return: Request response
        """
        response = requests.head(
            "{org_instance}/services/data/v{api_version}/{rest_url}".format(
                org_instance=self.instance, api_version=api_version, rest_url=rest_url
            ),
            headers=self.sf_headers
        )

        return response

    def rest_api_post(self, rest_url, body, api_version):
        """
        POST request to the REST API
        :return: JSON string of the POST response
        """
        response = requests.post(
            "{org_instance}/services/data/v{api_version}/{rest_url}".format(
                org_instance=self.instance, api_version=api_version, rest_url=rest_url
            ),
            data=body,
            headers=self.sf_headers
        )

        return response

    def rest_api_put(self, rest_url, body, api_version):
        """
        PUT request to the REST API - Not tested
        :return: JSON string of the PUT response
        """
        response = requests.put(
            "{org_instance}/services/data/v{api_version}/{rest_url}".format(
                org_instance=self.instance, api_version=api_version, rest_url=rest_url
            ),
            data=body,
            headers=self.sf_headers
        )

        return response

    def rest_api_patch(self, rest_url, body, api_version):
        """
        PATCH request to the REST API - Not tested
        :return: JSON string of the PATCH response
        """
        response = requests.patch(
            "{org_instance}/services/data/v{api_version}/{rest_url}".format(
                org_instance=self.instance, api_version=api_version, rest_url=rest_url
            ),
            data=body,
            headers=self.sf_headers
        )

        return response

    def rest_api_delete(self, rest_url, api_version):
        """
        DELETE request to the REST API - Not tested
        :return: JSON string of the DELETE response
        """
        response = requests.delete(
            "{org_instance}/services/data/v{api_version}/{rest_url}".format(
                org_instance=self.instance, api_version=api_version, rest_url=rest_url
            ),
            headers=self.sf_headers
        )

        return response
