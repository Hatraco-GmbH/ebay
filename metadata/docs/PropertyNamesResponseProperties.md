# PropertyNamesResponseProperties

This type defines the properties and dataset for a specified category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** | This field defines the types of properties are returned for the specified catalog-enabled category.&lt;br&gt;&lt;br&gt;&lt;b&gt;Valid values:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;&lt;code&gt;DisplayableProductDetails&lt;/code&gt;: Properties for use in a user interface to describe products.&lt;/li&gt;&lt;li&gt;&lt;code&gt;DisplayableSearchResults&lt;/code&gt;: Properties for use in results for product searches.&lt;/li&gt;&lt;li&gt;&lt;code&gt;Searchable&lt;/code&gt;: Properties for use in searches.&lt;/li&gt;&lt;li&gt;&lt;code&gt;Sortable&lt;/code&gt;: Properties that are suitable for sorting.&lt;/li&gt;&lt;/ul&gt; | [optional] 
**property_names** | [**List[PropertyNamesResponsePropertyNames]**](PropertyNamesResponsePropertyNames.md) | This array specifies the names of the properties associated with the specified category in the specified marketplace.&lt;br&gt;&lt;br&gt;For example, typical vehicle property names are &#39;Make&#39;, &#39;Model&#39;, &#39;Year&#39;, &#39;Engine&#39;, and &#39;Trim&#39;, but will vary based on the eBay marketplace and the eBay category. | [optional] 

## Example

```python
from ebaymetadata.models.property_names_response_properties import PropertyNamesResponseProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyNamesResponseProperties from a JSON string
property_names_response_properties_instance = PropertyNamesResponseProperties.from_json(json)
# print the JSON string representation of the object
print(PropertyNamesResponseProperties.to_json())

# convert the object into a dict
property_names_response_properties_dict = property_names_response_properties_instance.to_dict()
# create an instance of PropertyNamesResponseProperties from a dict
property_names_response_properties_from_dict = PropertyNamesResponseProperties.from_dict(property_names_response_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


