# ProductResponseCompatibilityDetails

This type defines the compatibility details for a product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note_details** | [**List[PropertyFilterInner]**](PropertyFilterInner.md) | This array returns additional comments about the corresponding product in the form of name-value pairs. | [optional] 
**product_details** | [**List[PropertyValues]**](PropertyValues.md) | This array returns details about the product in the form of name-value pairs.  | [optional] 

## Example

```python
from ebaymetadata.models.product_response_compatibility_details import ProductResponseCompatibilityDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProductResponseCompatibilityDetails from a JSON string
product_response_compatibility_details_instance = ProductResponseCompatibilityDetails.from_json(json)
# print the JSON string representation of the object
print(ProductResponseCompatibilityDetails.to_json())

# convert the object into a dict
product_response_compatibility_details_dict = product_response_compatibility_details_instance.to_dict()
# create an instance of ProductResponseCompatibilityDetails from a dict
product_response_compatibility_details_from_dict = ProductResponseCompatibilityDetails.from_dict(product_response_compatibility_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


