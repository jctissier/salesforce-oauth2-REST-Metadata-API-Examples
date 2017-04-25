# Salesforce OAuth2 Examples (Python)

## Table of Content
| Topic                         | Documentation | Code  |
| ------------------------------|:-------------:|:-----:|
| Oauth - Username-Password     | [Doc](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_username_password_oauth_flow.htm)           | [Code](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/Salesforce-Username-Password-Oauth.py)  |
| REST API                      | Doc           | Code  |
| SOAP API                      | Doc           | Code  |

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
| [Salesforce Documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_user_agent_oauth_flow.htm)                         | [Code Sample](https://github.com/jctissier/Salesforce-Oauth2-REST-SOAP-API-Python-Examples/blob/master/Oauth2-Flow/Salesforce-User-Agent-Oauth.py) |
| ------------------------------|:-------------:|

**Example**
```Python
oauth = SalesforceOAuth2(
    client_id='your_client_id',
    redirect_uri='https://www.enter-url-here.com/',                     # Must match Connected App's Callback URL
    sandbox=True
)
response = oauth.get_access_token()
print(response.text)                                                    # Response's text content, find the Oauth2 URL
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
window.location.href ='https://test.salesforce.com/?ec=302&startURL=%2Fsetup%2Fsecur%2FRemoteAccessAuthorizationPage.apexp%3Fsource%3DCAAAAVunKc0dfaE8wSjAwMDAwMDAwMDA0AAAAzvLd_MBDrJdD85NeTpeBvyJvMu13glHu-8SVW8OQVZoQkVxSt-DVCbYGXkgb-HaElPfp89r4HoQgxLsRC1awHznfguj2J1oJF3JRBdT3R2qgxT3l9yYCkzGnbE5-sdugAbszvylp78uGqPEJGguDD8a10tk7tktDeH02k5NWmF4UX8NM1oIiR_heDIw8TNOYRbTFhnqmSugZEGMiRj6ao7BTl1lxCtoZFERLtdKciNqkC0fLuFXFW4BDcQwTBacXfNm2ScrVZDGeRrNeHQYfJnPDJG1prLKJDrNOIyMtBslcoyYnDuuqBR0ENCdp64Yh69o74fVJMgwEjyM3ugVFHASpZp0AaWAy0P9XA5VXhNTA7eXFp9jLUw89NKNs5xwpxJOZe66oypSSVNjFCETsK8qVTzPCkL4QgGKLAd3Pzf5kXYSGpCTT7sZohaFY7yAMzJAn7gU7jsiA2D68dl-rjMgIGydVuGFq_4LF-EW4Zg%253D%253D';
```
* Open URL in browser, you will be redirected to Salesforce's login page. 
* Enter your credentials and sign in, if successful, you will automatically be redirected to your <redirect_uri> ('https://www.enter-url-here.com/')

