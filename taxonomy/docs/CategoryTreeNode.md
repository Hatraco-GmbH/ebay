# CategoryTreeNode

This type contains information about all nodes of a category tree or subtree hierarchy, including and below the specified <b>Category</b>, down to the leaf nodes. It is a recursive structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**Category**](Category.md) |  | [optional] 
**category_tree_node_level** | **int** | The absolute level of the current category tree node in the hierarchy of its category tree.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; The root node of any full category tree is always at level &lt;code&gt;&lt;b&gt;0&lt;/b&gt;&lt;/code&gt;. &lt;/span&gt; | [optional] 
**child_category_tree_nodes** | [**List[CategoryTreeNode]**](CategoryTreeNode.md) | An array of one or more category tree nodes that are the immediate children of the current category tree node, as well as their children, recursively down to the leaf nodes.&lt;br&gt;&lt;br&gt;&lt;i&gt;Returned only if&lt;/i&gt; the current category tree node is not a leaf node (the value of &lt;b&gt;leafCategoryTreeNode&lt;/b&gt; is &lt;code&gt;false&lt;/code&gt;). | [optional] 
**leaf_category_tree_node** | **bool** | A value of &lt;code&gt;true&lt;/code&gt; indicates that the current category tree node is a leaf node (it has no child nodes). A value of &lt;code&gt;false&lt;/code&gt; indicates that the current node has one or more child nodes, which are identified by the &lt;b&gt;childCategoryTreeNodes&lt;/b&gt; array.&lt;br&gt;&lt;br&gt;&lt;i&gt;Returned only if&lt;/i&gt; the value of this field is &lt;code&gt;true&lt;/code&gt;. | [optional] 
**parent_category_tree_node_href** | **str** | The href portion of the &lt;b&gt;getCategorySubtree&lt;/b&gt; call that retrieves the subtree below the parent of this category tree node.&lt;br&gt;&lt;br&gt;&lt;i&gt;Not returned if&lt;/i&gt; the current category tree node is the root node of its tree. | [optional] 

## Example

```python
from ebaytaxonomy.models.category_tree_node import CategoryTreeNode

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryTreeNode from a JSON string
category_tree_node_instance = CategoryTreeNode.from_json(json)
# print the JSON string representation of the object
print(CategoryTreeNode.to_json())

# convert the object into a dict
category_tree_node_dict = category_tree_node_instance.to_dict()
# create an instance of CategoryTreeNode from a dict
category_tree_node_from_dict = CategoryTreeNode.from_dict(category_tree_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


