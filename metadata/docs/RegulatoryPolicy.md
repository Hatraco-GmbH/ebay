# RegulatoryPolicy

A type that defines the regulatory policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The unique identifier of the leaf category to which the corresponding policies pertain. | [optional] 
**category_tree_id** | **str** | The unique identifier of the category tree, which reflects the specified marketplace. | [optional] 
**supported_attributes** | [**List[RegulatoryAttribute]**](RegulatoryAttribute.md) | A list of supported regulatory attributes for this marketplace. | [optional] 

## Example

```python
from ebaymetadata.models.regulatory_policy import RegulatoryPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of RegulatoryPolicy from a JSON string
regulatory_policy_instance = RegulatoryPolicy.from_json(json)
# print the JSON string representation of the object
print(RegulatoryPolicy.to_json())

# convert the object into a dict
regulatory_policy_dict = regulatory_policy_instance.to_dict()
# create an instance of RegulatoryPolicy from a dict
regulatory_policy_from_dict = RegulatoryPolicy.from_dict(regulatory_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


