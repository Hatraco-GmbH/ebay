# Availability

This type is used to specify the quantity of the inventory item that is available for purchase if the item will be shipped to the buyer, and the quantity of the inventory item that is available for In-Store Pickup at one or more of the merchant's physical stores. In-Store Pickup is only available to large merchants selling on the US, UK, Germany, and Australia sites.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_at_location_availability** | [**List[PickupAtLocationAvailability]**](PickupAtLocationAvailability.md) | This container consists of an array of one or more of the merchant&#39;s physical store locations where the inventory item is available for In-Store Pickup orders. The merchant&#39;s location, the quantity available, and the fulfillment time (how soon the item will be ready for pickup after the order takes place) are all in this container. In-Store Pickup is only available to large merchants selling on the US, UK, Germany, and Australia sites. | [optional] 
**ship_to_location_availability** | [**ShipToLocationAvailability**](ShipToLocationAvailability.md) |  | [optional] 

## Example

```python
from ebayinventory.models.availability import Availability

# TODO update the JSON string below
json = "{}"
# create an instance of Availability from a JSON string
availability_instance = Availability.from_json(json)
# print the JSON string representation of the object
print(Availability.to_json())

# convert the object into a dict
availability_dict = availability_instance.to_dict()
# create an instance of Availability from a dict
availability_from_dict = Availability.from_dict(availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


