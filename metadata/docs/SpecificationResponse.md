# SpecificationResponse

This type defines the fields used in the <b>getCompatibilitiesBySpecification</b> response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compatibility_details** | [**List[Compatibility]**](Compatibility.md) | This container returns the list of all compatible application name-value pairs for the given filter criteria. | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from ebaymetadata.models.specification_response import SpecificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationResponse from a JSON string
specification_response_instance = SpecificationResponse.from_json(json)
# print the JSON string representation of the object
print(SpecificationResponse.to_json())

# convert the object into a dict
specification_response_dict = specification_response_instance.to_dict()
# create an instance of SpecificationResponse from a dict
specification_response_from_dict = SpecificationResponse.from_dict(specification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


