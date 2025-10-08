# Location

A complex type that is used to provide the physical address of a location, and it geo-coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**geo_coordinates** | [**GeoCoordinates**](GeoCoordinates.md) |  | [optional] 
**location_id** | **str** | A unique eBay-assigned ID for the location. &lt;br&gt;&lt;br&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; This field should not be confused with the seller-defined &lt;b&gt;merchantLocationKey&lt;/b&gt; value. It is the &lt;b&gt;merchantLocationKey&lt;/b&gt; value which is used to identify an inventory location when working with inventory location API calls. The &lt;strong&gt;locationId&lt;/strong&gt; value is only used internally by eBay.&lt;/span&gt; | [optional] 

## Example

```python
from ebayinventory.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


