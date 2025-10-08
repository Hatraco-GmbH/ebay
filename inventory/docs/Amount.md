# Amount

This type is used to express a dollar value and the applicable currency.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | A three-digit string value representing the type of currency being used. Both the &lt;strong&gt;value&lt;/strong&gt; and &lt;strong&gt;currency&lt;/strong&gt; fields are required/always returned when expressing prices. &lt;br&gt;&lt;br&gt;See the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/types/ba:CurrencyCodeEnum\&quot; target&#x3D;\&quot;_blank\&quot;&gt;CurrencyCodeEnum&lt;/a&gt; type for the full list of currencies and their corresponding three-digit string values. | [optional] 
**value** | **str** | A string representation of a dollar value expressed in the currency specified in the &lt;strong&gt;currency&lt;/strong&gt; field. Both the &lt;strong&gt;value&lt;/strong&gt; and &lt;strong&gt;currency&lt;/strong&gt; fields are required/always returned when expressing prices. | [optional] 

## Example

```python
from ebayinventory.models.amount import Amount

# TODO update the JSON string below
json = "{}"
# create an instance of Amount from a JSON string
amount_instance = Amount.from_json(json)
# print the JSON string representation of the object
print(Amount.to_json())

# convert the object into a dict
amount_dict = amount_instance.to_dict()
# create an instance of Amount from a dict
amount_from_dict = Amount.from_dict(amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


