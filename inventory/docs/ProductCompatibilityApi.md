# ebayinventory.ProductCompatibilityApi

All URIs are relative to *https://api.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_replace_product_compatibility**](ProductCompatibilityApi.md#create_or_replace_product_compatibility) | **PUT** /inventory_item/{sku}/product_compatibility | 
[**delete_product_compatibility**](ProductCompatibilityApi.md#delete_product_compatibility) | **DELETE** /inventory_item/{sku}/product_compatibility | 
[**get_product_compatibility**](ProductCompatibilityApi.md#get_product_compatibility) | **GET** /inventory_item/{sku}/product_compatibility | 

# **create_or_replace_product_compatibility**
> BaseResponse create_or_replace_product_compatibility(body, content_language, sku)



This call is used by the seller to create or replace a list of products that are compatible with the inventory item. The inventory item is identified with a SKU value in the URI. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future. In addition to the authorization header, which is required for all eBay REST API calls, the createOrReplaceProductCompatibility call also requires the Content-Language header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be en-US. To view other supported Content-Language values, and to read more about all supported HTTP headers for eBay REST API calls, see the HTTP request headers topic in the Using eBay RESTful APIs document.

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
content_language = 'content_language_example' # str | This request header sets the natural language that will be provided in the field values of the request payload.
sku = 'sku_example' # str | A SKU (stock keeping unit) is an unique identifier defined by a seller for a product

try:
    api_response = api_instance.create_or_replace_product_compatibility(body, content_language, sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductCompatibilityApi->create_or_replace_product_compatibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Compatibility**](Compatibility.md)| Details of the compatibility | 
 **content_language** | **str**| This request header sets the natural language that will be provided in the field values of the request payload. | 
 **sku** | **str**| A SKU (stock keeping unit) is an unique identifier defined by a seller for a product | 

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
sku = 'sku_example' # str | A SKU (stock keeping unit) is an unique identifier defined by a seller for a product

try:
    api_instance.delete_product_compatibility(sku)
except ApiException as e:
    print("Exception when calling ProductCompatibilityApi->delete_product_compatibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**| A SKU (stock keeping unit) is an unique identifier defined by a seller for a product | 

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
sku = 'sku_example' # str | A SKU (stock keeping unit) is an unique identifier defined by a seller for a product

try:
    api_response = api_instance.get_product_compatibility(sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductCompatibilityApi->get_product_compatibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**| A SKU (stock keeping unit) is an unique identifier defined by a seller for a product | 

### Return type

[**Compatibility**](Compatibility.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

