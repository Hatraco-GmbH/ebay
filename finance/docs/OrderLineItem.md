# OrderLineItem

This type is used to show the fees and donations that are deducted from a seller payout for each line item in an order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**donations** | [**List[Fee]**](Fee.md) | The list of donations applied to the line item.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note: &lt;/b&gt;Currently, this array is only returned if the seller chooses to donate a percentage of the sales proceeds to a charitable organization registered with the eBay for Charity program.&lt;/span&gt; | [optional] 
**fee_basis_amount** | [**Amount**](Amount.md) |  | [optional] 
**line_item_id** | **str** | The unique identifier of an order line item. | [optional] 
**marketplace_fees** | [**List[Fee]**](Fee.md) | An array of all fees accrued for the order line item and deducted from a seller payout. | [optional] 

## Example

```python
from ebayfinance.models.order_line_item import OrderLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLineItem from a JSON string
order_line_item_instance = OrderLineItem.from_json(json)
# print the JSON string representation of the object
print(OrderLineItem.to_json())

# convert the object into a dict
order_line_item_dict = order_line_item_instance.to_dict()
# create an instance of OrderLineItem from a dict
order_line_item_from_dict = OrderLineItem.from_dict(order_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


