# ProductSafetyLabelsResponse

A type that defines the response fields for the <b>getProductSafetyLabels</b> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pictograms** | [**List[ProductSafetyLabelPictogram]**](ProductSafetyLabelPictogram.md) | This array contains a list of pictograms of product safety labels  for the specified marketplace. | [optional] 
**statements** | [**List[ProductSafetyLabelStatement]**](ProductSafetyLabelStatement.md) | This array contains available product safety labels statements for the specified marketplace.  | [optional] 

## Example

```python
from ebaymetadata.models.product_safety_labels_response import ProductSafetyLabelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSafetyLabelsResponse from a JSON string
product_safety_labels_response_instance = ProductSafetyLabelsResponse.from_json(json)
# print the JSON string representation of the object
print(ProductSafetyLabelsResponse.to_json())

# convert the object into a dict
product_safety_labels_response_dict = product_safety_labels_response_instance.to_dict()
# create an instance of ProductSafetyLabelsResponse from a dict
product_safety_labels_response_from_dict = ProductSafetyLabelsResponse.from_dict(product_safety_labels_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


