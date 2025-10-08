# ProductSafetyLabelPictogram

A type that describes pictograms for product safety labels.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pictogram_description** | **str** | The description of the pictogram localized to the default language of the marketplace.  | [optional] 
**pictogram_id** | **str** | The identifier of the pictogram. | [optional] 
**pictogram_url** | **str** | The URL of the pictogram. | [optional] 

## Example

```python
from ebaymetadata.models.product_safety_label_pictogram import ProductSafetyLabelPictogram

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSafetyLabelPictogram from a JSON string
product_safety_label_pictogram_instance = ProductSafetyLabelPictogram.from_json(json)
# print the JSON string representation of the object
print(ProductSafetyLabelPictogram.to_json())

# convert the object into a dict
product_safety_label_pictogram_dict = product_safety_label_pictogram_instance.to_dict()
# create an instance of ProductSafetyLabelPictogram from a dict
product_safety_label_pictogram_from_dict = ProductSafetyLabelPictogram.from_dict(product_safety_label_pictogram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


