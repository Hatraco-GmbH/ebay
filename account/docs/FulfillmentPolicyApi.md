# ebayaccount.FulfillmentPolicyApi

All URIs are relative to *https://api.ebay.com/sell/account/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fulfillment_policy**](FulfillmentPolicyApi.md#create_fulfillment_policy) | **POST** /fulfillment_policy/ | 
[**delete_fulfillment_policy**](FulfillmentPolicyApi.md#delete_fulfillment_policy) | **DELETE** /fulfillment_policy/{fulfillmentPolicyId} | 
[**get_fulfillment_policies**](FulfillmentPolicyApi.md#get_fulfillment_policies) | **GET** /fulfillment_policy | 
[**get_fulfillment_policy**](FulfillmentPolicyApi.md#get_fulfillment_policy) | **GET** /fulfillment_policy/{fulfillmentPolicyId} | 
[**get_fulfillment_policy_by_name**](FulfillmentPolicyApi.md#get_fulfillment_policy_by_name) | **GET** /fulfillment_policy/get_by_policy_name | 
[**update_fulfillment_policy**](FulfillmentPolicyApi.md#update_fulfillment_policy) | **PUT** /fulfillment_policy/{fulfillmentPolicyId} | 


# **create_fulfillment_policy**
> SetFulfillmentPolicyResponse create_fulfillment_policy(content_type, fulfillment_policy_request)

This method creates a new fulfillment policy for an eBay marketplace where the policy encapsulates seller's terms for fulfilling item purchases. Fulfillment policies include the shipment options that the seller offers to buyers.  <br><br>A successful request returns the <b>getFulfillmentPolicy</b> URI to the new policy in the <b>Location</b> response header and the ID for the new policy is returned in the response payload.  <p class="tablenote"><b>Tip:</b> For details on creating and using the business policies supported by the Account API, see <a href="/api-docs/sell/static/seller-accounts/business-policies.html">eBay business policies</a>.</p>

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.fulfillment_policy_request import FulfillmentPolicyRequest
from ebayaccount.models.set_fulfillment_policy_response import SetFulfillmentPolicyResponse
from ebayaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/account/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayaccount.Configuration(
    host = "https://api.ebay.com/sell/account/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayaccount.FulfillmentPolicyApi(api_client)
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    fulfillment_policy_request = ebayaccount.FulfillmentPolicyRequest() # FulfillmentPolicyRequest | Request to create a seller account fulfillment policy.

    try:
        api_response = api_instance.create_fulfillment_policy(content_type, fulfillment_policy_request)
        print("The response of FulfillmentPolicyApi->create_fulfillment_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentPolicyApi->create_fulfillment_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **fulfillment_policy_request** | [**FulfillmentPolicyRequest**](FulfillmentPolicyRequest.md)| Request to create a seller account fulfillment policy. | 

### Return type

[**SetFulfillmentPolicyResponse**](SetFulfillmentPolicyResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location -  <br>  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fulfillment_policy**
> delete_fulfillment_policy(fulfillment_policy_id)

This method deletes a fulfillment policy. Supply the ID of the policy you want to delete in the <b>fulfillmentPolicyId</b> path parameter.

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/account/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayaccount.Configuration(
    host = "https://api.ebay.com/sell/account/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayaccount.FulfillmentPolicyApi(api_client)
    fulfillment_policy_id = 'fulfillment_policy_id_example' # str | This path parameter specifies the ID of the fulfillment policy to delete.<br><br> This ID can be retrieved for a fulfillment policy by using the <a href=\"/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\" target=\"_blank \">getFulfillmentPolicies</a> method.

    try:
        api_instance.delete_fulfillment_policy(fulfillment_policy_id)
    except Exception as e:
        print("Exception when calling FulfillmentPolicyApi->delete_fulfillment_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_policy_id** | **str**| This path parameter specifies the ID of the fulfillment policy to delete.&lt;br&gt;&lt;br&gt; This ID can be retrieved for a fulfillment policy by using the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getFulfillmentPolicies&lt;/a&gt; method. | 

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_policies**
> FulfillmentPolicyResponse get_fulfillment_policies(marketplace_id, content_language=content_language)

This method retrieves all the fulfillment policies configured for the marketplace you specify using the <code>marketplace_id</code> query parameter.

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.fulfillment_policy_response import FulfillmentPolicyResponse
from ebayaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/account/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayaccount.Configuration(
    host = "https://api.ebay.com/sell/account/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayaccount.FulfillmentPolicyApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This query parameter specifies the eBay marketplace of the policies you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum
    content_language = 'content_language_example' # str | Get the correct policies for a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, get the policies for the French locale of the Canadian marketplace by specifying <code>fr-CA</code> for the <code>Content-Language</code> header. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>. For details on header values, see <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank\">HTTP request headers</a>. (optional)

    try:
        api_response = api_instance.get_fulfillment_policies(marketplace_id, content_language=content_language)
        print("The response of FulfillmentPolicyApi->get_fulfillment_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentPolicyApi->get_fulfillment_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This query parameter specifies the eBay marketplace of the policies you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum | 
 **content_language** | **str**| Get the correct policies for a marketplace that supports multiple locales using the &lt;code&gt;Content-Language&lt;/code&gt; request header. For example, get the policies for the French locale of the Canadian marketplace by specifying &lt;code&gt;fr-CA&lt;/code&gt; for the &lt;code&gt;Content-Language&lt;/code&gt; header. Likewise, target the Dutch locale of the Belgium marketplace by setting &lt;code&gt;Content-Language: nl-BE&lt;/code&gt;. For details on header values, see &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP request headers&lt;/a&gt;. | [optional] 

### Return type

[**FulfillmentPolicyResponse**](FulfillmentPolicyResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_policy**
> FulfillmentPolicy get_fulfillment_policy(fulfillment_policy_id)

This method retrieves the complete details of a fulfillment policy. Supply the ID of the policy you want to retrieve using the <b>fulfillmentPolicyId</b> path parameter.

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.fulfillment_policy import FulfillmentPolicy
from ebayaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/account/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayaccount.Configuration(
    host = "https://api.ebay.com/sell/account/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayaccount.FulfillmentPolicyApi(api_client)
    fulfillment_policy_id = 'fulfillment_policy_id_example' # str | This path parameter specifies the ID of the fulfillment policy you want to retrieve.<br><br> This ID can be retrieved for a fulfillment policy by using the <a href=\"/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\" target=\"_blank \">getFulfillmentPolicies</a> method.

    try:
        api_response = api_instance.get_fulfillment_policy(fulfillment_policy_id)
        print("The response of FulfillmentPolicyApi->get_fulfillment_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentPolicyApi->get_fulfillment_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_policy_id** | **str**| This path parameter specifies the ID of the fulfillment policy you want to retrieve.&lt;br&gt;&lt;br&gt; This ID can be retrieved for a fulfillment policy by using the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getFulfillmentPolicies&lt;/a&gt; method. | 

### Return type

[**FulfillmentPolicy**](FulfillmentPolicy.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_policy_by_name**
> FulfillmentPolicy get_fulfillment_policy_by_name(marketplace_id, name, content_language=content_language)

This method retrieves the details for a specific fulfillment policy. In the request, supply both the policy <code>name</code> and its associated <code>marketplace_id</code> as query parameters.

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.fulfillment_policy import FulfillmentPolicy
from ebayaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/account/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayaccount.Configuration(
    host = "https://api.ebay.com/sell/account/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayaccount.FulfillmentPolicyApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This query parameter specifies the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum
    name = 'name_example' # str | This query parameter specifies the seller-defined name of the fulfillment policy you want to retrieve.<br><br>This value can be retrieved for a fulfillment policy by using the <a href=\"/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\" target=\"_blank \">getFulfillmentPolicies</a> method.
    content_language = 'content_language_example' # str | Get the correct policies for a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, get the policies for the French locale of the Canadian marketplace by specifying <code>fr-CA</code> for the <code>Content-Language</code> header. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>. For details on header values, see <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank\">HTTP request headers</a>. (optional)

    try:
        api_response = api_instance.get_fulfillment_policy_by_name(marketplace_id, name, content_language=content_language)
        print("The response of FulfillmentPolicyApi->get_fulfillment_policy_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentPolicyApi->get_fulfillment_policy_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This query parameter specifies the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum | 
 **name** | **str**| This query parameter specifies the seller-defined name of the fulfillment policy you want to retrieve.&lt;br&gt;&lt;br&gt;This value can be retrieved for a fulfillment policy by using the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getFulfillmentPolicies&lt;/a&gt; method. | 
 **content_language** | **str**| Get the correct policies for a marketplace that supports multiple locales using the &lt;code&gt;Content-Language&lt;/code&gt; request header. For example, get the policies for the French locale of the Canadian marketplace by specifying &lt;code&gt;fr-CA&lt;/code&gt; for the &lt;code&gt;Content-Language&lt;/code&gt; header. Likewise, target the Dutch locale of the Belgium marketplace by setting &lt;code&gt;Content-Language: nl-BE&lt;/code&gt;. For details on header values, see &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP request headers&lt;/a&gt;. | [optional] 

### Return type

[**FulfillmentPolicy**](FulfillmentPolicy.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fulfillment_policy**
> SetFulfillmentPolicyResponse update_fulfillment_policy(fulfillment_policy_id, content_type, fulfillment_policy_request)

This method updates an existing fulfillment policy. Specify the policy you want to update using the <b>fulfillment_policy_id</b> path parameter. Supply a complete policy payload with the updates you want to make; this call overwrites the existing policy with the new details specified in the payload.

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.fulfillment_policy_request import FulfillmentPolicyRequest
from ebayaccount.models.set_fulfillment_policy_response import SetFulfillmentPolicyResponse
from ebayaccount.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/account/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayaccount.Configuration(
    host = "https://api.ebay.com/sell/account/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayaccount.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayaccount.FulfillmentPolicyApi(api_client)
    fulfillment_policy_id = 'fulfillment_policy_id_example' # str | This path parameter specifies the ID of the fulfillment policy you want to update.<br><br>This ID can be retrieved for a specific fulfillment policy by using the <a href=\"/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\" target=\"_blank \">getFulfillmentPolicies</a> method.
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    fulfillment_policy_request = ebayaccount.FulfillmentPolicyRequest() # FulfillmentPolicyRequest | Fulfillment policy request

    try:
        api_response = api_instance.update_fulfillment_policy(fulfillment_policy_id, content_type, fulfillment_policy_request)
        print("The response of FulfillmentPolicyApi->update_fulfillment_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentPolicyApi->update_fulfillment_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_policy_id** | **str**| This path parameter specifies the ID of the fulfillment policy you want to update.&lt;br&gt;&lt;br&gt;This ID can be retrieved for a specific fulfillment policy by using the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getFulfillmentPolicies&lt;/a&gt; method. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **fulfillment_policy_request** | [**FulfillmentPolicyRequest**](FulfillmentPolicyRequest.md)| Fulfillment policy request | 

### Return type

[**SetFulfillmentPolicyResponse**](SetFulfillmentPolicyResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

