# FeesSummaryResponse

This type is used by the base response payload for the <strong>getListingFees</strong> call. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_summaries** | [**List[FeeSummary]**](FeeSummary.md) | This container consists of an array of one or more listing fees that the seller can expect to pay for unpublished offers specified in the call request. Many fee types will get returned even when they are &lt;code&gt;0.0&lt;/code&gt;. | [optional] 

## Example

```python
from ebayinventory.models.fees_summary_response import FeesSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeesSummaryResponse from a JSON string
fees_summary_response_instance = FeesSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(FeesSummaryResponse.to_json())

# convert the object into a dict
fees_summary_response_dict = fees_summary_response_instance.to_dict()
# create an instance of FeesSummaryResponse from a dict
fees_summary_response_from_dict = FeesSummaryResponse.from_dict(fees_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


