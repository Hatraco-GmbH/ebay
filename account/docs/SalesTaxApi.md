# ebayaccount.SalesTaxApi

All URIs are relative to *https://api.ebay.com/sell/account/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_or_replace_sales_tax**](SalesTaxApi.md#bulk_create_or_replace_sales_tax) | **POST** /bulk_create_or_replace_sales_tax | 
[**create_or_replace_sales_tax**](SalesTaxApi.md#create_or_replace_sales_tax) | **PUT** /sales_tax/{countryCode}/{jurisdictionId} | 
[**delete_sales_tax**](SalesTaxApi.md#delete_sales_tax) | **DELETE** /sales_tax/{countryCode}/{jurisdictionId} | 
[**get_sales_tax**](SalesTaxApi.md#get_sales_tax) | **GET** /sales_tax/{countryCode}/{jurisdictionId} | 
[**get_sales_taxes**](SalesTaxApi.md#get_sales_taxes) | **GET** /sales_tax | 


# **bulk_create_or_replace_sales_tax**
> UpdatedSalesTaxResponse bulk_create_or_replace_sales_tax(bulk_sales_tax_input)

This method creates or updates multiple sales-tax table entries.<br><br><i>Sales-tax tables</i> can be set up for countries that support different <i>tax jurisdictions</i>.<br><br><span class="tablenote"><b>Note:</b> Sales-tax tables are only available for the US (EBAY_US) and Canada (EBAY_CA) marketplaces.</span><br>Each sales-tax table entry comprises the following parameters:<ul><li><code>countryCode</code></li><li><code>jurisdictionId</code></li><li><code>salesTaxPercentage</code></li><li><code>shippingAndHandlingTaxed</code></li></ul><br>Valid jurisdiction IDs are retrieved using <b><a href="/api-docs/sell/metadata/resources/country/methods/getSalesTaxJurisdictions" target="_blank">getSalesTaxJurisdictions</a></b> in the Metadata API.<br><br>For details about using this call, refer to <a href="/api-docs/sell/static/seller-accounts/tax-tables.html">Establishing sales-tax tables</a>.<br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> In the US, eBay now calculates, collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC. Sellers can no longer specify sales-tax rates for these jurisdictions using a tax table.<br><br>However, sellers may continue to use a sales-tax table to set rates for the following US territories:<ul><li>American Samoa (AS)</li><li>Guam (GU)</li><li>Northern Mariana Islands (MP)</li><li>Palau (PW)</li><li>US Virgin Islands (VI)</li></ul>For additional information, refer to <a href="https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 " target="_blank">Taxes and import charges</a>.</p></div>

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.bulk_sales_tax_input import BulkSalesTaxInput
from ebayaccount.models.updated_sales_tax_response import UpdatedSalesTaxResponse
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
    api_instance = ebayaccount.SalesTaxApi(api_client)
    bulk_sales_tax_input = ebayaccount.BulkSalesTaxInput() # BulkSalesTaxInput | List of sales taxes to be updated

    try:
        api_response = api_instance.bulk_create_or_replace_sales_tax(bulk_sales_tax_input)
        print("The response of SalesTaxApi->bulk_create_or_replace_sales_tax:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesTaxApi->bulk_create_or_replace_sales_tax: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_sales_tax_input** | [**BulkSalesTaxInput**](BulkSalesTaxInput.md)| List of sales taxes to be updated | 

### Return type

[**UpdatedSalesTaxResponse**](UpdatedSalesTaxResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**207** | partial success |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_replace_sales_tax**
> create_or_replace_sales_tax(country_code, jurisdiction_id, content_type, sales_tax_base)

This method creates or updates a sales-tax table entry for a jurisdiction. Specify the tax table entry you want to configure using the two path parameters: <b>countryCode</b> and <b>jurisdictionId</b>.  <br><br>A tax table entry for a jurisdiction is comprised of two fields: one for the jurisdiction's sales-tax rate and another that's a boolean value indicating whether or not shipping and handling are taxed in the jurisdiction.<br><br>You can set up <i>sales-tax tables</i> for countries that support different <i>tax jurisdictions</i>.<br><br><span class="tablenote"><b>Note:</b> Sales-tax tables are only available for the US (EBAY_US) and Canada (EBAY_CA) marketplaces.</span><br>Retrieve valid jurisdiction IDs using <b><a href="/api-docs/sell/metadata/resources/country/methods/getSalesTaxJurisdictions" target="_blank">getSalesTaxJurisdictions</a></b> in the Metadata API.<br><br>For details about using this call, refer to <a href="/api-docs/sell/static/seller-accounts/tax-tables.html">Establishing sales-tax tables</a>.<br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> In the US, eBay now calculates, collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC. Sellers can no longer specify sales-tax rates for these jurisdictions using a tax table.<br><br>However, sellers may continue to use a sales-tax table to set rates for the following US territories:<ul><li>American Samoa (AS)</li><li>Guam (GU)</li><li>Northern Mariana Islands (MP)</li><li>Palau (PW)</li><li>US Virgin Islands (VI)</li></ul>For additional information, refer to <a href="https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 " target="_blank">Taxes and import charges</a>.</p></div>

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.sales_tax_base import SalesTaxBase
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
    api_instance = ebayaccount.SalesTaxApi(api_client)
    country_code = 'country_code_example' # str | This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> code for the country for which you want to create a sales tax table entry.<br><br><span class=\"tablenote\"><b>Note:</b> Sales-tax tables are available only for the US and Canada marketplaces. Therefore, the only supported values are:<ul><li><code>US</code></li><li><code>CA</code></li></ul></span>
    jurisdiction_id = 'jurisdiction_id_example' # str | This path parameter specifies the ID of the tax jurisdiction for the table entry to be created.<br><br>Valid jurisdiction IDs can be retrieved using the <a href=\"/api-docs/sell/metadata/resources/country/methods/getSalesTaxJurisdictions\" target=\"_blank \">getSalesTaxJurisdiction</a> method of the Metadata API.<br><br><span class=\"tablenote\"><b>Note:</b> When <code>countryCode</code> is set to <code>US</code>, the only supported values for <code>jurisdictionId</code> are:<ul><li><code>AS</code> (American Samoa)</li><li><code>GU</code> (Guam)</li><li><code>MP</code> (Northern Mariana Islands)</li><li><code>PW</code> (Palau)</li><li><code>VI</code> (US Virgin Islands)</li></ul></span>
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>.<br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    sales_tax_base = ebayaccount.SalesTaxBase() # SalesTaxBase | A container that describes the how the sales tax is calculated.

    try:
        api_instance.create_or_replace_sales_tax(country_code, jurisdiction_id, content_type, sales_tax_base)
    except Exception as e:
        print("Exception when calling SalesTaxApi->create_or_replace_sales_tax: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| This path parameter specifies the two-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166&lt;/a&gt; code for the country for which you want to create a sales tax table entry.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Sales-tax tables are available only for the US and Canada marketplaces. Therefore, the only supported values are:&lt;ul&gt;&lt;li&gt;&lt;code&gt;US&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;CA&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt; | 
 **jurisdiction_id** | **str**| This path parameter specifies the ID of the tax jurisdiction for the table entry to be created.&lt;br&gt;&lt;br&gt;Valid jurisdiction IDs can be retrieved using the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/country/methods/getSalesTaxJurisdictions\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getSalesTaxJurisdiction&lt;/a&gt; method of the Metadata API.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; When &lt;code&gt;countryCode&lt;/code&gt; is set to &lt;code&gt;US&lt;/code&gt;, the only supported values for &lt;code&gt;jurisdictionId&lt;/code&gt; are:&lt;ul&gt;&lt;li&gt;&lt;code&gt;AS&lt;/code&gt; (American Samoa)&lt;/li&gt;&lt;li&gt;&lt;code&gt;GU&lt;/code&gt; (Guam)&lt;/li&gt;&lt;li&gt;&lt;code&gt;MP&lt;/code&gt; (Northern Mariana Islands)&lt;/li&gt;&lt;li&gt;&lt;code&gt;PW&lt;/code&gt; (Palau)&lt;/li&gt;&lt;li&gt;&lt;code&gt;VI&lt;/code&gt; (US Virgin Islands)&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt; | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;.&lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **sales_tax_base** | [**SalesTaxBase**](SalesTaxBase.md)| A container that describes the how the sales tax is calculated. | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sales_tax**
> delete_sales_tax(country_code, jurisdiction_id)

This call deletes a sales-tax table entry for a jurisdiction. Specify the jurisdiction to delete using the <b>countryCode</b> and <b>jurisdictionId</b> path parameters.<br><br><span class="tablenote"><b>Note:</b> Sales-tax tables are only available for the US (EBAY_US) and Canada (EBAY_CA) marketplaces.</span>

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
    api_instance = ebayaccount.SalesTaxApi(api_client)
    country_code = 'country_code_example' # str | This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> code for the country whose sales tax table entry you want to delete.<br><br><span class=\"tablenote\"><b>Note:</b> Sales-tax tables are available only for the US and Canada marketplaces. Therefore, the only supported values are:<ul><li><code>US</code></li><li><code>CA</code></li></ul></span>
    jurisdiction_id = 'jurisdiction_id_example' # str | This path parameter specifies the ID of the sales tax jurisdiction whose table entry you want to delete.<br><br>Valid jurisdiction IDs can be retrieved using the <a href=\"/api-docs/sell/metadata/resources/country/methods/getSalesTaxJurisdictions\" target=\"_blank \">getSalesTaxJurisdiction</a> method of the Metadata API.<br><br><span class=\"tablenote\"><b>Note:</b> When <code>countryCode</code> is set to <code>US</code>, the only supported values for <code>jurisdictionId</code> are:<ul><li><code>AS</code> (American Samoa)</li><li><code>GU</code> (Guam)</li><li><code>MP</code> (Northern Mariana Islands)</li><li><code>PW</code> (Palau)</li><li><code>VI</code> (US Virgin Islands)</li></ul></span>

    try:
        api_instance.delete_sales_tax(country_code, jurisdiction_id)
    except Exception as e:
        print("Exception when calling SalesTaxApi->delete_sales_tax: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| This path parameter specifies the two-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166&lt;/a&gt; code for the country whose sales tax table entry you want to delete.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Sales-tax tables are available only for the US and Canada marketplaces. Therefore, the only supported values are:&lt;ul&gt;&lt;li&gt;&lt;code&gt;US&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;CA&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt; | 
 **jurisdiction_id** | **str**| This path parameter specifies the ID of the sales tax jurisdiction whose table entry you want to delete.&lt;br&gt;&lt;br&gt;Valid jurisdiction IDs can be retrieved using the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/country/methods/getSalesTaxJurisdictions\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getSalesTaxJurisdiction&lt;/a&gt; method of the Metadata API.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; When &lt;code&gt;countryCode&lt;/code&gt; is set to &lt;code&gt;US&lt;/code&gt;, the only supported values for &lt;code&gt;jurisdictionId&lt;/code&gt; are:&lt;ul&gt;&lt;li&gt;&lt;code&gt;AS&lt;/code&gt; (American Samoa)&lt;/li&gt;&lt;li&gt;&lt;code&gt;GU&lt;/code&gt; (Guam)&lt;/li&gt;&lt;li&gt;&lt;code&gt;MP&lt;/code&gt; (Northern Mariana Islands)&lt;/li&gt;&lt;li&gt;&lt;code&gt;PW&lt;/code&gt; (Palau)&lt;/li&gt;&lt;li&gt;&lt;code&gt;VI&lt;/code&gt; (US Virgin Islands)&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt; | 

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
**204** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_tax**
> SalesTax get_sales_tax(country_code, jurisdiction_id)

This call retrieves the current sales-tax table entry for a specific tax jurisdiction. Specify the jurisdiction to retrieve using the <b>countryCode</b> and <b>jurisdictionId</b> path parameters. All four response fields will be returned if a sales-tax entry exists for the tax jurisdiction. Otherwise, the response will be returned as empty.<br><br><span class="tablenote"><b>Note:</b> Sales-tax tables are only available for the US (EBAY_US) and Canada (EBAY_CA) marketplaces.</span><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> In the US, eBay now calculates, collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC. Sellers can no longer specify sales-tax rates for these jurisdictions using a tax table.<br><br>However, sellers may continue to use a sales-tax table to set rates for the following US territories:<ul><li>American Samoa (AS)</li><li>Guam (GU)</li><li>Northern Mariana Islands (MP)</li><li>Palau (PW)</li><li>US Virgin Islands (VI)</li></ul>For additional information, refer to <a href="https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 " target="_blank">Taxes and import charges</a>.</p></div>

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.sales_tax import SalesTax
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
    api_instance = ebayaccount.SalesTaxApi(api_client)
    country_code = 'country_code_example' # str | This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> code for the country whose sales tax table you want to retrieve.<br><br><span class=\"tablenote\"><b>Note:</b> Sales-tax tables are available only for the US and Canada marketplaces. Therefore, the only supported values are:<ul><li><code>US</code></li><li><code>CA</code></li></ul></span>
    jurisdiction_id = 'jurisdiction_id_example' # str | This path parameter specifies the ID of the sales tax jurisdiction for the tax table entry to be retrieved.<br><br>Valid jurisdiction IDs can be retrieved using the <a href=\"/api-docs/sell/metadata/resources/country/methods/getSalesTaxJurisdictions\" target=\"_blank \">getSalesTaxJurisdiction</a> method of the Metadata API.<br><br><span class=\"tablenote\"><b>Note:</b> When <code>countryCode</code> is set to <code>US</code>, the only supported values for <code>jurisdictionId</code> are:<ul><li><code>AS</code> (American Samoa)</li><li><code>GU</code> (Guam</li><li><code>MP</code> Northern Mariana Islands</li><li><code>PW (Palau)</li><li><code>VI</code> (US Virgin Islands)</li></ul></span>

    try:
        api_response = api_instance.get_sales_tax(country_code, jurisdiction_id)
        print("The response of SalesTaxApi->get_sales_tax:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesTaxApi->get_sales_tax: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| This path parameter specifies the two-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166&lt;/a&gt; code for the country whose sales tax table you want to retrieve.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Sales-tax tables are available only for the US and Canada marketplaces. Therefore, the only supported values are:&lt;ul&gt;&lt;li&gt;&lt;code&gt;US&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;CA&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt; | 
 **jurisdiction_id** | **str**| This path parameter specifies the ID of the sales tax jurisdiction for the tax table entry to be retrieved.&lt;br&gt;&lt;br&gt;Valid jurisdiction IDs can be retrieved using the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/country/methods/getSalesTaxJurisdictions\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getSalesTaxJurisdiction&lt;/a&gt; method of the Metadata API.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; When &lt;code&gt;countryCode&lt;/code&gt; is set to &lt;code&gt;US&lt;/code&gt;, the only supported values for &lt;code&gt;jurisdictionId&lt;/code&gt; are:&lt;ul&gt;&lt;li&gt;&lt;code&gt;AS&lt;/code&gt; (American Samoa)&lt;/li&gt;&lt;li&gt;&lt;code&gt;GU&lt;/code&gt; (Guam&lt;/li&gt;&lt;li&gt;&lt;code&gt;MP&lt;/code&gt; Northern Mariana Islands&lt;/li&gt;&lt;li&gt;&lt;code&gt;PW (Palau)&lt;/li&gt;&lt;li&gt;&lt;code&gt;VI&lt;/code&gt; (US Virgin Islands)&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt; | 

### Return type

[**SalesTax**](SalesTax.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_taxes**
> SalesTaxes get_sales_taxes(country_code)

Use this call to retrieve all sales tax table entries that the seller has defined for a specific country. All four response fields will be returned for each tax jurisdiction that matches the search criteria. If no sales tax rates are defined for the specified, a <code>204 No Content</code> status code is returned with no response payload.<br><br><span class="tablenote"><b>Note:</b> Sales-tax tables are only available for the US (EBAY_US) and Canada (EBAY_CA) marketplaces.</span><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> In the US, eBay now calculates, collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC. Sellers can no longer specify sales-tax rates for these jurisdictions using a tax table.<br><br>However, sellers may continue to use a sales-tax table to set rates for the following US territories:<ul><li>American Samoa (AS)</li><li>Guam (GU)</li><li>Northern Mariana Islands (MP)</li><li>Palau (PW)</li><li>US Virgin Islands (VI)</li></ul>For additional information, refer to <a href="https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 " target="_blank">Taxes and import charges</a>.</p></div>

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.sales_taxes import SalesTaxes
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
    api_instance = ebayaccount.SalesTaxApi(api_client)
    country_code = 'country_code_example' # str | This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> code for the country whose tax table you want to retrieve.<br><br><span class=\"tablenote\"><b>Note:</b> Sales-tax tables are available only for the US and Canada marketplaces. Therefore, the only supported values are:<ul><li><code>US</code></li><li><code>CA</code></li></ul></span> For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:CountryCodeEnum

    try:
        api_response = api_instance.get_sales_taxes(country_code)
        print("The response of SalesTaxApi->get_sales_taxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesTaxApi->get_sales_taxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| This path parameter specifies the two-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166&lt;/a&gt; code for the country whose tax table you want to retrieve.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Sales-tax tables are available only for the US and Canada marketplaces. Therefore, the only supported values are:&lt;ul&gt;&lt;li&gt;&lt;code&gt;US&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;CA&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt; For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:CountryCodeEnum | 

### Return type

[**SalesTaxes**](SalesTaxes.md)

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

