# ebaymetadata.MarketplaceApi

All URIs are relative to *https://api.ebay.com/sell/metadata/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_automotive_parts_compatibility_policies**](MarketplaceApi.md#get_automotive_parts_compatibility_policies) | **GET** /marketplace/{marketplace_id}/get_automotive_parts_compatibility_policies | 
[**get_category_policies**](MarketplaceApi.md#get_category_policies) | **GET** /marketplace/{marketplace_id}/get_category_policies | 
[**get_classified_ad_policies**](MarketplaceApi.md#get_classified_ad_policies) | **GET** /marketplace/{marketplace_id}/get_classified_ad_policies | 
[**get_currencies**](MarketplaceApi.md#get_currencies) | **GET** /marketplace/{marketplace_id}/get_currencies | 
[**get_extended_producer_responsibility_policies**](MarketplaceApi.md#get_extended_producer_responsibility_policies) | **GET** /marketplace/{marketplace_id}/get_extended_producer_responsibility_policies | 
[**get_hazardous_materials_labels**](MarketplaceApi.md#get_hazardous_materials_labels) | **GET** /marketplace/{marketplace_id}/get_hazardous_materials_labels | 
[**get_item_condition_policies**](MarketplaceApi.md#get_item_condition_policies) | **GET** /marketplace/{marketplace_id}/get_item_condition_policies | 
[**get_listing_structure_policies**](MarketplaceApi.md#get_listing_structure_policies) | **GET** /marketplace/{marketplace_id}/get_listing_structure_policies | 
[**get_listing_type_policies**](MarketplaceApi.md#get_listing_type_policies) | **GET** /marketplace/{marketplace_id}/get_listing_type_policies | 
[**get_motors_listing_policies**](MarketplaceApi.md#get_motors_listing_policies) | **GET** /marketplace/{marketplace_id}/get_motors_listing_policies | 
[**get_negotiated_price_policies**](MarketplaceApi.md#get_negotiated_price_policies) | **GET** /marketplace/{marketplace_id}/get_negotiated_price_policies | 
[**get_product_safety_labels**](MarketplaceApi.md#get_product_safety_labels) | **GET** /marketplace/{marketplace_id}/get_product_safety_labels | 
[**get_regulatory_policies**](MarketplaceApi.md#get_regulatory_policies) | **GET** /marketplace/{marketplace_id}/get_regulatory_policies | 
[**get_return_policies**](MarketplaceApi.md#get_return_policies) | **GET** /marketplace/{marketplace_id}/get_return_policies | 
[**get_shipping_policies**](MarketplaceApi.md#get_shipping_policies) | **GET** /marketplace/{marketplace_id}/get_shipping_policies | 
[**get_site_visibility_policies**](MarketplaceApi.md#get_site_visibility_policies) | **GET** /marketplace/{marketplace_id}/get_site_visibility_policies | 


# **get_automotive_parts_compatibility_policies**
> AutomotivePartsCompatibilityPolicyResponse get_automotive_parts_compatibility_policies(marketplace_id, filter=filter, accept_encoding=accept_encoding)

This method returns the eBay policies that define how to list automotive parts compatibility items in the categories of the specified marketplace.  <br><br>By default, this method returns all categories that support parts compatibility. You can limit the size of the result set by using the <b>filter</b> query parameter to specify only the category IDs you want to review.<br><br><span class="tablenote"><b>Note: </b>To return policy information for the eBay US marketplace, specify <code>EBAY_MOTORS_US</code> as the path parameter for <b>marketplace_id</b>.</span><br><span class="tablenote"><span style="color:#478415"><strong>Tip:</strong></span> This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span><br>If you specify a valid marketplace ID but that marketplace does not contain policy information, or if you filter out all results, a <b>204 No content</b> status code is returned with an empty response body.

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.automotive_parts_compatibility_policy_response import AutomotivePartsCompatibilityPolicyResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information is retrieved.  <br><br><span class=\"tablenote\"><b>Note: </b>Only the following eBay marketplaces support automotive parts compatibility: <ul> <li>EBAY_MOTORS_US</li> <li>EBAY_AU</li> <li>EBAY_CA</li> <li>EBAY_DE</li> <li>EBAY_ES</li> <li>EBAY_FR</li> <li>EBAY_GB</li> <li>EBAY_IT</li></ul></span>
    filter = 'filter_example' # str | This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply <b>categoryId</b> values for the sections of the tree you want returned. Use the <a href=\"/api-docs/commerce/taxonomy/overview.html\" target=\"_blank \">Taxonomy API</a> to retrieve category ID values.<br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  <br><br><b>Example:</b> <code>filter=categoryIds:{183521|183523|183524}</code>  <br><br><span class=\"tablenote\"><b>Note: </b>URL-encoding of the parameter list is no longer required.</span> (optional)
    accept_encoding = 'accept_encoding_example' # str | This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to <code>gzip</code>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (optional)

    try:
        api_response = api_instance.get_automotive_parts_compatibility_policies(marketplace_id, filter=filter, accept_encoding=accept_encoding)
        print("The response of MarketplaceApi->get_automotive_parts_compatibility_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_automotive_parts_compatibility_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information is retrieved.  &lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note: &lt;/b&gt;Only the following eBay marketplaces support automotive parts compatibility: &lt;ul&gt; &lt;li&gt;EBAY_MOTORS_US&lt;/li&gt; &lt;li&gt;EBAY_AU&lt;/li&gt; &lt;li&gt;EBAY_CA&lt;/li&gt; &lt;li&gt;EBAY_DE&lt;/li&gt; &lt;li&gt;EBAY_ES&lt;/li&gt; &lt;li&gt;EBAY_FR&lt;/li&gt; &lt;li&gt;EBAY_GB&lt;/li&gt; &lt;li&gt;EBAY_IT&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt; | 
 **filter** | **str**| This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree you want returned. Use the &lt;a href&#x3D;\&quot;/api-docs/commerce/taxonomy/overview.html\&quot; target&#x3D;\&quot;_blank \&quot;&gt;Taxonomy API&lt;/a&gt; to retrieve category ID values.&lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{183521|183523|183524}&lt;/code&gt;  &lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note: &lt;/b&gt;URL-encoding of the parameter list is no longer required.&lt;/span&gt; | [optional] 
 **accept_encoding** | **str**| This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to &lt;code&gt;gzip&lt;/code&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | [optional] 

### Return type

[**AutomotivePartsCompatibilityPolicyResponse**](AutomotivePartsCompatibilityPolicyResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_policies**
> CategoryPolicyResponse get_category_policies(marketplace_id, filter=filter, accept_language=accept_language)

This method returns eBay category policy metadata for all leaf categories on the specified marketplace.<p>By default, this method returns metadata on all leaf categories. You can limit the size of the result set by using the <b>filter</b> query parameter to specify only the leaf category IDs you want to review.</p><p>If you specify a valid marketplace ID but that marketplace does not contain policy information, or if you filter out all results, a successful call returns a <b>204 No content</b> status code with an empty response body.</p>

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.category_policy_response import CategoryPolicyResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information is retrieved.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values.
    filter = 'filter_example' # str | This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the <b>categoryId</b> for one or more leaf categories. You can verify if a category is a leaf category by using the <a href=\"/api-docs/commerce/taxonomy/overview.html\" target=\"_blank \">Taxonomy API</a> and looking for a <code>\"leafCategory\": true</code> tag.  <br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.<br><br><b>Example:</b> <code>filter=categoryIds:{3767|171784}</code> (optional)
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_category_policies(marketplace_id, filter=filter, accept_language=accept_language)
        print("The response of MarketplaceApi->get_category_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_category_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information is retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values. | 
 **filter** | **str**| This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the &lt;b&gt;categoryId&lt;/b&gt; for one or more leaf categories. You can verify if a category is a leaf category by using the &lt;a href&#x3D;\&quot;/api-docs/commerce/taxonomy/overview.html\&quot; target&#x3D;\&quot;_blank \&quot;&gt;Taxonomy API&lt;/a&gt; and looking for a &lt;code&gt;\&quot;leafCategory\&quot;: true&lt;/code&gt; tag.  &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.&lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{3767|171784}&lt;/code&gt; | [optional] 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**CategoryPolicyResponse**](CategoryPolicyResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classified_ad_policies**
> ClassifiedAdPolicyResponse get_classified_ad_policies(marketplace_id, filter=filter, accept_language=accept_language)

This method returns eBay classified ad policy metadata for all leaf categories on the specified marketplace.<p>By default, this method returns metadata on all leaf categories. You can limit the size of the result set by using the <b>filter</b> query parameter to specify only the leaf category IDs you want to review.</p><p>If you specify a valid marketplace ID but that marketplace does not contain policy information, or if you filter out all results, a successful call returns a <b>204 No content</b> status code with an empty response body.</p><p><span class="tablenote"><span style="color:#004680"><strong>Note: </strong>This method does not support classified ads for eBay US Motors categories (EBAY_MOTORS_US). For eBay Motors Pro users, use <a href="/api-docs/sell/metadata/resources/marketplace/methods/getMotorsListingPolicies"  target="_blank">getMotorsListingPolicies</a>.</span></p>

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.classified_ad_policy_response import ClassifiedAdPolicyResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information is retrieved.<br><br>See <a href=\"/api-docs/sell/metadata/types/bas:MarketplaceIdEnum\" target=\"_blank\">MarketplaceIdEnum</a> for a list of supported eBay marketplace ID values.
    filter = 'filter_example' # str | This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the <b>categoryId</b> for one or more leaf categories. You can verify if a category is a leaf category by using the <a href=\"/api-docs/commerce/taxonomy/overview.html\" target=\"_blank \">Taxonomy API</a> and looking for a <code>\"leafCategory\": true</code> tag.   <br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.<br><br><b>Example:</b><code>filter=categoryIds:{3767|171784}</code> (optional)
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_classified_ad_policies(marketplace_id, filter=filter, accept_language=accept_language)
        print("The response of MarketplaceApi->get_classified_ad_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_classified_ad_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information is retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/types/bas:MarketplaceIdEnum\&quot; target&#x3D;\&quot;_blank\&quot;&gt;MarketplaceIdEnum&lt;/a&gt; for a list of supported eBay marketplace ID values. | 
 **filter** | **str**| This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the &lt;b&gt;categoryId&lt;/b&gt; for one or more leaf categories. You can verify if a category is a leaf category by using the &lt;a href&#x3D;\&quot;/api-docs/commerce/taxonomy/overview.html\&quot; target&#x3D;\&quot;_blank \&quot;&gt;Taxonomy API&lt;/a&gt; and looking for a &lt;code&gt;\&quot;leafCategory\&quot;: true&lt;/code&gt; tag.   &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.&lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt;&lt;code&gt;filter&#x3D;categoryIds:{3767|171784}&lt;/code&gt; | [optional] 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**ClassifiedAdPolicyResponse**](ClassifiedAdPolicyResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies**
> GetCurrenciesResponse get_currencies(marketplace_id, accept_language=accept_language)

This method returns the default currency used by the eBay marketplace specified in the request. This is the currency that the seller should use when providing price data for this marketplace through listing APIs.

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.get_currencies_response import GetCurrenciesResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which currency information is retrieved.<br><br>See the <a href=\"/api-docs/sell/metadata/types/bas:MarketplaceIdEnum\" target=\"_blank\">MarketplaceIdEnum</a> type for a list of supported eBay marketplace ID values.
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada and French Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.<br><br><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_BE</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the Dutch Belgium marketplace.</span></li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code> and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span></ul> (optional)

    try:
        api_response = api_instance.get_currencies(marketplace_id, accept_language=accept_language)
        print("The response of MarketplaceApi->get_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_currencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which currency information is retrieved.&lt;br&gt;&lt;br&gt;See the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/types/bas:MarketplaceIdEnum\&quot; target&#x3D;\&quot;_blank\&quot;&gt;MarketplaceIdEnum&lt;/a&gt; type for a list of supported eBay marketplace ID values. | 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada and French Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_BE&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the Dutch Belgium marketplace.&lt;/span&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt; and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt;&lt;/ul&gt; | [optional] 

### Return type

[**GetCurrenciesResponse**](GetCurrenciesResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_producer_responsibility_policies**
> ExtendedProducerResponsibilityPolicyResponse get_extended_producer_responsibility_policies(marketplace_id, filter=filter, accept_encoding=accept_encoding, accept_language=accept_language)

This method returns the Extended Producer Responsibility policies for one, multiple, or all eBay categories in an eBay marketplace.<br><br>The identifier of the eBay marketplace is passed in as a path parameter, and unless one or more eBay category IDs are passed in through the filter query parameter, this method will return metadata on every applicable category for the specified marketplace.<br><br><span class="tablenote"><span style="color:#004680"><strong>Note:</strong></span> Currently, the Extended Producer Responsibility policies are only applicable to a limited number of categories.</span><br><span class="tablenote"><span style="color:#004680"><strong>Note: </strong></span>Extended Producer Responsibility IDs are no longer set at the listing level so category-level metadata is no longer returned. Instead, sellers will provide/manage these IDs at the account level by going to <a href="https://accountsettings.ebay.fr/epr-fr " target="_blank">Account Settings</a>.</span><br><span class="tablenote"><span style="color:#478415"><strong>Tip:</strong></span> This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span>

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.extended_producer_responsibility_policy_response import ExtendedProducerResponsibilityPolicyResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information shall be retrieved.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values.
    filter = 'filter_example' # str | A query parameter that can be used to limit the response by returning policy information for only the selected sections of the category tree. Supply <b>categoryId</b> values for the sections of the tree that should be returned.<br><br>When a <b>categoryId</b> value is specified, the returned category tree includes the policies for that parent node, as well as the policies for any child nodes below that parent node.<br><br>Pass in the <b>categoryId</b> values using a URL-encoded, pipe-separated ('|') list. For example:<br><br><code>filter=categoryIds%3A%7B100%7C101%7C102%7D</code><br><br><b>Maximum:</b> 50 (optional)
    accept_encoding = 'accept_encoding_example' # str | This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to <code>gzip</code>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (optional)
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_extended_producer_responsibility_policies(marketplace_id, filter=filter, accept_encoding=accept_encoding, accept_language=accept_language)
        print("The response of MarketplaceApi->get_extended_producer_responsibility_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_extended_producer_responsibility_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information shall be retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values. | 
 **filter** | **str**| A query parameter that can be used to limit the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree that should be returned.&lt;br&gt;&lt;br&gt;When a &lt;b&gt;categoryId&lt;/b&gt; value is specified, the returned category tree includes the policies for that parent node, as well as the policies for any child nodes below that parent node.&lt;br&gt;&lt;br&gt;Pass in the &lt;b&gt;categoryId&lt;/b&gt; values using a URL-encoded, pipe-separated (&#39;|&#39;) list. For example:&lt;br&gt;&lt;br&gt;&lt;code&gt;filter&#x3D;categoryIds%3A%7B100%7C101%7C102%7D&lt;/code&gt;&lt;br&gt;&lt;br&gt;&lt;b&gt;Maximum:&lt;/b&gt; 50 | [optional] 
 **accept_encoding** | **str**| This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to &lt;code&gt;gzip&lt;/code&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | [optional] 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**ExtendedProducerResponsibilityPolicyResponse**](ExtendedProducerResponsibilityPolicyResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hazardous_materials_labels**
> HazardousMaterialDetailsResponse get_hazardous_materials_labels(marketplace_id, accept_language=accept_language)

This method returns hazardous materials label information for the specified eBay marketplace. The information includes IDs, descriptions, and URLs (as applicable) for the available signal words, statements, and pictograms. The returned statements are localized for the default language of the marketplace. If a marketplace does not support hazardous materials label information, no response payload is returned, but only a <b>204 No content</b> status code.<p>This information is used by the seller to add hazardous materials label related information to their listings (see <a href='/api-docs/sell/static/metadata/feature-regulatorhazmatcontainer.html'>Specifying hazardous material related information</a>).</p>

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.hazardous_material_details_response import HazardousMaterialDetailsResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which hazardous materials label information shall be retrieved.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values.
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_hazardous_materials_labels(marketplace_id, accept_language=accept_language)
        print("The response of MarketplaceApi->get_hazardous_materials_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_hazardous_materials_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which hazardous materials label information shall be retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values. | 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**HazardousMaterialDetailsResponse**](HazardousMaterialDetailsResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_condition_policies**
> ItemConditionPolicyResponse get_item_condition_policies(marketplace_id, filter=filter, accept_encoding=accept_encoding, accept_language=accept_language)

This method returns item condition metadata on one, multiple, or all eBay categories on an eBay marketplace. This metadata consists of the different item conditions (with IDs) that an eBay category supports, and a boolean to indicate if an eBay category requires an item condition. <br><br>If applicable, this metadata also shows the different condition descriptors (with IDs) that an eBay category supports.<br><br><span class="tablenote"><b>Note:</b> Currently, condition grading is only applicable to the following trading card categories: <ul><li>Non-Sport Trading Card Singles</li><li>CCG Individual Cards</li><li>Sports Trading Cards Singles</li></ul></span><br>The identifier of the eBay marketplace is passed in as a path parameter, and unless one or more eBay category IDs are passed in through the <b>filter</b> query parameter, this method will return metadata on every single category for the specified marketplace. If you only want to view item condition metadata for one eBay category or a select group of eBay categories, you can pass in up to 50 eBay category ID through the <b>filter</b> query parameter.<br><br><span class="tablenote"><span style="color:#FF0000"><strong>Important:</strong></span> <b>Certified - Refurbished</b>-eligible sellers, and sellers who are eligible to list with the new values (EXCELLENT_REFURBISHED, VERY_GOOD_REFURBISHED, and GOOD_REFURBISHED) must use an OAuth token created with the <a href="/api-docs/static/oauth-authorization-code-grant.html" target="_blank">authorization code grant flow</a> and <b>https://api.ebay.com/oauth/api_scope/sell.inventory</b> scope in order to retrieve the refurbished conditions for the relevant categories.<br/><br/>See the <a href="/api-docs/sell/static/metadata/condition-id-values.html#Category " target="_blank">eBay Refurbished Program - Category and marketplace support</a> topic for the categories and marketplaces that support these refurbished conditions<br/><br/>These restricted item conditions will not be returned if an OAuth token created with the <a href="/api-docs/static/oauth-client-credentials-grant.html" target="_blank">client credentials grant flow</a> and <b>https://api.ebay.com/oauth/api_scope</b> scope is used, or if any seller is not eligible to list with that item condition. <br/><br/> See the <a href="/api-docs/static/oauth-scopes.html" target="_blank">Specifying OAuth scopes</a> topic for more information about specifying scopes.</span><br><br><span class="tablenote"><span style="color:#478415"><strong>Tip:</strong></span> This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span>

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.item_condition_policy_response import ItemConditionPolicyResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information is retrieved.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values.
    filter = 'filter_example' # str | This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply <b>categoryId</b> values for the sections of the tree you want returned.  <br><br>When you specify a <b>categoryId</b> value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  <br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  <br><br><b>Example:</b> <code>filter=categoryIds:{100|101|102}</code>  <br><br>Note that you must URL-encode the parameter list, which results in the following filter for the above example: <br><br> &nbsp;&nbsp;<code>filter=categoryIds%3A%7B100%7C101%7C102%7D</code> (optional)
    accept_encoding = 'accept_encoding_example' # str | This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to <code>gzip</code>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (optional)
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_item_condition_policies(marketplace_id, filter=filter, accept_encoding=accept_encoding, accept_language=accept_language)
        print("The response of MarketplaceApi->get_item_condition_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_item_condition_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information is retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values. | 
 **filter** | **str**| This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree you want returned.  &lt;br&gt;&lt;br&gt;When you specify a &lt;b&gt;categoryId&lt;/b&gt; value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{100|101|102}&lt;/code&gt;  &lt;br&gt;&lt;br&gt;Note that you must URL-encode the parameter list, which results in the following filter for the above example: &lt;br&gt;&lt;br&gt; &amp;nbsp;&amp;nbsp;&lt;code&gt;filter&#x3D;categoryIds%3A%7B100%7C101%7C102%7D&lt;/code&gt; | [optional] 
 **accept_encoding** | **str**| This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to &lt;code&gt;gzip&lt;/code&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | [optional] 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**ItemConditionPolicyResponse**](ItemConditionPolicyResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_structure_policies**
> ListingStructurePolicyResponse get_listing_structure_policies(marketplace_id, filter=filter, accept_encoding=accept_encoding, accept_language=accept_language)

This method returns the eBay policies that define the allowed listing structures for the categories of a specific marketplace. The listing-structure policies currently pertain to whether or not you can list items with variations.  <br><br>By default, this method returns the entire category tree for the specified marketplace. You can limit the size of the result set by using the <b>filter</b> query parameter to specify only the category IDs you want to review.<br><br><span class="tablenote"><span style="color:#478415"><strong>Tip:</strong></span> This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span>

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.listing_structure_policy_response import ListingStructurePolicyResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information is retrieved. <br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values.
    filter = 'filter_example' # str | This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply <b>categoryId</b> values for the sections of the tree you want returned.  <br><br>When you specify a <b>categoryId</b> value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  <br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  <br><br><b>Example:</b> <code>filter=categoryIds:{100|101|102}</code>  <br><br>Note that you must URL-encode the parameter list, which results in the following filter for the above example: <br><br> &nbsp;&nbsp;<code>filter=categoryIds%3A%7B100%7C101%7C102%7D</code> (optional)
    accept_encoding = 'accept_encoding_example' # str | This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to <code>gzip</code>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (optional)
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_listing_structure_policies(marketplace_id, filter=filter, accept_encoding=accept_encoding, accept_language=accept_language)
        print("The response of MarketplaceApi->get_listing_structure_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_listing_structure_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information is retrieved. &lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values. | 
 **filter** | **str**| This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree you want returned.  &lt;br&gt;&lt;br&gt;When you specify a &lt;b&gt;categoryId&lt;/b&gt; value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{100|101|102}&lt;/code&gt;  &lt;br&gt;&lt;br&gt;Note that you must URL-encode the parameter list, which results in the following filter for the above example: &lt;br&gt;&lt;br&gt; &amp;nbsp;&amp;nbsp;&lt;code&gt;filter&#x3D;categoryIds%3A%7B100%7C101%7C102%7D&lt;/code&gt; | [optional] 
 **accept_encoding** | **str**| This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to &lt;code&gt;gzip&lt;/code&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | [optional] 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**ListingStructurePolicyResponse**](ListingStructurePolicyResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_type_policies**
> ListingTypePoliciesResponse get_listing_type_policies(marketplace_id, filter=filter, accept_language=accept_language)

This method returns eBay listing type policy metadata for all leaf categories on the specified marketplace. <p>By default, this method returns metadata on all leaf categories. You can limit the size of the result set by using the <b>filter</b> query parameter to specify only the leaf category IDs you want to review.</p><p>If you specify a valid marketplace ID but that marketplace does not contain policy information, or if you filter out all results, a successful call returns a <b>204 No content</b> status code with an empty response body.</p>

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.listing_type_policies_response import ListingTypePoliciesResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information is retrieved.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values.
    filter = 'filter_example' # str | This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the <b>categoryId</b> for one or more leaf categories. You can verify if a category is a leaf category by using the <a href=\"/api-docs/commerce/taxonomy/overview.html\" target=\"_blank \">Taxonomy API</a> and looking for a <code>\"leafCategory\": true</code> tag.<br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.<br><br><b>Example:</b> <code>filter=categoryIds:{3767|171784}</code> (optional)
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_listing_type_policies(marketplace_id, filter=filter, accept_language=accept_language)
        print("The response of MarketplaceApi->get_listing_type_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_listing_type_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information is retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values. | 
 **filter** | **str**| This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the &lt;b&gt;categoryId&lt;/b&gt; for one or more leaf categories. You can verify if a category is a leaf category by using the &lt;a href&#x3D;\&quot;/api-docs/commerce/taxonomy/overview.html\&quot; target&#x3D;\&quot;_blank \&quot;&gt;Taxonomy API&lt;/a&gt; and looking for a &lt;code&gt;\&quot;leafCategory\&quot;: true&lt;/code&gt; tag.&lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.&lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{3767|171784}&lt;/code&gt; | [optional] 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**ListingTypePoliciesResponse**](ListingTypePoliciesResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_motors_listing_policies**
> MotorsListingPoliciesResponse get_motors_listing_policies(marketplace_id, filter=filter, accept_language=accept_language)

This method returns eBay Motors policy metadata for all leaf categories on the specified marketplace. <p>By default, this method returns metadata on all leaf categories. You can limit the size of the result set by using the <b>filter</b> query parameter to specify only the leaf category IDs you want to review.</p><p>If you specify a valid marketplace ID but that marketplace does not contain policy information, or if you filter out all results, a successful call returns a <b>204 No content</b> status code with an empty response body.</p><p><span class="tablenote"><span style="color:#004680"><strong>Note:</strong></span> To return policy information for eBay US Motors categories, specify <b>marketplace_id</b> as <code>EBAY_MOTORS_US</code>.</span></p>

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.motors_listing_policies_response import MotorsListingPoliciesResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information is retrieved.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values.
    filter = 'filter_example' # str | This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the <b>categoryId</b> for one or more leaf categories. You can verify if a category is a leaf category by using the <a href=\"/api-docs/commerce/taxonomy/overview.html\" target=\"_blank \">Taxonomy API</a> and looking for a <code>\"leafCategory\": true</code> tag. <br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.<br><br><b>Example:</b> <code>filter=categoryIds:{3767|171784}</code> (optional)
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_motors_listing_policies(marketplace_id, filter=filter, accept_language=accept_language)
        print("The response of MarketplaceApi->get_motors_listing_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_motors_listing_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information is retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values. | 
 **filter** | **str**| This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the &lt;b&gt;categoryId&lt;/b&gt; for one or more leaf categories. You can verify if a category is a leaf category by using the &lt;a href&#x3D;\&quot;/api-docs/commerce/taxonomy/overview.html\&quot; target&#x3D;\&quot;_blank \&quot;&gt;Taxonomy API&lt;/a&gt; and looking for a &lt;code&gt;\&quot;leafCategory\&quot;: true&lt;/code&gt; tag. &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.&lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{3767|171784}&lt;/code&gt; | [optional] 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**MotorsListingPoliciesResponse**](MotorsListingPoliciesResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_negotiated_price_policies**
> NegotiatedPricePolicyResponse get_negotiated_price_policies(marketplace_id, filter=filter, accept_encoding=accept_encoding, accept_language=accept_language)

This method returns the eBay policies that define the supported negotiated price features (like "best offer") for the categories of a specific marketplace.  <br><br>By default, this method returns the entire category tree for the specified marketplace. You can limit the size of the result set by using the <b>filter</b> query parameter to specify only the category IDs you want to review.<br><br><span class="tablenote"><span style="color:#478415"><strong>Tip:</strong></span> This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span>

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.negotiated_price_policy_response import NegotiatedPricePolicyResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information is retrieved.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values.
    filter = 'filter_example' # str | This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply <b>categoryId</b> values for the sections of the tree you want returned.  <br><br>When you specify a <b>categoryId</b> value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  <br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  <br><br><b>Example:</b> <code>filter=categoryIds:{100|101|102}</code>  <br><br>Note that you must URL-encode the parameter list, which results in the following filter for the above example: <br><br> &nbsp;&nbsp;<code>filter=categoryIds%3A%7B100%7C101%7C102%7D</code> (optional)
    accept_encoding = 'accept_encoding_example' # str | This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to <code>gzip</code>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (optional)
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_negotiated_price_policies(marketplace_id, filter=filter, accept_encoding=accept_encoding, accept_language=accept_language)
        print("The response of MarketplaceApi->get_negotiated_price_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_negotiated_price_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information is retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values. | 
 **filter** | **str**| This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree you want returned.  &lt;br&gt;&lt;br&gt;When you specify a &lt;b&gt;categoryId&lt;/b&gt; value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{100|101|102}&lt;/code&gt;  &lt;br&gt;&lt;br&gt;Note that you must URL-encode the parameter list, which results in the following filter for the above example: &lt;br&gt;&lt;br&gt; &amp;nbsp;&amp;nbsp;&lt;code&gt;filter&#x3D;categoryIds%3A%7B100%7C101%7C102%7D&lt;/code&gt; | [optional] 
 **accept_encoding** | **str**| This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to &lt;code&gt;gzip&lt;/code&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | [optional] 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**NegotiatedPricePolicyResponse**](NegotiatedPricePolicyResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_safety_labels**
> ProductSafetyLabelsResponse get_product_safety_labels(marketplace_id)

This method returns product safety label information for the specified eBay marketplace. The information includes IDs, descriptions, and URLs (as applicable) for the available statements and pictograms. The returned statements are localized for the default language of the marketplace. If a marketplace does not support product safety label information, no response payload is returned, but only a <b>204 No content</b> status code.<p>This information is used by the seller to add product safety label related information to their listings. The <a href="/api-docs/sell/metadata/resources/marketplace/methods/getRegulatoryPolicies" target="_blank">getRegulatoryPolicies</a> method can be used to see which categories recommend or require product safety labels.</p>

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.product_safety_labels_response import ProductSafetyLabelsResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information is retrieved.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values. See the following note for exceptions.<span class=\"tablenote\"><span style=\"color:#478415\"><strong>Note: </strong></span>This method is not supported in the <code>EBAY_HK</code>, <code>EBAY_MY</code>, <code>EBAY_TW</code>, or <code>EBAY_PH</code> marketplaces.</span>

    try:
        api_response = api_instance.get_product_safety_labels(marketplace_id)
        print("The response of MarketplaceApi->get_product_safety_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_product_safety_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information is retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values. See the following note for exceptions.&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#478415\&quot;&gt;&lt;strong&gt;Note: &lt;/strong&gt;&lt;/span&gt;This method is not supported in the &lt;code&gt;EBAY_HK&lt;/code&gt;, &lt;code&gt;EBAY_MY&lt;/code&gt;, &lt;code&gt;EBAY_TW&lt;/code&gt;, or &lt;code&gt;EBAY_PH&lt;/code&gt; marketplaces.&lt;/span&gt; | 

### Return type

[**ProductSafetyLabelsResponse**](ProductSafetyLabelsResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_regulatory_policies**
> RegulatoryPolicyResponse get_regulatory_policies(marketplace_id, filter=filter, accept_language=accept_language)

This method returns regulatory policies for one, multiple, or all eBay categories in an eBay marketplace. The identifier of the eBay marketplace is passed in as a path parameter, and unless one or more eBay category IDs are passed in through the filter query parameter, this method will return metadata for every listing category in the specified marketplace.</p><p><span class="tablenote"><span style="color:#478415"><strong>Tip:</strong></span> This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span></p>

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.regulatory_policy_response import RegulatoryPolicyResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information shall be retrieved.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values.<span class=\"tablenote\"><span style=\"color:#478415\"><strong>Note: </strong></span>This method is not supported in the <code>EBAY_HK</code>, <code>EBAY_MY</code>, <code>EBAY_TW</code>, or <code>EBAY_PH</code> marketplaces.</span>
    filter = 'filter_example' # str | A query parameter that can be used to limit the response by returning policy information for only the selected sections of the category tree. Supply <b>categoryId</b> values for the sections of the tree that should be returned.<br><br>Pass in the <b>categoryId</b> values using a URL-encoded, pipe-separated ('|') list. For example: <br><br><code>filter=categoryIds%3A%7B100%7C101%7C102%7D</code><br><br><b>Maximum:</b> 50 (optional)
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_regulatory_policies(marketplace_id, filter=filter, accept_language=accept_language)
        print("The response of MarketplaceApi->get_regulatory_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_regulatory_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information shall be retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values.&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#478415\&quot;&gt;&lt;strong&gt;Note: &lt;/strong&gt;&lt;/span&gt;This method is not supported in the &lt;code&gt;EBAY_HK&lt;/code&gt;, &lt;code&gt;EBAY_MY&lt;/code&gt;, &lt;code&gt;EBAY_TW&lt;/code&gt;, or &lt;code&gt;EBAY_PH&lt;/code&gt; marketplaces.&lt;/span&gt; | 
 **filter** | **str**| A query parameter that can be used to limit the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree that should be returned.&lt;br&gt;&lt;br&gt;Pass in the &lt;b&gt;categoryId&lt;/b&gt; values using a URL-encoded, pipe-separated (&#39;|&#39;) list. For example: &lt;br&gt;&lt;br&gt;&lt;code&gt;filter&#x3D;categoryIds%3A%7B100%7C101%7C102%7D&lt;/code&gt;&lt;br&gt;&lt;br&gt;&lt;b&gt;Maximum:&lt;/b&gt; 50 | [optional] 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**RegulatoryPolicyResponse**](RegulatoryPolicyResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_policies**
> ReturnPolicyResponse get_return_policies(marketplace_id, filter=filter, accept_encoding=accept_encoding, accept_language=accept_language)

This method returns the eBay policies that define whether or not you must include a return policy for the items you list in the categories of a specific marketplace, plus the guidelines for creating domestic and international return policies in the different eBay categories.  <br><br>By default, this method returns the entire category tree for the specified marketplace. You can limit the size of the result set by using the <b>filter</b> query parameter to specify only the category IDs you want to review.<br><br><span class="tablenote"><span style="color:#478415"><strong>Tip:</strong></span> This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span>

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.return_policy_response import ReturnPolicyResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information is retrieved.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values.
    filter = 'filter_example' # str | This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply <b>categoryId</b> values for the sections of the tree you want returned.  <br><br>When you specify a <b>categoryId</b> value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  <br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  <br><br><b>Example:</b> <code>filter=categoryIds:{100|101|102}</code>  <br><br>Note that you must URL-encode the parameter list, which results in the following filter for the above example: <br><br> &nbsp;&nbsp;<code>filter=categoryIds%3A%7B100%7C101%7C102%7D</code> (optional)
    accept_encoding = 'accept_encoding_example' # str | This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to <code>gzip</code>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (optional)
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_return_policies(marketplace_id, filter=filter, accept_encoding=accept_encoding, accept_language=accept_language)
        print("The response of MarketplaceApi->get_return_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_return_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information is retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values. | 
 **filter** | **str**| This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree you want returned.  &lt;br&gt;&lt;br&gt;When you specify a &lt;b&gt;categoryId&lt;/b&gt; value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{100|101|102}&lt;/code&gt;  &lt;br&gt;&lt;br&gt;Note that you must URL-encode the parameter list, which results in the following filter for the above example: &lt;br&gt;&lt;br&gt; &amp;nbsp;&amp;nbsp;&lt;code&gt;filter&#x3D;categoryIds%3A%7B100%7C101%7C102%7D&lt;/code&gt; | [optional] 
 **accept_encoding** | **str**| This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to &lt;code&gt;gzip&lt;/code&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | [optional] 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**ReturnPolicyResponse**](ReturnPolicyResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipping_policies**
> ShippingPoliciesResponse get_shipping_policies(marketplace_id, filter=filter, accept_language=accept_language)

This method returns eBay shipping policy metadata for all leaf categories on the specified marketplace.<p>By default, this method returns metadata on all leaf categories. You can limit the size of the result set by using the <b>filter</b> query parameter to specify only the leaf category IDs you want to review.</p><p>If you specify a valid marketplace ID but that marketplace does not contain policy information, or if you filter out all results, a successful call returns a <b>204 No content</b> status code with an empty response body.

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.shipping_policies_response import ShippingPoliciesResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information is retrieved.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values.
    filter = 'filter_example' # str | This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the <b>categoryId</b> for one or more leaf categories. You can verify if a category is a leaf category by using the <a href=\"/api-docs/commerce/taxonomy/overview.html\" target=\"_blank \">Taxonomy API</a> and looking for a <code>\"leafCategory\": true</code> tag. <br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.<br><br><b>Example:</b> <code>filter=categoryIds:{3767|171784}</code> (optional)
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_shipping_policies(marketplace_id, filter=filter, accept_language=accept_language)
        print("The response of MarketplaceApi->get_shipping_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_shipping_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information is retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values. | 
 **filter** | **str**| This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the &lt;b&gt;categoryId&lt;/b&gt; for one or more leaf categories. You can verify if a category is a leaf category by using the &lt;a href&#x3D;\&quot;/api-docs/commerce/taxonomy/overview.html\&quot; target&#x3D;\&quot;_blank \&quot;&gt;Taxonomy API&lt;/a&gt; and looking for a &lt;code&gt;\&quot;leafCategory\&quot;: true&lt;/code&gt; tag. &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.&lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{3767|171784}&lt;/code&gt; | [optional] 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**ShippingPoliciesResponse**](ShippingPoliciesResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_visibility_policies**
> SiteVisibilityPoliciesResponse get_site_visibility_policies(marketplace_id, filter=filter, accept_language=accept_language)

This method returns eBay international site visibility policy metadata for all leaf categories on the specified marketplace.<p>By default, this method returns metadata on all leaf categories. You can limit the size of the result set by using the <b>filter</b> query parameter to specify only the leaf category IDs you want to review.</p><p>If you specify a valid marketplace ID but that marketplace does not contain policy information, or if you filter out all results, a successful call returns a <b>204 No content</b> status code with an empty response body.

### Example

* OAuth Authentication (api_auth):
* OAuth Authentication (api_auth):

```python
import ebaymetadata
from ebaymetadata.models.site_visibility_policies_response import SiteVisibilityPoliciesResponse
from ebaymetadata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/metadata/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymetadata.Configuration(
    host = "https://api.ebay.com/sell/metadata/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymetadata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymetadata.MarketplaceApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | This path parameter specifies the eBay marketplace for which policy information is retrieved.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl\" target=\"_blank\">HTTP Request Headers</a> for a list of supported eBay marketplace ID values.
    filter = 'filter_example' # str | This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the <b>categoryId</b> for one or more leaf categories. You can verify if a category is a leaf category by using the <a href=\"/api-docs/commerce/taxonomy/overview.html\" target=\"_blank \">Taxonomy API</a> and looking for a <code>\"leafCategory\": true</code> tag. <br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.<br><br><b>Example:</b><code>filter=categoryIds:{3767|171784}</code> (optional)
    accept_language = 'accept_language_example' # str | This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class=\"tablenote\"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (optional)

    try:
        api_response = api_instance.get_site_visibility_policies(marketplace_id, filter=filter, accept_language=accept_language)
        print("The response of MarketplaceApi->get_site_visibility_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_site_visibility_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| This path parameter specifies the eBay marketplace for which policy information is retrieved.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP Request Headers&lt;/a&gt; for a list of supported eBay marketplace ID values. | 
 **filter** | **str**| This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the &lt;b&gt;categoryId&lt;/b&gt; for one or more leaf categories. You can verify if a category is a leaf category by using the &lt;a href&#x3D;\&quot;/api-docs/commerce/taxonomy/overview.html\&quot; target&#x3D;\&quot;_blank \&quot;&gt;Taxonomy API&lt;/a&gt; and looking for a &lt;code&gt;\&quot;leafCategory\&quot;: true&lt;/code&gt; tag. &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.&lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt;&lt;code&gt;filter&#x3D;categoryIds:{3767|171784}&lt;/code&gt; | [optional] 
 **accept_language** | **str**| This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.&lt;br&gt;&lt;br&gt;Follow the instructions below to retrieve metadata for these three marketplaces:&lt;ul&gt;&lt;li&gt;&lt;b&gt;French Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Dutch Belgium&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_BE&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;nl-BE&lt;/code&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;French Canada&lt;/b&gt;: Set the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter value to &lt;code&gt;EBAY_CA&lt;/code&gt;, and include the &lt;b&gt;Accept-Language&lt;/b&gt; header with a value of &lt;code&gt;fr-CA&lt;/code&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If &lt;code&gt;EBAY_CA&lt;/code&gt; is set as the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter and the &lt;b&gt;Accept-Language&lt;/b&gt; header is not used, the marketplace will default to the English Canada marketplace.&lt;/span&gt; | [optional] 

### Return type

[**SiteVisibilityPoliciesResponse**](SiteVisibilityPoliciesResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

