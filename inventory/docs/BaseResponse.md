# BaseResponse

This is the base response of the <strong>createOrReplaceInventoryItem</strong>, <strong>createOrReplaceInventoryItemGroup</strong>, and <strong>createOrReplaceProductCompatibility</strong> calls. A response payload will only be returned for these three calls if one or more errors or warnings occur with the call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | [**List[Error]**](Error.md) | This container will be returned in a call response payload if one or more warnings or errors are triggered when an Inventory API call is made. This container will contain detailed information about the error or warning. | [optional] 

## Example

```python
from ebayinventory.models.base_response import BaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponse from a JSON string
base_response_instance = BaseResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponse.to_json())

# convert the object into a dict
base_response_dict = base_response_instance.to_dict()
# create an instance of BaseResponse from a dict
base_response_from_dict = BaseResponse.from_dict(base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


