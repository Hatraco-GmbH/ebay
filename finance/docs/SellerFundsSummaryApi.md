# ebayfinance.SellerFundsSummaryApi

All URIs are relative to *https://apiz.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_seller_funds_summary**](SellerFundsSummaryApi.md#get_seller_funds_summary) | **GET** /seller_funds_summary | 

# **get_seller_funds_summary**
> SellerFundsSummaryResponse get_seller_funds_summary()



This method retrieves all pending funds that have not yet been distibuted through a seller payout. There are no input parameters for this method. The response payload includes available funds, funds being processed, funds on hold, and also an aggregate count of all three of these categories. If there are no funds that are pending, on hold, or being processed for the seller's account, no response payload is returned, and an http status code of 204 - No Content is returned instead.

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

try:
    api_response = api_instance.get_seller_funds_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellerFundsSummaryApi->get_seller_funds_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SellerFundsSummaryResponse**](SellerFundsSummaryResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

