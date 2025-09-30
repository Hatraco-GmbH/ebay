# ebaymetadata.CountryApi

All URIs are relative to *https://api.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sales_tax_jurisdictions**](CountryApi.md#get_sales_tax_jurisdictions) | **GET** /country/{countryCode}/sales_tax_jurisdiction | 

# **get_sales_tax_jurisdictions**
> SalesTaxJurisdictions get_sales_tax_jurisdictions(country_code)



This method retrieves all sales-tax jurisdictions for the country specified in the <b>countryCode</b> path parameter. Countries with valid sales-tax jurisdictions are Canada and the US.<br><br>The response from this call tells you the jurisdictions for which a seller can configure tax tables. Although setting up tax tables is optional, you can use the <b>createOrReplaceSalesTax</b> method in the <b>Account API</b> call to configure the tax tables for the jurisdictions into which you sell.<br><br><span class=\"tablenote\"><b>Note:</b> Sales-tax tables are only available for the US (EBAY_US) and Canada (EBAY_CA) marketplaces.</span><br><br><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span> In the US, eBay now calculates, collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC. Sellers can no longer specify sales-tax rates for these jurisdictions using a tax table.<br><br>However, sellers may continue to use a sales-tax table to set rates for the following US territories:<ul><li>American Samoa (AS)</li><li>Guam (GU)</li><li>Northern Mariana Islands (MP)</li><li>Palau (PW)</li><li>US Virgin Islands (VI)</li></ul>For additional information, refer to <a href=\"https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 \" target=\"_blank\">Taxes and import charges</a>.</p></div>

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
api_instance = ebaymetadata.CountryApi(ebaymetadata.ApiClient(configuration))
country_code = 'country_code_example' # str | This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> country code for the country whose jurisdictions you want to retrieve.<br><br><span class=\"tablenote\"><b>Note:</b> Sales-tax tables are available only for the US and Canada marketplaces. Therefore, the only supported values are:<ul><li><code>US</code></li><li><code>CA</code></li></ul></span>

try:
    api_response = api_instance.get_sales_tax_jurisdictions(country_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryApi->get_sales_tax_jurisdictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| This path parameter specifies the two-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166&lt;/a&gt; country code for the country whose jurisdictions you want to retrieve.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Sales-tax tables are available only for the US and Canada marketplaces. Therefore, the only supported values are:&lt;ul&gt;&lt;li&gt;&lt;code&gt;US&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;CA&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt; | 

### Return type

[**SalesTaxJurisdictions**](SalesTaxJurisdictions.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

