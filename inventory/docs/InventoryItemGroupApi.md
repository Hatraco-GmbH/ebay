# ebayinventory.InventoryItemGroupApi

All URIs are relative to *https://api.ebay.com/sell/inventory/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_replace_inventory_item_group**](InventoryItemGroupApi.md#create_or_replace_inventory_item_group) | **PUT** /inventory_item_group/{inventoryItemGroupKey} | 
[**delete_inventory_item_group**](InventoryItemGroupApi.md#delete_inventory_item_group) | **DELETE** /inventory_item_group/{inventoryItemGroupKey} | 
[**get_inventory_item_group**](InventoryItemGroupApi.md#get_inventory_item_group) | **GET** /inventory_item_group/{inventoryItemGroupKey} | 


# **create_or_replace_inventory_item_group**
> BaseResponse create_or_replace_inventory_item_group(content_language, inventory_item_group_key, content_type, inventory_item_group)

<span class="tablenote"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.</span><br>This call creates a new inventory item group or updates an existing inventory item group. It is up to sellers whether they want to create a complete inventory item group record right from the start, or sellers can provide only some information with the initial <strong>createOrReplaceInventoryItemGroup</strong> call, and then make one or more additional <strong>createOrReplaceInventoryItemGroup</strong> calls to complete the inventory item group record. Upon first creating an inventory item group record, the only required elements are  the <strong>inventoryItemGroupKey</strong> identifier in the call URI, and the members of the inventory item group specified through the <strong>variantSKUs</strong> array in the request payload.<br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see <a href="/api-docs/sell/static/inventory/publishing-offers.html#inventory_item_group " target="_blank">Inventory item group fields</a> for a list of fields required to publish an offer.</p></span></div><br><span class="tablenote"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> and <code>Content-Language</code> headers. See the <a href="/api-docs/sell/inventory/resources/inventory_item_group/methods/createOrReplaceInventoryItemGroup#h3-request-headers">HTTP request headers</a> for more information.</span><br>In the case of updating/replacing an existing inventory item group, this call does a complete replacement of the existing inventory item group record, so all fields (including the member SKUs) that make up the inventory item group are required, regardless of whether their values changed. So, when replacing/updating an inventory item group record, it is advised that the seller run a <strong>getInventoryItemGroup</strong> call for that inventory item group to see all of its current values/settings/members before attempting to update the record. And if changes are made to an inventory item group that is part of a live, multiple-variation eBay listing, these changes automatically update the eBay listing. For example, if a SKU value is removed from the inventory item group, the corresponding product variation will be removed from the eBay listing as well.<br><br>In addition to the required inventory item group identifier and member SKUs, other key information that is set with this call include: <ul> <li>Title and description of the inventory item group. The string values provided in these fields will actually become the listing title and listing description of the listing once the first SKU of the inventory item group is published successfully</li> <li>Common aspects that inventory items in the group share</li> <li>Product aspects that vary within each product variation</li> <li>Links to images demonstrating the variations of the product, and these images should correspond to the product aspect that is set with the <strong>variesBy.aspectsImageVariesBy</strong> field</li> </ul><br><span class="tablenote"><b>Note:</b> For more information, see <a href="/api-docs/sell/static/inventory/inventory-item-groups.html" target="_blank">Creating and managing inventory item groups</a>.</span>

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.base_response import BaseResponse
from ebayinventory.models.inventory_item_group import InventoryItemGroup
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
    api_instance = ebayinventory.InventoryItemGroupApi(api_client)
    content_language = 'content_language_example' # str | This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be <code>en-US</code> for English or <code>de-DE</code> for German.<br><br>For more information on the Content-Language header, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    inventory_item_group_key = 'inventory_item_group_key_example' # str | This path parameter specifies the unique identifier of the inventory item group being created or updated. This identifier is defined by the seller.<br><br>This value cannot be changed once it is set.<br><br><b>Max Length:</b> 50
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    inventory_item_group = ebayinventory.InventoryItemGroup() # InventoryItemGroup | Details of the inventory Item Group

    try:
        api_response = api_instance.create_or_replace_inventory_item_group(content_language, inventory_item_group_key, content_type, inventory_item_group)
        print("The response of InventoryItemGroupApi->create_or_replace_inventory_item_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryItemGroupApi->create_or_replace_inventory_item_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_language** | **str**| This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be &lt;code&gt;en-US&lt;/code&gt; for English or &lt;code&gt;de-DE&lt;/code&gt; for German.&lt;br&gt;&lt;br&gt;For more information on the Content-Language header, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **inventory_item_group_key** | **str**| This path parameter specifies the unique identifier of the inventory item group being created or updated. This identifier is defined by the seller.&lt;br&gt;&lt;br&gt;This value cannot be changed once it is set.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max Length:&lt;/b&gt; 50 | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **inventory_item_group** | [**InventoryItemGroup**](InventoryItemGroup.md)| Details of the inventory Item Group | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Content-Language -  <br>  |
**201** | Created |  * Content-Language -  <br>  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inventory_item_group**
> delete_inventory_item_group(inventory_item_group_key)

This call deletes the inventory item group for a given <strong>inventoryItemGroupKey</strong> value.

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
    api_instance = ebayinventory.InventoryItemGroupApi(api_client)
    inventory_item_group_key = 'inventory_item_group_key_example' # str | This path parameter specifies the unique identifier of the inventory item group being deleted. This value is assigned by the seller when an inventory item group is created.

    try:
        api_instance.delete_inventory_item_group(inventory_item_group_key)
    except Exception as e:
        print("Exception when calling InventoryItemGroupApi->delete_inventory_item_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_item_group_key** | **str**| This path parameter specifies the unique identifier of the inventory item group being deleted. This value is assigned by the seller when an inventory item group is created. | 

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

# **get_inventory_item_group**
> InventoryItemGroup get_inventory_item_group(inventory_item_group_key)

This call retrieves the inventory item group for a given <strong>inventoryItemGroupKey</strong> value. The <strong>inventoryItemGroupKey</strong> value is passed in at the end of the call URI.

### Example

* OAuth Authentication (api_auth):

```python
import ebayinventory
from ebayinventory.models.inventory_item_group import InventoryItemGroup
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
    api_instance = ebayinventory.InventoryItemGroupApi(api_client)
    inventory_item_group_key = 'inventory_item_group_key_example' # str | This path parameter specifies the unique identifier of the inventory item group being retrieved. This value is assigned by the seller when an inventory item group is created.

    try:
        api_response = api_instance.get_inventory_item_group(inventory_item_group_key)
        print("The response of InventoryItemGroupApi->get_inventory_item_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryItemGroupApi->get_inventory_item_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_item_group_key** | **str**| This path parameter specifies the unique identifier of the inventory item group being retrieved. This value is assigned by the seller when an inventory item group is created. | 

### Return type

[**InventoryItemGroup**](InventoryItemGroup.md)

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

