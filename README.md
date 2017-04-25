# Salesforce OAuth2 Examples (Python)

## Table of Content
| Topic                         | Documentation | Code  |
| ------------------------------|:-------------:|:-----:|
| Oauth - Username-Password     | Doc           | Code  |
| REST API                      | Doc           | Code  |
| SOAP API                      | Doc           | Code  |

## 1 - Username-Password OAuth Authentication Flow
[Salesforce Documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_username_password_oauth_flow.htm)

**Example**
```Python
oauth = SalesforceOAuth2(
    client_id='your_client_id',
    client_secret='your_client_secret',
    username='your_username',
    password='your_password',
    token='your_token',
    sandbox=True
)
sf_authentication = oauth.get_access_token()
response = sf_authentication.json()
print(response)
```
*JSON Response*
```JSON
{
    'signature': 'B4UPTuymHFtTDZiI728H0LZ1/4LxebOjestj+EcwFDU=',
    'issued_at': '1493144749805',
    'instance_url': 'https://na40.salesforce.com',
    'id': 'https://test.salesforce.com/id/00D7B000000DFeXUAW/0057A000001Zp0CQRD',
    'token_type': 'Bearer',
    'access_token': '00D7AA00000DFeX!AQcAQCOOnJsOicbB6mknoxIH02wxjljnjKI739g1EoDBEOpQXomAV1iMG2EWGuU2gJ26o40ixi6jyD3AstyLgkiU29GNod2d'
}
```

