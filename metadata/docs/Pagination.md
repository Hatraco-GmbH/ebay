# Pagination

This type defines the pagination settings for a result set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of results showing on the current page of results. | [optional] 
**limit** | **int** | The max number of entries that can be returned on a single page. | [optional] 
**offset** | **int** | The number of items that will be skipped in the result set before returning the first item in the paginated response. | [optional] 
**total** | **int** | The total number of results in a result set. | [optional] 

## Example

```python
from ebaymetadata.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print(Pagination.to_json())

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_from_dict = Pagination.from_dict(pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


