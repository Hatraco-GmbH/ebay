# LocationAvailabilityDetails

This type provides the unique identifier of an inventory location that is associated with a SKU within a listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_location_key** | **str** | The unique identifier of a seller’s fulfillment center location where inventory is available for the item or item variation.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; When creating a location mapping using the &lt;b&gt;createOrReplaceSkuLocationMapping&lt;/b&gt; method, the value entered in this field &lt;b&gt;must&lt;/b&gt; be associated with a location with the &lt;code&gt;FULFILLMENT_CENTER&lt;/code&gt; location type, or an error will occur. Sellers can check the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/location/methods/getInventoryLocations#response.locations.locationTypes\&quot; target&#x3D;\&quot;_blank\&quot;&gt;locationTypes&lt;/a&gt; array in the response of the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/location/methods/getInventoryLocations\&quot; target&#x3D;\&quot;_blank\&quot;&gt;getInventoryLocations&lt;/a&gt; method to see if their location has a value of &lt;code&gt;FULFILLMENT_CENTER&lt;/code&gt;.&lt;/span&gt; | [optional] 

## Example

```python
from ebayinventory.models.location_availability_details import LocationAvailabilityDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LocationAvailabilityDetails from a JSON string
location_availability_details_instance = LocationAvailabilityDetails.from_json(json)
# print the JSON string representation of the object
print(LocationAvailabilityDetails.to_json())

# convert the object into a dict
location_availability_details_dict = location_availability_details_instance.to_dict()
# create an instance of LocationAvailabilityDetails from a dict
location_availability_details_from_dict = LocationAvailabilityDetails.from_dict(location_availability_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


