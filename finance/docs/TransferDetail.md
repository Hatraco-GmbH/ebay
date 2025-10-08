# TransferDetail

This type is used by the <b>transferDetail</b> container, which provides more details about the transfer and the charge(s) associated with the transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_adjustment** | [**BalanceAdjustment**](BalanceAdjustment.md) |  | [optional] 
**charges** | [**List[Charge]**](Charge.md) | This container is an array of one or more charges related to the transfer. Charges can be related to an order cancellation, order return, case, payment dispute, etc. | [optional] 
**total_charge_net_amount** | [**Amount**](Amount.md) |  | [optional] 

## Example

```python
from ebayfinance.models.transfer_detail import TransferDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TransferDetail from a JSON string
transfer_detail_instance = TransferDetail.from_json(json)
# print the JSON string representation of the object
print(TransferDetail.to_json())

# convert the object into a dict
transfer_detail_dict = transfer_detail_instance.to_dict()
# create an instance of TransferDetail from a dict
transfer_detail_from_dict = TransferDetail.from_dict(transfer_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


