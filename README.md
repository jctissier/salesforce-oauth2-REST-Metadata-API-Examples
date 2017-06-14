# Salesforce OAuth2, REST API and Metadata API Examples (Python 3+)

Python implementations of Salesforce Oauth2 Flows, as well as authenticated REST API and Metadata API requests. Grab the code from this repository and get started!

Using these code samples, you could easily spin up a web app that will interact with your various Salesforce Orgs and manipulate your data. 


## Table of Contents
| Topic                         | SF Documentation | Code Sample |
| ------------------------------|:----------------:|:-----------:|
| [Oauth - Username-Password](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/README.md#1---username-password-oauth-authentication-flow)     | [Link](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_username_password_oauth_flow.htm)           | [Link](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/salesforce_username_password_flow.py)  |
| [Oauth - User-Agent](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/README.md#2---user-agent-oauth-authentication-flow)     | [Link](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_user_agent_oauth_flow.htm)           | [Link](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/salesforce_user_agent_flow.py)  |
| [Oauth - Web Server](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/README.md#3---web-server-oauth-authentication-flow)     | [Link](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_web_server_oauth_flow.htm)           | [Link](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/salesforce_web_server_flow.py)  |
| [Force.com REST API](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples#rest-api-using-the-username-password-oauth-authentication-flow)                      | [Link](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.htm)           | [Link](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/REST-API/rest_api.py)  |
| [Metadata API](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/README.md#metadata-api---username-password-oauth-authentication-flow) - Not completed                      | [Link]           | [Link]  |
| [Notes](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/README.md#notes)                

***

## 1 - Username-Password OAuth Authentication Flow
| [Salesforce Documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_username_password_oauth_flow.htm)                         | [Code Sample](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/salesforce_username_password_flow.py) |
| ------------------------------|:-------------:|

**Example**
```Python
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
```
*JSON Response*
```JSON
{
    "signature": "B4UPTuymHFtTDZiI728H0LZ1/4LxebOjestj+EcwFDU=",
    "issued_at": "1493144749805",
    "instance_url": "https://na40.salesforce.com",
    "id": "https://test.salesforce.com/id/00D7B000000DFeXUAW/0057A000001Zp0CQRD",
    "token_type": "Bearer",
    "access_token": "00D7AA00000DFeX!AQcAQCOOnJsOicbB6mknoxIH02wxjljnjKI739g1EoDBEOpQXomAV1iMG2EWGuU2gJ26o40ixi6jyD3AstyLgkiU29GNod2d"
}
```

***

## 2 - User-Agent OAuth Authentication Flow
| [Salesforce Documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_user_agent_oauth_flow.htm)                         | [Code Sample](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/salesforce_user_agent_flow.py) |
| ------------------------------|:-------------:|

**Example**

This example was created from a Python script, which is why I had to scrape the authorization URL. Once setup on a proper App, redirect to Salesforce's authentication will happen automatically.

```Python
oauth = SalesforceOAuth2(
    client_id='your_client_id',
    redirect_uri='https://www.enter-url-here.com/',   # Must match Connected App's Callback URL
    sandbox=True
)
response = oauth.get_access_token()
print(response.text)                                  # Response's text content, find the Oauth2 URL
```
*Response Text - HTML*
```HTML
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta HTTP-EQUIV="PRAGMA" CONTENT="NO-CACHE">
<script>
if (this.SfdcApp && this.SfdcApp.projectOneNavigator) { SfdcApp.projectOneNavigator.handleRedirect(''https://test.salesforce.com/?ec=302&startURL=%2Fsetup%2Fsecur%2FRemoteAccessAuthorizationPage.apexp%3Fsource%3DCAAAAVunKc0dfaE8wSjAwMDAwMDAwMDA0AAAAzvLd_MBDrJdD85NeTpeBvyJvMu13glHu-8SVW8OQVZoQkVxSt-DVCbYGXkgb-HaElPfp89r4HoQgxLsRC1awHznfguj2J1oJF3JRBdT3R2qgxT3l9yYCkzGnbE5-sdugAbszvylp78uGqPEJGguDD8a10tk7tktDeH02k5NWmF4UX8NM1oIiR_heDIw8TNOYRbTFhnqmSugZEGMiRj6ao7BTl1lxCtoZFERLtdKciNqkC0fLuFXFW4BDcQwTBacXfNm2ScrVZDGeRrNeHQYfJnPDJG1prLKJDrNOIyMtBslcoyYnDuuqBR0ENCdp64Yh69o74fVJMgwEjyM3ugVFHASpZp0AaWAy0P9XA5VXhNTA7eXFp9jLUw89NKNs5xwpxJOZe66oypSSVNjFCETsK8qVTzPCkL4QgGKLAd3Pzf5kXYSGpCTT7sZohaFY7yAMzJAn7gU7jsiA2D68dl-rjMgIGydVuGFq_4LF-EW4Zg%253D%253D'); }  else 
if (window.location.replace){ 
window.location.replace('https://test.salesforce.com/?ec=302&startURL=%2Fsetup%2Fsecur%2FRemoteAccessAuthorizationPage.apexp%3Fsource%3DCAAAAVunKc0dfaE8wSjAwMDAwMDAwMDA0AAAAzvLd_MBDrJdD85NeTpeBvyJvMu13glHu-8SVW8OQVZoQkVxSt-DVCbYGXkgb-HaElPfp89r4HoQgxLsRC1awHznfguj2J1oJF3JRBdT3R2qgxT3l9yYCkzGnbE5-sdugAbszvylp78uGqPEJGguDD8a10tk7tktDeH02k5NWmF4UX8NM1oIiR_heDIw8TNOYRbTFhnqmSugZEGMiRj6ao7BTl1lxCtoZFERLtdKciNqkC0fLuFXFW4BDcQwTBacXfNm2ScrVZDGeRrNeHQYfJnPDJG1prLKJDrNOIyMtBslcoyYnDuuqBR0ENCdp64Yh69o74fVJMgwEjyM3ugVFHASpZp0AaWAy0P9XA5VXhNTA7eXFp9jLUw89NKNs5xwpxJOZe66oypSSVNjFCETsK8qVTzPCkL4QgGKLAd3Pzf5kXYSGpCTT7sZohaFY7yAMzJAn7gU7jsiA2D68dl-rjMgIGydVuGFq_4LF-EW4Zg%253D%253D');
} else {;
window.location.href ='https://test.salesforce.com/?ec=302&startURL=%2Fsetup%2Fsecur%2FRemoteAccessAuthorizationPage.apexp%3Fsource%3DCAAAAVunKc0dfaE8wSjAwMDAwMDAwMDA0AAAAzvLd_MBDrJdD85NeTpeBvyJvMu13glHu-8SVW8OQVZoQkVxSt-DVCbYGXkgb-HaElPfp89r4HoQgxLsRC1awHznfguj2J1oJF3JRBdT3R2qgxT3l9yYCkzGnbE5-sdugAbszvylp78uGqPEJGguDD8a10tk7tktDeH02k5NWmF4UX8NM1oIiR_heDIw8TNOYRbTFhnqmSugZEGMiRj6ao7BTl1lxCtoZFERLtdKciNqkC0fLuFXFW4BDcQwTBacXfNm2ScrVZDGeRrNeHQYfJnPDJG1prLKJDrNOIyMtBslcoyYnDuuqBR0ENCdp64Yh69o74fVJMgwEjyM3ugVFHASpZp0AaWAy0P9XA5VXhNTA7eXFp9jLUw89NKNs5xwpxJOZe66oypSSVNjFCETsK8qVTzPCkL4QgGKLAd3Pzf5kXYSGpCTT7sZohaFY7yAMzJAn7gU7jsiA2D68dl-rjMgIGydVuGFq_4LF-EW4Zg%253D%253D';
} 
</script>
</head>
</html>
<!-- Body events -->
<script type="text/javascript">function bodyOnLoad(){if(window.PreferenceBits){window.PreferenceBits.prototype.csrfToken="null";};}function bodyOnBeforeUnload(){}function bodyOnFocus(){}function bodyOnUnload(){}</script>		
</body>
</html>
```
*Extract Redirect URL*
```Javascript
window.location.href = 'https://test.salesforce.com/?ec=302&startURL=%2Fsetup%2Fsecur%2FRemoteAccessAuthorizationPage.apexp%3Fsource%3DCAAAAVunKc0dfaE8wSjAwMDAwMDAwMDA0AAAAzvLd_MBDrJdD85NeTpeBvyJvMu13glHu-8SVW8OQVZoQkVxSt-DVCbYGXkgb-HaElPfp89r4HoQgxLsRC1awHznfguj2J1oJF3JRBdT3R2qgxT3l9yYCkzGnbE5-sdugAbszvylp78uGqPEJGguDD8a10tk7tktDeH02k5NWmF4UX8NM1oIiR_heDIw8TNOYRbTFhnqmSugZEGMiRj6ao7BTl1lxCtoZFERLtdKciNqkC0fLuFXFW4BDcQwTBacXfNm2ScrVZDGeRrNeHQYfJnPDJG1prLKJDrNOIyMtBslcoyYnDuuqBR0ENCdp64Yh69o74fVJMgwEjyM3ugVFHASpZp0AaWAy0P9XA5VXhNTA7eXFp9jLUw89NKNs5xwpxJOZe66oypSSVNjFCETsK8qVTzPCkL4QgGKLAd3Pzf5kXYSGpCTT7sZohaFY7yAMzJAn7gU7jsiA2D68dl-rjMgIGydVuGFq_4LF-EW4Zg%253D%253D';
```
* Open URL in browser, you will be redirected to Salesforce's login page. 
* Enter your credentials and sign in, if successful, you will automatically be redirected to your <redirect_uri> (example: 'https://www.enter-url-here.com/') and the authentication parameters will be attached to the URL.

*Extract parameters from Callback URL - [(with a URL Decoder)](http://meyerweb.com/eric/tools/dencoder/)*
```Markdown
https://www.enter-url-here.com/#
    access_token=00D7A000000DFeX%21AQcAQAq3T51g1uXSy13a0OLnzgJftZZDu6yMeYycS_Tgcb4r_m9Pl.0ttCVQjEfBRGk3xaDDPjCX3EMwozIDiTW4Ug9siU0z&
    instance_url=https%3A%2F%2Fna40.salesforce.com&
    id=https%3A%2F%2Ftest.salesforce.com%2Fid%2F00D7A000000DFeXUAW%2F0057A000001XZo7QAG&
    issued_at=1493149331818&
    signature=7CGg53xYc7zJvGQI%2FCpCREC9Vg7BnnNkbIZpb4ZPrHk%3D&
    scope=full&
    token_type=Bearer
```

***

## 3 - Web Server OAuth Authentication Flow
| [Salesforce Documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_web_server_oauth_flow.htm)                         | [Code Sample](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/salesforce_web_server_flow.py) |
| ------------------------------|:-------------:|

**Example**

This flow is normally used on a Web App, but the example below is done in Python since it's easier to show in an example.

```Python
import webbrowser                           
import urllib.parse as urlparse

oauth = SalesforceOAuth2(
    client_id='your_client_id',
    client_secret='your_client_secret',
    redirect_uri='https://www.enter-url-here.com/',
    sandbox=True                        # True = test.salesforce.com, False = login.salesforce.com
)

oauth_redirect = oauth.authorize_login_url()
webbrowser.open(oauth_redirect)         # This will open the Authentication Salesforce Login page
```
* Fill in your credentials and Login, you will be redirected to your app's callback URL, Copy the URL Link (with the parameters)
```Python
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
```
*JSON Response*
```JSON
{
    "signature": "B4UPTuymHFtTDZiI728H0LZ1/4LxebOjestj+EcwFDU=",
    "issued_at": "1493144749805",
    "instance_url": "https://na40.salesforce.com",
    "id": "https://test.salesforce.com/id/00D7B000000DFeXUAW/0057A000001Zp0CQRD",
    "token_type": "Bearer",
    "access_token": "00D7AA00000DFeX!AQcAQCOOnJsOicbB6mknoxIH02wxjljnjKI739g1EoDBEOpQXomAV1iMG2EWGuU2gJ26o40ixi6jyD3AstyLgkiU29GNod2d",
    "scope": "full",
    "id_token": "<1108 characters long>"
}
```

***

## REST API - Username-Password OAuth Authentication Flow
| [Salesforce Documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.htm)                         | [Code Sample](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Salesforce-APIs/REST_Api.py) |
| ------------------------------|:-------------:|

**Example**

Username-Password Flow is the easiest to use as an example. 

```Python
oauth = SalesforceOAuth2(
    client_id='your_client_id',
    client_secret='your_client_secret',
    username='your_username',
    password='your_password',
    token='your_token',
    sandbox=True                        # True = test.salesforce.com, False = login.salesforce.com
)
sf_authentication = oauth.get_access_token()
json_response = sf_authentication.json()
```
* Authenticate and extract the ```access_token``` and ```instance_url``` from the JSON response.
```Python
access_token = json_response['access_token']
instance_url = json_response['instance_url']
```
* Create a REST API request with the authenticated credentials
```Python
rest = RESTApi(access_token=access_token, instance_url=instance_url)
get_request = rest.rest_api_get(rest_url='sobjects/Account', api_version='39.0')    # full url = instance_url/services/data/v39.0/sobjects/Account
print(get_request)                  # <Response [200]>
print(get_request.json())

"""
{'recentItems': [], 'objectDescribe': {'feedEnabled': True, 'layoutable': True, 'replicateable': True, 'deprecatedAndHidden': False, 'updateable': True, 'mergeable': True, 'activateable': False, 'name': 'Account', 'searchable': True, 'queryable': True, 'undeletable': True, 'retrieveable': True, 'deletable': True, 'mruEnabled': True, 'isSubtype': False, 'customSetting': False, 'label': 'Account', 'triggerable': True, 'hasSubtypes': False, 'custom': False, 'urls': {'listviews': '/services/data/v39.0/sobjects/Account/listviews', 'compactLayouts': '/services/data/v39.0/sobjects/Account/describe/compactLayouts', 'defaultValues': '/services/data/v39.0/sobjects/Account/defaultValues?recordTypeId&fields', 'quickActions': '/services/data/v39.0/sobjects/Account/quickActions', 'rowTemplate': '/services/data/v39.0/sobjects/Account/{ID}', 'layouts': '/services/data/v39.0/sobjects/Account/describe/layouts', 'sobject': '/services/data/v39.0/sobjects/Account', 'describe': '/services/data/v39.0/sobjects/Account/describe', 'approvalLayouts': '/services/data/v39.0/sobjects/Account/describe/approvalLayouts'}, 'keyPrefix': '001', 'labelPlural': 'Accounts', 'createable': True}}
"""
```

***

## Metadata API - Username-Password OAuth Authentication Flow
| [Salesforce Documentation](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/file_based.htm)                         | [Code Sample](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Salesforce-APIs/Metadata_Api.py) |
| ------------------------------|:-------------:|

**Example**

Username-Password Flow is the easiest to use as an example. (Same setup as REST API)

```Python
oauth = SalesforceOAuth2(
    client_id='your_client_id',
    client_secret='your_client_secret',
    username='your_username',
    password='your_password',
    token='your_token',
    sandbox=True                        # True = test.salesforce.com, False = login.salesforce.com
)
sf_authentication = oauth.get_access_token()
json_response = sf_authentication.json()
```
* Authenticate and extract the ```access_token``` and ```instance_url``` from the JSON response.
```Python
access_token = json_response['access_token']
instance_url = json_response['instance_url']
```



## Notes
**Author**: Jean-Claude Tissier

Feel free to contribute and create an issue if you are having problems with some of the code.
