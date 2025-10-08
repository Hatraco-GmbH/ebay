# WithdrawResponse

The base response of the <strong>withdrawOffer</strong> call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_id** | **str** | The unique identifier of the eBay listing associated with the offer that was withdrawn. This field will not be returned if the eBay listing was not successfully ended. | [optional] 
**warnings** | [**List[Error]**](Error.md) | This container will be returned if there were one or more warnings associated with the attempt to withdraw the offer. | [optional] 

## Example

```python
from ebayinventory.models.withdraw_response import WithdrawResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawResponse from a JSON string
withdraw_response_instance = WithdrawResponse.from_json(json)
# print the JSON string representation of the object
print(WithdrawResponse.to_json())

# convert the object into a dict
withdraw_response_dict = withdraw_response_instance.to_dict()
# create an instance of WithdrawResponse from a dict
withdraw_response_from_dict = WithdrawResponse.from_dict(withdraw_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


