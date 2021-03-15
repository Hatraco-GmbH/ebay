# ebayfinance.TransferApi

All URIs are relative to *https://apiz.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transfer**](TransferApi.md#get_transfer) | **GET** /transfer/{transfer_Id} | 

# **get_transfer**
> Transfer get_transfer(transfer_id)



This method retrieves detailed information regarding a TRANSFER transaction type. A TRANSFER is a monetary transaction type that involves a seller transferring money to eBay for reimbursement of one or more charges. For example, when a seller reimburses eBay for a buyer refund. If an ID is passed into the URI that is an identifier for another transaction type, this call will return an http status code of 404 Not found.

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
api_instance = ebayfinance.TransferApi(ebayfinance.ApiClient(configuration))
transfer_id = 'transfer_id_example' # str | The unique identifier of the TRANSFER transaction type you wish to retrieve.

try:
    api_response = api_instance.get_transfer(transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferApi->get_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **str**| The unique identifier of the TRANSFER transaction type you wish to retrieve. | 

### Return type

[**Transfer**](Transfer.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

