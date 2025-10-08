# Fee

This type is used to express expected listing fees that the seller may incur for one or more unpublished offers, as well as any eBay-related promotional discounts being applied toward a specific fee. These fees are the expected cumulative fees per eBay marketplace (which is indicated in the <strong>marketplaceId</strong> field).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) |  | [optional] 
**fee_type** | **str** | The value returned in this field indicates the type of listing fee that the seller may incur if one or more unpublished offers (offers are specified in the call request) are published on the marketplace specified in the &lt;strong&gt;marketplaceId&lt;/strong&gt; field. Applicable listing fees will often include things such as &lt;code&gt;InsertionFee&lt;/code&gt; or &lt;code&gt;SubtitleFee&lt;/code&gt;, but many fee types will get returned even when they are &lt;code&gt;0.0&lt;/code&gt;.&lt;br&gt;&lt;br&gt;See the &lt;a href&#x3D;\&quot;https://pages.ebay.com/help/sell/fees.html \&quot; target&#x3D;\&quot;_blank\&quot;&gt;Standard selling fees&lt;/a&gt; help page for more information on listing fees. | [optional] 
**promotional_discount** | [**Amount**](Amount.md) |  | [optional] 

## Example

```python
from ebayinventory.models.fee import Fee

# TODO update the JSON string below
json = "{}"
# create an instance of Fee from a JSON string
fee_instance = Fee.from_json(json)
# print the JSON string representation of the object
print(Fee.to_json())

# convert the object into a dict
fee_dict = fee_instance.to_dict()
# create an instance of Fee from a dict
fee_from_dict = Fee.from_dict(fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


