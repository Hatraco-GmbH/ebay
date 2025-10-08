# AvailabilityWithAll

This type is used to specify the quantity of the inventory items that are available for purchase if the items will be shipped to the buyer, and the quantity of the inventory items that are available for In-Store Pickup at one or more of the merchant's physical stores.<br><br>In-Store Pickup is only available to large merchants selling on the US, UK, Germany, and Australia sites.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_at_location_availability** | [**List[PickupAtLocationAvailability]**](PickupAtLocationAvailability.md) | This container consists of an array of one or more of the merchant&#39;s physical stores where the inventory item is available for in-store pickup.&lt;br&gt;&lt;br&gt;The store ID, the quantity available, and the fulfillment time (how soon the item will be ready for pickup after the order occurs) are all returned in this container. | [optional] 
**ship_to_location_availability** | [**ShipToLocationAvailabilityWithAll**](ShipToLocationAvailabilityWithAll.md) |  | [optional] 

## Example

```python
from ebayinventory.models.availability_with_all import AvailabilityWithAll

# TODO update the JSON string below
json = "{}"
# create an instance of AvailabilityWithAll from a JSON string
availability_with_all_instance = AvailabilityWithAll.from_json(json)
# print the JSON string representation of the object
print(AvailabilityWithAll.to_json())

# convert the object into a dict
availability_with_all_dict = availability_with_all_instance.to_dict()
# create an instance of AvailabilityWithAll from a dict
availability_with_all_from_dict = AvailabilityWithAll.from_dict(availability_with_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


