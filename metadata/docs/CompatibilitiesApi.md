# ebaymetadata.CompatibilitiesApi

All URIs are relative to *https://api.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_compatibilities_by_specification**](CompatibilitiesApi.md#get_compatibilities_by_specification) | **POST** /compatibilities/get_compatibilities_by_specification | 
[**get_compatibility_property_names**](CompatibilitiesApi.md#get_compatibility_property_names) | **POST** /compatibilities/get_compatibility_property_names | 
[**get_compatibility_property_values**](CompatibilitiesApi.md#get_compatibility_property_values) | **POST** /compatibilities/get_compatibility_property_values | 
[**get_multi_compatibility_property_values**](CompatibilitiesApi.md#get_multi_compatibility_property_values) | **POST** /compatibilities/get_multi_compatibility_property_values | 
[**get_product_compatibilities**](CompatibilitiesApi.md#get_product_compatibilities) | **POST** /compatibilities/get_product_compatibilities | 

# **get_compatibilities_by_specification**
> SpecificationResponse get_compatibilities_by_specification(x_ebay_c_marketplace_id, content_type, body=body)



This method is used to retrieve all compatible application name-value pairs for a part based on the provided specification(s).<br><br>The part's relevant dimensions and/or characteristics can be provided through the <b>specifications</b> container. For example, when retrieving compatible application name-value pairs for a tire, the tire's dimensions (such as the section width or rim diameter) should be provided.<br><br>By default, all compatible application name-value pairs for the specifications are returned. You can limit the size of the result set by using the <b>compatibilityPropertyFilters</b> array to specify the properties (such as make, model, year, or trim) you wish to be included in the response.<br><br><span class=\"tablenote\"><b>Note:</b> The <a href=\"/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyNames\" target=\"_blank \">getCompatibilityPropertyNames</a> and <a href=\"/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyValues\" target=\"_blank \">getCompatibilityPropertyValues</a> methods can be used to retrieve valid property names and values that can be used as the name-value pairs to define specifications.</span>

### Example
```python
from __future__ import print_function
import time
import ebaymetadata
from ebaymetadata.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaymetadata.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaymetadata.CompatibilitiesApi(ebaymetadata.ApiClient(configuration))
x_ebay_c_marketplace_id = 'x_ebay_c_marketplace_id_example' # str | This header identifies the seller's eBay marketplace.<br><br>See <a href=\"/api-docs/sell/metadata/overview.html#requirements\" target=\"_blank \">Metadata API requirements and restrictions</a> for supported values.
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client.<br><br>Its value should be set to <code>application/json</code>.<br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a> in the <a href=\"/api-docs/static/ebay-rest-landing.html\" target=\"_blank\">Using eBay RESTful APIs</a> guide.
body = ebaymetadata.SpecificationRequest() # SpecificationRequest | This type defines the properties and specifications to use to search for compatibilities. (optional)

try:
    api_response = api_instance.get_compatibilities_by_specification(x_ebay_c_marketplace_id, content_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompatibilitiesApi->get_compatibilities_by_specification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ebay_c_marketplace_id** | **str**| This header identifies the seller&#x27;s eBay marketplace.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/overview.html#requirements\&quot; target&#x3D;\&quot;_blank \&quot;&gt;Metadata API requirements and restrictions&lt;/a&gt; for supported values. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client.&lt;br&gt;&lt;br&gt;Its value should be set to &lt;code&gt;application/json&lt;/code&gt;.&lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt; in the &lt;a href&#x3D;\&quot;/api-docs/static/ebay-rest-landing.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Using eBay RESTful APIs&lt;/a&gt; guide. | 
 **body** | [**SpecificationRequest**](SpecificationRequest.md)| This type defines the properties and specifications to use to search for compatibilities. | [optional] 

### Return type

[**SpecificationResponse**](SpecificationResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compatibility_property_names**
> PropertyNamesResponse get_compatibility_property_names(x_ebay_c_marketplace_id, content_type, body=body)



This method is used to retrieve product compatibility property names for the specified compatibility-enabled category.<br><br>Compatibility property names can be used alongside the corresponding compatibility property value (retrieved using the <a href=\"/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyValues\" target=\"_blank \">getCompatibilityPropertyValues</a> method) to describe the assembly for which an item is compatible.<br><br>The <b>categoryId</b> of the compatibility-enabled category for which to retrieve compatibility property names is required in the request body.<br><br>By default, all property names within the compatibility category of the specified compatibility-enable category are returned. You can limit the size of the result set by using the <b>dataset</b> array to specify the types of properties you want returned.

### Example
```python
from __future__ import print_function
import time
import ebaymetadata
from ebaymetadata.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaymetadata.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaymetadata.CompatibilitiesApi(ebaymetadata.ApiClient(configuration))
x_ebay_c_marketplace_id = 'x_ebay_c_marketplace_id_example' # str | This header identifies the seller's eBay marketplace.<br><br>See <a href=\"/api-docs/sell/metadata/overview.html#requirements\" target=\"_blank \">Metadata API requirements and restrictions</a> for supported values.
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client.<br><br>Its value should be set to <code>application/json</code>.<br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a> in the <a href=\"/api-docs/static/ebay-rest-landing.html\" target=\"_blank\">Using eBay RESTful APIs</a> guide.
body = ebaymetadata.PropertyNamesRequest() # PropertyNamesRequest | This type defines the properties used to retrieve compatibility property names. (optional)

try:
    api_response = api_instance.get_compatibility_property_names(x_ebay_c_marketplace_id, content_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompatibilitiesApi->get_compatibility_property_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ebay_c_marketplace_id** | **str**| This header identifies the seller&#x27;s eBay marketplace.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/overview.html#requirements\&quot; target&#x3D;\&quot;_blank \&quot;&gt;Metadata API requirements and restrictions&lt;/a&gt; for supported values. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client.&lt;br&gt;&lt;br&gt;Its value should be set to &lt;code&gt;application/json&lt;/code&gt;.&lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt; in the &lt;a href&#x3D;\&quot;/api-docs/static/ebay-rest-landing.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Using eBay RESTful APIs&lt;/a&gt; guide. | 
 **body** | [**PropertyNamesRequest**](PropertyNamesRequest.md)| This type defines the properties used to retrieve compatibility property names. | [optional] 

### Return type

[**PropertyNamesResponse**](PropertyNamesResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compatibility_property_values**
> PropertyValuesResponse get_compatibility_property_values(x_ebay_c_marketplace_id, content_type, body=body)



This method is used to retrieve product compatibility property values associated with a single property name, in the specified category.<br><br>Compatibility property values can be used alongside the corresponding compatibility property name (retrieved using the <a href=\"/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyNames\" target=\"_blank \">getCompatibilityPropertyNames</a> method) to describe the assembly for which an item is compatible.<br><br>The <b>categoryId</b> of the compatibility-enabled category for which to retrieve compatibility property values is required in the request body, as well as the <b>propertyName</b> for which you wish to retrieve associated values.<br><br>By default, all property values associated with the specified <b>propertyName</b> are returned. You can limit the size of the result set by using the <b>propertyFilter</b> array. Only property values associated with the specified name-value pairs will be returned.

### Example
```python
from __future__ import print_function
import time
import ebaymetadata
from ebaymetadata.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaymetadata.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaymetadata.CompatibilitiesApi(ebaymetadata.ApiClient(configuration))
x_ebay_c_marketplace_id = 'x_ebay_c_marketplace_id_example' # str | This header identifies the seller's eBay marketplace.<br><br>See <a href=\"/api-docs/sell/metadata/overview.html#requirements\" target=\"_blank \">Metadata API requirements and restrictions</a> for supported values.
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client.<br><br>Its value should be set to <code>application/json</code>.<br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a> in the <a href=\"/api-docs/static/ebay-rest-landing.html\" target=\"_blank\">Using eBay RESTful APIs</a> guide.
body = ebaymetadata.PropertyValuesRequest() # PropertyValuesRequest | This type defines the category ID and property name for which to retrieve values. (optional)

try:
    api_response = api_instance.get_compatibility_property_values(x_ebay_c_marketplace_id, content_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompatibilitiesApi->get_compatibility_property_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ebay_c_marketplace_id** | **str**| This header identifies the seller&#x27;s eBay marketplace.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/overview.html#requirements\&quot; target&#x3D;\&quot;_blank \&quot;&gt;Metadata API requirements and restrictions&lt;/a&gt; for supported values. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client.&lt;br&gt;&lt;br&gt;Its value should be set to &lt;code&gt;application/json&lt;/code&gt;.&lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt; in the &lt;a href&#x3D;\&quot;/api-docs/static/ebay-rest-landing.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Using eBay RESTful APIs&lt;/a&gt; guide. | 
 **body** | [**PropertyValuesRequest**](PropertyValuesRequest.md)| This type defines the category ID and property name for which to retrieve values. | [optional] 

### Return type

[**PropertyValuesResponse**](PropertyValuesResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multi_compatibility_property_values**
> MultiCompatibilityPropertyValuesResponse get_multi_compatibility_property_values(x_ebay_c_marketplace_id, content_type, body=body)



This method is used to retrieve product compatibility property values associated with multiple property names, in the specified category.<br><br>Compatibility property values can be used alongside the corresponding compatibility property name (retrieved using the <a href=\"/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyNames\" target=\"_blank \">getCompatibilityPropertyNames</a> method) to describe the assembly for which an item is compatible.<br><br>The <b>categoryId</b> of the compatibility-enabled category for which to retrieve compatibility property values is required in the request body, as well as the <b>propertyNames</b> for which you wish to retrieve associated property values. The <b>propertyFilter</b> array is also required to constrain the output. Only property values associated with the specified name-value pairs will be returned.

### Example
```python
from __future__ import print_function
import time
import ebaymetadata
from ebaymetadata.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaymetadata.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaymetadata.CompatibilitiesApi(ebaymetadata.ApiClient(configuration))
x_ebay_c_marketplace_id = 'x_ebay_c_marketplace_id_example' # str | This header identifies the seller's eBay marketplace.<br><br>See <a href=\"/api-docs/sell/metadata/overview.html#requirements\" target=\"_blank \">Metadata API requirements and restrictions</a> for supported values.
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client.<br><br>Its value should be set to <code>application/json</code>.<br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a> in the <a href=\"/api-docs/static/ebay-rest-landing.html\" target=\"_blank\">Using eBay RESTful APIs</a> guide.
body = ebaymetadata.MultiCompatibilityPropertyValuesRequest() # MultiCompatibilityPropertyValuesRequest | This type defines the category ID and property names for which to retrieve values. (optional)

try:
    api_response = api_instance.get_multi_compatibility_property_values(x_ebay_c_marketplace_id, content_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompatibilitiesApi->get_multi_compatibility_property_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ebay_c_marketplace_id** | **str**| This header identifies the seller&#x27;s eBay marketplace.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/overview.html#requirements\&quot; target&#x3D;\&quot;_blank \&quot;&gt;Metadata API requirements and restrictions&lt;/a&gt; for supported values. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client.&lt;br&gt;&lt;br&gt;Its value should be set to &lt;code&gt;application/json&lt;/code&gt;.&lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt; in the &lt;a href&#x3D;\&quot;/api-docs/static/ebay-rest-landing.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Using eBay RESTful APIs&lt;/a&gt; guide. | 
 **body** | [**MultiCompatibilityPropertyValuesRequest**](MultiCompatibilityPropertyValuesRequest.md)| This type defines the category ID and property names for which to retrieve values. | [optional] 

### Return type

[**MultiCompatibilityPropertyValuesResponse**](MultiCompatibilityPropertyValuesResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_compatibilities**
> ProductResponse get_product_compatibilities(x_ebay_c_marketplace_id, content_type, body=body)



This method is used to retrieve all available item compatibility details for the specified product.<br><br>Item compatibility details can be used to see the properties for which an item is compatible. For example, if you are searching for a part for a specific vehicle, you can use this method to see the years, engine, and/or trim for which the part is compatible. Item compatibility details are returned as name-value pairs.<br><br>The product for which to retrieve item compatibility details must be provided through the <b>productIdentifier</b> field. This value can be either an eBay specific identifier (such as an ePID) or an external identifier (such as a UPC).<br><br>By default, all available item compatibility details for the specified product are returned. You can limit the size of the result set using the <b>dataset</b> or <b>datasetPropertyName</b> fields to specify the types of properties you want returned in the response. The <b>applicationPropertyFilter</b> array can also be used so that only parts compatible with the specified name-value pairs are returned.

### Example
```python
from __future__ import print_function
import time
import ebaymetadata
from ebaymetadata.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaymetadata.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaymetadata.CompatibilitiesApi(ebaymetadata.ApiClient(configuration))
x_ebay_c_marketplace_id = 'x_ebay_c_marketplace_id_example' # str | This header identifies the seller's eBay marketplace.<br><br>See <a href=\"/api-docs/sell/metadata/overview.html#requirements\" target=\"_blank \">Metadata API requirements and restrictions</a> for supported values.
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client.<br><br>Its value should be set to <code>application/json</code>.<br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a> in the <a href=\"/api-docs/static/ebay-rest-landing.html\" target=\"_blank\">Using eBay RESTful APIs</a> guide.
body = ebaymetadata.ProductRequest() # ProductRequest | This type defines properties for which to find compatibilities. (optional)

try:
    api_response = api_instance.get_product_compatibilities(x_ebay_c_marketplace_id, content_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompatibilitiesApi->get_product_compatibilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ebay_c_marketplace_id** | **str**| This header identifies the seller&#x27;s eBay marketplace.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/overview.html#requirements\&quot; target&#x3D;\&quot;_blank \&quot;&gt;Metadata API requirements and restrictions&lt;/a&gt; for supported values. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client.&lt;br&gt;&lt;br&gt;Its value should be set to &lt;code&gt;application/json&lt;/code&gt;.&lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt; in the &lt;a href&#x3D;\&quot;/api-docs/static/ebay-rest-landing.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Using eBay RESTful APIs&lt;/a&gt; guide. | 
 **body** | [**ProductRequest**](ProductRequest.md)| This type defines properties for which to find compatibilities. | [optional] 

### Return type

[**ProductResponse**](ProductResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

