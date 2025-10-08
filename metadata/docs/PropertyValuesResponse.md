# PropertyValuesResponse

This type defines the response fields used in the <b>getCompatibilityPropertyValues</b> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_version** | **str** | The version number of the metadata. This version is upticked whenever there are compatibility name changes for the specified marketplace. | [optional] 
**property_name** | **str** | The name of the property specified in the request. | [optional] 
**property_values** | **List[str]** | This array specifies the property values associated with the specified &lt;b&gt;propertyName&lt;/b&gt;, in the specified category. | [optional] 

## Example

```python
from ebaymetadata.models.property_values_response import PropertyValuesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyValuesResponse from a JSON string
property_values_response_instance = PropertyValuesResponse.from_json(json)
# print the JSON string representation of the object
print(PropertyValuesResponse.to_json())

# convert the object into a dict
property_values_response_dict = property_values_response_instance.to_dict()
# create an instance of PropertyValuesResponse from a dict
property_values_response_from_dict = PropertyValuesResponse.from_dict(property_values_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


