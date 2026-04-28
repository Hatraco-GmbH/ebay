# SalesTaxInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | This parameter specifies the two-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166&lt;/a&gt; code of the country for which a sales-tax table entry is to be created or updated.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Sales-tax tables are available only for the US and Canada marketplaces. Therefore, the only supported values are:&lt;ul&gt;&lt;li&gt;&lt;code&gt;US&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;CA&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt; | [optional] 
**sales_tax_jurisdiction_id** | **str** | This parameter specifies the ID of the tax jurisdiction for which a sales-tax table entry is to be created or updated.&lt;br&gt;&lt;br&gt;Valid jurisdiction IDs can be retrieved using the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/country/methods/getSalesTaxJurisdictions\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getSalesTaxJurisdiction&lt;/a&gt; method of the Metadata API.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; When &lt;code&gt;countryCode&lt;/code&gt; is set to &lt;code&gt;US&lt;/code&gt;, the only supported values for &lt;code&gt;jurisdictionId&lt;/code&gt; are:&lt;ul&gt;&lt;li&gt;&lt;code&gt;AS&lt;/code&gt; (American Samoa)&lt;/li&gt;&lt;li&gt;&lt;code&gt;GU&lt;/code&gt; (Guam)&lt;/li&gt;&lt;li&gt;&lt;code&gt;MP&lt;/code&gt; (Northern Mariana Islands)&lt;/li&gt;&lt;li&gt;&lt;code&gt;PW&lt;/code&gt; (Palau)&lt;/li&gt;&lt;li&gt;&lt;code&gt;VI&lt;/code&gt; (US Virgin Islands)&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt; | [optional] 
**sales_tax_percentage** | **str** | This parameter specifies the sales tax rate for the specified &lt;b&gt;salesTaxJurisdictionId&lt;/b&gt;. When applicable to an order, this sales tax rate will be applied to the sales price. The &lt;b&gt;shippingAndHandlingTaxed&lt;/b&gt; value indicates whether or not sales tax is also applied to shipping and handling charges&lt;br&gt;&lt;br&gt;Although it is a string, a percentage value is set here, such as &lt;code&gt;7.75&lt;/code&gt;. | [optional] 
**shipping_and_handling_taxed** | **bool** | This parameter is set to &lt;code&gt;true&lt;/code&gt; if the seller wishes to apply sales tax to shipping and handling charges and not just the total sales price of an order. Otherwise, this parameter&#39;s value should be set to &lt;code&gt;false&lt;/code&gt;. | [optional] 

## Example

```python
from ebayaccount.models.sales_tax_input import SalesTaxInput

# TODO update the JSON string below
json = "{}"
# create an instance of SalesTaxInput from a JSON string
sales_tax_input_instance = SalesTaxInput.from_json(json)
# print the JSON string representation of the object
print(SalesTaxInput.to_json())

# convert the object into a dict
sales_tax_input_dict = sales_tax_input_instance.to_dict()
# create an instance of SalesTaxInput from a dict
sales_tax_input_from_dict = SalesTaxInput.from_dict(sales_tax_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


