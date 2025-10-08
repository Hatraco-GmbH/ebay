# MultiCompatibilityPropertyValuesResponse

This type defines the response fields for the <b>getMultiCompatibilityPropertyValues</b> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compatibilities** | [**List[Compatibility]**](Compatibility.md) | This container defines the compatibility details associated with the specified property name value(s). | [optional] 
**metadata_version** | **str** | The version number of the metadata. This version is upticked whenever there are compatibility name changes for the specified marketplace. | [optional] 

## Example

```python
from ebaymetadata.models.multi_compatibility_property_values_response import MultiCompatibilityPropertyValuesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultiCompatibilityPropertyValuesResponse from a JSON string
multi_compatibility_property_values_response_instance = MultiCompatibilityPropertyValuesResponse.from_json(json)
# print the JSON string representation of the object
print(MultiCompatibilityPropertyValuesResponse.to_json())

# convert the object into a dict
multi_compatibility_property_values_response_dict = multi_compatibility_property_values_response_instance.to_dict()
# create an instance of MultiCompatibilityPropertyValuesResponse from a dict
multi_compatibility_property_values_response_from_dict = MultiCompatibilityPropertyValuesResponse.from_dict(multi_compatibility_property_values_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


