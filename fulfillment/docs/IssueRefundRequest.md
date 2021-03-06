# IssueRefundRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason_for_refund** | **str** | The enumeration value passed into this field indicates the reason for the refund. One of the defined enumeration values in the ReasonForRefundEnum type must be used. This field is required, and it is highly recommended that sellers use the correct refund reason, especially in the case of a buyer-requested cancellation or &#x27;buyer remorse&#x27; return to indicate that there was nothing wrong with the item(s) or with the shipment of the order. Note: If issuing refunds for more than one order line item, keep in mind that the refund reason must be the same for each of the order line items. If the refund reason is different for one or more order line items in an order, the seller would need to make separate issueRefund calls, one for each refund reason. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/fulfillment/types/api:ReasonForRefundEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**comment** | **str** | This free-text field allows the seller to clarify why the refund is being issued to the buyer. Max Length: 100 | [optional] 
**refund_items** | [**list[RefundItem]**](RefundItem.md) | The refundItems array is only required if the seller is issuing a refund for one or more individual order line items in a multiple line item order. Otherwise, the seller just uses the orderLevelRefundAmount container to specify the amount of the refund for the entire order. | [optional] 
**order_level_refund_amount** | [**SimpleAmount**](SimpleAmount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

