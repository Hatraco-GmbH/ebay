# FormatAllocation

This type is used to indicate the quantities of the inventory items that are reserved for the different listing formats of the SKU offers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auction** | **int** | This integer value indicates the quantity of the inventory item that is reserved for the published auction format offers of the SKU. | [optional] 
**fixed_price** | **int** | This integer value indicates the quantity of the inventory item that is available for the fixed-price offers of the SKU. | [optional] 

## Example

```python
from ebayinventory.models.format_allocation import FormatAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of FormatAllocation from a JSON string
format_allocation_instance = FormatAllocation.from_json(json)
# print the JSON string representation of the object
print(FormatAllocation.to_json())

# convert the object into a dict
format_allocation_dict = format_allocation_instance.to_dict()
# create an instance of FormatAllocation from a dict
format_allocation_from_dict = FormatAllocation.from_dict(format_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


