# PropertyFilterInner

This type is used to define the available compatibility property filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** | The name of the property being described.&lt;br&gt;&lt;br&gt;For example, typical vehicle property names are &#39;Make&#39;, &#39;Model&#39;, &#39;Year&#39;, &#39;Engine&#39;, and &#39;Trim&#39;, but will vary based on the eBay marketplace and the eBay category. Use the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyNames\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getCompatibilityPropertyNames&lt;/a&gt; method to retrieve valid property names for a specified category. | [optional] 
**property_value** | **str** | The value for the property specified in the &lt;b&gt;properyName&lt;/b&gt; field.&lt;br&gt;&lt;br&gt;For example, if the &lt;b&gt;propertyName&lt;/b&gt; is &lt;code&gt;Make&lt;/code&gt;, then the &lt;b&gt;propertyValue&lt;/b&gt; will be the specific make of the vehicle, such as &lt;code&gt;Toyota&lt;/code&gt;. Use the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyValues\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getCompatibilityPropertyValues&lt;/a&gt; to retreive valid property values associated with a specified property name. | [optional] 
**unit_of_measurement** | **str** | The unit of measurement of the property being described, if applicable. | [optional] 
**url** | **str** | The URL associated with the property being described, if applicable. | [optional] 

## Example

```python
from ebaymetadata.models.property_filter_inner import PropertyFilterInner

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyFilterInner from a JSON string
property_filter_inner_instance = PropertyFilterInner.from_json(json)
# print the JSON string representation of the object
print(PropertyFilterInner.to_json())

# convert the object into a dict
property_filter_inner_dict = property_filter_inner_instance.to_dict()
# create an instance of PropertyFilterInner from a dict
property_filter_inner_from_dict = PropertyFilterInner.from_dict(property_filter_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


