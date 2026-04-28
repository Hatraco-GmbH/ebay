# ebayaccount.AdvertisingEligibilityApi

All URIs are relative to *https://api.ebay.com/sell/account/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_advertising_eligibility**](AdvertisingEligibilityApi.md#get_advertising_eligibility) | **GET** /advertising_eligibility | 


# **get_advertising_eligibility**
> SellerEligibilityMultiProgramResponse get_advertising_eligibility(x_ebay_c_marketplace_id, program_types=program_types)

This method allows developers to check the seller eligibility status for eBay advertising programs.

### Example

* OAuth Authentication (api_auth):

```python
import ebayaccount
from ebayaccount.models.seller_eligibility_multi_program_response import SellerEligibilityMultiProgramResponse
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
    api_instance = ebayaccount.AdvertisingEligibilityApi(api_client)
    x_ebay_c_marketplace_id = 'x_ebay_c_marketplace_id_example' # str | The unique identifier of the eBay marketplace for which the seller eligibility status shall be checked. This header is required or the call will fail.<br><br>See the <a href=\"/api-docs/sell/account/types/ba:MarketplaceIdEnum \" target=\"_blank \">MarketplaceIdEnum</a> type for the supported marketplace ID values.
    program_types = 'program_types_example' # str | A comma-separated list of eBay advertising programs for which eligibility status will be returned.<br><br> See the <a href=\"/api-docs/sell/account/types/plser:AdvertisingProgramEnum\" target=\"_blank\"> AdvertisingProgramEnum</a> type for a list of supported values.<br><br>If no programs are specified, the results will be returned for all programs. (optional)

    try:
        api_response = api_instance.get_advertising_eligibility(x_ebay_c_marketplace_id, program_types=program_types)
        print("The response of AdvertisingEligibilityApi->get_advertising_eligibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvertisingEligibilityApi->get_advertising_eligibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ebay_c_marketplace_id** | **str**| The unique identifier of the eBay marketplace for which the seller eligibility status shall be checked. This header is required or the call will fail.&lt;br&gt;&lt;br&gt;See the &lt;a href&#x3D;\&quot;/api-docs/sell/account/types/ba:MarketplaceIdEnum \&quot; target&#x3D;\&quot;_blank \&quot;&gt;MarketplaceIdEnum&lt;/a&gt; type for the supported marketplace ID values. | 
 **program_types** | **str**| A comma-separated list of eBay advertising programs for which eligibility status will be returned.&lt;br&gt;&lt;br&gt; See the &lt;a href&#x3D;\&quot;/api-docs/sell/account/types/plser:AdvertisingProgramEnum\&quot; target&#x3D;\&quot;_blank\&quot;&gt; AdvertisingProgramEnum&lt;/a&gt; type for a list of supported values.&lt;br&gt;&lt;br&gt;If no programs are specified, the results will be returned for all programs. | [optional] 

### Return type

[**SellerEligibilityMultiProgramResponse**](SellerEligibilityMultiProgramResponse.md)

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

