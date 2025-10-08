# AncestorReference

This type contains information about one of the ancestors of a suggested category. An ordered list of these references describes the path from the suggested category to the root of the category tree it belongs to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The unique identifier of the eBay ancestor category.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; The root node of a full default category tree includes the &lt;b&gt;categoryId&lt;/b&gt; field, but its value should not be relied upon. It provides no useful information for application development.&lt;/span&gt; | [optional] 
**category_name** | **str** | The name of the ancestor category identified by &lt;b&gt;categoryId&lt;/b&gt;. | [optional] 
**category_subtree_node_href** | **str** | The href portion of the &lt;b&gt;getCategorySubtree&lt;/b&gt; call that retrieves the subtree below the ancestor category node. | [optional] 
**category_tree_node_level** | **int** | The absolute level of the ancestor category node in the hierarchy of its category tree.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; The root node of any full category tree is always at level &lt;code&gt;&lt;b&gt;0&lt;/b&gt;&lt;/code&gt;. &lt;/span&gt; | [optional] 

## Example

```python
from ebaytaxonomy.models.ancestor_reference import AncestorReference

# TODO update the JSON string below
json = "{}"
# create an instance of AncestorReference from a JSON string
ancestor_reference_instance = AncestorReference.from_json(json)
# print the JSON string representation of the object
print(AncestorReference.to_json())

# convert the object into a dict
ancestor_reference_dict = ancestor_reference_instance.to_dict()
# create an instance of AncestorReference from a dict
ancestor_reference_from_dict = AncestorReference.from_dict(ancestor_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


