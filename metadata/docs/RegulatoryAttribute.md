# RegulatoryAttribute

A type that defines the attributes of a regulatory policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique value identifying a specific regulatory attribute. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:RegulatoryAttributeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**usage** | **str** | The enumeration value in this field indicates whether the corresponding attribute is recommended or required for the corresponding leaf category. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:GenericUsageEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from ebaymetadata.models.regulatory_attribute import RegulatoryAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of RegulatoryAttribute from a JSON string
regulatory_attribute_instance = RegulatoryAttribute.from_json(json)
# print the JSON string representation of the object
print(RegulatoryAttribute.to_json())

# convert the object into a dict
regulatory_attribute_dict = regulatory_attribute_instance.to_dict()
# create an instance of RegulatoryAttribute from a dict
regulatory_attribute_from_dict = RegulatoryAttribute.from_dict(regulatory_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


