# ShippingPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The unique identifier of the eBay leaf category for which metadata is being returned. | [optional] 
**category_tree_id** | **str** | The unique identifier of the category tree. | [optional] 
**global_shipping_enabled** | **bool** | Indicates if the Global Shipping Program (GSP) is supported for the category. &lt;p&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#004680\&quot;&gt;&lt;strong&gt;Note: &lt;/strong&gt;GSP is only supported by the eBay UK marketplace (&lt;code&gt;EBAY_GB&lt;/code&gt;).&lt;/span&gt;&lt;/p&gt; | [optional] 
**group1_max_flat_shipping_cost** | [**Amount**](Amount.md) |  | [optional] 
**group2_max_flat_shipping_cost** | [**Amount**](Amount.md) |  | [optional] 
**group3_max_flat_shipping_cost** | [**Amount**](Amount.md) |  | [optional] 
**handling_time_enabled** | **bool** | Indicates if a seller&#x27;s stated handling time is enabled for a category. A handling time is generally needed for items that are shipped to the buyer, but not necessarily applicable to freight shipping or local pickup. | [optional] 
**max_flat_shipping_cost** | [**Amount**](Amount.md) |  | [optional] 
**shipping_terms_required** | **bool** | Indicates whether the category requires sellers to specify shipping details at listing time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

