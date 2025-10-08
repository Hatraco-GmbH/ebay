# ProductSafetyLabelStatement

A type that describes statements for product safety labels.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_description** | **str** | The description of the statement localized to the default language of the marketplace.  | [optional] 
**statement_id** | **str** | The identifier of the statement. | [optional] 

## Example

```python
from ebaymetadata.models.product_safety_label_statement import ProductSafetyLabelStatement

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSafetyLabelStatement from a JSON string
product_safety_label_statement_instance = ProductSafetyLabelStatement.from_json(json)
# print the JSON string representation of the object
print(ProductSafetyLabelStatement.to_json())

# convert the object into a dict
product_safety_label_statement_dict = product_safety_label_statement_instance.to_dict()
# create an instance of ProductSafetyLabelStatement from a dict
product_safety_label_statement_from_dict = ProductSafetyLabelStatement.from_dict(product_safety_label_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


