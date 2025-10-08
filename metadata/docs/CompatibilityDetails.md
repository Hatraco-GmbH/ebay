# CompatibilityDetails

This type defines the compatible property names and values associated with the product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** | The name of the property being described. | [optional] 
**property_value** | **str** | The value for the property specified in the &lt;b&gt;propertyName&lt;/b&gt; field. | [optional] 

## Example

```python
from ebaymetadata.models.compatibility_details import CompatibilityDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CompatibilityDetails from a JSON string
compatibility_details_instance = CompatibilityDetails.from_json(json)
# print the JSON string representation of the object
print(CompatibilityDetails.to_json())

# convert the object into a dict
compatibility_details_dict = compatibility_details_instance.to_dict()
# create an instance of CompatibilityDetails from a dict
compatibility_details_from_dict = CompatibilityDetails.from_dict(compatibility_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


