# ListingTypePolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The unique identifier of the eBay leaf category for which metadata is being returned. | [optional] 
**category_tree_id** | **str** | The unique identifier of the category tree. | [optional] 
**digital_good_delivery_enabled** | **bool** | A &lt;code&gt;true&lt;/code&gt; value in this field indicates that the leaf category supports the listing of items (such as gift cards) that can be delivered electronically via a download link or sent to a buyer&#x27;s email address. | [optional] 
**listing_durations** | [**list[ListingDuration]**](ListingDuration.md) | An array of eBay listing types and the supported durations for the corresponding leaf category. If a specific eBay listing type does not appear for a leaf category, it indicates that the category does not support that listing type. | [optional] 
**pickup_drop_off_enabled** | **bool** | A true value in this field indicates that items listed in the category (specified in the &lt;b&gt;listingTypePolicies.categoryId&lt;/b&gt; field) may be enabled with the &#x27;Click and Collect&#x27; feature. With the &#x27;Click and Collect&#x27; feature, a buyer can purchase certain items on an eBay site and collect them at a local store. Buyers are notified by eBay once their items are available. A false value in this field indicates that items listed in the category are not eligible for the &#x27;Click and Collect&#x27; feature. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

