# keymanagement.SigningKeyApi

All URIs are relative to *https://apiz.ebay.com/developer/key_management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_signing_key**](SigningKeyApi.md#create_signing_key) | **POST** /signing_key | 
[**get_signing_key**](SigningKeyApi.md#get_signing_key) | **GET** /signing_key/{signing_key_id} | 
[**get_signing_keys**](SigningKeyApi.md#get_signing_keys) | **GET** /signing_key | 


# **create_signing_key**
> SigningKey create_signing_key(content_type, create_signing_key_request=create_signing_key_request)

This method creates keypairs using one of the following ciphers:<ul><li>ED25519 (Edwards Curve)</li><li>RSA</li></ul><span class="tablenote"><b>Note:</b> The recommended signature cipher is <b>ED25519</b> (Edwards Curve) since it uses much shorter keys and therefore decreases the header size. However, for development frameworks that do not support ED25519, RSA is also supported.</span><br/>Following a successful completion, the following keys are returned:<ul><li>Private Key</li><li>Public Key</li><li>Public Key as JWE</li></ul>Once keypairs are created, developers are <b>strongly advised</b> to create and store a local copy of each keypair for future reference. Although the <b>Public Key</b>, <b>Public Key as JWE</b>, and metadata for keypairs may be retrieved by the <code>getSigningKey</code> and <code>getSigningKeys</code> methods, in order to further ensure the security of confidential client information, eBay does not store the <b>Private Key</b> value in any system. If a developer loses their <b>Private Key</b> they must generate new keypairs using the <code>createSigningKey</code> method.<br/><span class="tablenote"><b>Note:</b> For additional information about using keypairs, refer to <a href= "/develop/guides/digital-signatures-for-apis " target= "_blank ">Digital Signatures for APIs</a>.</span>

### Example

* OAuth Authentication (api_auth):

```python
import keymanagement
from keymanagement.models.create_signing_key_request import CreateSigningKeyRequest
from keymanagement.models.signing_key import SigningKey
from keymanagement.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apiz.ebay.com/developer/key_management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = keymanagement.Configuration(
    host = "https://apiz.ebay.com/developer/key_management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with keymanagement.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = keymanagement.SigningKeyApi(api_client)
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    create_signing_key_request = keymanagement.CreateSigningKeyRequest() # CreateSigningKeyRequest |  (optional)

    try:
        api_response = api_instance.create_signing_key(content_type, create_signing_key_request=create_signing_key_request)
        print("The response of SigningKeyApi->create_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SigningKeyApi->create_signing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **create_signing_key_request** | [**CreateSigningKeyRequest**](CreateSigningKeyRequest.md)|  | [optional] 

### Return type

[**SigningKey**](SigningKey.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signing_key**
> SigningKey get_signing_key(signing_key_id)

This method returns the <b>Public Key</b>, <b>Public Key as JWE</b>, and metadata for a specified <code>signingKeyId</code> associated with the application key making the call.<br/><br/><span class="tablenote"><b>Note:</b> It is important to note that the <code>privateKey</code> value is <b>not</b> returned. In order to further ensure the security of confidential client information, eBay does <b>not</b> store the <code>privateKey</code> value in any system. If a developer loses their <code>privateKey</code> they must generate new keypairs using the <code>createSigningKey</code> method.</span>

### Example

* OAuth Authentication (api_auth):

```python
import keymanagement
from keymanagement.models.signing_key import SigningKey
from keymanagement.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apiz.ebay.com/developer/key_management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = keymanagement.Configuration(
    host = "https://apiz.ebay.com/developer/key_management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with keymanagement.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = keymanagement.SigningKeyApi(api_client)
    signing_key_id = 'signing_key_id_example' # str | The system-generated eBay ID of the keypairs being requested.

    try:
        api_response = api_instance.get_signing_key(signing_key_id)
        print("The response of SigningKeyApi->get_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SigningKeyApi->get_signing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signing_key_id** | **str**| The system-generated eBay ID of the keypairs being requested. | 

### Return type

[**SigningKey**](SigningKey.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signing_keys**
> QuerySigningKeysResponse get_signing_keys()

This method returns the <b>Public Key</b>, <b>Public Key as JWE</b>, and metadata for all keypairs associated with the application key making the call.<br/><br/><span class="tablenote"><b>Note:</b> It is important to note that <code>privateKey</code> values are <b>not</b> returned. In order to further ensure the security of confidential client information, eBay does <b>not</b> store <code>privateKey</code> values in any system. If a developer loses their <code>privateKey</code> they must generate new keypairs set using the <code>createSigningKey</code> method.</span>

### Example

* OAuth Authentication (api_auth):

```python
import keymanagement
from keymanagement.models.query_signing_keys_response import QuerySigningKeysResponse
from keymanagement.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apiz.ebay.com/developer/key_management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = keymanagement.Configuration(
    host = "https://apiz.ebay.com/developer/key_management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with keymanagement.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = keymanagement.SigningKeyApi(api_client)

    try:
        api_response = api_instance.get_signing_keys()
        print("The response of SigningKeyApi->get_signing_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SigningKeyApi->get_signing_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**QuerySigningKeysResponse**](QuerySigningKeysResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

