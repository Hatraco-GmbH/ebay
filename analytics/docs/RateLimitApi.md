# ebayanalytics.RateLimitApi

All URIs are relative to *https://api.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rate_limits**](RateLimitApi.md#get_rate_limits) | **GET** /rate_limit/ | 

# **get_rate_limits**
> RateLimitsResponse get_rate_limits(api_context=api_context, api_name=api_name)



This method retrieves the call limit and utilization data for an application. The data is retrieved for all RESTful APIs and the legacy Trading API.  <br><br>The response from <b>getRateLimits</b> includes a list of the applicable resources and the \"call limit\", or quota, that is set for each resource. In addition to quota information, the response also includes the number of remaining calls available before the limit is reached, the time remaining before the quota resets, the number of calls made to the specific resource, and the length of the \"time window\" to which the quota applies.  <br><br>By default, this method returns utilization data for all RESTful API and the legacy Trading API resources. Use the <b>api_name</b> and <b>api_context</b> query parameters to filter the response to only the desired APIs.  <br><br>For more on call limits, see <a href=\"https://developer.ebay.com/support/app-check \" target=\"_blank\">Application Growth Check</a>.

### Example
```python
from __future__ import print_function
import time
import ebayanalytics
from ebayanalytics.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayanalytics.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayanalytics.RateLimitApi(ebayanalytics.ApiClient(configuration))
api_context = 'api_context_example' # str | This optional query parameter filters the result to include only the specified API context. <br><br><b>Valid values:</b> <ul><li><code>buy</code></li><li><code>sell</code></li> <li><code>commerce</code></li><li><code>developer</code></li><li><code>tradingapi</code></li></ul> (optional)
api_name = 'api_name_example' # str | This optional query parameter filters the result to include only the APIs specified. <br><br><b>Example values:</b> <ul> <li><code>browse</code> for the <a href=\"/../develop/apis/restful-apis/buy-apis#buy-apis\" target=\"_blank\">Buy APIs</a></li> <li><code>inventory</code> for the <a href=\"/../develop/apis/restful-apis/sell-apis#sell-apis\" target=\"_blank\">Sell APIs</a></li>  <li><code>taxonomy</code> for the <a href=\"/../develop/apis/restful-apis/commerce-apis#commerce-apis\" target=\"_blank\">Commerce APIs</a></li>  <li><code>tradingapi</code> for the <a href=\"/../Devzone/XML/docs/Reference/eBay/index.html\" target=\"_blank\">Trading APIs</a></li></ul> (optional)

try:
    api_response = api_instance.get_rate_limits(api_context=api_context, api_name=api_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RateLimitApi->get_rate_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_context** | **str**| This optional query parameter filters the result to include only the specified API context. &lt;br&gt;&lt;br&gt;&lt;b&gt;Valid values:&lt;/b&gt; &lt;ul&gt;&lt;li&gt;&lt;code&gt;buy&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;sell&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;commerce&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;developer&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;tradingapi&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 
 **api_name** | **str**| This optional query parameter filters the result to include only the APIs specified. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example values:&lt;/b&gt; &lt;ul&gt; &lt;li&gt;&lt;code&gt;browse&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../develop/apis/restful-apis/buy-apis#buy-apis\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Buy APIs&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;inventory&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../develop/apis/restful-apis/sell-apis#sell-apis\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Sell APIs&lt;/a&gt;&lt;/li&gt;  &lt;li&gt;&lt;code&gt;taxonomy&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../develop/apis/restful-apis/commerce-apis#commerce-apis\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Commerce APIs&lt;/a&gt;&lt;/li&gt;  &lt;li&gt;&lt;code&gt;tradingapi&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../Devzone/XML/docs/Reference/eBay/index.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Trading APIs&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**RateLimitsResponse**](RateLimitsResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

