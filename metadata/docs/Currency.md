# Currency

The type defining valid currencies for the marketplace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The three-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 4217&lt;/a&gt; code returned.  &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Restriction: &lt;/b&gt; Only the currency of the marketplace is supported. Examples: on the US marketplace, the only currency supported is the United States dollar, &lt;code&gt;USD&lt;/code&gt;; on the Canadian marketplace, the only currency supported is the Canadian dollar, &lt;code&gt;CAD&lt;/code&gt;. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/bas:CurrencyCodeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**description** | **str** | The description of the returned three-letter code. For example, if the code is &lt;code&gt;USD&lt;/code&gt;, the description returned would be &lt;code&gt;US Dollar&lt;/code&gt;. | [optional] 

## Example

```python
from ebaymetadata.models.currency import Currency

# TODO update the JSON string below
json = "{}"
# create an instance of Currency from a JSON string
currency_instance = Currency.from_json(json)
# print the JSON string representation of the object
print(Currency.to_json())

# convert the object into a dict
currency_dict = currency_instance.to_dict()
# create an instance of Currency from a dict
currency_from_dict = Currency.from_dict(currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


