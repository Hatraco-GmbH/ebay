# BalanceAdjustment

This type is used by the <b>balanceAdjustment</b> container, which shows the seller payout balance that will be applied toward the charges outlined in the <b>charges</b> array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment_amount** | [**Amount**](Amount.md) |  | [optional] 
**adjustment_type** | **str** | The enumeration value returned here indicates if the charge is a &lt;code&gt;DEBIT&lt;/code&gt; or a &lt;code&gt;CREDIT&lt;/code&gt; to the seller. Generally, all transfer transaction types are going to be &lt;code&gt;DEBIT&lt;/code&gt;, since the money is being tranferred from the seller to eBay. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/finances/types/pay:BookingEntryEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from ebayfinance.models.balance_adjustment import BalanceAdjustment

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceAdjustment from a JSON string
balance_adjustment_instance = BalanceAdjustment.from_json(json)
# print the JSON string representation of the object
print(BalanceAdjustment.to_json())

# convert the object into a dict
balance_adjustment_dict = balance_adjustment_instance.to_dict()
# create an instance of BalanceAdjustment from a dict
balance_adjustment_from_dict = BalanceAdjustment.from_dict(balance_adjustment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


