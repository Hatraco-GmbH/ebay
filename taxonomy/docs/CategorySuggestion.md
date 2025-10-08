# CategorySuggestion

This type contains information about a suggested category tree leaf node that corresponds to keywords provided in the request. It includes details about each of the category's ancestor nodes extending up to the root of the category tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**Category**](Category.md) |  | [optional] 
**category_tree_node_ancestors** | [**List[AncestorReference]**](AncestorReference.md) | An ordered list of category references that describes the location of the suggested category in the specified category tree. The list identifies the category&#39;s ancestry as a sequence of parent nodes, from the current node&#39;s immediate parent to the root node of the category tree.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; The root node of a full default category tree includes &lt;b&gt;categoryId&lt;/b&gt; and &lt;b&gt;categoryName&lt;/b&gt; fields, but their values should not be relied upon. They provide no useful information for application development.&lt;/span&gt; | [optional] 
**category_tree_node_level** | **int** | The absolute level of the category tree node in the hierarchy of its category tree.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; The root node of any full category tree is always at level &lt;code&gt;&lt;b&gt;0&lt;/b&gt;&lt;/code&gt;.&lt;/span&gt; | [optional] 
**relevancy** | **str** | This field is reserved for internal or future use. | [optional] 

## Example

```python
from ebaytaxonomy.models.category_suggestion import CategorySuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of CategorySuggestion from a JSON string
category_suggestion_instance = CategorySuggestion.from_json(json)
# print the JSON string representation of the object
print(CategorySuggestion.to_json())

# convert the object into a dict
category_suggestion_dict = category_suggestion_instance.to_dict()
# create an instance of CategorySuggestion from a dict
category_suggestion_from_dict = CategorySuggestion.from_dict(category_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


