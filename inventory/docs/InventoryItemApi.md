# ebayinventory.InventoryItemApi

All URIs are relative to *https://api.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_or_replace_inventory_item**](InventoryItemApi.md#bulk_create_or_replace_inventory_item) | **POST** /bulk_create_or_replace_inventory_item | 
[**bulk_get_inventory_item**](InventoryItemApi.md#bulk_get_inventory_item) | **POST** /bulk_get_inventory_item | 
[**bulk_update_price_quantity**](InventoryItemApi.md#bulk_update_price_quantity) | **POST** /bulk_update_price_quantity | 
[**create_or_replace_inventory_item**](InventoryItemApi.md#create_or_replace_inventory_item) | **PUT** /inventory_item/{sku} | 
[**delete_inventory_item**](InventoryItemApi.md#delete_inventory_item) | **DELETE** /inventory_item/{sku} | 
[**get_inventory_item**](InventoryItemApi.md#get_inventory_item) | **GET** /inventory_item/{sku} | 
[**get_inventory_items**](InventoryItemApi.md#get_inventory_items) | **GET** /inventory_item | 

# **bulk_create_or_replace_inventory_item**
> BulkInventoryItemResponse bulk_create_or_replace_inventory_item(body, content_type, content_language)



<span class=\"tablenote\"><strong>Note:</strong> Please note that any eBay listing created using the Inventory API cannot be revised or relisted using the Trading API calls.</span><br><span class=\"tablenote\"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.</span><br>This call can be used to create and/or update up to 25 new inventory item records. It is up to sellers whether they want to create a complete inventory item records right from the start, or sellers can provide only some information with the initial <strong>bulkCreateOrReplaceInventoryItem</strong> call, and then make one or more additional <strong>bulkCreateOrReplaceInventoryItem</strong> calls to complete all required fields for the inventory item records and prepare for publishing. Upon first creating inventory item records, only the SKU values are required.<br><br><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see <a href=\"/api-docs/sell/static/inventory/publishing-offers.html#inventory_item \" target=\"_blank\">Inventory item fields</a> for a list of fields required to publish an offer.</p></span></div><br><span class=\"tablenote\"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all eBay REST API calls, this call also requires the <code>Content-Language</code> and <code>Content-Type</code> headers. See the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/bulkCreateOrReplaceInventoryItem#h3-request-headers\">HTTP request headers</a> section for more information.</span><br> In the case of updating existing inventory item records, the <strong>bulkCreateOrReplaceInventoryItem</strong> call will do a complete replacement of the existing inventory item records, so all fields that are currently defined for the inventory item record are required in that update action, regardless of whether their values changed. So, when replacing/updating an inventory item record, it is advised that the seller run a 'Get' call to retrieve the full details of the inventory item records and see all of its current values/settings before attempting to update the records. Any changes that are made to inventory item records that are part of one or more active eBay listings, a successful call will automatically update these active listings. <br><br>The key information that is set with the <strong>bulkCreateOrReplaceInventoryItem</strong> call include: <ul> <li>Seller-defined SKU value for the product. Each seller product, including products within an item inventory group, must have their own SKU value. </li> <li>Condition of the item</li> <li>Product details, including any product identifier(s), such as a UPC, ISBN, EAN, or Brand/Manufacturer Part Number pair, a product description, a product title, product/item aspects, and links to images. eBay will use any supplied eBay Product ID (ePID) or a GTIN (UPC, ISBN, or EAN) and attempt to match those identifiers to a product in the eBay Catalog, and if a product match is found, the product details for the inventory item will automatically be populated.</li> <li>Quantity of the inventory item that is available for purchase</li> <li>Package weight and dimensions, which is required if the seller will be offering calculated shipping options. The package weight will also be required if the seller will be providing flat-rate shipping services, but charging a weight surcharge.</li> </ul><p>For those who prefer to create or update a single inventory item record, the <strong>createOrReplaceInventoryItem</strong> method can be used.</p>

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
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.BulkInventoryItem() # BulkInventoryItem | Details of the inventories with sku and locale
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
content_language = 'content_language_example' # str | This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be <code>en-US</code> for English or <code>de-DE</code> for German.<br><br>For more information on the Content-Language header, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.

try:
    api_response = api_instance.bulk_create_or_replace_inventory_item(body, content_type, content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryItemApi->bulk_create_or_replace_inventory_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkInventoryItem**](BulkInventoryItem.md)| Details of the inventories with sku and locale | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **content_language** | **str**| This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be &lt;code&gt;en-US&lt;/code&gt; for English or &lt;code&gt;de-DE&lt;/code&gt; for German.&lt;br&gt;&lt;br&gt;For more information on the Content-Language header, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 

### Return type

[**BulkInventoryItemResponse**](BulkInventoryItemResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_get_inventory_item**
> BulkGetInventoryItemResponse bulk_get_inventory_item(body, content_type)



This call retrieves up to 25 inventory item records. The SKU value of each inventory item record to retrieve is specified in the request payload.<br><br><span class=\"tablenote\"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> header. See the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/bulkGetInventoryItem#h3-request-headers\">HTTP request headers</a> for more information.</span><br>For those who prefer to retrieve only one inventory item record by SKU value, the <strong>getInventoryItem</strong> method can be used. To retrieve all inventory item records defined on the seller's account, the <strong>getInventoryItems</strong> method can be used (with pagination control if desired).

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
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.BulkGetInventoryItem() # BulkGetInventoryItem | Details of the inventories with sku and locale
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.

try:
    api_response = api_instance.bulk_get_inventory_item(body, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryItemApi->bulk_get_inventory_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkGetInventoryItem**](BulkGetInventoryItem.md)| Details of the inventories with sku and locale | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 

### Return type

[**BulkGetInventoryItemResponse**](BulkGetInventoryItemResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_price_quantity**
> BulkPriceQuantityResponse bulk_update_price_quantity(body, content_type)



This call is used by the seller to update the total ship-to-home quantity of one inventory item, and/or to update the price and/or quantity of one or more offers associated with one inventory item. Up to 25 offers associated with an inventory item may be updated with one <strong>bulkUpdatePriceQuantity</strong> call. Only one SKU (one product) can be updated per call.<br><br><span class=\"tablenote\"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.</span><br><span class=\"tablenote\"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> header. See the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/bulkUpdatePriceQuantity#h3-request-headers\">HTTP request headers</a> for more information.</span><br>The <strong>getOffers</strong> call can be used to retrieve all offers associated with a SKU. The seller will just pass in the correct SKU value through the <strong>sku</strong> query parameter. To update an offer, the <strong>offerId</strong> value is required, and this value is returned in the <strong>getOffers</strong> call response. It is also useful to know which offers are unpublished and which ones are published. To get this status, look for the <strong>status</strong> value in the <strong>getOffers</strong> call response. Offers in the published state are live eBay listings, and these listings will be revised with a successful <strong>bulkUpdatePriceQuantity</strong> call.<br><br>An issue will occur if duplicate <strong>offerId</strong> values are passed through the same <strong>offers</strong> container, or if one or more of the specified offers are associated with different products/SKUs.<br><br><span class=\"tablenote\"><strong>Note:</strong> For multiple-variation listings, it is recommended that the <strong>bulkUpdatePriceQuantity</strong> call be used to update price and quantity information for each SKU within that multiple-variation listing instead of using <strong>createOrReplaceInventoryItem</strong> calls to update the price and quantity for each SKU. Just remember that only one SKU (one product variation) can be updated per call.</span></p>

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
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.BulkPriceQuantity() # BulkPriceQuantity | Price and allocation details for the given SKU and Marketplace
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.

try:
    api_response = api_instance.bulk_update_price_quantity(body, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryItemApi->bulk_update_price_quantity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkPriceQuantity**](BulkPriceQuantity.md)| Price and allocation details for the given SKU and Marketplace | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 

### Return type

[**BulkPriceQuantityResponse**](BulkPriceQuantityResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_replace_inventory_item**
> BaseResponse create_or_replace_inventory_item(body, content_language, content_type, sku)



<span class=\"tablenote\"><strong>Note:</strong> Please note that any eBay listing created using the Inventory API cannot be revised or relisted using the Trading API calls.</span><br><span class=\"tablenote\"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.</span><br>This call creates a new inventory item record or replaces an existing inventory item record. It is up to sellers whether they want to create a complete inventory item record right from the start, or sellers can provide only some information with the initial <strong>createOrReplaceInventoryItem</strong> call, and then make one or more additional <strong>createOrReplaceInventoryItem</strong> calls to complete all required fields for the inventory item record and prepare it for publishing. Upon first creating an inventory item record, only the SKU value in the call path is required.<br><br><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see <a href=\"/api-docs/sell/static/inventory/publishing-offers.html#inventory_item \" target=\"_blank\">Inventory item fields</a> for a list of fields required to publish an offer.</p></span></div><br><span class=\"tablenote\"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> and <code>Content-Language</code> headers. See the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/createOrReplaceInventoryItem#h3-request-headers\">HTTP request headers</a> for more information.</span><br> In the case of replacing an existing inventory item record, the <strong>createOrReplaceInventoryItem</strong> call will do a complete replacement of the existing inventory item record, so all fields that are currently defined for the inventory item record are required in that update action, regardless of whether their values changed. So, when replacing/updating an inventory item record, it is advised that the seller run a <strong>getInventoryItem</strong> call to retrieve the full inventory item record and see all of its current values/settings before attempting to update the record. And if changes are made to an inventory item that is part of one or more active eBay listings, a successful call will automatically update these eBay listings. <br><br>The key information that is set with the <strong>createOrReplaceInventoryItem</strong> call include: <ul> <li>Seller-defined SKU value for the product. Each seller product, including products within an item inventory group, must have their own SKU value. This SKU value is passed in at the end of the call URI</li> <li>Condition of the item</li> <li>Product details, including any product identifier(s), such as a UPC, ISBN, EAN, or Brand/Manufacturer Part Number pair, a product description, a product title, product/item aspects, and links to images. eBay will use any supplied eBay Product ID (ePID) or a GTIN (UPC, ISBN, or EAN) and attempt to match those identifiers to a product in the eBay Catalog, and if a product match is found, the product details for the inventory item will automatically be populated.</li> <li>Quantity of the inventory item that is available for purchase</li> <li>Package weight and dimensions, which is required if the seller will be offering calculated shipping options. The package weight will also be required if the seller will be providing flat-rate shipping services, but charging a weight surcharge.</li> </ul> <p>In addition to the <code>authorization</code> header, which is required for all eBay REST API calls, the <strong>createOrReplaceInventoryItem</strong> call also requires the <code>Content-Language</code> header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be <code>en-US</code>. To view other supported <code>Content-Language</code> values, and to read more about all supported HTTP headers for eBay REST API calls, see the <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank\">HTTP request headers</a> topic in the <strong>Using eBay RESTful APIs</strong> document.</p><p>For those who prefer to create or update numerous inventory item records with one call (up to 25 at a time), the <strong>bulkCreateOrReplaceInventoryItem</strong> method can be used.</p>

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
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.InventoryItem() # InventoryItem | Details of the inventory item record.
content_language = 'content_language_example' # str | This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be <code>en-US</code> for English or <code>de-DE</code> for German.<br><br>For more information on the Content-Language header, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
sku = 'sku_example' # str | This path parameter specifies the seller-defined SKU value for the inventory item being created or updated. SKU values must be unique across the seller's inventory. <br><br><strong>Max length</strong>: 50

try:
    api_response = api_instance.create_or_replace_inventory_item(body, content_language, content_type, sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryItemApi->create_or_replace_inventory_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryItem**](InventoryItem.md)| Details of the inventory item record. | 
 **content_language** | **str**| This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be &lt;code&gt;en-US&lt;/code&gt; for English or &lt;code&gt;de-DE&lt;/code&gt; for German.&lt;br&gt;&lt;br&gt;For more information on the Content-Language header, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **sku** | **str**| This path parameter specifies the seller-defined SKU value for the inventory item being created or updated. SKU values must be unique across the seller&#x27;s inventory. &lt;br&gt;&lt;br&gt;&lt;strong&gt;Max length&lt;/strong&gt;: 50 | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inventory_item**
> delete_inventory_item(sku)



This call is used to delete an inventory item record associated with a specified SKU. A successful call will not only delete that inventory item record, but will also have the following effects:<ul><li>Delete any and all unpublished offers associated with that SKU;</li><li>Delete any and all single-variation eBay listings associated with that SKU;</li><li>Automatically remove that SKU from a multiple-variation listing and remove that SKU from any and all inventory item groups in which that SKU was a member.</li></ul><p>The <code>authorization</code> header is the only required HTTP header for this call. See the <strong>HTTP request headers</strong> section for more information.</p>

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
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
sku = 'sku_example' # str | This path parameter specifies the seller-defined SKU value of the product whose inventory item record you wish to delete.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\" target=\"_blank \">getInventoryItems</a> method to retrieve SKU values.<br><br><strong>Max length</strong>: 50

try:
    api_instance.delete_inventory_item(sku)
except ApiException as e:
    print("Exception when calling InventoryItemApi->delete_inventory_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**| This path parameter specifies the seller-defined SKU value of the product whose inventory item record you wish to delete.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getInventoryItems&lt;/a&gt; method to retrieve SKU values.&lt;br&gt;&lt;br&gt;&lt;strong&gt;Max length&lt;/strong&gt;: 50 | 

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_item**
> InventoryItemWithSkuLocaleGroupid get_inventory_item(sku)



This call retrieves the inventory item record for a given SKU. The SKU value is passed in at the end of the call URI. There is no request payload for this call.<br><br>The <code>authorization</code> header is the only required HTTP header for this call, and it is required for all Inventory API calls. See the <strong>HTTP request headers</strong> section for more information.<br><br>For those who prefer to retrieve numerous inventory item records by SKU value with one call (up to 25 at a time), the <strong>bulkGetInventoryItem</strong> method can be used. To retrieve all inventory item records defined on the seller's account, the <strong>getInventoryItems</strong> method can be used (with pagination control if desired).

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
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
sku = 'sku_example' # str | This path parameter specifies the seller-defined SKU value of the product whose inventory item record you wish to retrieve.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\" target=\"_blank \">getInventoryItems</a> method to retrieve SKU values.<br><br><strong>Max length</strong>: 50

try:
    api_response = api_instance.get_inventory_item(sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryItemApi->get_inventory_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**| This path parameter specifies the seller-defined SKU value of the product whose inventory item record you wish to retrieve.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getInventoryItems&lt;/a&gt; method to retrieve SKU values.&lt;br&gt;&lt;br&gt;&lt;strong&gt;Max length&lt;/strong&gt;: 50 | 

### Return type

[**InventoryItemWithSkuLocaleGroupid**](InventoryItemWithSkuLocaleGroupid.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_items**
> InventoryItems get_inventory_items(limit=limit, offset=offset)



This call retrieves all inventory item records defined for the seller's account. The <strong>limit</strong> query parameter allows the seller to control how many records are returned per page, and the <strong>offset</strong> query parameter is used to retrieve a specific page of records. The seller can make multiple calls to scan through multiple pages of records. There is no request payload for this call.<br><br>The <code>authorization</code> header is the only required HTTP header for this call, and it is required for all Inventory API calls. See the <strong>HTTP request headers</strong> section for more information.<br><br>For those who prefer to retrieve numerous inventory item records by SKU value with one call (up to 25 at a time), the <strong>bulkGetInventoryItem</strong> method can be used.

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
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
limit = 'limit_example' # str | The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be an integer from <code>1</code> to <code>200</code>.<br><br><strong>Min:</strong> 1<br><br><strong>Max:</strong> 200<br><br><b>Default:</b> 25 (optional)
offset = 'offset_example' # str | The value passed in this query parameter sets the page number to retrieve. The first page of records has a value of <code>0</code>, the second page of records has a value of <code>1</code>, and so on. If this query parameter is not set, its value defaults to <code>0</code>, and the first page of records is returned.  (optional)

try:
    api_response = api_instance.get_inventory_items(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryItemApi->get_inventory_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be an integer from &lt;code&gt;1&lt;/code&gt; to &lt;code&gt;200&lt;/code&gt;.&lt;br&gt;&lt;br&gt;&lt;strong&gt;Min:&lt;/strong&gt; 1&lt;br&gt;&lt;br&gt;&lt;strong&gt;Max:&lt;/strong&gt; 200&lt;br&gt;&lt;br&gt;&lt;b&gt;Default:&lt;/b&gt; 25 | [optional] 
 **offset** | **str**| The value passed in this query parameter sets the page number to retrieve. The first page of records has a value of &lt;code&gt;0&lt;/code&gt;, the second page of records has a value of &lt;code&gt;1&lt;/code&gt;, and so on. If this query parameter is not set, its value defaults to &lt;code&gt;0&lt;/code&gt;, and the first page of records is returned.  | [optional] 

### Return type

[**InventoryItems**](InventoryItems.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

