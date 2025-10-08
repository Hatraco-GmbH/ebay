# ebayfinance.TransferApi

All URIs are relative to *https://apiz.ebay.com/sell/finances/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transfer**](TransferApi.md#get_transfer) | **GET** /transfer/{transfer_Id} | 


# **get_transfer**
> Transfer get_transfer(x_ebay_c_marketplace_id, transfer_id)

<div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> Due to EU &amp; UK Payments regulatory requirements, an additional security verification via Digital Signatures is required for certain API calls that are made on behalf of EU/UK sellers, including all <b>Finances API</b> methods. Please refer to <a href="/develop/guides/digital-signatures-for-apis " target="_blank">Digital Signatures for APIs</a> to learn more on the impacted APIs and the process to create signatures to be included in the HTTP payload.</p></div><br>This method retrieves detailed information regarding a <code>TRANSFER</code> transaction type. A <code>TRANSFER</code> is a  monetary transaction type that involves a seller transferring money to eBay for reimbursement of one or more charges. For example, when a seller reimburses eBay for a buyer refund.<br><br>If an ID is passed into the URI that is an identifier for another transaction type, this call will return an http status code of <code>404 Not found</code>.

### Example

* OAuth Authentication (api_auth):

```python
import ebayfinance
from ebayfinance.models.transfer import Transfer
from ebayfinance.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apiz.ebay.com/sell/finances/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayfinance.Configuration(
    host = "https://apiz.ebay.com/sell/finances/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayfinance.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayfinance.TransferApi(api_client)
    x_ebay_c_marketplace_id = 'x_ebay_c_marketplace_id_example' # str | This header identifies the seller's eBay marketplace.<br><br>See <a href=\"/api-docs/static/rest-request-components.html#marketpl \" target=\"_blank \">HTTP request headers</a> for the marketplace ID values.<br><br><span class=\"tablenote\"><b>Note:</b> If a marketplace ID value is not provided, the default value of <code>EBAY_US</code> is used.</span>
    transfer_id = 'transfer_id_example' # str | This path parameter is used to specify the unique identifier of the <code>TRANSFER</code> transaction type you wish to retrieve.<br><br>Use the <a href=\"/api-docs/sell/finances/resources/transaction/methods/getTransactions\" target=\"_blank \">getTransactions</a> method to retrieve this value by setting the <b>transactionType</b> filter to <code>TRANSFER</code>. The <b>transfer_id</b> value will then be returned in the <b>transaction_id</b> field of the response.

    try:
        api_response = api_instance.get_transfer(x_ebay_c_marketplace_id, transfer_id)
        print("The response of TransferApi->get_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferApi->get_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ebay_c_marketplace_id** | **str**| This header identifies the seller&#39;s eBay marketplace.&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl \&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt; for the marketplace ID values.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If a marketplace ID value is not provided, the default value of &lt;code&gt;EBAY_US&lt;/code&gt; is used.&lt;/span&gt; | 
 **transfer_id** | **str**| This path parameter is used to specify the unique identifier of the &lt;code&gt;TRANSFER&lt;/code&gt; transaction type you wish to retrieve.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/finances/resources/transaction/methods/getTransactions\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getTransactions&lt;/a&gt; method to retrieve this value by setting the &lt;b&gt;transactionType&lt;/b&gt; filter to &lt;code&gt;TRANSFER&lt;/code&gt;. The &lt;b&gt;transfer_id&lt;/b&gt; value will then be returned in the &lt;b&gt;transaction_id&lt;/b&gt; field of the response. | 

### Return type

[**Transfer**](Transfer.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad Request |  -  |
**404** | Not found. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

