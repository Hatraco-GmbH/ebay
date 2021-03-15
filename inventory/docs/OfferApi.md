# ebayinventory.OfferApi

All URIs are relative to *https://api.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_offer**](OfferApi.md#bulk_create_offer) | **POST** /bulk_create_offer | 
[**bulk_publish_offer**](OfferApi.md#bulk_publish_offer) | **POST** /bulk_publish_offer | 
[**create_offer**](OfferApi.md#create_offer) | **POST** /offer | 
[**delete_offer**](OfferApi.md#delete_offer) | **DELETE** /offer/{offerId} | 
[**get_listing_fees**](OfferApi.md#get_listing_fees) | **POST** /offer/get_listing_fees | 
[**get_offer**](OfferApi.md#get_offer) | **GET** /offer/{offerId} | 
[**get_offers**](OfferApi.md#get_offers) | **GET** /offer | 
[**publish_offer**](OfferApi.md#publish_offer) | **POST** /offer/{offerId}/publish/ | 
[**publish_offer_by_inventory_item_group**](OfferApi.md#publish_offer_by_inventory_item_group) | **POST** /offer/publish_by_inventory_item_group/ | 
[**update_offer**](OfferApi.md#update_offer) | **PUT** /offer/{offerId} | 
[**withdraw_offer**](OfferApi.md#withdraw_offer) | **POST** /offer/{offerId}/withdraw | 
[**withdraw_offer_by_inventory_item_group**](OfferApi.md#withdraw_offer_by_inventory_item_group) | **POST** /offer/withdraw_by_inventory_item_group | 

# **bulk_create_offer**
> BulkOfferResponse bulk_create_offer(body)



This call creates multiple offers (up to 25) for specific inventory items on a specific eBay marketplace. Although it is not a requirement for the seller to create complete offers (with all necessary details) right from the start, eBay recommends that the seller provide all necessary details with this call since there is currently no bulk operation available to update multiple offers with one call. The following fields are always required in the request payload: sku, marketplaceId, and (listing) format. Other information that will be required before a offer can be published are highlighted below: Inventory location Offer price Available quantity eBay listing category Referenced listing policy profiles to set payment, return, and fulfillment values/settings Note: Though the includeCatalogProductDetails parameter is not required to be submitted in the request, the parameter defaults to true if omitted. If the call is successful, unique offerId values are returned in the response for each successfully created offer. The offerId value will be required for many other offer-related calls. Note that this call only stages an offer for publishing. The seller must run either the publishOffer, bulkPublishOffer, or publishOfferByInventoryItemGroup call to convert offer(s) into an active single- or multiple-variation listing. In addition to the authorization header, which is required for all eBay REST API calls, the bulkCreateOffer call also requires the Content-Language header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be en-US. To view other supported Content-Language values, and to read more about all supported HTTP headers for eBay REST API calls, see the HTTP request headers topic in the Using eBay RESTful APIs document. For those who prefer to create a single offer per call, the createOffer method can be used instead.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.OfferApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.BulkEbayOfferDetailsWithKeys() # BulkEbayOfferDetailsWithKeys | Details of the offer for the channel

try:
    api_response = api_instance.bulk_create_offer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->bulk_create_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkEbayOfferDetailsWithKeys**](BulkEbayOfferDetailsWithKeys.md)| Details of the offer for the channel | 

### Return type

[**BulkOfferResponse**](BulkOfferResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_publish_offer**
> BulkPublishResponse bulk_publish_offer(body)



This call is used to convert unpublished offers (up to 25) into published offers, or live eBay listings. The unique identifier (offerId) of each offer to publlish is passed into the request payload. It is possible that some unpublished offers will be successfully created into eBay listings, but others may fail. The response payload will show the results for each offerId value that is passed into the request payload. The errors and warnings containers will be returned for an offer that had one or more issues being published. For those who prefer to publish one offer per call, the publishOffer method can be used instead. In the case of a multiple-variation listing, the publishOfferByInventoryItemGroup call should be used instead, as this call will convert all unpublished offers associated with an inventory item group into a multiple-variation listing.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.OfferApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.BulkOffer() # BulkOffer | The base request of the bulkPublishOffer method.

try:
    api_response = api_instance.bulk_publish_offer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->bulk_publish_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkOffer**](BulkOffer.md)| The base request of the bulkPublishOffer method. | 

### Return type

[**BulkPublishResponse**](BulkPublishResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_offer**
> OfferResponse create_offer(body, content_language)



This call creates an offer for a specific inventory item on a specific eBay marketplace. It is up to the sellers whether they want to create a complete offer (with all necessary details) right from the start, or sellers can provide only some information with the initial createOffer call, and then make one or more subsequent updateOffer calls to complete the offer and prepare to publish the offer. Upon first creating an offer, the following fields are required in the request payload: sku, marketplaceId, and (listing) format. Other information that will be required before an offer can be published are highlighted below. These settings are either set with createOffer, or they can be set with a subsequent updateOffer call: Inventory location Offer price Available quantity eBay listing category Referenced listing policy profiles to set payment, return, and fulfillment values/settings Note: Though the includeCatalogProductDetails parameter is not required to be submitted in the request, the parameter defaults to true if omitted. If the call is successful, a unique offerId value is returned in the response. This value will be required for many other offer-related calls. Note that this call only stages an offer for publishing. The seller must run the publishOffer call to convert the offer to an active eBay listing. In addition to the authorization header, which is required for all eBay REST API calls, the createOffer call also requires the Content-Language header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be en-US. To view other supported Content-Language values, and to read more about all supported HTTP headers for eBay REST API calls, see the HTTP request headers topic in the Using eBay RESTful APIs document. For those who prefer to create multiple offers (up to 25 at a time) with one call, the bulkCreateOffer method can be used.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.OfferApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.EbayOfferDetailsWithKeys() # EbayOfferDetailsWithKeys | Details of the offer for the channel
content_language = 'content_language_example' # str | This request header sets the natural language that will be provided in the field values of the request payload.

try:
    api_response = api_instance.create_offer(body, content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->create_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EbayOfferDetailsWithKeys**](EbayOfferDetailsWithKeys.md)| Details of the offer for the channel | 
 **content_language** | **str**| This request header sets the natural language that will be provided in the field values of the request payload. | 

### Return type

[**OfferResponse**](OfferResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_offer**
> delete_offer(offer_id)



If used against an unpublished offer, this call will permanently delete that offer. In the case of a published offer (or live eBay listing), a successful call will either end the single-variation listing associated with the offer, or it will remove that product variation from the eBay listing and also automatically remove that product variation from the inventory item group. In the case of a multiple-variation listing, the deleteOffer will not remove the product variation from the listing if that variation has one or more sales. If that product variation has one or more sales, the seller can alternately just set the available quantity of that product variation to 0, so it is not available in the eBay search or View Item page, and then the seller can remove that product variation from the inventory item group at a later time.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.OfferApi(ebayinventory.ApiClient(configuration))
offer_id = 'offer_id_example' # str | The unique identifier of the offer to delete. The unique identifier of the offer (offerId) is passed in at the end of the call URI.

try:
    api_instance.delete_offer(offer_id)
except ApiException as e:
    print("Exception when calling OfferApi->delete_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| The unique identifier of the offer to delete. The unique identifier of the offer (offerId) is passed in at the end of the call URI. | 

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_fees**
> FeesSummaryResponse get_listing_fees(body=body)



This call is used to retrieve the expected listing fees for up to 250 unpublished offers. An array of one or more offerId values are passed in under the offers container. In the response payload, all listing fees are grouped by eBay marketplace, and listing fees per offer are not shown. A fees container will be returned for each eBay marketplace where the seller is selling the products associated with the specified offers. Errors will occur if the seller passes in offerIds that represent published offers, so this call should be made before the seller publishes offers with the publishOffer.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.OfferApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.OfferKeysWithId() # OfferKeysWithId | List of offers that needs fee information (optional)

try:
    api_response = api_instance.get_listing_fees(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->get_listing_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OfferKeysWithId**](OfferKeysWithId.md)| List of offers that needs fee information | [optional] 

### Return type

[**FeesSummaryResponse**](FeesSummaryResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer**
> EbayOfferDetailsWithAll get_offer(offer_id)



This call retrieves a specific published or unpublished offer. The unique identifier of the offer (offerId) is passed in at the end of the call URI. The authorization header is the only required HTTP header for this call. See the HTTP request headers section for more information.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.OfferApi(ebayinventory.ApiClient(configuration))
offer_id = 'offer_id_example' # str | The unique identifier of the offer that is to be retrieved.

try:
    api_response = api_instance.get_offer(offer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->get_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| The unique identifier of the offer that is to be retrieved. | 

### Return type

[**EbayOfferDetailsWithAll**](EbayOfferDetailsWithAll.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offers**
> Offers get_offers(format=format, limit=limit, marketplace_id=marketplace_id, offset=offset, sku=sku)



This call retrieves all existing offers for the specified SKU value. The seller has the option of limiting the offers that are retrieved to a specific eBay marketplace, or to a listing format. Note: At this time, the same SKU value can not be offered across multiple eBay marketplaces, and the only supported listing format is fixed-price, so the marketplace_id and format query parameters currently do not have any practical use for this call. The authorization header is the only required HTTP header for this call. See the HTTP request headers section for more information.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.OfferApi(ebayinventory.ApiClient(configuration))
format = 'format_example' # str | This enumeration value sets the listing format for the offer. This query parameter will be passed in if the seller only wants to see offers in this specified listing format. (optional)
limit = 'limit_example' # str | The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be a positive integer value. If this query parameter is not set, up to 100 records will be returned on each page of results. (optional)
marketplace_id = 'marketplace_id_example' # str | The unique identifier of the eBay marketplace. This query parameter will be passed in if the seller only wants to see the product's offers on a specific eBay marketplace. Note: At this time, the same SKU value can not be offered across multiple eBay marketplaces, so the marketplace_id query parameter currently does not have any practical use for this call. (optional)
offset = 'offset_example' # str | The value passed in this query parameter sets the page number to retrieve. Although this field is a string, the value passed in this field should be a integer value equal to or greater than 0. The first page of records has a value of 0, the second page of records has a value of 1, and so on. If this query parameter is not set, its value defaults to 0, and the first page of records is returned. (optional)
sku = 'sku_example' # str | The seller-defined SKU value is passed in as a query parameter. All offers associated with this product are returned in the response. Max length: 50. (optional)

try:
    api_response = api_instance.get_offers(format=format, limit=limit, marketplace_id=marketplace_id, offset=offset, sku=sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->get_offers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| This enumeration value sets the listing format for the offer. This query parameter will be passed in if the seller only wants to see offers in this specified listing format. | [optional] 
 **limit** | **str**| The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be a positive integer value. If this query parameter is not set, up to 100 records will be returned on each page of results. | [optional] 
 **marketplace_id** | **str**| The unique identifier of the eBay marketplace. This query parameter will be passed in if the seller only wants to see the product&#x27;s offers on a specific eBay marketplace. Note: At this time, the same SKU value can not be offered across multiple eBay marketplaces, so the marketplace_id query parameter currently does not have any practical use for this call. | [optional] 
 **offset** | **str**| The value passed in this query parameter sets the page number to retrieve. Although this field is a string, the value passed in this field should be a integer value equal to or greater than 0. The first page of records has a value of 0, the second page of records has a value of 1, and so on. If this query parameter is not set, its value defaults to 0, and the first page of records is returned. | [optional] 
 **sku** | **str**| The seller-defined SKU value is passed in as a query parameter. All offers associated with this product are returned in the response. Max length: 50. | [optional] 

### Return type

[**Offers**](Offers.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_offer**
> PublishResponse publish_offer(offer_id)



This call is used to convert an unpublished offer into a published offer, or live eBay listing. The unique identifier of the offer (offerId) is passed in at the end of the call URI. For those who prefer to publish multiple offers (up to 25 at a time) with one call, the bulkPublishOffer method can be used. In the case of a multiple-variation listing, the publishOfferByInventoryItemGroup call should be used instead, as this call will convert all unpublished offers associated with an inventory item group into a multiple-variation listing.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.OfferApi(ebayinventory.ApiClient(configuration))
offer_id = 'offer_id_example' # str | The unique identifier of the offer that is to be published.

try:
    api_response = api_instance.publish_offer(offer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->publish_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| The unique identifier of the offer that is to be published. | 

### Return type

[**PublishResponse**](PublishResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_offer_by_inventory_item_group**
> PublishResponse publish_offer_by_inventory_item_group(body)



Note: Please note that any eBay listing created using the Inventory API cannot be revised or relisted using the Trading API calls. This call is used to convert all unpublished offers associated with an inventory item group into an active, multiple-variation listing. The unique identifier of the inventory item group (inventoryItemGroupKey) is passed in the request payload. All inventory items and their corresponding offers in the inventory item group must be valid (meet all requirements) for the publishOfferByInventoryItemGroup call to be completely successful. For any inventory items in the group that are missing required data or have no corresponding offers, the publishOfferByInventoryItemGroup will create a new multiple-variation listing, but any inventory items with missing required data/offers will not be in the newly-created listing. If any inventory items in the group to be published have invalid data, or one or more of the inventory items have conflicting data with one another, the publishOfferByInventoryItemGroup call will fail. Be sure to check for any error or warning messages in the call response for any applicable information about one or more inventory items/offers having issues.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.OfferApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.PublishByInventoryItemGroupRequest() # PublishByInventoryItemGroupRequest | The identifier of the inventory item group to publish and the eBay marketplace where the listing will be published is needed in the request payload.

try:
    api_response = api_instance.publish_offer_by_inventory_item_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->publish_offer_by_inventory_item_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublishByInventoryItemGroupRequest**](PublishByInventoryItemGroupRequest.md)| The identifier of the inventory item group to publish and the eBay marketplace where the listing will be published is needed in the request payload. | 

### Return type

[**PublishResponse**](PublishResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_offer**
> OfferResponse update_offer(body, content_language, offer_id)



This call updates an existing offer. An existing offer may be in published state (active eBay listing), or in an unpublished state and yet to be published with the publishOffer call. The unique identifier (offerId) for the offer to update is passed in at the end of the call URI. The updateOffer call does a complete replacement of the existing offer object, so all fields that make up the current offer object are required, regardless of whether their values changed. Other information that is required before an unpublished offer can be published or before a published offer can be revised include: Inventory location Offer price Available quantity eBay listing category Referenced listing policy profiles to set payment, return, and fulfillment values/settings Note: Though the includeCatalogProductDetails parameter is not required to be submitted in the request, the parameter defaults to true if omitted from both the updateOffer and the createOffer calls. If a value is specified in the updateOffer call, this value will be used. For published offers, the listingDescription field is also required to update the offer/eBay listing. For unpublished offers, this field is not necessarily required unless it is already set for the unpublished offer. In addition to the authorization header, which is required for all eBay REST API calls, the updateOffer call also requires the Content-Language header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be en-US. To view other supported Content-Language values, and to read more about all supported HTTP headers for eBay REST API calls, see the HTTP request headers topic in the Using eBay RESTful APIs document.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.OfferApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.EbayOfferDetailsWithId() # EbayOfferDetailsWithId | Details of the offer for the channel
content_language = 'content_language_example' # str | This request header sets the natural language that will be provided in the field values of the request payload.
offer_id = 'offer_id_example' # str | The unique identifier of the offer that is being updated. This identifier is passed in at the end of the call URI.

try:
    api_response = api_instance.update_offer(body, content_language, offer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->update_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EbayOfferDetailsWithId**](EbayOfferDetailsWithId.md)| Details of the offer for the channel | 
 **content_language** | **str**| This request header sets the natural language that will be provided in the field values of the request payload. | 
 **offer_id** | **str**| The unique identifier of the offer that is being updated. This identifier is passed in at the end of the call URI. | 

### Return type

[**OfferResponse**](OfferResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_offer**
> WithdrawResponse withdraw_offer(offer_id)



This call is used to end a single-variation listing that is associated with the specified offer. This call is used in place of the deleteOffer call if the seller only wants to end the listing associated with the offer but does not want to delete the offer object. With this call, the offer object remains, but it goes into the unpublished state, and will require a publishOffer call to relist the offer. To end a multiple-variation listing that is associated with an inventory item group, the withdrawOfferByInventoryItemGroup method can be used. This call only ends the multiple-variation listing associated with an inventory item group but does not delete the inventory item group object, nor does it delete any of the offers associated with the inventory item group, but instead all of these offers go into the unpublished state.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.OfferApi(ebayinventory.ApiClient(configuration))
offer_id = 'offer_id_example' # str | The unique identifier of the offer that is to be withdrawn. This value is passed into the path of the call URI.

try:
    api_response = api_instance.withdraw_offer(offer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->withdraw_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| The unique identifier of the offer that is to be withdrawn. This value is passed into the path of the call URI. | 

### Return type

[**WithdrawResponse**](WithdrawResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_offer_by_inventory_item_group**
> withdraw_offer_by_inventory_item_group(body)



This call is used to end a multiple-variation eBay listing that is associated with the specified inventory item group. This call only ends multiple-variation eBay listing associated with the inventory item group but does not delete the inventory item group object. Similarly, this call also does not delete any of the offers associated with the inventory item group, but instead all of these offers go into the unpublished state. If the seller wanted to relist the multiple-variation eBay listing, they could use the publishOfferByInventoryItemGroup method.

### Example
```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.OfferApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.WithdrawByInventoryItemGroupRequest() # WithdrawByInventoryItemGroupRequest | The base request of the withdrawOfferByInventoryItemGroup call.

try:
    api_instance.withdraw_offer_by_inventory_item_group(body)
except ApiException as e:
    print("Exception when calling OfferApi->withdraw_offer_by_inventory_item_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WithdrawByInventoryItemGroupRequest**](WithdrawByInventoryItemGroupRequest.md)| The base request of the withdrawOfferByInventoryItemGroup call. | 

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

