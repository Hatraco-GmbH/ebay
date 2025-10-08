# ModelProperty

This type defines the property name and value for an order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_display_name** | **str** | The display name of the motor vehicle aspect. This is the localized name of the compatibility property. | [optional] 
**property_name** | **str** | The name of the motor vehicle aspect.&lt;br&gt;&lt;br&gt;For example, typical vehicle property names are &#39;Make&#39;, &#39;Model&#39;, &#39;Year&#39;, &#39;Engine&#39;, and &#39;Trim&#39;, but will vary based on the eBay marketplace and the eBay category. | [optional] 
**property_value** | **str** | The value of the property specified in the &lt;b&gt;propertyName&lt;/b&gt; field.&lt;br&gt;&lt;br&gt;For example, if the &lt;b&gt;propertyName&lt;/b&gt; is &lt;code&gt;Make&lt;/code&gt;, then the &lt;b&gt;propertyValue&lt;/b&gt; will be the specific make of the vehicle, such as &lt;code&gt;Toyota&lt;/code&gt;. | [optional] 

## Example

```python
from ebayfulfillment.models.model_property import ModelProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ModelProperty from a JSON string
model_property_instance = ModelProperty.from_json(json)
# print the JSON string representation of the object
print(ModelProperty.to_json())

# convert the object into a dict
model_property_dict = model_property_instance.to_dict()
# create an instance of ModelProperty from a dict
model_property_from_dict = ModelProperty.from_dict(model_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


