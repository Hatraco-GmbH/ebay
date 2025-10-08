# SellerFundsSummaryResponse

This type is used by the response payload of the <strong>getSellerFundsSummary</strong> method. All of the funds returned in  <strong>getSellerFundsSummary</strong> are funds that have not yet been paid to the seller through a seller payout. If there are no funds that are pending, on hold, or being processed for the seller's account, no response payload is returned, and an http status code of <code>204 - No Content</code> is returned instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_funds** | [**Amount**](Amount.md) |  | [optional] 
**funds_on_hold** | [**Amount**](Amount.md) |  | [optional] 
**processing_funds** | [**Amount**](Amount.md) |  | [optional] 
**total_funds** | [**Amount**](Amount.md) |  | [optional] 

## Example

```python
from ebayfinance.models.seller_funds_summary_response import SellerFundsSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SellerFundsSummaryResponse from a JSON string
seller_funds_summary_response_instance = SellerFundsSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(SellerFundsSummaryResponse.to_json())

# convert the object into a dict
seller_funds_summary_response_dict = seller_funds_summary_response_instance.to_dict()
# create an instance of SellerFundsSummaryResponse from a dict
seller_funds_summary_response_from_dict = SellerFundsSummaryResponse.from_dict(seller_funds_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


