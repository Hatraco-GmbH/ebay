# ShippingFulfillment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_id** | **str** | The unique identifier of the fulfillment; for example, 9405509699937003457459. This eBay-generated value is created with a successful createShippingFulfillment call. | [optional] 
**line_items** | [**list[LineItemReference]**](LineItemReference.md) | This array contains a list of one or more line items (and purchased quantity) to which the fulfillment applies. | [optional] 
**shipment_tracking_number** | **str** | The tracking number provided by the shipping carrier for the package shipped in this fulfillment. This field is returned if available. | [optional] 
**shipped_date** | **str** | The date and time that the fulfillment package was shipped. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field should only be returned if the package has been shipped. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z | [optional] 
**shipping_carrier_code** | **str** | The eBay code identifying the shipping carrier for this fulfillment. This field is returned if available. Note: The Trading API&#x27;s ShippingCarrierCodeType enumeration type contains the most current list of eBay shipping carrier codes and the countries served by each carrier. See ShippingCarrierCodeType. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

