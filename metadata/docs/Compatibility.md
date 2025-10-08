# Compatibility

This type defines the property names and values that are compatible with the property name values specified in the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compatibility_details** | [**List[CompatibilityDetails]**](CompatibilityDetails.md) | This array returns a list of compatibility details associated with the specified property name(s). | [optional] 

## Example

```python
from ebaymetadata.models.compatibility import Compatibility

# TODO update the JSON string below
json = "{}"
# create an instance of Compatibility from a JSON string
compatibility_instance = Compatibility.from_json(json)
# print the JSON string representation of the object
print(Compatibility.to_json())

# convert the object into a dict
compatibility_dict = compatibility_instance.to_dict()
# create an instance of Compatibility from a dict
compatibility_from_dict = Compatibility.from_dict(compatibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


