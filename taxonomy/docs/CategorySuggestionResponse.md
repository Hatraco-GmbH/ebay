# CategorySuggestionResponse

This type contains an array of suggested category tree nodes that are considered by eBay to most closely correspond to the keywords provided in a query string, from a specified category tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_suggestions** | [**List[CategorySuggestion]**](CategorySuggestion.md) | Contains details about one or more suggested categories that correspond to the provided keywords. The array of suggested categories is sorted in order of eBay&#39;s confidence of the relevance of each category (the first category is the most relevant).&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;&lt;span style&#x3D;\&quot;color:red\&quot;&gt;Important:&lt;/span&gt;&lt;/strong&gt; This call is not supported in the Sandbox environment. It will return a response payload in which the &lt;b&gt;categoryName&lt;/b&gt; fields contain random or boilerplate text regardless of the query submitted. &lt;/span&gt; | [optional] 
**category_tree_id** | **str** | The unique identifier of the eBay category tree from which suggestions are returned. | [optional] 
**category_tree_version** | **str** | The version of the category tree identified by &lt;b&gt;categoryTreeId&lt;/b&gt;. It&#39;s a good idea to cache this value for comparison so you can determine if this category tree has been modified in subsequent calls. | [optional] 

## Example

```python
from ebaytaxonomy.models.category_suggestion_response import CategorySuggestionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CategorySuggestionResponse from a JSON string
category_suggestion_response_instance = CategorySuggestionResponse.from_json(json)
# print the JSON string representation of the object
print(CategorySuggestionResponse.to_json())

# convert the object into a dict
category_suggestion_response_dict = category_suggestion_response_instance.to_dict()
# create an instance of CategorySuggestionResponse from a dict
category_suggestion_response_from_dict = CategorySuggestionResponse.from_dict(category_suggestion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


