# ebaymedia
The <b>Media API</b> lets sellers to create, upload, and retrieve files, including:<ul><li>videos</li><li>documents (for GPSR regulations)</li></ul>

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1_beta.2.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import ebaymedia 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ebaymedia
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import ebaymedia
from ebaymedia.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaymedia.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaymedia.DocumentApi(ebaymedia.ApiClient(configuration))
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
body = ebaymedia.CreateDocumentRequest() # CreateDocumentRequest |  (optional)

try:
    api_response = api_instance.create_document(content_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->create_document: %s\n" % e)

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaymedia.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaymedia.DocumentApi(ebaymedia.ApiClient(configuration))
document_id = 'document_id_example' # str | The unique identifier of the document for which status and metadata is being retrieved.<br><br>This value is returned in the response of the <a href=\"/api-docs/commerce/media/resources/document/methods/createDocument\" target=\"_blank\">createDocument</a> method.

try:
    api_response = api_instance.get_document(document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->get_document: %s\n" % e)

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaymedia.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaymedia.DocumentApi(ebaymedia.ApiClient(configuration))
document_id = 'document_id_example' # str | The unique identifier of the document to be uploaded.<br><br>This value is returned in the response of the <a href=\"/api-docs/commerce/media/resources/document/methods/createDocument\" target=\"_blank\">createDocument</a> method.
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>multipart/form-data</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.

try:
    api_response = api_instance.upload_document(document_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->upload_document: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://apim.ebay.com{basePath}*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DocumentApi* | [**create_document**](docs/DocumentApi.md#create_document) | **POST** /document | 
*DocumentApi* | [**get_document**](docs/DocumentApi.md#get_document) | **GET** /document/{document_id} | 
*DocumentApi* | [**upload_document**](docs/DocumentApi.md#upload_document) | **POST** /document/{document_id}/upload | 
*VideoApi* | [**create_video**](docs/VideoApi.md#create_video) | **POST** /video | 
*VideoApi* | [**get_video**](docs/VideoApi.md#get_video) | **GET** /video/{video_id} | 
*VideoApi* | [**upload_video**](docs/VideoApi.md#upload_video) | **POST** /video/{video_id}/upload | 

## Documentation For Models

 - [CreateDocumentRequest](docs/CreateDocumentRequest.md)
 - [CreateDocumentResponse](docs/CreateDocumentResponse.md)
 - [CreateVideoRequest](docs/CreateVideoRequest.md)
 - [DocumentMetadata](docs/DocumentMetadata.md)
 - [DocumentResponse](docs/DocumentResponse.md)
 - [Error](docs/Error.md)
 - [ErrorParameter](docs/ErrorParameter.md)
 - [Image](docs/Image.md)
 - [InputStream](docs/InputStream.md)
 - [Moderation](docs/Moderation.md)
 - [Play](docs/Play.md)
 - [Video](docs/Video.md)

## Documentation For Authorization


## api_auth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://auth.ebay.com/oauth2/authorize
- **Scopes**: 
 - **https://api.ebay.com/oauth/api_scope/sell.inventory**: View and manage your inventory and offers


## Author


