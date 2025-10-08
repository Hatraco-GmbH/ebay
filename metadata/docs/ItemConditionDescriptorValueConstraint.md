# ItemConditionDescriptorValueConstraint

This type shows the constraints on a condition descriptor value, such as any associated condition descriptor ID and condition descriptor value IDs required for a listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable_to_condition_descriptor_id** | **str** | This string is returned if the corresponding condition descriptor value requires an associated condition descriptor that must also be specified in a listing. The condition descriptor ID for the associated condition descriptors is returned here. | [optional] 
**applicable_to_condition_descriptor_value_ids** | **List[str]** | This array is returned if the corresponding condition descriptor value is required for one or more associated condition descriptor values that must also be specified in a listing. The condition descriptor values IDs for the associated condition descriptor values are returned here. | [optional] 

## Example

```python
from ebaymetadata.models.item_condition_descriptor_value_constraint import ItemConditionDescriptorValueConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ItemConditionDescriptorValueConstraint from a JSON string
item_condition_descriptor_value_constraint_instance = ItemConditionDescriptorValueConstraint.from_json(json)
# print the JSON string representation of the object
print(ItemConditionDescriptorValueConstraint.to_json())

# convert the object into a dict
item_condition_descriptor_value_constraint_dict = item_condition_descriptor_value_constraint_instance.to_dict()
# create an instance of ItemConditionDescriptorValueConstraint from a dict
item_condition_descriptor_value_constraint_from_dict = ItemConditionDescriptorValueConstraint.from_dict(item_condition_descriptor_value_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


