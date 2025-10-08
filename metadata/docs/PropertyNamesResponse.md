# PropertyNamesResponse

This type defines the fields returned in the <b>getCompatibilityPropertyNames</b> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The unique identifier of the eBay category specified in the request. | [optional] 
**properties** | [**List[PropertyNamesResponseProperties]**](PropertyNamesResponseProperties.md) | This array contains all of the properties for the specified category. | [optional] 

## Example

```python
from ebaymetadata.models.property_names_response import PropertyNamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyNamesResponse from a JSON string
property_names_response_instance = PropertyNamesResponse.from_json(json)
# print the JSON string representation of the object
print(PropertyNamesResponse.to_json())

# convert the object into a dict
property_names_response_dict = property_names_response_instance.to_dict()
# create an instance of PropertyNamesResponse from a dict
property_names_response_from_dict = PropertyNamesResponse.from_dict(property_names_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


