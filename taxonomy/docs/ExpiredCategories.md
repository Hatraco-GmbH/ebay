# ExpiredCategories

This type is used by the <b>getExpiredCategories</b> response to indicate any eBay leaf categories in the specified category tree that have expired and the currently active leaf categories that have replaced them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expired_categories** | [**List[ExpiredCategory]**](ExpiredCategory.md) | An array of expired category ID(s) for the requested category tree, and the currently active category ID(s) that have replaced them. | [optional] 

## Example

```python
from ebaytaxonomy.models.expired_categories import ExpiredCategories

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiredCategories from a JSON string
expired_categories_instance = ExpiredCategories.from_json(json)
# print the JSON string representation of the object
print(ExpiredCategories.to_json())

# convert the object into a dict
expired_categories_dict = expired_categories_instance.to_dict()
# create an instance of ExpiredCategories from a dict
expired_categories_from_dict = ExpiredCategories.from_dict(expired_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


