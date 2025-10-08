# LocationResponse

This type is used by the base response payload for the <strong>getInventoryLocations</strong> call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The URI of the current page of results from the result set. | [optional] 
**limit** | **int** | The number of items returned on a single page from the result set. | [optional] 
**next** | **str** | The URI for the following page of results. This value is returned only if there is an additional page of results to display from the result set. &lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 2048 | [optional] 
**offset** | **int** | The number of results skipped in the result set before listing the first returned result. This value is set in the request with the &lt;b&gt;offset&lt;/b&gt; query parameter. &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note: &lt;/strong&gt;The items in a paginated result set use a zero-based list where the first item in the list has an offset of &lt;code&gt;0&lt;/code&gt;.&lt;/p&gt; | [optional] 
**prev** | **str** | The URI for the preceding page of results. This value is returned only if there is a previous page of results to display from the result set. &lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 2048 | [optional] 
**total** | **int** | The total number of items retrieved in the result set.&lt;br&gt;&lt;br&gt;If no items are found, this field is returned with a value of &lt;code&gt;0&lt;/code&gt;. | [optional] 
**locations** | [**List[InventoryLocationResponse]**](InventoryLocationResponse.md) | An array of one or more of the merchant&#39;s inventory locations. | [optional] 

## Example

```python
from ebayinventory.models.location_response import LocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LocationResponse from a JSON string
location_response_instance = LocationResponse.from_json(json)
# print the JSON string representation of the object
print(LocationResponse.to_json())

# convert the object into a dict
location_response_dict = location_response_instance.to_dict()
# create an instance of LocationResponse from a dict
location_response_from_dict = LocationResponse.from_dict(location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


