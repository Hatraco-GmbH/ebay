# ConditionDescriptor

This type is used by the seller to provide additional information about the condition of an item in a structured format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **str** | This string provides additional information about a condition descriptor. Open text is passed in this field.&lt;br&gt;&lt;br&gt;In the case of trading cards, this field houses the optional &lt;b&gt;Certification Number&lt;/b&gt; condition descriptor for graded cards. &lt;br&gt;&lt;br&gt;&lt;b&gt;Max Length:&lt;/b&gt; 30 characters | [optional] 
**name** | **str** | This string provides the name of a condition descriptor. A numeric ID is passed in this field. This numeric ID maps to the name of a condition descriptor. Condition descriptor name-value pairs provide more information about an item&#39;s condition in a structured way. &lt;br&gt;&lt;br&gt;To retrieve all condition descriptor name numeric IDs for a category, refer to the &lt;b&gt;conditionDescriptorId&lt;/b&gt; field returned in the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/marketplace/methods/getItemConditionPolicies \&quot; target&#x3D;\&quot;_blank\&quot;&gt;getItemConditionPolicies&lt;/a&gt; method of Metadata API. &lt;br&gt;&lt;br&gt;In the case of trading cards, this field is used to provide condition descriptors for a card. For graded cards, the condition descriptors for &lt;b&gt;Grader&lt;/b&gt; and &lt;b&gt;Grade&lt;/b&gt; are required, while the condition descriptor for &lt;b&gt;Certification Number&lt;/b&gt; is optional. For ungraded cards, only the &lt;b&gt;Card Condition&lt;/b&gt; condition descriptor is required. | [optional] 
**values** | **List[str]** | This array provides the value(s) associated with a condition descriptor. One or more numeric IDs is passed in this field. Commas are used as delimiters between successive name/value pairs. These numeric IDs map to the values associated with a condition descriptor name. Condition descriptor name-value pairs provide more information about an item&#39;s condition in a structured way. &lt;br&gt;&lt;br&gt;To retrieve all condition descriptor value numeric IDs for a category, refer to the &lt;b&gt;ConditionDescriptorValueId&lt;/b&gt; array returned in the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/marketplace/methods/getItemConditionPolicies \&quot; target&#x3D;\&quot;_blank\&quot;&gt;getItemConditionPolicies&lt;/a&gt; method of Metadata API. &lt;br&gt;&lt;br&gt;In the case of trading cards, this field houses the information on the &lt;b&gt;Grader&lt;/b&gt; and &lt;b&gt;Grade&lt;/b&gt; descriptors of graded cards and the &lt;b&gt;Card Condition&lt;/b&gt; descriptor for ungraded cards. | [optional] 

## Example

```python
from ebayinventory.models.condition_descriptor import ConditionDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionDescriptor from a JSON string
condition_descriptor_instance = ConditionDescriptor.from_json(json)
# print the JSON string representation of the object
print(ConditionDescriptor.to_json())

# convert the object into a dict
condition_descriptor_dict = condition_descriptor_instance.to_dict()
# create an instance of ConditionDescriptor from a dict
condition_descriptor_from_dict = ConditionDescriptor.from_dict(condition_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


