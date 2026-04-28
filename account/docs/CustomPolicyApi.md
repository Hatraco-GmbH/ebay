# ebayaccount.CustomPolicyApi

All URIs are relative to *https://api.ebay.com/sell/account/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_policy**](CustomPolicyApi.md#create_custom_policy) | **POST** /custom_policy/ | 
[**get_custom_policies**](CustomPolicyApi.md#get_custom_policies) | **GET** /custom_policy/ | 
[**get_custom_policy**](CustomPolicyApi.md#get_custom_policy) | **GET** /custom_policy/{custom_policy_id} | 
[**update_custom_policy**](CustomPolicyApi.md#update_custom_policy) | **PUT** /custom_policy/{custom_policy_id} | 


# **create_custom_policy**
> object create_custom_policy(content_type, custom_policy_create_request)

This method creates a new custom policy that specifies the seller's terms for complying with local governmental regulations. Each Custom Policy targets a <b>policyType</b>. Multiple policies may be created as using the following custom policy types:<ul><li>PRODUCT_COMPLIANCE: Product Compliance policies disclose product information as required for regulatory compliance. <br/><br/><span class="tablenote"><strong>Note:</strong> A maximum of 60 Product Compliance policies per seller may be created.</span></li><li>TAKE_BACK: Takeback policies describe the seller's legal obligation to take back a previously purchased item when the buyer purchases a new one. <br/><br/><span class="tablenote"><strong>Note:</strong> A maximum of 18 Takeback policies per seller may be created.</span></li></ul>A successful create policy call returns an HTTP status code of <b>201 Created</b> with the system-generated policy ID included in the Location response header.

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.custom_policy_create_request import CustomPolicyCreateRequest
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
    api_instance = ebayaccount.CustomPolicyApi(api_client)
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    custom_policy_create_request = ebayaccount.CustomPolicyCreateRequest() # CustomPolicyCreateRequest | Request to create a new Custom Policy.

    try:
        api_response = api_instance.create_custom_policy(content_type, custom_policy_create_request)
        print("The response of CustomPolicyApi->create_custom_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPolicyApi->create_custom_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **custom_policy_create_request** | [**CustomPolicyCreateRequest**](CustomPolicyCreateRequest.md)| Request to create a new Custom Policy. | 

### Return type

**object**

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
**409** | Policy Name already used/ Maximum no of policies per site reached |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_policies**
> CustomPolicyResponse get_custom_policies(policy_types=policy_types)

This method retrieves the list of custom policies defined for a seller's account. To limit the returned custom policies, specify the <b>policy_types</b> query parameter.

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.custom_policy_response import CustomPolicyResponse
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
    api_instance = ebayaccount.CustomPolicyApi(api_client)
    policy_types = 'policy_types_example' # str | This query parameter specifies the type of custom policies to be returned.<br><br>Multiple policy types may be requested in a single call by providing a comma-delimited set of all policy types to be returned.<br><br><span class=\"tablenote\"><strong>Note:</strong> Omitting this query parameter from a request will also return policies of all policy types.</span><br> See the <a href=\"/api-docs/sell/account/types/api:CustomPolicyTypeEnum\" target=\"_blank \">CustomPolicyTypeEnum</a> type for a list of supported values. (optional)

    try:
        api_response = api_instance.get_custom_policies(policy_types=policy_types)
        print("The response of CustomPolicyApi->get_custom_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPolicyApi->get_custom_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_types** | **str**| This query parameter specifies the type of custom policies to be returned.&lt;br&gt;&lt;br&gt;Multiple policy types may be requested in a single call by providing a comma-delimited set of all policy types to be returned.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; Omitting this query parameter from a request will also return policies of all policy types.&lt;/span&gt;&lt;br&gt; See the &lt;a href&#x3D;\&quot;/api-docs/sell/account/types/api:CustomPolicyTypeEnum\&quot; target&#x3D;\&quot;_blank \&quot;&gt;CustomPolicyTypeEnum&lt;/a&gt; type for a list of supported values. | [optional] 

### Return type

[**CustomPolicyResponse**](CustomPolicyResponse.md)

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

# **get_custom_policy**
> CustomPolicy get_custom_policy(custom_policy_id)

This method retrieves the custom policy specified by the <b>custom_policy_id</b> path parameter.

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.custom_policy import CustomPolicy
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
    api_instance = ebayaccount.CustomPolicyApi(api_client)
    custom_policy_id = 'custom_policy_id_example' # str | This path parameter is the unique identifier of the custom policy to retrieve.<br><br> This ID can be retrieved for a custom policy by using the <a href=\"/api-docs/sell/account/resources/custom_policy/methods/getCustomPolicies\" target=\"_blank \">getCustomPolicies</a> method.

    try:
        api_response = api_instance.get_custom_policy(custom_policy_id)
        print("The response of CustomPolicyApi->get_custom_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPolicyApi->get_custom_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_policy_id** | **str**| This path parameter is the unique identifier of the custom policy to retrieve.&lt;br&gt;&lt;br&gt; This ID can be retrieved for a custom policy by using the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/custom_policy/methods/getCustomPolicies\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getCustomPolicies&lt;/a&gt; method. | 

### Return type

[**CustomPolicy**](CustomPolicy.md)

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

# **update_custom_policy**
> update_custom_policy(custom_policy_id, content_type, custom_policy_request)

This method updates an existing custom policy specified by the <b>custom_policy_id</b> path parameter. Since this method overwrites the policy's <b>name</b>, <b>label</b>, and <b>description</b> fields, always include the complete and current text of all three policy fields in the request payload, even if they are not being updated.<br/> <br/>For example, the value for the <b>label</b> field is to be updated, but the <b>name</b> and <b>description</b> values will remain unchanged. The existing <b>name</b> and <b>description</b> values, as they are defined in the current policy, must also be passed in. <br/><br/>A successful policy update call returns an HTTP status code of <b>204 No Content</b>.

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.custom_policy_request import CustomPolicyRequest
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
    api_instance = ebayaccount.CustomPolicyApi(api_client)
    custom_policy_id = 'custom_policy_id_example' # str | This path parameter is the unique identifier of the custom policy to update.<br><br><span class=\"tablenote\"><b>Note:</b> A list of custom policies defined for a seller's account that includes this ID can be retrieved by calling the <a href=\"/api-docs/sell/account/resources/custom_policy/methods/getCustomPolicies\" target=\"_blank \">getCustomPolicies</a> method.</span>
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    custom_policy_request = ebayaccount.CustomPolicyRequest() # CustomPolicyRequest | Request to update a current custom policy.

    try:
        api_instance.update_custom_policy(custom_policy_id, content_type, custom_policy_request)
    except Exception as e:
        print("Exception when calling CustomPolicyApi->update_custom_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_policy_id** | **str**| This path parameter is the unique identifier of the custom policy to update.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; A list of custom policies defined for a seller&#39;s account that includes this ID can be retrieved by calling the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/custom_policy/methods/getCustomPolicies\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getCustomPolicies&lt;/a&gt; method.&lt;/span&gt; | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **custom_policy_request** | [**CustomPolicyRequest**](CustomPolicyRequest.md)| Request to update a current custom policy. | 

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Policy Name already used/ Maximum no of policies per site reached |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

