# DisabledProductFilter

This type defines the booleans used to determine if a product is excluded from eBay selling and/or review.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_for_ebay_reviews** | **bool** | Specifies whether to filter out products excluded for eBay reviews.&lt;br&gt;&lt;br&gt;If set to &lt;code&gt;true&lt;/code&gt;, items excluded from eBay reviews are not returned. | [optional] 
**exclude_for_ebay_selling** | **bool** | Specifies whether to filter out products excluded for eBay selling.&lt;br&gt;&lt;br&gt;If set to &lt;code&gt;true&lt;/code&gt;, items excluded from eBay selling are not returned. | [optional] 

## Example

```python
from ebaymetadata.models.disabled_product_filter import DisabledProductFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DisabledProductFilter from a JSON string
disabled_product_filter_instance = DisabledProductFilter.from_json(json)
# print the JSON string representation of the object
print(DisabledProductFilter.to_json())

# convert the object into a dict
disabled_product_filter_dict = disabled_product_filter_instance.to_dict()
# create an instance of DisabledProductFilter from a dict
disabled_product_filter_from_dict = DisabledProductFilter.from_dict(disabled_product_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


