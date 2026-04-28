# SalesTaxes

This type is used by the root response of the <b>getSalesTaxes</b> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_taxes** | [**List[SalesTax]**](SalesTax.md) | An array of one or more sales-tax rate entries for a specified country.&lt;br&gt;&lt;br&gt;If no sales-tax rate entries are set up, no response payload is returned, but an HTTP status code of &lt;code&gt;204 No Content&lt;/code&gt; is returned. | [optional] 

## Example

```python
from ebayaccount.models.sales_taxes import SalesTaxes

# TODO update the JSON string below
json = "{}"
# create an instance of SalesTaxes from a JSON string
sales_taxes_instance = SalesTaxes.from_json(json)
# print the JSON string representation of the object
print(SalesTaxes.to_json())

# convert the object into a dict
sales_taxes_dict = sales_taxes_instance.to_dict()
# create an instance of SalesTaxes from a dict
sales_taxes_from_dict = SalesTaxes.from_dict(sales_taxes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


