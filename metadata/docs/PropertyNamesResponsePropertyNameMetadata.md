# PropertyNamesResponsePropertyNameMetadata

This type defines the property name metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_sequence** | **int** | The numeric value indicating the ordering position of the property. | [optional] 

## Example

```python
from ebaymetadata.models.property_names_response_property_name_metadata import PropertyNamesResponsePropertyNameMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyNamesResponsePropertyNameMetadata from a JSON string
property_names_response_property_name_metadata_instance = PropertyNamesResponsePropertyNameMetadata.from_json(json)
# print the JSON string representation of the object
print(PropertyNamesResponsePropertyNameMetadata.to_json())

# convert the object into a dict
property_names_response_property_name_metadata_dict = property_names_response_property_name_metadata_instance.to_dict()
# create an instance of PropertyNamesResponsePropertyNameMetadata from a dict
property_names_response_property_name_metadata_from_dict = PropertyNamesResponsePropertyNameMetadata.from_dict(property_names_response_property_name_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


