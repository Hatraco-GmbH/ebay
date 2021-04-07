# ebayanalytics.CustomerservicemetricApi

All URIs are relative to *https://api.ebay.com/sell/analytics/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_service_metric**](CustomerservicemetricApi.md#get_customer_service_metric) | **GET** /customer_service_metric/{customer_service_metric_type}/{evaluation_type} | 


# **get_customer_service_metric**
> GetCustomerServiceMetricResponse get_customer_service_metric(customer_service_metric_type, evaluation_marketplace_id, evaluation_type)



Use this method to retrieve a seller's performance and rating for the customer service metric. Control the response from the getCustomerServiceMetric method using the following path and query parameters: customer_service_metric_type controls the type of customer service transactions evaluated for the metric rating. evaluation_type controls the period you want to review. evaluation_marketplace_id specifies the target marketplace for the evaluation. Currently, metric data is returned for only peer benchmarking. For more detail on the workings of peer benchmarking, see Service metrics policy.

### Example 
```python
import time
import ebayanalytics
from ebayanalytics.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Authorization Code
ebayanalytics.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayanalytics.CustomerservicemetricApi()
customer_service_metric_type = 'customer_service_metric_type_example' # str | Use this path parameter to specify the type of customer service metrics and benchmark data you want returned for the seller. Supported types are: ITEM_NOT_AS_DESCRIBED ITEM_NOT_RECEIVED
evaluation_marketplace_id = 'evaluation_marketplace_id_example' # str | Use this query parameter to specify the Marketplace ID to evaluate for the customer service metrics and benchmark data. For the list of supported marketplaces, see Analytics API requirements and restrictions. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/analytics/types/bas:MarketplaceIdEnum
evaluation_type = 'evaluation_type_example' # str | Use this path parameter to specify the type of the seller evaluation you want returned, either: CURRENT &ndash; A monthly evaluation that occurs on the 20th of every month. PROJECTED &ndash; A daily evaluation that provides a projection of how the seller is currently performing with regards to the upcoming evaluation period.

try: 
    api_response = api_instance.get_customer_service_metric(customer_service_metric_type, evaluation_marketplace_id, evaluation_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CustomerservicemetricApi->get_customer_service_metric: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_service_metric_type** | **str**| Use this path parameter to specify the type of customer service metrics and benchmark data you want returned for the seller. Supported types are: ITEM_NOT_AS_DESCRIBED ITEM_NOT_RECEIVED | 
 **evaluation_marketplace_id** | **str**| Use this query parameter to specify the Marketplace ID to evaluate for the customer service metrics and benchmark data. For the list of supported marketplaces, see Analytics API requirements and restrictions. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/analytics/types/bas:MarketplaceIdEnum | 
 **evaluation_type** | **str**| Use this path parameter to specify the type of the seller evaluation you want returned, either: CURRENT &amp;ndash; A monthly evaluation that occurs on the 20th of every month. PROJECTED &amp;ndash; A daily evaluation that provides a projection of how the seller is currently performing with regards to the upcoming evaluation period. | 

### Return type

[**GetCustomerServiceMetricResponse**](GetCustomerServiceMetricResponse.md)

### Authorization

[Authorization Code](../README.md#Authorization Code)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

