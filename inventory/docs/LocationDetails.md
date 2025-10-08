# LocationDetails

This type is used by the <b>createInventoryLocation</b> call to provide an full or partial address of an inventory location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**geo_coordinates** | [**GeoCoordinates**](GeoCoordinates.md) |  | [optional] 

## Example

```python
from ebayinventory.models.location_details import LocationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LocationDetails from a JSON string
location_details_instance = LocationDetails.from_json(json)
# print the JSON string representation of the object
print(LocationDetails.to_json())

# convert the object into a dict
location_details_dict = location_details_instance.to_dict()
# create an instance of LocationDetails from a dict
location_details_from_dict = LocationDetails.from_dict(location_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


