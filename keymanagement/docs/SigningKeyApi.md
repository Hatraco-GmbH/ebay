# keymanagement.SigningKeyApi

All URIs are relative to *https://apiz.ebay.com/developer/key_management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_signing_key**](SigningKeyApi.md#create_signing_key) | **POST** /signing_key | 
[**get_signing_key**](SigningKeyApi.md#get_signing_key) | **GET** /signing_key/{signing_key_id} | 
[**get_signing_keys**](SigningKeyApi.md#get_signing_keys) | **GET** /signing_key | 


# **create_signing_key**
> SigningKey create_signing_key(body=body)



This method creates keypairs using one of the following ciphers:<ul><li>ED25519 (Edwards Curve)</li><li>RSA</li></ul><span class=\"tablenote\"><b>Note:</b> The recommended signature cipher is <b>ED25519</b> (Edwards Curve) since it uses much shorter keys and therefore decreases the header size. However, for development frameworks that do not support ED25519, RSA is also supported.</span><br/>Following a successful completion, the following keys are returned:<ul><li>Private Key</li><li>Public Key</li><li>Public Key as JWE</li></ul>Once keypairs are created, developers are <b>strongly advised</b> to create and store a local copy of each keypair for future reference. Although the <b>Public Key</b>, <b>Public Key as JWE</b>, and metadata for keypairs may be retrieved by the <code>getSigningKey</code> and <code>getSigningKeys</code> methods, in order to further ensure the security of confidential client information, eBay does not store the <b>Private Key</b> value in any system. If a developer loses their <b>Private Key</b> they must generate new keypairs using the <code>createSigningKey</code> method.<br/><span class=\"tablenote\"><b>Note:</b> For additional information about using keypairs, refer to <a href= \"/develop/guides/digital-signatures-for-apis \" target= \"_blank \">Digital Signatures for APIs</a>.</span>

### Example
```python
from __future__ import print_function
import time
import keymanagement
from keymanagement.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Client Credentials
configuration = keymanagement.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = keymanagement.SigningKeyApi(keymanagement.ApiClient(configuration))
body = keymanagement.CreateSigningKeyRequest() # CreateSigningKeyRequest |  (optional)

try:
    api_response = api_instance.create_signing_key(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigningKeyApi->create_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSigningKeyRequest**](CreateSigningKeyRequest.md)|  | [optional] 

### Return type

[**SigningKey**](SigningKey.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signing_key**
> SigningKey get_signing_key(signing_key_id)



This method returns the <b>Public Key</b>, <b>Public Key as JWE</b>, and metadata for a specified <code>signingKeyId</code> associated with the application key making the call.<br/><br/><span class=\"tablenote\"><b>Note:</b> It is important to note that the <code>privateKey</code> value is <b>not</b> returned. In order to further ensure the security of confidential client information, eBay does <b>not</b> store the <code>privateKey</code> value in any system. If a developer loses their <code>privateKey</code> they must generate new keypairs using the <code>createSigningKey</code> method.</span>

### Example
```python
from __future__ import print_function
import time
import keymanagement
from keymanagement.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Client Credentials
configuration = keymanagement.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = keymanagement.SigningKeyApi(keymanagement.ApiClient(configuration))
signing_key_id = 'signing_key_id_example' # str | The system-generated eBay ID of the keypairs being requested.

try:
    api_response = api_instance.get_signing_key(signing_key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigningKeyApi->get_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signing_key_id** | **str**| The system-generated eBay ID of the keypairs being requested. | 

### Return type

[**SigningKey**](SigningKey.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signing_keys**
> QuerySigningKeysResponse get_signing_keys()



This method returns the <b>Public Key</b>, <b>Public Key as JWE</b>, and metadata for all keypairs associated with the application key making the call.<br/><br/><span class=\"tablenote\"><b>Note:</b> It is important to note that <code>privateKey</code> values are <b>not</b> returned. In order to further ensure the security of confidential client information, eBay does <b>not</b> store <code>privateKey</code> values in any system. If a developer loses their <code>privateKey</code> they must generate new keypairs set using the <code>createSigningKey</code> method.</span>

### Example
```python
from __future__ import print_function
import time
import keymanagement
from keymanagement.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Client Credentials
configuration = keymanagement.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = keymanagement.SigningKeyApi(keymanagement.ApiClient(configuration))

try:
    api_response = api_instance.get_signing_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigningKeyApi->get_signing_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QuerySigningKeysResponse**](QuerySigningKeysResponse.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

