# PropertyFilterInner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** | The name of the property being described.&lt;br&gt;&lt;br&gt;For example, typical vehicle property names are &#x27;Make&#x27;, &#x27;Model&#x27;, &#x27;Year&#x27;, &#x27;Engine&#x27;, and &#x27;Trim&#x27;, but will vary based on the eBay marketplace and the eBay category. Use the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyNames\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getCompatibilityPropertyNames&lt;/a&gt; method to retrieve valid property names for a specified category. | [optional] 
**property_value** | **str** | The value for the property specified in the &lt;b&gt;properyName&lt;/b&gt; field.&lt;br&gt;&lt;br&gt;For example, if the &lt;b&gt;propertyName&lt;/b&gt; is &lt;code&gt;Make&lt;/code&gt;, then the &lt;b&gt;propertyValue&lt;/b&gt; will be the specific make of the vehicle, such as &lt;code&gt;Toyota&lt;/code&gt;. Use the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyValues\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getCompatibilityPropertyValues&lt;/a&gt; to retreive valid property values associated with a specified property name. | [optional] 
**unit_of_measurement** | **str** | The unit of measurement of the property being described, if applicable. | [optional] 
**url** | **str** | The URL associated with the property being described, if applicable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

