# LineItemReference

This type identifies the line item and quantity of that line item that comprises one fulfillment, such as a shipping package.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_id** | **str** | This is the unique identifier of the eBay order line item that is part of the shipping fulfillment.&lt;br&gt;&lt;br&gt;Line item Ids can be found in the lineItems.&lt;b&gt;lineItemId&lt;/b&gt; field of the &lt;a href&#x3D;\&quot;/api-docs/sell/fulfillment/resources/order/methods/getOrders\&quot; target&#x3D;\&quot;_blank\&quot;&gt;getOrders&lt;/a&gt; response. | [optional] 
**quantity** | **int** | This is the number of lineItems associated with the &lt;a href&#x3D;\&quot;#request.trackingNumber\&quot;&gt;trackingNumber&lt;/a&gt; specified by the seller. This must be a whole number greater than zero (0).&lt;br&gt;&lt;br&gt;&lt;b&gt;Default:&lt;/b&gt; 1 | [optional] 

## Example

```python
from ebayfulfillment.models.line_item_reference import LineItemReference

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemReference from a JSON string
line_item_reference_instance = LineItemReference.from_json(json)
# print the JSON string representation of the object
print(LineItemReference.to_json())

# convert the object into a dict
line_item_reference_dict = line_item_reference_instance.to_dict()
# create an instance of LineItemReference from a dict
line_item_reference_from_dict = LineItemReference.from_dict(line_item_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


