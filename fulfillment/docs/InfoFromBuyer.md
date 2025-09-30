# InfoFromBuyer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_on_hold** | **bool** | When the value of this field is &lt;code&gt;true&lt;/code&gt; it indicates that the buyer&#x27;s note regarding the payment dispute (i.e., the &lt;b&gt;buyerProvided.note&lt;/b&gt; field,) is on hold. When this is the case, the &lt;b&gt;buyerProvided.note&lt;/b&gt; field will not be returned.&lt;br&gt;&lt;br&gt;When the value of this field is &lt;code&gt;false&lt;/code&gt;, it is not returned. | [optional] 
**note** | **str** | This field shows any note that was left by the buyer in regard to the dispute. | [optional] 
**return_shipment_tracking** | [**list[TrackingInfo]**](TrackingInfo.md) | This array shows shipment tracking information for one or more shipping packages being returned to the buyer after a payment dispute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

