# ebaytaxonomy.CategoryTreeApi

All URIs are relative to *https://api.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_item_aspects**](CategoryTreeApi.md#fetch_item_aspects) | **GET** /category_tree/{category_tree_id}/fetch_item_aspects | Get Aspects for All Leaf Categories in a Marketplace
[**get_category_subtree**](CategoryTreeApi.md#get_category_subtree) | **GET** /category_tree/{category_tree_id}/get_category_subtree | Get a Category Subtree
[**get_category_suggestions**](CategoryTreeApi.md#get_category_suggestions) | **GET** /category_tree/{category_tree_id}/get_category_suggestions | Get Suggested Categories
[**get_category_tree**](CategoryTreeApi.md#get_category_tree) | **GET** /category_tree/{category_tree_id} | Get a Category Tree
[**get_compatibility_properties**](CategoryTreeApi.md#get_compatibility_properties) | **GET** /category_tree/{category_tree_id}/get_compatibility_properties | Get Compatibility Properties
[**get_compatibility_property_values**](CategoryTreeApi.md#get_compatibility_property_values) | **GET** /category_tree/{category_tree_id}/get_compatibility_property_values | Get Compatibility Property Values
[**get_default_category_tree_id**](CategoryTreeApi.md#get_default_category_tree_id) | **GET** /get_default_category_tree_id | Get a Default Category Tree ID
[**get_expired_categories**](CategoryTreeApi.md#get_expired_categories) | **GET** /category_tree/{category_tree_id}/get_expired_categories | 
[**get_item_aspects_for_category**](CategoryTreeApi.md#get_item_aspects_for_category) | **GET** /category_tree/{category_tree_id}/get_item_aspects_for_category | 

# **fetch_item_aspects**
> GetCategoriesAspectResponse fetch_item_aspects(category_tree_id)

Get Aspects for All Leaf Categories in a Marketplace

This method returns a complete list of aspects for all of the leaf categories that belong to an eBay marketplace. The eBay marketplace is specified through the <b>category_tree_id</b> URI parameter.<br><br><span class=\"tablenote\"> <strong>Note:</strong> A successful call returns a payload as a gzipped JSON file sent as a binary file using the content-type:application/octet-stream in the response. This file may be large (over 100 MB, compressed). Extract the JSON file from the compressed file with a utility that handles .gz or .gzip. The open source <a href=\"https://github.com/eBay/taxonomy-sdk \" target=\"_blank\">Taxonomy SDK</a> can be used to compare the aspect metadata that is returned in this response. The <b>Taxonomy SDK</b> uses this call to surface changes (new, modified, and removed entities) between an updated version of a bulk downloaded file relative to a previous version.</span>

### Example
```python
from __future__ import print_function
import time
import ebaytaxonomy
from ebaytaxonomy.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaytaxonomy.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaytaxonomy.CategoryTreeApi(ebaytaxonomy.ApiClient(configuration))
category_tree_id = 'category_tree_id_example' # str | The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using the <b>getDefaultCategoryTreeId</b> method.

try:
    # Get Aspects for All Leaf Categories in a Marketplace
    api_response = api_instance.fetch_item_aspects(category_tree_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryTreeApi->fetch_item_aspects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_tree_id** | **str**| The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using the &lt;b&gt;getDefaultCategoryTreeId&lt;/b&gt; method. | 

### Return type

[**GetCategoriesAspectResponse**](GetCategoriesAspectResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_subtree**
> CategorySubtree get_category_subtree(category_id, category_tree_id, accept_encoding=accept_encoding)

Get a Category Subtree

This call retrieves the details of all nodes of the category tree hierarchy (the subtree) below a specified category of a category tree. You identify the tree using the <b>category_tree_id</b> parameter, which was returned by the <b>getDefaultCategoryTreeId</b> call in the <b>categoryTreeId</b> field.<br><br><span class=\"tablenote\"> <strong>Note:</strong> This method can return a very large payload, so gzip compression is supported. To enable gzip compression, include the <code>Accept-Encoding</code> header and set its value to <code>gzip</code> as shown below: <br><br><code>&nbsp;&nbsp;Accept-Encoding: gzip</code></span>

### Example
```python
from __future__ import print_function
import time
import ebaytaxonomy
from ebaytaxonomy.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaytaxonomy.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaytaxonomy.CategoryTreeApi(ebaytaxonomy.ApiClient(configuration))
category_id = 'category_id_example' # str | The unique identifier of the category at the top of the subtree being requested. Metadata on this category and all its descendant categories are retrieved.<br><br><span class=\"tablenote\"><strong>Note:</strong> If the <b>category_id</b> submitted identifies a leaf node of the tree, the call response will contain information about only that leaf node, which is a valid subtree.<!-- <br><br> This call also returns an error if <b>category_id</b> identifies a deprecated category. This can occur if you routinely cache your category trees. Use the <b>Get Deprecated Categories and Mapping</b> call to determine which current category should be used in place of the deprecated category, and use the <b>getCategoryTree</b> call to update your cached copy of the tree. --> </span>
category_tree_id = 'category_tree_id_example' # str | The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using the <b>getDefaultCategoryTreeId</b> method.
accept_encoding = 'accept_encoding_example' # str | This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to <code>gzip</code>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (optional)

try:
    # Get a Category Subtree
    api_response = api_instance.get_category_subtree(category_id, category_tree_id, accept_encoding=accept_encoding)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryTreeApi->get_category_subtree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The unique identifier of the category at the top of the subtree being requested. Metadata on this category and all its descendant categories are retrieved.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; If the &lt;b&gt;category_id&lt;/b&gt; submitted identifies a leaf node of the tree, the call response will contain information about only that leaf node, which is a valid subtree.&lt;!-- &lt;br&gt;&lt;br&gt; This call also returns an error if &lt;b&gt;category_id&lt;/b&gt; identifies a deprecated category. This can occur if you routinely cache your category trees. Use the &lt;b&gt;Get Deprecated Categories and Mapping&lt;/b&gt; call to determine which current category should be used in place of the deprecated category, and use the &lt;b&gt;getCategoryTree&lt;/b&gt; call to update your cached copy of the tree. --&gt; &lt;/span&gt; | 
 **category_tree_id** | **str**| The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using the &lt;b&gt;getDefaultCategoryTreeId&lt;/b&gt; method. | 
 **accept_encoding** | **str**| This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to &lt;code&gt;gzip&lt;/code&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | [optional] 

### Return type

[**CategorySubtree**](CategorySubtree.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_suggestions**
> CategorySuggestionResponse get_category_suggestions(category_tree_id, q)

Get Suggested Categories

This call returns an array of category tree leaf nodes in the specified category tree that are considered by eBay to most closely correspond to the query string <b>q</b>. Returned with each suggested node is a localized name for that category (based on the <b>Accept-Language</b> header specified for the call), and details about each of the category's ancestor nodes, extending from its immediate parent up to the root of the category tree.<br><br>You identify the tree using the <b>category_tree_id</b> parameter, which was returned by the <b>getDefaultCategoryTreeId</b> call in the <b>categoryTreeId</b> field.<br><br><span class=\"tablenote\"> <strong><span style=\"color:red\">Important:</span></strong> This call is not supported in the Sandbox environment. It will return a response payload in which the <b>categoryName</b> fields contain random or boilerplate text regardless of the query submitted.</span>

### Example
```python
from __future__ import print_function
import time
import ebaytaxonomy
from ebaytaxonomy.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaytaxonomy.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaytaxonomy.CategoryTreeApi(ebaytaxonomy.ApiClient(configuration))
category_tree_id = 'category_tree_id_example' # str | The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using the <b>getDefaultCategoryTreeId</b> method.
q = 'q_example' # str | A quoted string that describes or characterizes the item being offered for sale. The string format is free form, and can contain any combination of phrases or keywords. eBay will parse the string and return suggested categories for the item.

try:
    # Get Suggested Categories
    api_response = api_instance.get_category_suggestions(category_tree_id, q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryTreeApi->get_category_suggestions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_tree_id** | **str**| The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using the &lt;b&gt;getDefaultCategoryTreeId&lt;/b&gt; method. | 
 **q** | **str**| A quoted string that describes or characterizes the item being offered for sale. The string format is free form, and can contain any combination of phrases or keywords. eBay will parse the string and return suggested categories for the item. | 

### Return type

[**CategorySuggestionResponse**](CategorySuggestionResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_tree**
> CategoryTree get_category_tree(category_tree_id, accept_encoding=accept_encoding)

Get a Category Tree

This method retrieves the complete category tree that is identified by the <b>category_tree_id</b> parameter. The value of <b>category_tree_id</b> was returned by the <b>getDefaultCategoryTreeId</b> method in the <b>categoryTreeId</b> field. The response contains details of all nodes of the specified eBay category tree, as well as the eBay marketplaces that use this category tree.<br><br><span class=\"tablenote\"> <strong>Note:</strong> This method can return a very large payload, so gzip compression is supported. To enable gzip compression, include the <code>Accept-Encoding</code> header and set its value to <code>gzip</code> as shown below: <br><br><code>&nbsp;&nbsp;Accept-Encoding: gzip</code></span>

### Example
```python
from __future__ import print_function
import time
import ebaytaxonomy
from ebaytaxonomy.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaytaxonomy.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaytaxonomy.CategoryTreeApi(ebaytaxonomy.ApiClient(configuration))
category_tree_id = 'category_tree_id_example' # str | The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using the <b>getDefaultCategoryTreeId</b> method.
accept_encoding = 'accept_encoding_example' # str | This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to <code>gzip</code>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (optional)

try:
    # Get a Category Tree
    api_response = api_instance.get_category_tree(category_tree_id, accept_encoding=accept_encoding)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryTreeApi->get_category_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_tree_id** | **str**| The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using the &lt;b&gt;getDefaultCategoryTreeId&lt;/b&gt; method. | 
 **accept_encoding** | **str**| This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to &lt;code&gt;gzip&lt;/code&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | [optional] 

### Return type

[**CategoryTree**](CategoryTree.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compatibility_properties**
> GetCompatibilityMetadataResponse get_compatibility_properties(category_tree_id, category_id)

Get Compatibility Properties

This call retrieves the compatible vehicle aspects that are used to define a motor vehicle that is compatible with a motor vehicle part or accessory. The values that are retrieved here might include motor vehicle aspects such as 'Make', 'Model', 'Year', 'Engine', and 'Trim', and each of these aspects are localized for the eBay marketplace.<br><br> The <strong>category_tree_id</strong> value is passed in as a path parameter, and this value identifies the eBay category tree. The <strong>category_id</strong> value is passed in as a query parameter, as this parameter is also required. The specified category must be a category that supports parts compatibility.<br><br> At this time, this operation only supports parts and accessories listings for cars, trucks, and motorcycles (not boats, power sports, or any other vehicle types). Only the following eBay marketplaces support parts compatibility:<ul><li>eBay US (Motors and non-Motors categories)</li><li>eBay Canada (Motors and non-Motors categories)</li><li>eBay UK</li><li>eBay Germany</li><li>eBay Australia</li><li>eBay France</li><li>eBay Italy</li><li>eBay Spain</li></ul>

### Example
```python
from __future__ import print_function
import time
import ebaytaxonomy
from ebaytaxonomy.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaytaxonomy.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaytaxonomy.CategoryTreeApi(ebaytaxonomy.ApiClient(configuration))
category_tree_id = 'category_tree_id_example' # str | This is the unique identifier of category tree. The following is the list of <strong>category_tree_id</strong> values and the eBay marketplaces that they represent. One of these ID values must be passed in as a path parameter, and the <strong>category_id</strong> value, that is passed in as query parameter, must be a valid eBay category on that eBay marketplace that supports parts compatibility for cars, trucks, or motorcycles.<br><br><ul><li>eBay US: 0</li><li>eBay Motors US: 100</li><li>eBay Canada: 2</li><li>eBay UK: 3</li><li>eBay Germany: 77</li><li>eBay Australia: 15</li><li>eBay France: 71</li><li>eBay Italy: 101</li><li>eBay Spain: 186</li></ul>
category_id = 'category_id_example' # str | The unique identifier of an eBay category. This eBay category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility for cars, trucks, or motorcycles.<br><br> The <b>getAutomotivePartsCompatibilityPolicies</b> method of the Selling Metadata API can be used to retrieve all eBay categories for an eBay marketplace that support parts compatibility for vehicles.

try:
    # Get Compatibility Properties
    api_response = api_instance.get_compatibility_properties(category_tree_id, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryTreeApi->get_compatibility_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_tree_id** | **str**| This is the unique identifier of category tree. The following is the list of &lt;strong&gt;category_tree_id&lt;/strong&gt; values and the eBay marketplaces that they represent. One of these ID values must be passed in as a path parameter, and the &lt;strong&gt;category_id&lt;/strong&gt; value, that is passed in as query parameter, must be a valid eBay category on that eBay marketplace that supports parts compatibility for cars, trucks, or motorcycles.&lt;br&gt;&lt;br&gt;&lt;ul&gt;&lt;li&gt;eBay US: 0&lt;/li&gt;&lt;li&gt;eBay Motors US: 100&lt;/li&gt;&lt;li&gt;eBay Canada: 2&lt;/li&gt;&lt;li&gt;eBay UK: 3&lt;/li&gt;&lt;li&gt;eBay Germany: 77&lt;/li&gt;&lt;li&gt;eBay Australia: 15&lt;/li&gt;&lt;li&gt;eBay France: 71&lt;/li&gt;&lt;li&gt;eBay Italy: 101&lt;/li&gt;&lt;li&gt;eBay Spain: 186&lt;/li&gt;&lt;/ul&gt; | 
 **category_id** | **str**| The unique identifier of an eBay category. This eBay category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility for cars, trucks, or motorcycles.&lt;br&gt;&lt;br&gt; The &lt;b&gt;getAutomotivePartsCompatibilityPolicies&lt;/b&gt; method of the Selling Metadata API can be used to retrieve all eBay categories for an eBay marketplace that support parts compatibility for vehicles. | 

### Return type

[**GetCompatibilityMetadataResponse**](GetCompatibilityMetadataResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compatibility_property_values**
> GetCompatibilityPropertyValuesResponse get_compatibility_property_values(category_tree_id, compatibility_property, category_id, filter=filter)

Get Compatibility Property Values

This call retrieves applicable compatible vehicle property values based on the specified eBay marketplace, specified eBay category, and filters used in the request. Compatible vehicle properties are returned in the <strong>compatibilityProperties.name</strong> field of a <strong>getCompatibilityProperties</strong> response. <br><br> One compatible vehicle property applicable to the specified eBay marketplace and eBay category is specified through the required <strong>compatibility_property</strong> filter. Then, the user has the option of further restricting the compatible vehicle property values that are returned in the response by specifying one or more compatible vehicle property name/value pairs through the <strong>filter</strong> query parameter.<br><br>See the documentation in <strong>URI parameters</strong> section for more information on using the <strong>compatibility_property</strong> and <strong>filter</strong> query parameters together to customize the data that is retrieved.

### Example
```python
from __future__ import print_function
import time
import ebaytaxonomy
from ebaytaxonomy.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaytaxonomy.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaytaxonomy.CategoryTreeApi(ebaytaxonomy.ApiClient(configuration))
category_tree_id = 'category_tree_id_example' # str | This is the unique identifier of the category tree. The following is the list of <strong>category_tree_id</strong> values and the eBay marketplaces that they represent. One of these ID values must be passed in as a path parameter, and the <strong>category_id</strong> value, that is passed in as query parameter, must be a valid eBay category on that eBay marketplace that supports parts compatibility for cars, trucks, or motorcycles.<br><br><ul><li>eBay US: 0</li><li>eBay Motors US: 100</li><li>eBay Canada: 2</li><li>eBay UK: 3</li><li>eBay Germany: 77</li><li>eBay Australia: 15</li><li>eBay France: 71</li><li>eBay Italy: 101</li><li>eBay Spain: 186</li></ul>
compatibility_property = 'compatibility_property_example' # str | One compatible vehicle property applicable to the specified eBay marketplace and eBay category is specified in this required filter. Compatible vehicle properties are returned in the <strong>compatibilityProperties.name</strong> field of a <strong>getCompatibilityProperties</strong> response. <br><br> For example, if you wanted to retrieve all vehicle trims for a 2018 Toyota Camry, you would set this filter as follows: <code>compatibility_property=Trim</code> and then include the following three name/value filters through one <strong>filter</strong> parameter: <code>filter=Year:2018,Make:Toyota,Model:Camry</code>.<br><br>So, putting this all together, the URI would look something like this:<br><br><pre><code>GET https://api.ebay.com/commerce/<br>taxonomy/v1/category_tree/100/<br>get_compatibility_property_values?<br><strong>category_id</strong>=6016&<strong>compatibility_property</strong>=Trim<br>&<strong>filter</strong>=Year:2018,Make:Toyota,Model:Camry</code></pre>
category_id = 'category_id_example' # str | The unique identifier of an eBay category. This eBay category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility for cars, trucks, or motorcycles.<br><br> The <strong>getAutomotivePartsCompatibilityPolicies</strong> method of the Selling Metadata API can be used to retrieve all eBay categories for an eBay marketplace that support parts compatibility for vehicles.
filter = 'filter_example' # str | One or more compatible vehicle property name/value pairs are passed in through this query parameter. The compatible vehicle property name and corresponding value are delimited with a colon (:), such as <code>filter=Year:2018</code>, and multiple compatible vehicle property name/value pairs are delimited with a comma (,).<br><br><span class=\"tablenote\"><b>Note:</b> Commas are used as delimiters between filter values. If a value includes a comma (e.g., <code>BodyStyle:AWD B9 8W5<b>,</b>C8WD</code>) you <b>must</b> include a backslash (<b>\\</b>) immediately before the comma to prevent it from being evaluated as a delimiter.<br><br>As with all query parameter values, the filter parameters must be URL encoded. For more information about encoding request parameters, refer to <a href=\"/api-docs/static/rest-request-components.html#parameters\" target=\"_blank\">URL encoding query parameter values</a>.</span><br>For example, to retrieve all vehicle trims for a 2022 Audi A4:<ul><li>Set the <strong>compatibility_property</strong> filter to <code>compatibility_property=Trim</code></li><li>Include the following name/value filters using one <strong>filter</strong> parameter:<ul><li><code>Year:2022</code></li><li><code>Make:Audi</code></li><li><code>Model:A4</code></li><li><code>BodyStyle:AWD B9 8W5\\,8WD</code></li></ul></li></ul>The resulting comma-separated filter query parameter is:<pre><code>filter=Year:2022,Make:Audi,Model:A4,BodyStyle:AWD B9 8W5\\,8WD</code></pre><br>The following sample shows the same filter but with URL encoding for the blank spaces.<br><pre><code>GET https://api.ebay.com/commerce/<br>taxonomy/v1/category_tree/100/<br>get_compatibility_property_values?<b>category_id</b>=6016&<b>compatibility_property</b>=Trim&<b>filter</b>=Year:2022,Make:Audi,Model:A4,BodyStyle:AWD%20B9%208W5%5C%2C8WD</code></pre><br><span class=\"tablenote\"><b>Note:</b> While not required, it is strongly recommended that users limit the size of the result set by using the <b>filter</b> query parameter. Failure to do so may result in a timeout error if too much data is attempted to be returned.</span> For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/commerce/taxonomy/types/txn:ConstraintFilter (optional)

try:
    # Get Compatibility Property Values
    api_response = api_instance.get_compatibility_property_values(category_tree_id, compatibility_property, category_id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryTreeApi->get_compatibility_property_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_tree_id** | **str**| This is the unique identifier of the category tree. The following is the list of &lt;strong&gt;category_tree_id&lt;/strong&gt; values and the eBay marketplaces that they represent. One of these ID values must be passed in as a path parameter, and the &lt;strong&gt;category_id&lt;/strong&gt; value, that is passed in as query parameter, must be a valid eBay category on that eBay marketplace that supports parts compatibility for cars, trucks, or motorcycles.&lt;br&gt;&lt;br&gt;&lt;ul&gt;&lt;li&gt;eBay US: 0&lt;/li&gt;&lt;li&gt;eBay Motors US: 100&lt;/li&gt;&lt;li&gt;eBay Canada: 2&lt;/li&gt;&lt;li&gt;eBay UK: 3&lt;/li&gt;&lt;li&gt;eBay Germany: 77&lt;/li&gt;&lt;li&gt;eBay Australia: 15&lt;/li&gt;&lt;li&gt;eBay France: 71&lt;/li&gt;&lt;li&gt;eBay Italy: 101&lt;/li&gt;&lt;li&gt;eBay Spain: 186&lt;/li&gt;&lt;/ul&gt; | 
 **compatibility_property** | **str**| One compatible vehicle property applicable to the specified eBay marketplace and eBay category is specified in this required filter. Compatible vehicle properties are returned in the &lt;strong&gt;compatibilityProperties.name&lt;/strong&gt; field of a &lt;strong&gt;getCompatibilityProperties&lt;/strong&gt; response. &lt;br&gt;&lt;br&gt; For example, if you wanted to retrieve all vehicle trims for a 2018 Toyota Camry, you would set this filter as follows: &lt;code&gt;compatibility_property&#x3D;Trim&lt;/code&gt; and then include the following three name/value filters through one &lt;strong&gt;filter&lt;/strong&gt; parameter: &lt;code&gt;filter&#x3D;Year:2018,Make:Toyota,Model:Camry&lt;/code&gt;.&lt;br&gt;&lt;br&gt;So, putting this all together, the URI would look something like this:&lt;br&gt;&lt;br&gt;&lt;pre&gt;&lt;code&gt;GET https://api.ebay.com/commerce/&lt;br&gt;taxonomy/v1/category_tree/100/&lt;br&gt;get_compatibility_property_values?&lt;br&gt;&lt;strong&gt;category_id&lt;/strong&gt;&#x3D;6016&amp;&lt;strong&gt;compatibility_property&lt;/strong&gt;&#x3D;Trim&lt;br&gt;&amp;&lt;strong&gt;filter&lt;/strong&gt;&#x3D;Year:2018,Make:Toyota,Model:Camry&lt;/code&gt;&lt;/pre&gt; | 
 **category_id** | **str**| The unique identifier of an eBay category. This eBay category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility for cars, trucks, or motorcycles.&lt;br&gt;&lt;br&gt; The &lt;strong&gt;getAutomotivePartsCompatibilityPolicies&lt;/strong&gt; method of the Selling Metadata API can be used to retrieve all eBay categories for an eBay marketplace that support parts compatibility for vehicles. | 
 **filter** | **str**| One or more compatible vehicle property name/value pairs are passed in through this query parameter. The compatible vehicle property name and corresponding value are delimited with a colon (:), such as &lt;code&gt;filter&#x3D;Year:2018&lt;/code&gt;, and multiple compatible vehicle property name/value pairs are delimited with a comma (,).&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Commas are used as delimiters between filter values. If a value includes a comma (e.g., &lt;code&gt;BodyStyle:AWD B9 8W5&lt;b&gt;,&lt;/b&gt;C8WD&lt;/code&gt;) you &lt;b&gt;must&lt;/b&gt; include a backslash (&lt;b&gt;\\&lt;/b&gt;) immediately before the comma to prevent it from being evaluated as a delimiter.&lt;br&gt;&lt;br&gt;As with all query parameter values, the filter parameters must be URL encoded. For more information about encoding request parameters, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#parameters\&quot; target&#x3D;\&quot;_blank\&quot;&gt;URL encoding query parameter values&lt;/a&gt;.&lt;/span&gt;&lt;br&gt;For example, to retrieve all vehicle trims for a 2022 Audi A4:&lt;ul&gt;&lt;li&gt;Set the &lt;strong&gt;compatibility_property&lt;/strong&gt; filter to &lt;code&gt;compatibility_property&#x3D;Trim&lt;/code&gt;&lt;/li&gt;&lt;li&gt;Include the following name/value filters using one &lt;strong&gt;filter&lt;/strong&gt; parameter:&lt;ul&gt;&lt;li&gt;&lt;code&gt;Year:2022&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;Make:Audi&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;Model:A4&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;BodyStyle:AWD B9 8W5\\,8WD&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ul&gt;The resulting comma-separated filter query parameter is:&lt;pre&gt;&lt;code&gt;filter&#x3D;Year:2022,Make:Audi,Model:A4,BodyStyle:AWD B9 8W5\\,8WD&lt;/code&gt;&lt;/pre&gt;&lt;br&gt;The following sample shows the same filter but with URL encoding for the blank spaces.&lt;br&gt;&lt;pre&gt;&lt;code&gt;GET https://api.ebay.com/commerce/&lt;br&gt;taxonomy/v1/category_tree/100/&lt;br&gt;get_compatibility_property_values?&lt;b&gt;category_id&lt;/b&gt;&#x3D;6016&amp;&lt;b&gt;compatibility_property&lt;/b&gt;&#x3D;Trim&amp;&lt;b&gt;filter&lt;/b&gt;&#x3D;Year:2022,Make:Audi,Model:A4,BodyStyle:AWD%20B9%208W5%5C%2C8WD&lt;/code&gt;&lt;/pre&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; While not required, it is strongly recommended that users limit the size of the result set by using the &lt;b&gt;filter&lt;/b&gt; query parameter. Failure to do so may result in a timeout error if too much data is attempted to be returned.&lt;/span&gt; For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/commerce/taxonomy/types/txn:ConstraintFilter | [optional] 

### Return type

[**GetCompatibilityPropertyValuesResponse**](GetCompatibilityPropertyValuesResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_category_tree_id**
> BaseCategoryTree get_default_category_tree_id(marketplace_id)

Get a Default Category Tree ID

A given eBay marketplace might use multiple category trees, but one of those trees is considered to be the default for that marketplace. This call retrieves a reference to the default category tree associated with the specified eBay marketplace ID. The response includes only the tree's unique identifier and version, which you can use to retrieve more details about the tree, its structure, and its individual category nodes.

### Example
```python
from __future__ import print_function
import time
import ebaytaxonomy
from ebaytaxonomy.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaytaxonomy.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaytaxonomy.CategoryTreeApi(ebaytaxonomy.ApiClient(configuration))
marketplace_id = 'marketplace_id_example' # str | The unique identifier of the eBay marketplace for which the category tree ID is requested. For a list of supported marketplace IDs, see <a href=\"/api-docs/commerce/taxonomy/static/supportedmarketplaces.html\">Marketplaces with Default Category Trees</a>.

try:
    # Get a Default Category Tree ID
    api_response = api_instance.get_default_category_tree_id(marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryTreeApi->get_default_category_tree_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The unique identifier of the eBay marketplace for which the category tree ID is requested. For a list of supported marketplace IDs, see &lt;a href&#x3D;\&quot;/api-docs/commerce/taxonomy/static/supportedmarketplaces.html\&quot;&gt;Marketplaces with Default Category Trees&lt;/a&gt;. | 

### Return type

[**BaseCategoryTree**](BaseCategoryTree.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expired_categories**
> ExpiredCategories get_expired_categories(category_tree_id)



This method retrieves the mappings of expired leaf categories in the specified category tree to their corresponding active leaf categories. Note that in some cases, several expired categories are mapped to a single active category.<br><br><span class=\"tablenote\"><b>Note:</b> This method only returns information about categories that have been mapped (i.e., combined categories and split categories). It does not return information about expired categories that have no corresponding active categories. When a category expires in this manner, any completed items that were listed in the expired category can still be found, but new listings cannot be created in the category.</span>

### Example
```python
from __future__ import print_function
import time
import ebaytaxonomy
from ebaytaxonomy.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaytaxonomy.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaytaxonomy.CategoryTreeApi(ebaytaxonomy.ApiClient(configuration))
category_tree_id = 'category_tree_id_example' # str | The unique identifier of the eBay category tree.<br><br>The category tree ID for an eBay marketplace can be retrieved using the <a href=\"/api-docs/commerce/taxonomy/resources/category_tree/methods/getDefaultCategoryTreeId\">getDefaultCategoryTreeId</a> method.

try:
    api_response = api_instance.get_expired_categories(category_tree_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryTreeApi->get_expired_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_tree_id** | **str**| The unique identifier of the eBay category tree.&lt;br&gt;&lt;br&gt;The category tree ID for an eBay marketplace can be retrieved using the &lt;a href&#x3D;\&quot;/api-docs/commerce/taxonomy/resources/category_tree/methods/getDefaultCategoryTreeId\&quot;&gt;getDefaultCategoryTreeId&lt;/a&gt; method. | 

### Return type

[**ExpiredCategories**](ExpiredCategories.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_aspects_for_category**
> AspectMetadata get_item_aspects_for_category(category_id, category_tree_id)



This call returns a list of <i>aspects</i> that are appropriate or necessary for accurately describing items in the specified leaf category. Each aspect identifies an item attribute (for example, color,) for which the seller will be required or encouraged to provide a value (or variation values) when offering an item in that category on eBay.<br><br>For each aspect, <b>getItemAspectsForCategory</b> provides complete metadata, including: <ul><li>The aspect's data type, format, and entry mode</li><li>Whether the aspect is required in listings</li><li>Whether the aspect can be used for item variations</li><li>Whether the aspect accepts multiple values for an item</li><li>Allowed values for the aspect</li></ul> Use this information to construct an interface through which sellers can enter or select the appropriate values for their items or item variations. Once you collect those values, include them as product aspects when creating inventory items using the Inventory API.

### Example
```python
from __future__ import print_function
import time
import ebaytaxonomy
from ebaytaxonomy.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaytaxonomy.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaytaxonomy.CategoryTreeApi(ebaytaxonomy.ApiClient(configuration))
category_id = 'category_id_example' # str | The unique identifier of the leaf category for which aspects are being requested.<br><br><span class=\"tablenote\"> <strong>Note:</strong> If the <b>category_id</b> submitted does not identify a leaf node of the tree, this call returns an error. </span>
category_tree_id = 'category_tree_id_example' # str | The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using the <b>getDefaultCategoryTreeId</b> method.

try:
    api_response = api_instance.get_item_aspects_for_category(category_id, category_tree_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryTreeApi->get_item_aspects_for_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The unique identifier of the leaf category for which aspects are being requested.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; If the &lt;b&gt;category_id&lt;/b&gt; submitted does not identify a leaf node of the tree, this call returns an error. &lt;/span&gt; | 
 **category_tree_id** | **str**| The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using the &lt;b&gt;getDefaultCategoryTreeId&lt;/b&gt; method. | 

### Return type

[**AspectMetadata**](AspectMetadata.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

