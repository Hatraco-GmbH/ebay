# Fee

This type is used to display fees that are automatically deducted from seller payouts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) |  | [optional] 
**fee_jurisdiction** | [**FeeJurisdiction**](FeeJurisdiction.md) |  | [optional] 
**fee_memo** | **str** | A description of the fee that was deducted from the seller payout. | [optional] 
**fee_type** | **str** | The enumeration value returned here indicates the type of fee that was deducted from the seller payout. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/finances/types/api:FeeTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from ebayfinance.models.fee import Fee

# TODO update the JSON string below
json = "{}"
# create an instance of Fee from a JSON string
fee_instance = Fee.from_json(json)
# print the JSON string representation of the object
print(Fee.to_json())

# convert the object into a dict
fee_dict = fee_instance.to_dict()
# create an instance of Fee from a dict
fee_from_dict = Fee.from_dict(fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


