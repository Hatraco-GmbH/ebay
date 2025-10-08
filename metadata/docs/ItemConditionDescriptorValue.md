# ItemConditionDescriptorValue

This type displays the possible values for the corresponding condition descriptor, along with help text and constraint information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_descriptor_value_additional_help_text** | **List[str]** | Additional information about the the condition of the item that is not included in the &lt;b&gt;conditionDescriptorValueHelpText&lt;/b&gt; field. | [optional] 
**condition_descriptor_value_constraints** | [**List[ItemConditionDescriptorValueConstraint]**](ItemConditionDescriptorValueConstraint.md) | The constraints on a condition descriptor value, such as which descriptor value IDs and Descriptor ID it is associated with. | [optional] 
**condition_descriptor_value_help_text** | **str** | A detailed description of the condition descriptor value.  | [optional] 
**condition_descriptor_value_id** | **str** | The unique identification number of a condition descriptor value associated with the &lt;b&gt;conditionDescriptorValueName&lt;/b&gt;. | [optional] 
**condition_descriptor_value_name** | **str** | The human-readable label for the condition descriptor value associated with the &lt;b&gt;conditionDescriptorValueID&lt;/b&gt;. | [optional] 

## Example

```python
from ebaymetadata.models.item_condition_descriptor_value import ItemConditionDescriptorValue

# TODO update the JSON string below
json = "{}"
# create an instance of ItemConditionDescriptorValue from a JSON string
item_condition_descriptor_value_instance = ItemConditionDescriptorValue.from_json(json)
# print the JSON string representation of the object
print(ItemConditionDescriptorValue.to_json())

# convert the object into a dict
item_condition_descriptor_value_dict = item_condition_descriptor_value_instance.to_dict()
# create an instance of ItemConditionDescriptorValue from a dict
item_condition_descriptor_value_from_dict = ItemConditionDescriptorValue.from_dict(item_condition_descriptor_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


