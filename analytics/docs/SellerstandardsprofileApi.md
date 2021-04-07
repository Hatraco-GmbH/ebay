# ebayanalytics.SellerstandardsprofileApi

All URIs are relative to *https://api.ebay.com/sell/analytics/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_seller_standards_profiles**](SellerstandardsprofileApi.md#find_seller_standards_profiles) | **GET** /seller_standards_profile | 
[**get_seller_standards_profile**](SellerstandardsprofileApi.md#get_seller_standards_profile) | **GET** /seller_standards_profile/{program}/{cycle} | 


# **find_seller_standards_profiles**
> FindSellerStandardsProfilesResponse find_seller_standards_profiles()



This call retrieves all the standards profiles for the associated seller. A standards profile is a set of eBay seller metrics and the seller's associated compliance values (either TOP_RATED, ABOVE_STANDARD, or BELOW_STANDARD). A seller's multiple profiles are distinguished by two criteria, a &quot;program&quot; and a &quot;cycle.&quot; A profile's program is one of three regions where the seller may have done business, or PROGRAM_GLOBAL to indicate all marketplaces where the seller has done business. The cycle value specifies whether the standards compliance values were determined at the last official eBay evaluation or at the time of the request.

### Example 
```python
import time
import ebayanalytics
from ebayanalytics.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Authorization Code
ebayanalytics.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayanalytics.SellerstandardsprofileApi()

try: 
    api_response = api_instance.find_seller_standards_profiles()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SellerstandardsprofileApi->find_seller_standards_profiles: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FindSellerStandardsProfilesResponse**](FindSellerStandardsProfilesResponse.md)

### Authorization

[Authorization Code](../README.md#Authorization Code)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_standards_profile**
> StandardsProfile get_seller_standards_profile(cycle, program)



This call retrieves a single standards profile for the associated seller. A standards profile is a set of eBay seller metrics and the seller's associated compliance values (either TOP_RATED, ABOVE_STANDARD, or BELOW_STANDARD). A seller can have multiple profiles distinguished by two criteria, a &quot;program&quot; and a &quot;cycle.&quot; A profile's program is one of three regions where the seller may have done business, or PROGRAM_GLOBAL to indicate all marketplaces where the seller has done business. The cycle value specifies whether the standards compliance values were determined at the last official eBay evaluation (CURRENT) or at the time of the request (PROJECTED). Both cycle and a program values are required URI parameters for this method.

### Example 
```python
import time
import ebayanalytics
from ebayanalytics.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Authorization Code
ebayanalytics.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayanalytics.SellerstandardsprofileApi()
cycle = 'cycle_example' # str | The period covered by the returned standards profile evaluation. Supply one of two values, CURRENT means the response reflects eBay's most recent monthly standards evaluation and PROJECTED means the response reflect the seller's projected monthly evaluation, as calculated at the time of the request.
program = 'program_example' # str | This input value specifies the region used to determine the seller's standards profile. Supply one of the four following values, PROGRAM_DE, PROGRAM_UK, PROGRAM_US, or PROGRAM_GLOBAL.

try: 
    api_response = api_instance.get_seller_standards_profile(cycle, program)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SellerstandardsprofileApi->get_seller_standards_profile: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | **str**| The period covered by the returned standards profile evaluation. Supply one of two values, CURRENT means the response reflects eBay&#39;s most recent monthly standards evaluation and PROJECTED means the response reflect the seller&#39;s projected monthly evaluation, as calculated at the time of the request. | 
 **program** | **str**| This input value specifies the region used to determine the seller&#39;s standards profile. Supply one of the four following values, PROGRAM_DE, PROGRAM_UK, PROGRAM_US, or PROGRAM_GLOBAL. | 

### Return type

[**StandardsProfile**](StandardsProfile.md)

### Authorization

[Authorization Code](../README.md#Authorization Code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

