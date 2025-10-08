# Category

This type contains information about a particular eBay category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The unique identifier of the eBay category within its category tree.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; The root node of a full default category tree includes the &lt;b&gt;categoryId&lt;/b&gt; field, but its value should not be relied upon. It provides no useful information for application development. &lt;/span&gt; | [optional] 
**category_name** | **str** | The name of the category identified by &lt;b&gt;categoryId&lt;/b&gt;. | [optional] 

## Example

```python
from ebaytaxonomy.models.category import Category

# TODO update the JSON string below
json = "{}"
# create an instance of Category from a JSON string
category_instance = Category.from_json(json)
# print the JSON string representation of the object
print(Category.to_json())

# convert the object into a dict
category_dict = category_instance.to_dict()
# create an instance of Category from a dict
category_from_dict = Category.from_dict(category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


