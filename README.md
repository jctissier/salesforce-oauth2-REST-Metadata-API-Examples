# Salesforce OAuth2, REST & SOAP API Examples (Python)

## Table of Contents
| Topic                         | SF Documentation | Code Sample |
| ------------------------------|:----------------:|:-----------:|
| [Oauth - Username-Password](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/README.md#1---username-password-oauth-authentication-flow)     | [Link](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_username_password_oauth_flow.htm)           | [Link](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/Salesforce-Username-Password-Oauth.py)  |
| [Oauth - User-Agent](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/README.md#2---user-agent-oauth-authentication-flow)     | [Link](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_user_agent_oauth_flow.htm)           | [Link](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/Salesforce-User-Agent-Flow.py)  |
| Oauth - Web Server     | [Link](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_web_server_oauth_flow.htm)           | [Link](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/Salesforce-Web-Server-Flow.py)  |
| REST API                      | Doc           | Code  |
| SOAP API                      | Doc           | Code  |

***

## 1 - Username-Password OAuth Authentication Flow
| [Salesforce Documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_username_password_oauth_flow.htm)                         | [Code Sample](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/Salesforce-Username-Password-Oauth.py) |
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

## 2 - User-Agent OAuth Authentication Flow
| [Salesforce Documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_user_agent_oauth_flow.htm)                         | [Code Sample](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/Salesforce-User-Agent-Flow.py) |
| ------------------------------|:-------------:|

**Example**

This example was done purely from a Python script, which is why I had to scrape the authorization URL. Once setup on a Web App, redirect to Salesforce's authentication will happen automatically.

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

*Extract parameters from Callback URL*
```Markdown
https://www.enter-url-here.com/#
    access_token=00D7A000000DFeX%21AQcAQAq3T51g1uXSy13a0OLnzgJftZZDu6yMeYycS_Tgcb4r_m9Pl.0ttCVQjEfBRGk3xaDDPjCX3EMwozIDiTW4Ug9siU0z&
    instance_url=https%3A%2F%2Flularoe--Dev.cs44.my.salesforce.com&
    id=https%3A%2F%2Ftest.salesforce.com%2Fid%2F00D7A000000DFeXUAW%2F0057A000001XZo7QAG&
    issued_at=1493149331818&
    signature=7CGg53xYc7zJvGQI%2FCpCREC9Vg7BnnNkbIZpb4ZPrHk%3D&
    scope=full&
    token_type=Bearer
```

## 3 - Web Server OAuth Authentication Flow
| [Salesforce Documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_web_server_oauth_flow.htm)                         | [Code Sample](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/Salesforce-Web-Server-Oauth.py) |
| ------------------------------|:-------------:|

**Example**
