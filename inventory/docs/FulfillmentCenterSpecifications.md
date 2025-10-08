# FulfillmentCenterSpecifications

This type is used to provide shipping specification details, such as the weekly cut-off schedule for order handling and cut-off override(s), for a fulfillment center location. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**same_day_shipping_cut_off_times** | [**SameDayShippingCutOffTimes**](SameDayShippingCutOffTimes.md) |  | [optional] 

## Example

```python
from ebayinventory.models.fulfillment_center_specifications import FulfillmentCenterSpecifications

# TODO update the JSON string below
json = "{}"
# create an instance of FulfillmentCenterSpecifications from a JSON string
fulfillment_center_specifications_instance = FulfillmentCenterSpecifications.from_json(json)
# print the JSON string representation of the object
print(FulfillmentCenterSpecifications.to_json())

# convert the object into a dict
fulfillment_center_specifications_dict = fulfillment_center_specifications_instance.to_dict()
# create an instance of FulfillmentCenterSpecifications from a dict
fulfillment_center_specifications_from_dict = FulfillmentCenterSpecifications.from_dict(fulfillment_center_specifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


