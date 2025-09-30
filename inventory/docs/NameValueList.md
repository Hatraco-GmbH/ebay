# NameValueList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This string value identifies the motor vehicle aspect, such as &#x27;make&#x27;, &#x27;model&#x27;, &#x27;year&#x27;, &#x27;trim&#x27;, and &#x27;engine&#x27;. Typically, the make, model, and year of the motor vehicle are always required, with the trim and engine being necessary sometimes, but it will be dependent on the part or accessory, and on the vehicle class.&lt;br&gt;&lt;br&gt;The &lt;a href&#x3D;\&quot;/api-docs/commerce/taxonomy/resources/category_tree/methods/getCompatibilityProperties\&quot; target&#x3D;\&quot;_blank\&quot;&gt;getCompatibilityProperties&lt;/a&gt; method of the Taxonomy API can be used to retrieve applicable vehicle aspect names for a specified category. | [optional] 
**value** | **str** | This string value identifies the motor vehicle aspect specified in the corresponding &lt;strong&gt;name&lt;/strong&gt; field. For example, if the &lt;strong&gt;name&lt;/strong&gt; field is &#x27;make&#x27;, this field may be &#x27;Toyota&#x27;, or if the &lt;strong&gt;name&lt;/strong&gt; field is &#x27;model&#x27;, this field may be &#x27;Camry&#x27;.&lt;br&gt;&lt;br&gt;The &lt;a href&#x3D;\&quot;/api-docs/commerce/taxonomy/resources/category_tree/methods/getCompatibilityPropertyValues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;getCompatibilityPropertyValues&lt;/a&gt; method of the Taxonomy API can be used to retrieve possible values for vehicle aspect names. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

