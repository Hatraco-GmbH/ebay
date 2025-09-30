# ebayfinance.SellerFundsSummaryApi

All URIs are relative to *https://apiz.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_seller_funds_summary**](SellerFundsSummaryApi.md#get_seller_funds_summary) | **GET** /seller_funds_summary | 

# **get_seller_funds_summary**
> SellerFundsSummaryResponse get_seller_funds_summary(x_ebay_c_marketplace_id)



<div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span> Due to EU &amp; UK Payments regulatory requirements, an additional security verification via Digital Signatures is required for certain API calls that are made on behalf of EU/UK sellers, including all <b>Finances API</b> methods. Please refer to <a href=\"/develop/guides/digital-signatures-for-apis \" target=\"_blank\">Digital Signatures for APIs</a> to learn more on the impacted APIs and the process to create signatures to be included in the HTTP payload.</p></div><br>This method retrieves all pending funds that have not yet been distibuted through a seller payout.<br><br>There are no input parameters for this method. The response payload includes available funds, funds being processed, funds on hold, and also an aggregate count of all three of these categories.<br><br>If there are no funds that are pending, on hold, or being processed for the seller's account, no response payload is returned, and an http status code of <code>204 - No Content</code> is returned instead.

### Example
```python
from __future__ import print_function
import time
import ebayfinance
from ebayfinance.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayfinance.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayfinance.SellerFundsSummaryApi(ebayfinance.ApiClient(configuration))
x_ebay_c_marketplace_id = 'x_ebay_c_marketplace_id_example' # str | This header identifies the seller's eBay marketplace.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl \" target=\"_blank \">HTTP request headers</a> for the marketplace ID values.<br><br><span class=\"tablenote\"><b>Note:</b> If a marketplace ID value is not provided, the default value of <code>EBAY_US</code> is used.</span>

try:
    api_response = api_instance.get_seller_funds_summary(x_ebay_c_marketplace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellerFundsSummaryApi->get_seller_funds_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ebay_c_marketplace_id** | **str**| This header identifies the seller&#x27;s eBay marketplace.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl \&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt; for the marketplace ID values.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If a marketplace ID value is not provided, the default value of &lt;code&gt;EBAY_US&lt;/code&gt; is used.&lt;/span&gt; | 

### Return type

[**SellerFundsSummaryResponse**](SellerFundsSummaryResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

