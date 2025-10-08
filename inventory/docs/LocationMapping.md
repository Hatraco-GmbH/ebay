# LocationMapping

This type provides an array of locations that are associated with a SKU within a listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locations** | [**List[LocationAvailabilityDetails]**](LocationAvailabilityDetails.md) | This array represents a collection of fulfillment center locations mapped to a SKU.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Only the first 50 locations mapped to a SKU will be considered when calculating estimated delivery dates. Sellers can set up more than 50 locations using this method, but only the first 50 locations will be considered for calculating the estimates.&lt;/span&gt; | [optional] 

## Example

```python
from ebayinventory.models.location_mapping import LocationMapping

# TODO update the JSON string below
json = "{}"
# create an instance of LocationMapping from a JSON string
location_mapping_instance = LocationMapping.from_json(json)
# print the JSON string representation of the object
print(LocationMapping.to_json())

# convert the object into a dict
location_mapping_dict = location_mapping_instance.to_dict()
# create an instance of LocationMapping from a dict
location_mapping_from_dict = LocationMapping.from_dict(location_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


