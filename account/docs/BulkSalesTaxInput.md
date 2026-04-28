# BulkSalesTaxInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_tax_input_list** | [**List[SalesTaxInput]**](SalesTaxInput.md) | The array of sales-tax table entries to be created or updated. | [optional] 

## Example

```python
from ebayaccount.models.bulk_sales_tax_input import BulkSalesTaxInput

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSalesTaxInput from a JSON string
bulk_sales_tax_input_instance = BulkSalesTaxInput.from_json(json)
# print the JSON string representation of the object
print(BulkSalesTaxInput.to_json())

# convert the object into a dict
bulk_sales_tax_input_dict = bulk_sales_tax_input_instance.to_dict()
# create an instance of BulkSalesTaxInput from a dict
bulk_sales_tax_input_from_dict = BulkSalesTaxInput.from_dict(bulk_sales_tax_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


