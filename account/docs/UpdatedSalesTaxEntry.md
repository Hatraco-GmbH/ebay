# UpdatedSalesTaxEntry

This container stores the array of sales-tax table entries that have been created or updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The two-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166&lt;/a&gt; code of the country associated with the sales-tax table entry. | [optional] 
**jurisdiction_id** | **str** | The ID of the tax jurisdiction associated with the sales-tax table entry. | [optional] 
**status_code** | **int** | The HTTP status code for the call.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; The system returns one HTTP status code regardless of the number of sales-tax table entries provided. Therefore, the same HTTP &lt;code&gt;statusCode&lt;/code&gt; will be listed for all sales-tax table entries returned in the payload.&lt;/span&gt; | [optional] 

## Example

```python
from ebayaccount.models.updated_sales_tax_entry import UpdatedSalesTaxEntry

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedSalesTaxEntry from a JSON string
updated_sales_tax_entry_instance = UpdatedSalesTaxEntry.from_json(json)
# print the JSON string representation of the object
print(UpdatedSalesTaxEntry.to_json())

# convert the object into a dict
updated_sales_tax_entry_dict = updated_sales_tax_entry_instance.to_dict()
# create an instance of UpdatedSalesTaxEntry from a dict
updated_sales_tax_entry_from_dict = UpdatedSalesTaxEntry.from_dict(updated_sales_tax_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


