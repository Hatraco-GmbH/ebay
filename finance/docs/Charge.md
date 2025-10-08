# Charge

This type is used by the <b>charge</b> container, which is an array of one or more charges related to the transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_id** | **str** | The unique identifier of an order cancellation. This field is only applicable and returned if the charge is related to an order  cancellation. | [optional] 
**case_id** | **str** | The unique identifier of a case filed against an order. This field is only applicable and returned if the charge is related to a case filed against an order. | [optional] 
**charge_net_amount** | [**Amount**](Amount.md) |  | [optional] 
**inquiry_id** | **str** | The unique identifier of an Item Not Received (INR) inquiry filed against an order. This field is only applicable and returned if the charge is related to has an INR inquiry filed against the order. | [optional] 
**order_id** | **str** | The unique identifier of the order that is associated with the charge. | [optional] 
**payment_dispute_id** | **str** | The unique identifier of a third-party payment dispute filed against an order. This occurs when the buyer files a dispute against the order with their payment provider, and then the dispute comes into eBay&#39;s system. This field is only applicable and returned if the charge is related to a third-party payment dispute filed against an order. | [optional] 
**refund_id** | **str** | The unique identifier of a buyer refund associated with the charge. | [optional] 
**return_id** | **str** | The unique identifier of an order return. This field is only applicable and returned if the charge is related to an order that was returned by the buyer. | [optional] 

## Example

```python
from ebayfinance.models.charge import Charge

# TODO update the JSON string below
json = "{}"
# create an instance of Charge from a JSON string
charge_instance = Charge.from_json(json)
# print the JSON string representation of the object
print(Charge.to_json())

# convert the object into a dict
charge_dict = charge_instance.to_dict()
# create an instance of Charge from a dict
charge_from_dict = Charge.from_dict(charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


