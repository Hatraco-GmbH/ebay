# UpdatedSalesTaxResponse

This type is used to return the list of new and updated sales-tax table entries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_sales_tax_entries** | [**List[UpdatedSalesTaxEntry]**](UpdatedSalesTaxEntry.md) | The array of new and updated sales-tax table entries. | [optional] 

## Example

```python
from ebayaccount.models.updated_sales_tax_response import UpdatedSalesTaxResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedSalesTaxResponse from a JSON string
updated_sales_tax_response_instance = UpdatedSalesTaxResponse.from_json(json)
# print the JSON string representation of the object
print(UpdatedSalesTaxResponse.to_json())

# convert the object into a dict
updated_sales_tax_response_dict = updated_sales_tax_response_instance.to_dict()
# create an instance of UpdatedSalesTaxResponse from a dict
updated_sales_tax_response_from_dict = UpdatedSalesTaxResponse.from_dict(updated_sales_tax_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


