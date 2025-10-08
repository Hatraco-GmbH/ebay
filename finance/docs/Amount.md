# Amount

This type is used to express the dollar value and currency used for any transaction retrieved with the <strong>Finances API</strong>, including an order total, a seller payout, a buyer refund, or a seller credit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**converted_from_currency** | **str** | The three-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 4217&lt;/a&gt; code representing the currency of the amount in the &lt;b&gt; convertedFromValue&lt;/b&gt; field. This value is the pre-conversion currency.&lt;br&gt;&lt;br&gt;This field is only returned if/when currency conversion was applied by eBay. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/finances/types/ba:CurrencyCodeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**converted_from_value** | **str** | The monetary amount before any conversion is performed, in the currency specified by the &lt;b&gt; convertedFromCurrency&lt;/b&gt; field. This value is the pre-conversion amount. The &lt;b&gt; value&lt;/b&gt; field contains the converted amount of this value, in the currency specified by the &lt;b&gt; currency&lt;/b&gt; field.&lt;br&gt;&lt;br&gt;This field is only returned if/when currency conversion was applied by eBay. | [optional] 
**converted_to_currency** | **str** | &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This field is only applicable for Mainland China sellers with an available CNY Bank payment instrument. This response can &lt;b&gt;only&lt;/b&gt; have a value of &lt;code&gt;CNY&lt;/code&gt;.&lt;/span&gt;The three-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 4217&lt;/a&gt; code representing the currency of the amount in the &lt;b&gt;convertedToValue&lt;/b&gt; field. &lt;br/&gt;&lt;br/&gt;This field is only returned for payouts to bank accounts when currency conversion was applied by eBay. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/finances/types/ba:CurrencyCodeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**converted_to_value** | **str** | &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This field is only applicable for Mainland China sellers with an available CNY Bank payment instrument. This response &lt;b&gt;only&lt;/b&gt; returns value in CNY.&lt;/span&gt;The monetary value after any conversion is performed, in the currency specified by the &lt;b&gt;convertedToCurrency&lt;/b&gt; field. This value is the converted amount. &lt;br/&gt;&lt;br/&gt;The field is only returned for payouts to bank accounts when currency conversion was applied by eBay. | [optional] 
**currency** | **str** | A three-letter ISO 4217 code that indicates the currency of the amount in the &lt;b&gt;value&lt;/b&gt; field. This field is always returned with any container using &lt;b&gt;Amount&lt;/b&gt; type. &lt;br&gt;&lt;br&gt;&lt;b&gt;Default&lt;/b&gt;: The currency of the authenticated user&#39;s country. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/finances/types/ba:CurrencyCodeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**exchange_rate** | **str** | The exchange rate used for the monetary conversion. This field shows the exchange rate used to convert the dollar value in the &lt;b&gt;value&lt;/b&gt; field from the dollar value in the &lt;b&gt;convertedFromValue&lt;/b&gt; field.&lt;br&gt;&lt;br&gt; For sellers in mainland China, this field shows shows the exchange rate to convert the dollar value in the &lt;b&gt;value&lt;/b&gt; field to the CNY value in the &lt;b&gt;convertedToValue&lt;/b&gt; field.&lt;br&gt;&lt;br&gt;This field is only returned when eBay does a currency version, and a currency conversion is generally needed if the buyer is viewing, or has purchased an item on an international site. &lt;br&gt;&lt;br&gt;This field is only returned if/when currency conversion was applied by eBay. | [optional] 
**value** | **str** | The monetary amount, in the currency specified by the &lt;b&gt;currency&lt;/b&gt; field. This field is always returned with any container using &lt;b&gt;Amount&lt;/b&gt; type. | [optional] 

## Example

```python
from ebayfinance.models.amount import Amount

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


