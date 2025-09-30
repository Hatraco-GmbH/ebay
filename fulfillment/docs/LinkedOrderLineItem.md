# LinkedOrderLineItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_aspects** | [**list[NameValuePair]**](NameValuePair.md) | This array contains the complete set of items aspects for the linked line item. For example:&lt;br&gt;&lt;pre&gt;\&quot;lineItemAspects\&quot;: [&lt;br&gt;    {&lt;br&gt;        \&quot;name\&quot;: \&quot;Tire Type\&quot;,&lt;br&gt;        \&quot;value\&quot;: \&quot;All Season\&quot;&lt;br&gt;    },&lt;br&gt;&lt;br&gt;    ...&lt;br&gt; &lt;br&gt;    {&lt;br&gt;        \&quot;name\&quot;: \&quot;Car Type\&quot;,&lt;br&gt;        \&quot;value\&quot;: \&quot;Performance\&quot;&lt;br&gt;    }&lt;br&gt;]&lt;/pre&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; All item specifics for the listing are returned. The name/value pairs returned are in the language of the linked line item&#x27;s listing site, which may vary from the seller&#x27;s language.&lt;/span&gt; | [optional] 
**line_item_id** | **str** | The unique identifier of the linked order line item. | [optional] 
**max_estimated_delivery_date** | **str** | The end of the date range in which the linked line item is expected to be delivered to the shipping address. | [optional] 
**min_estimated_delivery_date** | **str** | The beginning of the date range in which the linked line item is expected to be delivered to the shipping address. | [optional] 
**order_id** | **str** | The unique identifier of the order to which the linked line item belongs. | [optional] 
**seller_id** | **str** | The eBay user ID of the seller who sold the linked line item. For example, the user ID of the tire seller. | [optional] 
**shipments** | [**list[TrackingInfo]**](TrackingInfo.md) | An array containing any shipment tracking information available for the linked line item. | [optional] 
**title** | **str** | The listing title of the linked line item.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; The Item ID value for the listing will be returned in this field instead of the actual title if this particular listing is on-hold due to an eBay policy violation.&lt;/span&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

