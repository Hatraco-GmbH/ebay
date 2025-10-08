# Charge

This type is used to display the charge type and the amount of the charge against the buyer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) |  | [optional] 
**charge_type** | **str** | This field shows the type of buyer charge &lt;br&gt; &lt;br&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt; Note: &lt;/strong&gt; Currently, the only supported charge type is BUYER_PROTECTION. &lt;/span&gt; For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/fulfillment/types/sol:ChargeTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from ebayfulfillment.models.charge import Charge

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


