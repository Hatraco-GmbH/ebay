# SalesTaxJurisdiction

A unique ID for a sales tax jurisdiction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_tax_jurisdiction_id** | **str** | The unique ID for a sales-tax jurisdiction.&lt;br&gt;&lt;br&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt; When &lt;code&gt;countryCode&lt;/code&gt; is set to &lt;code&gt;US&lt;/code&gt;, IDs for all 50 states, Washington, DC, and all US territories will be returned. However, the only &lt;code&gt;salesTaxJurisdictionId&lt;/code&gt; values currently supported are:&lt;ul&gt;&lt;li&gt;&lt;code&gt;AS&lt;/code&gt; (American Samoa)&lt;/li&gt;&lt;li&gt;&lt;code&gt;GU&lt;/code&gt; (Guam&lt;/li&gt;&lt;li&gt;&lt;code&gt;MP&lt;/code&gt; Northern Mariana Islands&lt;/li&gt;&lt;li&gt;&lt;code&gt;PW (Palau)&lt;/li&gt;&lt;li&gt;&lt;code&gt;VI&lt;/code&gt; (US Virgin Islands)&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt;&lt;/div&gt; | [optional] 

## Example

```python
from ebaymetadata.models.sales_tax_jurisdiction import SalesTaxJurisdiction

# TODO update the JSON string below
json = "{}"
# create an instance of SalesTaxJurisdiction from a JSON string
sales_tax_jurisdiction_instance = SalesTaxJurisdiction.from_json(json)
# print the JSON string representation of the object
print(SalesTaxJurisdiction.to_json())

# convert the object into a dict
sales_tax_jurisdiction_dict = sales_tax_jurisdiction_instance.to_dict()
# create an instance of SalesTaxJurisdiction from a dict
sales_tax_jurisdiction_from_dict = SalesTaxJurisdiction.from_dict(sales_tax_jurisdiction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


