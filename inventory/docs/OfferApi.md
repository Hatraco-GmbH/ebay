# ebayinventory.OfferApi

All URIs are relative to *https://api.ebay.com/sell/inventory/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_offer**](OfferApi.md#bulk_create_offer) | **POST** /bulk_create_offer | 
[**bulk_publish_offer**](OfferApi.md#bulk_publish_offer) | **POST** /bulk_publish_offer | 
[**create_offer**](OfferApi.md#create_offer) | **POST** /offer | 
[**delete_offer**](OfferApi.md#delete_offer) | **DELETE** /offer/{offerId} | 
[**get_listing_fees**](OfferApi.md#get_listing_fees) | **POST** /offer/get_listing_fees | 
[**get_offer**](OfferApi.md#get_offer) | **GET** /offer/{offerId} | 
[**get_offers**](OfferApi.md#get_offers) | **GET** /offer | 
[**publish_offer**](OfferApi.md#publish_offer) | **POST** /offer/{offerId}/publish | 
[**publish_offer_by_inventory_item_group**](OfferApi.md#publish_offer_by_inventory_item_group) | **POST** /offer/publish_by_inventory_item_group | 
[**update_offer**](OfferApi.md#update_offer) | **PUT** /offer/{offerId} | 
[**withdraw_offer**](OfferApi.md#withdraw_offer) | **POST** /offer/{offerId}/withdraw | 
[**withdraw_offer_by_inventory_item_group**](OfferApi.md#withdraw_offer_by_inventory_item_group) | **POST** /offer/withdraw_by_inventory_item_group | 


# **bulk_create_offer**
> BulkOfferResponse bulk_create_offer(content_language, content_type, bulk_ebay_offer_details_with_keys)

This call creates multiple offers (up to 25) for specific inventory items on a specific eBay marketplace. Although it is not a requirement for the seller to create complete offers (with all necessary details) right from the start, eBay recommends that the seller provide all necessary details with this call since there is currently no bulk operation available to update multiple offers with one call. The following fields are always required in the request payload:  <strong>sku</strong>, <strong>marketplaceId</strong>, and (listing) <strong>format</strong>. <br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see <a href="/api-docs/sell/static/inventory/publishing-offers.html#offer" target="_blank">Offer fields</a> for a list of fields required to publish an offer.</p></span></div><br>Other information that will be required before a offer can be published are highlighted below: <ul><li>Inventory location</li> <li>Offer price</li> <li>Available quantity</li> <li>eBay listing category</li> <li>Referenced listing policy profiles to set payment, return, and fulfillment values/settings</li> </ul><p><span class="tablenote"><strong>Note:</strong> Though the <strong>includeCatalogProductDetails</strong> parameter is not required to be submitted in the request, the parameter defaults to <code>true</code> if omitted.</span><br><span class="tablenote"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> and <code>Content-Language</code> headers. See the <a href="/api-docs/sell/inventory/resources/offer/methods/bulkCreateOffer#h3-request-headers">HTTP request headers</a> for more information.</span></p> <p>If the call is successful, unique <strong>offerId</strong> values are returned in the response for each successfully created offer. The <strong>offerId</strong> value will be required for many other offer-related calls. Note that this call only stages an offer for publishing. The seller must run either the <strong>publishOffer</strong>, <strong>bulkPublishOffer</strong>, or <strong>publishOfferByInventoryItemGroup</strong> call to convert offer(s) into an active single- or multiple-variation listing.</p><p>For those who prefer to create a single offer per call, the <strong>createOffer</strong> method can be used instead.</p>

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.bulk_ebay_offer_details_with_keys import BulkEbayOfferDetailsWithKeys
from ebayinventory.models.bulk_offer_response import BulkOfferResponse
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.OfferApi(api_client)
    content_language = 'content_language_example' # str | This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be <code>en-US</code> for English or <code>de-DE</code> for German.<br><br>For more information on the Content-Language header, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    bulk_ebay_offer_details_with_keys = ebayinventory.BulkEbayOfferDetailsWithKeys() # BulkEbayOfferDetailsWithKeys | Details of the offer for the channel

    try:
        api_response = api_instance.bulk_create_offer(content_language, content_type, bulk_ebay_offer_details_with_keys)
        print("The response of OfferApi->bulk_create_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->bulk_create_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_language** | **str**| This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be &lt;code&gt;en-US&lt;/code&gt; for English or &lt;code&gt;de-DE&lt;/code&gt; for German.&lt;br&gt;&lt;br&gt;For more information on the Content-Language header, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **bulk_ebay_offer_details_with_keys** | [**BulkEbayOfferDetailsWithKeys**](BulkEbayOfferDetailsWithKeys.md)| Details of the offer for the channel | 

### Return type

[**BulkOfferResponse**](BulkOfferResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**207** | Multi-Status |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_publish_offer**
> BulkPublishResponse bulk_publish_offer(content_type, bulk_offer)

<span class="tablenote"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.</span><br>This call is used to convert unpublished offers (up to 25) into  published offers, or live eBay listings. The unique identifier (<strong>offerId</strong>) of each offer to publish is passed into the request payload. It is possible that some unpublished offers will be successfully created into eBay listings, but others may fail. The response payload will show the results for each <strong>offerId</strong> value that is passed into the request payload. The <strong>errors</strong> and <strong>warnings</strong> containers will be returned for an offer that had one or more issues being published. <br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>Publish offer note: Fields may be optional or conditionally required when calling the create or update methods, but become required when publishing the offer to create active listings. For this method, see <a href="/api-docs/sell/static/inventory/publishing-offers.html#offer" target="_blank">Offer fields</a> for a list of fields required to publish an offer.</p></span></div><br>For those who prefer to publish one offer per call, the <strong>publishOffer</strong> method can be used instead. In the case of a multiple-variation listing, the <strong>publishOfferByInventoryItemGroup</strong> call should be used instead, as this call will convert all unpublished offers associated with an inventory item group into a multiple-variation listing.

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.bulk_offer import BulkOffer
from ebayinventory.models.bulk_publish_response import BulkPublishResponse
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.OfferApi(api_client)
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    bulk_offer = ebayinventory.BulkOffer() # BulkOffer | The base request of the <strong>bulkPublishOffer</strong> method.

    try:
        api_response = api_instance.bulk_publish_offer(content_type, bulk_offer)
        print("The response of OfferApi->bulk_publish_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->bulk_publish_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **bulk_offer** | [**BulkOffer**](BulkOffer.md)| The base request of the &lt;strong&gt;bulkPublishOffer&lt;/strong&gt; method. | 

### Return type

[**BulkPublishResponse**](BulkPublishResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**207** | Multi-Status |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_offer**
> OfferResponse create_offer(content_language, content_type, ebay_offer_details_with_keys)

This call creates an offer for a specific inventory item on a specific eBay marketplace. It is up to the sellers whether they want to create a complete offer (with all necessary details) right from the start, or sellers can provide only some information with the initial <strong>createOffer</strong> call, and then make one or more subsequent <strong>updateOffer</strong> calls to complete the offer and prepare to publish the offer. Upon first creating an offer, the following fields are required in the request payload:  <strong>sku</strong>, <strong>marketplaceId</strong>, and (listing) <strong>format</strong>.<br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see <a href="/api-docs/sell/static/inventory/publishing-offers.html#offer" target="_blank">Offer fields</a> for a list of fields required to publish an offer.</p></span></div><br>Other information that will be required before an offer can be published are highlighted below. These settings are either set with <strong>createOffer</strong>, or they can be set with a subsequent <strong>updateOffer</strong> call: <ul><li>Inventory location</li> <li>Offer price</li> <li>Available quantity</li> <li>eBay listing category</li> <li>Referenced listing policy profiles to set payment, return, and fulfillment values/settings</li> </ul> <p><span class="tablenote"><strong>Note:</strong> Though the <strong>includeCatalogProductDetails</strong> parameter is not required to be submitted in the request, the parameter defaults to <code>true</code> if omitted.</span></p><span class="tablenote"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> and <code>Content-Language</code> headers. See the <a href="/api-docs/sell/inventory/resources/offer/methods/createOffer#h3-request-headers">HTTP request headers</a> for more information.</span><p>If the call is successful, a unique <strong>offerId</strong> value is returned in the response. This value will be required for many other offer-related calls. Note that this call only stages an offer for publishing. The seller must run the <strong>publishOffer</strong> call to convert the offer to an active eBay listing.</p><p>For those who prefer to create multiple offers (up to 25 at a time) with one call, the <strong>bulkCreateOffer</strong> method can be used.</p>

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.ebay_offer_details_with_keys import EbayOfferDetailsWithKeys
from ebayinventory.models.offer_response import OfferResponse
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.OfferApi(api_client)
    content_language = 'content_language_example' # str | This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be <code>en-US</code> for English or <code>de-DE</code> for German.<br><br>For more information on the Content-Language header, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    ebay_offer_details_with_keys = ebayinventory.EbayOfferDetailsWithKeys() # EbayOfferDetailsWithKeys | Details of the offer for the channel

    try:
        api_response = api_instance.create_offer(content_language, content_type, ebay_offer_details_with_keys)
        print("The response of OfferApi->create_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->create_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_language** | **str**| This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be &lt;code&gt;en-US&lt;/code&gt; for English or &lt;code&gt;de-DE&lt;/code&gt; for German.&lt;br&gt;&lt;br&gt;For more information on the Content-Language header, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **ebay_offer_details_with_keys** | [**EbayOfferDetailsWithKeys**](EbayOfferDetailsWithKeys.md)| Details of the offer for the channel | 

### Return type

[**OfferResponse**](OfferResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Content-Language -  <br>  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_offer**
> delete_offer(offer_id)

If used against an unpublished offer, this call will permanently delete that offer. In the case of a published offer (or live eBay listing), a successful call will either end the single-variation listing associated with the offer, or it will remove that product variation from the eBay listing and also automatically remove that product variation from the inventory item group. In the case of a multiple-variation listing, the <strong>deleteOffer</strong> will not remove the product variation from the listing if that variation has one or more sales. If that product variation has one or more sales, the seller can alternately just set the available quantity of that product variation to <code>0</code>, so it is not available in the eBay search or View Item page, and then the seller can remove that product variation from the inventory item group at a later time.

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.OfferApi(api_client)
    offer_id = 'offer_id_example' # str | This path parameter specifies the unique identifier of the offer being deleted.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffers\">getOffers</a> method to retrieve offer IDs.

    try:
        api_instance.delete_offer(offer_id)
    except Exception as e:
        print("Exception when calling OfferApi->delete_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| This path parameter specifies the unique identifier of the offer being deleted.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/offer/methods/getOffers\&quot;&gt;getOffers&lt;/a&gt; method to retrieve offer IDs. | 

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_fees**
> FeesSummaryResponse get_listing_fees(content_type, offer_keys_with_id=offer_keys_with_id)

This call is used to retrieve the expected listing fees for up to 250 unpublished offers. An array of one or more <strong>offerId</strong> values are passed in under the <strong>offers</strong> container.<br><br>In the response payload, all listing fees are grouped by eBay marketplace, and listing fees per offer are not shown. A <strong>fees</strong> container will be returned for each eBay marketplace where the seller is selling the products associated with the specified offers. <br><br>Errors will occur if the seller passes in <strong>offerIds</strong> that represent published offers, so this call should be made before the seller publishes offers with the <strong>publishOffer</strong>.

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.fees_summary_response import FeesSummaryResponse
from ebayinventory.models.offer_keys_with_id import OfferKeysWithId
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.OfferApi(api_client)
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    offer_keys_with_id = ebayinventory.OfferKeysWithId() # OfferKeysWithId | List of offers that needs fee information (optional)

    try:
        api_response = api_instance.get_listing_fees(content_type, offer_keys_with_id=offer_keys_with_id)
        print("The response of OfferApi->get_listing_fees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->get_listing_fees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **offer_keys_with_id** | [**OfferKeysWithId**](OfferKeysWithId.md)| List of offers that needs fee information | [optional] 

### Return type

[**FeesSummaryResponse**](FeesSummaryResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer**
> EbayOfferDetailsWithAll get_offer(offer_id)

This call retrieves a specific published or unpublished offer. The unique identifier of the offer (<strong>offerId</strong>) is passed in at the end of the call URI.<p>The <code>authorization</code> header is the only required HTTP header for this call. See the <strong>HTTP request headers</strong> section for more information.</p>

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.ebay_offer_details_with_all import EbayOfferDetailsWithAll
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.OfferApi(api_client)
    offer_id = 'offer_id_example' # str | This path parameter specifies the unique identifier of the offer that is to be retrieved.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffers\">getOffers</a> method to retrieve offer IDs.

    try:
        api_response = api_instance.get_offer(offer_id)
        print("The response of OfferApi->get_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->get_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| This path parameter specifies the unique identifier of the offer that is to be retrieved.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/offer/methods/getOffers\&quot;&gt;getOffers&lt;/a&gt; method to retrieve offer IDs. | 

### Return type

[**EbayOfferDetailsWithAll**](EbayOfferDetailsWithAll.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offers**
> Offers get_offers(format=format, limit=limit, marketplace_id=marketplace_id, offset=offset, sku=sku)

This call retrieves all existing offers for the specified SKU value. The seller has the option of limiting the offers that are retrieved to a specific eBay marketplace, or to a listing format.<br><br><span class="tablenote"><strong>Note:</strong> At this time, the same SKU value can not be offered across multiple eBay marketplaces, so the <strong>marketplace_id</strong> query parameter currently does not have any practical use for this call.</span><br><span class="tablenote"><strong>Note:</strong> The same SKU can be offered through an auction and a fixed-price listing concurrently. If this is the case, <b>getOffers</b> will return two offers. Otherwise, only one offer will be returned.</span><br>The <code>authorization</code> header is the only required HTTP header for this call. See the <strong>HTTP request headers</strong> section for more information.

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.offers import Offers
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.OfferApi(api_client)
    format = 'format_example' # str | This enumeration value sets the listing format for the offers being retrieved. This query parameter will be passed in if the seller only wants to see offers in a specified listing format, such as <code>FIXED_PRICE</code>. (optional)
    limit = 'limit_example' # str | The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be a positive integer value. If this query parameter is not set, up to 100 records will be returned on each page of results. (optional)
    marketplace_id = 'marketplace_id_example' # str | The unique identifier of the eBay marketplace. This query parameter will be passed in if the seller only wants to see the product's offers on a specific eBay marketplace.<br><br><span class=\"tablenote\"><strong>Note:</strong> At this time, the same SKU value can not be offered across multiple eBay marketplaces, so the <strong>marketplace_id</strong> query parameter currently does not have any practical use for this call.</span> (optional)
    offset = 'offset_example' # str | The value passed in this query parameter sets the page number to retrieve. Although this field is a string, the value passed in this field should be a integer value equal to or greater than <code>0</code>. The first page of records has a value of <code>0</code>, the second page of records has a value of <code>1</code>, and so on. If this query parameter is not set, its value defaults to <code>0</code>, and the first page of records is returned. (optional)
    sku = 'sku_example' # str | The seller-defined SKU value is passed in as a query parameter. All offers associated with this product are returned in the response. <br><br><span class=\"tablenote\"><strong>Note:</strong> The same SKU can be offered through an auction and a fixed-price listing concurrently. If this is the case, <b>getOffers</b> will return two offers. Otherwise, only one offer will be returned.</span><br>Use the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\">getInventoryItems</a> method to retrieve SKU values.<br><br><strong>Max length</strong>: 50. (optional)

    try:
        api_response = api_instance.get_offers(format=format, limit=limit, marketplace_id=marketplace_id, offset=offset, sku=sku)
        print("The response of OfferApi->get_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->get_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| This enumeration value sets the listing format for the offers being retrieved. This query parameter will be passed in if the seller only wants to see offers in a specified listing format, such as &lt;code&gt;FIXED_PRICE&lt;/code&gt;. | [optional] 
 **limit** | **str**| The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be a positive integer value. If this query parameter is not set, up to 100 records will be returned on each page of results. | [optional] 
 **marketplace_id** | **str**| The unique identifier of the eBay marketplace. This query parameter will be passed in if the seller only wants to see the product&#39;s offers on a specific eBay marketplace.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; At this time, the same SKU value can not be offered across multiple eBay marketplaces, so the &lt;strong&gt;marketplace_id&lt;/strong&gt; query parameter currently does not have any practical use for this call.&lt;/span&gt; | [optional] 
 **offset** | **str**| The value passed in this query parameter sets the page number to retrieve. Although this field is a string, the value passed in this field should be a integer value equal to or greater than &lt;code&gt;0&lt;/code&gt;. The first page of records has a value of &lt;code&gt;0&lt;/code&gt;, the second page of records has a value of &lt;code&gt;1&lt;/code&gt;, and so on. If this query parameter is not set, its value defaults to &lt;code&gt;0&lt;/code&gt;, and the first page of records is returned. | [optional] 
 **sku** | **str**| The seller-defined SKU value is passed in as a query parameter. All offers associated with this product are returned in the response. &lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The same SKU can be offered through an auction and a fixed-price listing concurrently. If this is the case, &lt;b&gt;getOffers&lt;/b&gt; will return two offers. Otherwise, only one offer will be returned.&lt;/span&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\&quot;&gt;getInventoryItems&lt;/a&gt; method to retrieve SKU values.&lt;br&gt;&lt;br&gt;&lt;strong&gt;Max length&lt;/strong&gt;: 50. | [optional] 

### Return type

[**Offers**](Offers.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_offer**
> PublishResponse publish_offer(offer_id)

<span class="tablenote"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.</span><br>This call is used to convert an unpublished offer into a published offer, or live eBay listing. The unique identifier of the offer (<strong>offerId</strong>) is passed in at the end of the call URI.<br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>Publish offer note: Fields may be optional or conditionally required when calling the create or update methods, but become required when publishing the offer to create active listings. For this method, see <a href="/api-docs/sell/static/inventory/publishing-offers.html#offer" target="_blank">Offer fields</a> for a list of fields required to publish an offer.</p></span></div><br>For those who prefer to publish multiple offers (up to 25 at a time) with one call, the <strong>bulkPublishOffer</strong> method can be used. In the case of a multiple-variation listing, the <strong>publishOfferByInventoryItemGroup</strong> call should be used instead, as this call will convert all unpublished offers associated with an inventory item group into a multiple-variation listing.

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.publish_response import PublishResponse
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.OfferApi(api_client)
    offer_id = 'offer_id_example' # str | This path parameter specifies the unique identifier of the offer that is to be published.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffers\">getOffers</a> method to retrieve offer IDs.

    try:
        api_response = api_instance.publish_offer(offer_id)
        print("The response of OfferApi->publish_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->publish_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| This path parameter specifies the unique identifier of the offer that is to be published.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/offer/methods/getOffers\&quot;&gt;getOffers&lt;/a&gt; method to retrieve offer IDs. | 

### Return type

[**PublishResponse**](PublishResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_offer_by_inventory_item_group**
> PublishResponse publish_offer_by_inventory_item_group(content_type, publish_by_inventory_item_group_request)

<span class="tablenote"><strong>Note:</strong> Please note that any eBay listing created using the Inventory API cannot be revised or relisted using the Trading API calls.</span><br><span class="tablenote"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.</span><br>This call is used to convert all unpublished offers associated with an inventory item group into an active, multiple-variation listing.<br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>Publish offer note: Fields may be optional or conditionally required when calling the create or update methods, but become required when publishing the offer to create active listings. For this method, see <a href="/api-docs/sell/static/inventory/publishing-offers.html#offer" target="_blank">Offer fields</a> for a list of fields required to publish an offer.</p></span></div><br>The unique identifier of the inventory item group (<strong>inventoryItemGroupKey</strong>) is passed in the request payload. All inventory items and their corresponding offers in the inventory item group must be valid (meet all requirements) for the <strong>publishOfferByInventoryItemGroup</strong> call to be completely successful. For any inventory items in the group that are missing required data or have no corresponding offers, the <strong>publishOfferByInventoryItemGroup</strong> will create a new multiple-variation listing, but any inventory items with missing required data/offers will not be in the newly-created listing. If any inventory items in the group to be published have invalid data, or one or more of the inventory items have conflicting data with one another, the <strong>publishOfferByInventoryItemGroup</strong> call will fail. Be sure to check for any error or warning messages in the call response for any applicable information about one or more inventory items/offers having issues.

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.publish_by_inventory_item_group_request import PublishByInventoryItemGroupRequest
from ebayinventory.models.publish_response import PublishResponse
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.OfferApi(api_client)
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    publish_by_inventory_item_group_request = ebayinventory.PublishByInventoryItemGroupRequest() # PublishByInventoryItemGroupRequest | The identifier of the inventory item group to publish and the eBay marketplace where the listing will be published is needed in the request payload.

    try:
        api_response = api_instance.publish_offer_by_inventory_item_group(content_type, publish_by_inventory_item_group_request)
        print("The response of OfferApi->publish_offer_by_inventory_item_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->publish_offer_by_inventory_item_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **publish_by_inventory_item_group_request** | [**PublishByInventoryItemGroupRequest**](PublishByInventoryItemGroupRequest.md)| The identifier of the inventory item group to publish and the eBay marketplace where the listing will be published is needed in the request payload. | 

### Return type

[**PublishResponse**](PublishResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_offer**
> OfferResponse update_offer(content_language, offer_id, content_type, ebay_offer_details_with_id)

This call updates an existing offer. An existing offer may be in published state (active eBay listing), or in an unpublished state and yet to be published with the <strong>publishOffer</strong> call. The unique identifier (<strong>offerId</strong>) for the offer to update is passed in at the end of the call URI. <br><br>The <strong>updateOffer</strong> call does a complete replacement of the existing offer object, so all fields that make up the current offer object are required, regardless of whether their values changed. <br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see <a href="/api-docs/sell/static/inventory/publishing-offers.html#offer" target="_blank">Offer fields</a> for a list of fields required to publish an offer.</p></span></div><br>Other information that is required before an unpublished offer can be published or before a published offer can be revised include: <ul><li>Inventory location</li> <li>Offer price</li> <li>Available quantity</li> <li>eBay listing category</li>  <li>Referenced listing policy profiles to set payment, return, and fulfillment values/settings</li> </ul> <p><span class="tablenote"><strong>Note:</strong> Though the <strong>includeCatalogProductDetails</strong> parameter is not required to be submitted in the request, the parameter defaults to <code>true</code> if omitted from both the <strong>updateOffer</strong> and the <strong>createOffer</strong> calls. If a value is specified in the <strong>updateOffer</strong> call, this value will be used.</span><br><span class="tablenote"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> and <code>Content-Language</code> headers. See the <a href="/api-docs/sell/inventory/resources/offer/methods/updateOffer#h3-request-headers">HTTP request headers</a> for more information.</span><br><span class="tablenote"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.</span></p> <p>For published offers, the <strong>listingDescription</strong> field is also required to update the offer/eBay listing. For unpublished offers, this field is not necessarily required unless it is already set for the unpublished offer.</p>

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.ebay_offer_details_with_id import EbayOfferDetailsWithId
from ebayinventory.models.offer_response import OfferResponse
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.OfferApi(api_client)
    content_language = 'content_language_example' # str | This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be <code>en-US</code> for English or <code>de-DE</code> for German.<br><br>For more information on the Content-Language header, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    offer_id = 'offer_id_example' # str | This path parameter specifies the unique identifier of the offer being updated.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffers\">getOffers</a> method to retrieve offer IDs.
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    ebay_offer_details_with_id = ebayinventory.EbayOfferDetailsWithId() # EbayOfferDetailsWithId | Details of the offer for the channel

    try:
        api_response = api_instance.update_offer(content_language, offer_id, content_type, ebay_offer_details_with_id)
        print("The response of OfferApi->update_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->update_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_language** | **str**| This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be &lt;code&gt;en-US&lt;/code&gt; for English or &lt;code&gt;de-DE&lt;/code&gt; for German.&lt;br&gt;&lt;br&gt;For more information on the Content-Language header, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **offer_id** | **str**| This path parameter specifies the unique identifier of the offer being updated.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/offer/methods/getOffers\&quot;&gt;getOffers&lt;/a&gt; method to retrieve offer IDs. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **ebay_offer_details_with_id** | [**EbayOfferDetailsWithId**](EbayOfferDetailsWithId.md)| Details of the offer for the channel | 

### Return type

[**OfferResponse**](OfferResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Content-Language -  <br>  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_offer**
> WithdrawResponse withdraw_offer(offer_id)

This call is used to end a single-variation listing that is associated with the specified offer. This call is used in place of the <strong>deleteOffer</strong> call if the seller only wants to end the listing associated with the offer but does not want to delete the offer object. With this call, the offer object remains, but it goes into the unpublished state, and will require a <strong>publishOffer</strong> call to relist the offer.<br><br>To end a multiple-variation listing that is associated with an inventory item group, the <strong>withdrawOfferByInventoryItemGroup</strong> method can be used. This call only ends the multiple-variation listing associated with an inventory item group but does not delete the inventory item group object, nor does it delete any of the offers associated with the inventory item group, but instead all of these offers go into the unpublished state.

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.withdraw_response import WithdrawResponse
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.OfferApi(api_client)
    offer_id = 'offer_id_example' # str | This path parameter specifies the unique identifier of the offer that is to be withdrawn.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffers\">getOffers</a> method to retrieve offer IDs.

    try:
        api_response = api_instance.withdraw_offer(offer_id)
        print("The response of OfferApi->withdraw_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->withdraw_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| This path parameter specifies the unique identifier of the offer that is to be withdrawn.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/offer/methods/getOffers\&quot;&gt;getOffers&lt;/a&gt; method to retrieve offer IDs. | 

### Return type

[**WithdrawResponse**](WithdrawResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_offer_by_inventory_item_group**
> withdraw_offer_by_inventory_item_group(content_type, withdraw_by_inventory_item_group_request)

This call is used to end a multiple-variation eBay listing that is associated with the specified inventory item group. This call only ends multiple-variation eBay listing associated with the inventory item group but does not delete the inventory item group object. Similarly, this call also does not delete any of the offers associated with the inventory item group, but instead all of these offers go into the unpublished state. If the seller wanted to relist the multiple-variation eBay listing, they could use the <strong>publishOfferByInventoryItemGroup</strong> method.

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.withdraw_by_inventory_item_group_request import WithdrawByInventoryItemGroupRequest
from ebayinventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ebayinventory.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebayinventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebayinventory.OfferApi(api_client)
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    withdraw_by_inventory_item_group_request = ebayinventory.WithdrawByInventoryItemGroupRequest() # WithdrawByInventoryItemGroupRequest | The base request of the <strong>withdrawOfferByInventoryItemGroup</strong> call.

    try:
        api_instance.withdraw_offer_by_inventory_item_group(content_type, withdraw_by_inventory_item_group_request)
    except Exception as e:
        print("Exception when calling OfferApi->withdraw_offer_by_inventory_item_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **withdraw_by_inventory_item_group_request** | [**WithdrawByInventoryItemGroupRequest**](WithdrawByInventoryItemGroupRequest.md)| The base request of the &lt;strong&gt;withdrawOfferByInventoryItemGroup&lt;/strong&gt; call. | 

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

