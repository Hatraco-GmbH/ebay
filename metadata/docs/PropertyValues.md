# PropertyValues

This type defines the name-value pair associated with a property value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** | The name of the property.&lt;br&gt;&lt;br&gt;For example, typical vehicle property names are &#39;Make&#39;, &#39;Model&#39;, &#39;Year&#39;, &#39;Engine&#39;, and &#39;Trim&#39;, but will vary based on the eBay marketplace and the eBay category. | [optional] 
**property_value** | **str** | The value for the property specified in the &lt;b&gt;properyName&lt;/b&gt; field.&lt;br&gt;&lt;br&gt;For example, if the &lt;b&gt;propertyName&lt;/b&gt; is &lt;code&gt;make&lt;/code&gt;, then the &lt;b&gt;propertyValue&lt;/b&gt; will be the specific make of the vehicle, such as &lt;code&gt;Toyota&lt;/code&gt;. | [optional] 

## Example

```python
from ebaymetadata.models.property_values import PropertyValues

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyValues from a JSON string
property_values_instance = PropertyValues.from_json(json)
# print the JSON string representation of the object
print(PropertyValues.to_json())

# convert the object into a dict
property_values_dict = property_values_instance.to_dict()
# create an instance of PropertyValues from a dict
property_values_from_dict = PropertyValues.from_dict(property_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


