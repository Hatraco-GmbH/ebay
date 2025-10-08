# PropertyNamesResponsePropertyNames

This type defines the fields associated with a property name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_display_name** | **str** | The display name of a property. This is the localized name of the compatible property. | [optional] 
**property_name** | **str** | The canonical name of a property. This value is used as part of the name-value pairs used to specify compatibility. | [optional] 
**property_name_metadata** | [**PropertyNamesResponsePropertyNameMetadata**](PropertyNamesResponsePropertyNameMetadata.md) |  | [optional] 

## Example

```python
from ebaymetadata.models.property_names_response_property_names import PropertyNamesResponsePropertyNames

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyNamesResponsePropertyNames from a JSON string
property_names_response_property_names_instance = PropertyNamesResponsePropertyNames.from_json(json)
# print the JSON string representation of the object
print(PropertyNamesResponsePropertyNames.to_json())

# convert the object into a dict
property_names_response_property_names_dict = property_names_response_property_names_instance.to_dict()
# create an instance of PropertyNamesResponsePropertyNames from a dict
property_names_response_property_names_from_dict = PropertyNamesResponsePropertyNames.from_dict(property_names_response_property_names_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


