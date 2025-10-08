# ebayinventory.ProductCompatibilityApi

All URIs are relative to *https://api.ebay.com/sell/inventory/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_replace_product_compatibility**](ProductCompatibilityApi.md#create_or_replace_product_compatibility) | **PUT** /inventory_item/{sku}/product_compatibility | 
[**delete_product_compatibility**](ProductCompatibilityApi.md#delete_product_compatibility) | **DELETE** /inventory_item/{sku}/product_compatibility | 
[**get_product_compatibility**](ProductCompatibilityApi.md#get_product_compatibility) | **GET** /inventory_item/{sku}/product_compatibility | 


# **create_or_replace_product_compatibility**
> BaseResponse create_or_replace_product_compatibility(content_language, sku, content_type, compatibility)

This call is used by the seller to create or replace a list of products that are compatible with the inventory item. The inventory item is identified with a SKU value in the URI. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.<br><br><span class="tablenote"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> and <code>Content-Language</code> headers. See the <a href="/api-docs/sell/inventory/resources/inventory_item/product_compatibility/methods/createOrReplaceProductCompatibility#h3-request-headers">HTTP request headers</a> for more information.</span>

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.base_response import BaseResponse
from ebayinventory.models.compatibility import Compatibility
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.ProductCompatibilityApi(api_client)
    content_language = 'content_language_example' # str | This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be <code>en-US</code> for English or <code>de-DE</code> for German.<br><br>For more information on the Content-Language header, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    sku = 'sku_example' # str | This path parameter specifies the SKU (stock keeping unit) of the inventory item associated with the compatibility list being created.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\" target=\"_blank \">getInventoryItems</a> method to retrieve SKU values.
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    compatibility = ebayinventory.Compatibility() # Compatibility | Details of the compatibility

    try:
        api_response = api_instance.create_or_replace_product_compatibility(content_language, sku, content_type, compatibility)
        print("The response of ProductCompatibilityApi->create_or_replace_product_compatibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCompatibilityApi->create_or_replace_product_compatibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_language** | **str**| This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be &lt;code&gt;en-US&lt;/code&gt; for English or &lt;code&gt;de-DE&lt;/code&gt; for German.&lt;br&gt;&lt;br&gt;For more information on the Content-Language header, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **sku** | **str**| This path parameter specifies the SKU (stock keeping unit) of the inventory item associated with the compatibility list being created.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getInventoryItems&lt;/a&gt; method to retrieve SKU values. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **compatibility** | [**Compatibility**](Compatibility.md)| Details of the compatibility | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Content-Language -  <br>  |
**201** | Created |  * Content-Language -  <br>  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_compatibility**
> delete_product_compatibility(sku)

This call is used by the seller to delete the list of products that are compatible with the inventory item that is associated with the compatible product list. The inventory item is identified with a SKU value in the URI. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.ProductCompatibilityApi(api_client)
    sku = 'sku_example' # str | This path parameter specifies the SKU (stock keeping unit) of the inventory item that is associated with the product compatibility list that is being deleted.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\" target=\"_blank \">getInventoryItems</a> method to retrieve SKU values.

    try:
        api_instance.delete_product_compatibility(sku)
    except Exception as e:
        print("Exception when calling ProductCompatibilityApi->delete_product_compatibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**| This path parameter specifies the SKU (stock keeping unit) of the inventory item that is associated with the product compatibility list that is being deleted.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getInventoryItems&lt;/a&gt; method to retrieve SKU values. | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_compatibility**
> Compatibility get_product_compatibility(sku)

This call is used by the seller to retrieve the list of products that are compatible with the inventory item. The SKU value for the inventory item is passed into the call URI, and a successful call with return the compatible vehicle list associated with this inventory item. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.compatibility import Compatibility
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.ProductCompatibilityApi(api_client)
    sku = 'sku_example' # str | This path parameter specifies the SKU (stock keeping unit) of the inventory item associated with the product compatibility list being retrieved.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\" target=\"_blank \">getInventoryItems</a> method to retrieve SKU values.

    try:
        api_response = api_instance.get_product_compatibility(sku)
        print("The response of ProductCompatibilityApi->get_product_compatibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCompatibilityApi->get_product_compatibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**| This path parameter specifies the SKU (stock keeping unit) of the inventory item associated with the product compatibility list being retrieved.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getInventoryItems&lt;/a&gt; method to retrieve SKU values. | 

### Return type

[**Compatibility**](Compatibility.md)

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

