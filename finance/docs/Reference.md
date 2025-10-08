# Reference

This field is returned for NON_SALE_CHARGE transactions that contain non-transactional seller fees.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **str** | The identifier of the transaction as specified by the &lt;strong&gt;referenceType&lt;/strong&gt;. For example, with a &lt;strong&gt;referenceType&lt;/strong&gt; of &lt;strong&gt;item_id&lt;/strong&gt;, the &lt;strong&gt;referenceId&lt;/strong&gt; refers to a unique item. This item may have several &lt;code&gt;NON_SALE_CHARGE&lt;/code&gt; transactions. | [optional] 
**reference_type** | **str** | An enumeration value that identifies the reference type associated with the &lt;strong&gt;referenceId&lt;/strong&gt;. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/finances/types/pay:ReferenceTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from ebayfinance.models.reference import Reference

# TODO update the JSON string below
json = "{}"
# create an instance of Reference from a JSON string
reference_instance = Reference.from_json(json)
# print the JSON string representation of the object
print(Reference.to_json())

# convert the object into a dict
reference_dict = reference_instance.to_dict()
# create an instance of Reference from a dict
reference_from_dict = Reference.from_dict(reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


