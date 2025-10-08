# SortOrderProperties

This type is used to define the property to be used in sorting. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **str** | Defines the order of the sort.&lt;br&gt;&lt;br&gt;&lt;b&gt;Valid values&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;&lt;code&gt;Ascending&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;Descending&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 
**property_name** | **str** | The name of the searchable property to be used for sorting.&lt;br&gt;&lt;br&gt;For example, typical vehicle property names are &#39;Make&#39;, &#39;Model&#39;, &#39;Year&#39;, &#39;Engine&#39;, and &#39;Trim&#39;, but will vary based on the eBay marketplace and the eBay category. | [optional] 

## Example

```python
from ebaymetadata.models.sort_order_properties import SortOrderProperties

# TODO update the JSON string below
json = "{}"
# create an instance of SortOrderProperties from a JSON string
sort_order_properties_instance = SortOrderProperties.from_json(json)
# print the JSON string representation of the object
print(SortOrderProperties.to_json())

# convert the object into a dict
sort_order_properties_dict = sort_order_properties_instance.to_dict()
# create an instance of SortOrderProperties from a dict
sort_order_properties_from_dict = SortOrderProperties.from_dict(sort_order_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


