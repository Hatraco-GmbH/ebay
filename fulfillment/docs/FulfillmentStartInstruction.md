# FulfillmentStartInstruction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ebay_supported_fulfillment** | **bool** | This field is only returned if its value is true and indicates that the fulfillment will be shipped via eBay&#x27;s Global Shipping Program. For more information, see the Global Shipping Program help topic. | [optional] 
**final_destination_address** | [**Address**](Address.md) |  | [optional] 
**fulfillment_instructions_type** | **str** | The enumeration value returned in this field indicates the method of fulfillment that will be used to deliver this set of line items (this package) to the buyer. This field will have a value of SHIP_TO if the ebaySupportedFulfillment field is returned with a value of true. See the FulfillmentInstructionsType definition for more information about different fulfillment types. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:FulfillmentInstructionsType&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**max_estimated_delivery_date** | **str** | This is the estimated latest date that the fulfillment will be completed. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned ifthe value of the fulfillmentInstructionsType field is DIGITAL or PREPARE_FOR_PICKUP. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z | [optional] 
**min_estimated_delivery_date** | **str** | This is the estimated earliest date that the fulfillment will be completed. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned if the value of the fulfillmentInstructionsType field is DIGITAL or PREPARE_FOR_PICKUP. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z | [optional] 
**pickup_step** | [**PickupStep**](PickupStep.md) |  | [optional] 
**shipping_step** | [**ShippingStep**](ShippingStep.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

