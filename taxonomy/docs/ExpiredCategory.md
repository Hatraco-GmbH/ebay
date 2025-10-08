# ExpiredCategory

This type defines the expired category ID for the requested category tree, and the currently active category ID that has replaced it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_category_id** | **str** | The unique identifier of the expired eBay leaf category. | [optional] 
**to_category_id** | **str** | The unique identifier of the currently active eBay leaf category that has replaced the expired leaf category.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; More than one &lt;b&gt;fromCategoryID&lt;/b&gt; value may map into the same &lt;b&gt;toCategoryID&lt;/b&gt; value, as multiple eBay categories may be consolidated into one new, expanded category.&lt;/span&gt; | [optional] 

## Example

```python
from ebaytaxonomy.models.expired_category import ExpiredCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiredCategory from a JSON string
expired_category_instance = ExpiredCategory.from_json(json)
# print the JSON string representation of the object
print(ExpiredCategory.to_json())

# convert the object into a dict
expired_category_dict = expired_category_instance.to_dict()
# create an instance of ExpiredCategory from a dict
expired_category_from_dict = ExpiredCategory.from_dict(expired_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


