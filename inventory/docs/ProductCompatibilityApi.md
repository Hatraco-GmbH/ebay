# ebayinventory.ProductCompatibilityApi

All URIs are relative to *https://api.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_replace_product_compatibility**](ProductCompatibilityApi.md#create_or_replace_product_compatibility) | **PUT** /inventory_item/{sku}/product_compatibility | 
[**delete_product_compatibility**](ProductCompatibilityApi.md#delete_product_compatibility) | **DELETE** /inventory_item/{sku}/product_compatibility | 
[**get_product_compatibility**](ProductCompatibilityApi.md#get_product_compatibility) | **GET** /inventory_item/{sku}/product_compatibility | 

# **create_or_replace_product_compatibility**
> BaseResponse create_or_replace_product_compatibility(body, content_language, content_type, sku)



This call is used by the seller to create or replace a list of products that are compatible with the inventory item. The inventory item is identified with a SKU value in the URI. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.<br><br><span class=\"tablenote\"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> and <code>Content-Language</code> headers. See the <a href=\"/api-docs/sell/inventory/resources/inventory_item/product_compatibility/methods/createOrReplaceProductCompatibility#h3-request-headers\">HTTP request headers</a> for more information.</span>

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.ProductCompatibilityApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.Compatibility() # Compatibility | Details of the compatibility
content_language = 'content_language_example' # str | This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be <code>en-US</code> for English or <code>de-DE</code> for German.<br><br>For more information on the Content-Language header, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
sku = 'sku_example' # str | This path parameter specifies the SKU (stock keeping unit) of the inventory item associated with the compatibility list being created.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\" target=\"_blank \">getInventoryItems</a> method to retrieve SKU values.

try:
    api_response = api_instance.create_or_replace_product_compatibility(body, content_language, content_type, sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductCompatibilityApi->create_or_replace_product_compatibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Compatibility**](Compatibility.md)| Details of the compatibility | 
 **content_language** | **str**| This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be &lt;code&gt;en-US&lt;/code&gt; for English or &lt;code&gt;de-DE&lt;/code&gt; for German.&lt;br&gt;&lt;br&gt;For more information on the Content-Language header, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **sku** | **str**| This path parameter specifies the SKU (stock keeping unit) of the inventory item associated with the compatibility list being created.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getInventoryItems&lt;/a&gt; method to retrieve SKU values. | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_compatibility**
> delete_product_compatibility(sku)



This call is used by the seller to delete the list of products that are compatible with the inventory item that is associated with the compatible product list. The inventory item is identified with a SKU value in the URI. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.ProductCompatibilityApi(ebayinventory.ApiClient(configuration))
sku = 'sku_example' # str | This path parameter specifies the SKU (stock keeping unit) of the inventory item that is associated with the product compatibility list that is being deleted.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\" target=\"_blank \">getInventoryItems</a> method to retrieve SKU values.

try:
    api_instance.delete_product_compatibility(sku)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_compatibility**
> Compatibility get_product_compatibility(sku)



This call is used by the seller to retrieve the list of products that are compatible with the inventory item. The SKU value for the inventory item is passed into the call URI, and a successful call with return the compatible vehicle list associated with this inventory item. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.ProductCompatibilityApi(ebayinventory.ApiClient(configuration))
sku = 'sku_example' # str | This path parameter specifies the SKU (stock keeping unit) of the inventory item associated with the product compatibility list being retrieved.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\" target=\"_blank \">getInventoryItems</a> method to retrieve SKU values.

try:
    api_response = api_instance.get_product_compatibility(sku)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

