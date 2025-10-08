# PropertyValuesRequest

This type defines the request fields used in the <b>getCompatibilityPropertyValues</b> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The unique identifier of the eBay leaf category for which to retrieve compatibility property values. This category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/marketplace/methods/getAutomotivePartsCompatibilityPolicies\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAutomotivePartsCompatibilityPolicies&lt;/a&gt; method to retrieve a list of categories that support parts compatibility. | [optional] 
**property_filters** | [**List[PropertyFilterInner]**](PropertyFilterInner.md) | This array can be used to specify the compatibility properties used limit the result set. Only values associated with the specified name-value pairs will be returned in the response.&lt;br&gt;&lt;br&gt;For example, if the &lt;b&gt;propertyName&lt;/b&gt; is set to &lt;code&gt;Make&lt;/code&gt; and the &lt;b&gt;propertyValue&lt;/b&gt; is set to &lt;code&gt;Honda&lt;/code&gt;, only compatible Honda vehicles will be returned. | [optional] 
**property_name** | **str** | This field specifies the name of the property for which to retrieve associated property values.&lt;br&gt;&lt;br&gt;For example, typical vehicle property names are &#39;Make&#39;, &#39;Model&#39;, &#39;Year&#39;, &#39;Engine&#39;, and &#39;Trim&#39;, but will vary based on the eBay marketplace and the eBay category. Use the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyNames\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getCompatibilityPropertyNames&lt;/a&gt; method to retrieve valid property names for a specified category. | [optional] 
**sort_order** | **str** | This field specifies the sort order for the property values in the result set.&lt;br&gt;&lt;br&gt;&lt;b&gt;Valid values:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;&lt;code&gt;Ascending&lt;/code&gt;&lt;/li&gt;&lt;li&gt;Descending&lt;/li&gt;&lt;/ul&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If no search order is specified, values are sorted in ascending order.&lt;/span&gt; | [optional] 

## Example

```python
from ebaymetadata.models.property_values_request import PropertyValuesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyValuesRequest from a JSON string
property_values_request_instance = PropertyValuesRequest.from_json(json)
# print the JSON string representation of the object
print(PropertyValuesRequest.to_json())

# convert the object into a dict
property_values_request_dict = property_values_request_instance.to_dict()
# create an instance of PropertyValuesRequest from a dict
property_values_request_from_dict = PropertyValuesRequest.from_dict(property_values_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


