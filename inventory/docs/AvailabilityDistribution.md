# AvailabilityDistribution

This type is used to set the available quantity of the inventory item at one or more warehouse locations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_time** | [**TimeDuration**](TimeDuration.md) |  | [optional] 
**merchant_location_key** | **str** | The unique identifier of an inventory location where quantity is available for the inventory item. This field is conditionally required to identify the inventory location that has quantity of the inventory item.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/location/methods/getInventoryLocations\&quot; target&#x3D;\&quot;_blank\&quot;&gt;getInventoryLocations&lt;/a&gt; method to retrieve merchant location keys. | [optional] 
**quantity** | **int** | The integer value passed into this field indicates the quantity of the inventory item that is available at this inventory location. This field is conditionally required. | [optional] 

## Example

```python
from ebayinventory.models.availability_distribution import AvailabilityDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of AvailabilityDistribution from a JSON string
availability_distribution_instance = AvailabilityDistribution.from_json(json)
# print the JSON string representation of the object
print(AvailabilityDistribution.to_json())

# convert the object into a dict
availability_distribution_dict = availability_distribution_instance.to_dict()
# create an instance of AvailabilityDistribution from a dict
availability_distribution_from_dict = AvailabilityDistribution.from_dict(availability_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


