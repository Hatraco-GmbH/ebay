# ebaynegotiation.OfferApi

All URIs are relative to *https://api.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_eligible_items**](OfferApi.md#find_eligible_items) | **GET** /find_eligible_items | 
[**send_offer_to_interested_buyers**](OfferApi.md#send_offer_to_interested_buyers) | **POST** /send_offer_to_interested_buyers | 

# **find_eligible_items**
> PagedEligibleItemCollection find_eligible_items(x_ebay_c_marketplace_id, limit=limit, offset=offset)



This method evaluates a seller's current listings and returns the set of IDs that are eligible for a seller-initiated discount offer to a buyer.  <br><br>A listing ID is returned only when one or more buyers have shown an \"interest\" in the listing.  <br><br>If any buyers have shown interest in a listing, the seller can initiate a \"negotiation\" with them by calling <a href=\"/api-docs/sell/negotiation/resources/offer/methods/sendOfferToInterestedBuyers\">sendOfferToInterestedBuyers</a>, which sends all interested buyers a message that offers the listing at a discount.  <br><br>For details about how to create seller offers to buyers, see <a href=\"/api-docs/sell/static/marketing/offers-to-buyers.html\" title=\"Selling Integration Guide\">Sending offers to buyers</a>.

### Example
```python
from __future__ import print_function
import time
import ebaynegotiation
from ebaynegotiation.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaynegotiation.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaynegotiation.OfferApi(ebaynegotiation.ApiClient(configuration))
x_ebay_c_marketplace_id = 'x_ebay_c_marketplace_id_example' # str | The eBay marketplace on which you want to search for eligible listings. <br><br>For a complete list of supported marketplaces, see <a href=\"/api-docs/sell/negotiation/overview.html#requirements\" title=\"Negotiation API Overview\">Negotiation API requirements and restrictions</a>.
limit = 'limit_example' # str | This query parameter specifies the maximum number of items to return from the result set on a page in the paginated response.<br><br><b>Minimum:</b> 1<br><br><b>Maximum:</b> 200<br><br><b>Default: </b>10 (optional)
offset = 'offset_example' # str | This query parameter specifies the number of results to skip in the result set before returning the first result in the paginated response.  <br><br>Combine <b>offset</b> with the <b>limit</b> query parameter to control the items returned in the response. For example, if you supply an <b>offset</b> of <code>0</code> and a <b>limit</b> of <code>10</code>, the first page of the response contains the first 10 results from the complete list of items retrieved by the call. If <b>offset</b> is <code>10</code> and <b>limit</b> is <code>20</code>, the first page of the response contains items 11-30 from the complete result set. <br><br><b>Default:</b> 0 (optional)

try:
    api_response = api_instance.find_eligible_items(x_ebay_c_marketplace_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->find_eligible_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ebay_c_marketplace_id** | **str**| The eBay marketplace on which you want to search for eligible listings. &lt;br&gt;&lt;br&gt;For a complete list of supported marketplaces, see &lt;a href&#x3D;\&quot;/api-docs/sell/negotiation/overview.html#requirements\&quot; title&#x3D;\&quot;Negotiation API Overview\&quot;&gt;Negotiation API requirements and restrictions&lt;/a&gt;. | 
 **limit** | **str**| This query parameter specifies the maximum number of items to return from the result set on a page in the paginated response.&lt;br&gt;&lt;br&gt;&lt;b&gt;Minimum:&lt;/b&gt; 1&lt;br&gt;&lt;br&gt;&lt;b&gt;Maximum:&lt;/b&gt; 200&lt;br&gt;&lt;br&gt;&lt;b&gt;Default: &lt;/b&gt;10 | [optional] 
 **offset** | **str**| This query parameter specifies the number of results to skip in the result set before returning the first result in the paginated response.  &lt;br&gt;&lt;br&gt;Combine &lt;b&gt;offset&lt;/b&gt; with the &lt;b&gt;limit&lt;/b&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;b&gt;offset&lt;/b&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;b&gt;limit&lt;/b&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 results from the complete list of items retrieved by the call. If &lt;b&gt;offset&lt;/b&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;b&gt;limit&lt;/b&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set. &lt;br&gt;&lt;br&gt;&lt;b&gt;Default:&lt;/b&gt; 0 | [optional] 

### Return type

[**PagedEligibleItemCollection**](PagedEligibleItemCollection.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_offer_to_interested_buyers**
> SendOfferToInterestedBuyersCollectionResponse send_offer_to_interested_buyers(x_ebay_c_marketplace_id, content_type, body=body)



This method sends eligible buyers offers to purchase items in a listing at a discount.  <br><br>When a buyer has shown <i>interest</i> in a listing, they become \"eligible\" to receive a seller-initiated offer to purchase the item(s).  <br><br>Sellers use <a href=\"/api-docs/sell/negotiation/resources/offer/methods/findEligibleItems\">findEligibleItems</a> to get the set of listings that have interested buyers. If a listing has interested buyers, sellers can use this method (<b>sendOfferToInterestedBuyers</b>) to send an offer to the buyers who are interested in the listing. The offer gives buyers the ability to purchase the associated listings at a discounted price.  <br><br>For details about how to create seller offers to buyers, see <a href=\"/api-docs/sell/static/marketing/offers-to-buyers.html\" title=\"Selling Integration Guide\">Sending offers to buyers</a>.

### Example
```python
from __future__ import print_function
import time
import ebaynegotiation
from ebaynegotiation.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaynegotiation.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaynegotiation.OfferApi(ebaynegotiation.ApiClient(configuration))
x_ebay_c_marketplace_id = 'x_ebay_c_marketplace_id_example' # str | The eBay marketplace on which your listings with \"eligible\" buyers appear.  <br><br>For a complete list of supported marketplaces, see <a href=\"/api-docs/sell/negotiation/overview.html#requirements\" title=\"Negotiation API Overview\">Negotiation API requirements and restrictions</a>.
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
body = ebaynegotiation.CreateOffersRequest() # CreateOffersRequest | Send offer to eligible items request. (optional)

try:
    api_response = api_instance.send_offer_to_interested_buyers(x_ebay_c_marketplace_id, content_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->send_offer_to_interested_buyers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ebay_c_marketplace_id** | **str**| The eBay marketplace on which your listings with \&quot;eligible\&quot; buyers appear.  &lt;br&gt;&lt;br&gt;For a complete list of supported marketplaces, see &lt;a href&#x3D;\&quot;/api-docs/sell/negotiation/overview.html#requirements\&quot; title&#x3D;\&quot;Negotiation API Overview\&quot;&gt;Negotiation API requirements and restrictions&lt;/a&gt;. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **body** | [**CreateOffersRequest**](CreateOffersRequest.md)| Send offer to eligible items request. | [optional] 

### Return type

[**SendOfferToInterestedBuyersCollectionResponse**](SendOfferToInterestedBuyersCollectionResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

