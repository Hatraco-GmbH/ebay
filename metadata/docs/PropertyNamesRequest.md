# PropertyNamesRequest

This type defines the request fields for the <b>getCompatibilityPropertyNames</b> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The unique identifier of the eBay leaf category for which to retrieve compatibility property names. This category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/marketplace/methods/getAutomotivePartsCompatibilityPolicies\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAutomotivePartsCompatibilityPolicies&lt;/a&gt; method to retrieve a list of categories that support parts compatibility. | [optional] 
**dataset** | **List[str]** | This array defines the properties that will be returned for the compatibility-enabled category.&lt;br&gt;&lt;br&gt; For example, if you specify &lt;code&gt;Searchable&lt;/code&gt;, the compatibility details will contain properties that can be used to search for products, such as make or model.&lt;br&gt;&lt;br&gt;&lt;b&gt;Valid values:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;&lt;code&gt;DisplayableProductDetails&lt;/code&gt;: Properties for use in a user interface to describe products.&lt;/li&gt;&lt;li&gt;&lt;code&gt;DisplayableSearchResults&lt;/code&gt;: Properties for use in results for product searches.&lt;/li&gt;&lt;li&gt;&lt;code&gt;Searchable&lt;/code&gt;: Properties for use in searches.&lt;/li&gt;&lt;li&gt;&lt;code&gt;Sortable&lt;/code&gt;: Properties that are suitable for sorting.&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Default:&lt;/b&gt; &lt;code&gt;DisplayableSearchResults&lt;/code&gt; | [optional] 

## Example

```python
from ebaymetadata.models.property_names_request import PropertyNamesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyNamesRequest from a JSON string
property_names_request_instance = PropertyNamesRequest.from_json(json)
# print the JSON string representation of the object
print(PropertyNamesRequest.to_json())

# convert the object into a dict
property_names_request_dict = property_names_request_instance.to_dict()
# create an instance of PropertyNamesRequest from a dict
property_names_request_from_dict = PropertyNamesRequest.from_dict(property_names_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


