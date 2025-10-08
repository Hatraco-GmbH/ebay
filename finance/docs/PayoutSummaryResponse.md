# PayoutSummaryResponse

This type is the base response type of the <strong>getPayoutSummary</strong> method, and contains the total count of seller payouts (that match the input criteria), the total count of monetary transactions (order payment, buyer refunds, or seller credits) associated with those payouts, and the total value of those seller payouts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) |  | [optional] 
**payout_count** | **int** | This integer value indicates the total count of payouts to the seller that match the input criteria. This field is always returned, even if there are no payouts that match the input criteria (its value will show &lt;code&gt;0&lt;/code&gt;). | [optional] 
**transaction_count** | **int** | This integer value indicates the total count of monetary transactions (order payments, buyer refunds, and seller credits) associated with the payouts that match the input criteria. This field is always returned, even if there are no payouts that match the input criteria (its value will show &lt;code&gt;0&lt;/code&gt;). If there is at least one payout that matches the input criteria, the value in this field will be at least &lt;code&gt;1&lt;/code&gt;. | [optional] 

## Example

```python
from ebayfinance.models.payout_summary_response import PayoutSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutSummaryResponse from a JSON string
payout_summary_response_instance = PayoutSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(PayoutSummaryResponse.to_json())

# convert the object into a dict
payout_summary_response_dict = payout_summary_response_instance.to_dict()
# create an instance of PayoutSummaryResponse from a dict
payout_summary_response_from_dict = PayoutSummaryResponse.from_dict(payout_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


