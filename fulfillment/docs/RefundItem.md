# RefundItem

This type is used if the seller is issuing a refund for one or more individual order line items in a multiple line item order. Otherwise, the seller just uses the <b>orderLevelRefundAmount</b> container to specify the amount of the refund for the entire order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_amount** | [**SimpleAmount**](SimpleAmount.md) |  | [optional] 
**line_item_id** | **str** | The unique identifier of an order line item. This identifier is created once a buyer purchases a &#39;Buy It Now&#39; item or if an auction listing ends with a winning bidder.&lt;br&gt;&lt;br&gt;Either this field or the &lt;b&gt;legacyReference&lt;/b&gt; container is needed to identify an individual order line item that will receive a refund.&lt;br&gt;&lt;br&gt; This value is returned using the &lt;a href&#x3D;\&quot;/api-docs/sell/fulfillment/resources/order/methods/getOrders\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getOrders&lt;/a&gt; method. | [optional] 
**legacy_reference** | [**LegacyReference**](LegacyReference.md) |  | [optional] 

## Example

```python
from ebayfulfillment.models.refund_item import RefundItem

# TODO update the JSON string below
json = "{}"
# create an instance of RefundItem from a JSON string
refund_item_instance = RefundItem.from_json(json)
# print the JSON string representation of the object
print(RefundItem.to_json())

# convert the object into a dict
refund_item_dict = refund_item_instance.to_dict()
# create an instance of RefundItem from a dict
refund_item_from_dict = RefundItem.from_dict(refund_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


