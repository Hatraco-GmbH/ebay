# GeoCoordinates

This type is used to express the Global Positioning System (GPS) latitude and longitude coordinates of an inventory location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | The latitude (North-South) component of the geographic coordinate. This field is required if a &lt;strong&gt;geoCoordinates&lt;/strong&gt; container is used.&lt;br&gt;&lt;br&gt;This field is returned if geographical coordinates are set for the location.&lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;33.089805&lt;/code&gt; | [optional] 
**longitude** | **float** | The longitude (East-West) component of the geographic coordinate. This field is required if a &lt;strong&gt;geoCoordinates&lt;/strong&gt; container is used.&lt;br&gt;&lt;br&gt;This field is returned if geographical coordinates are set for the location.&lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;-88.709822&lt;/code&gt; | [optional] 

## Example

```python
from ebayinventory.models.geo_coordinates import GeoCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of GeoCoordinates from a JSON string
geo_coordinates_instance = GeoCoordinates.from_json(json)
# print the JSON string representation of the object
print(GeoCoordinates.to_json())

# convert the object into a dict
geo_coordinates_dict = geo_coordinates_instance.to_dict()
# create an instance of GeoCoordinates from a dict
geo_coordinates_from_dict = GeoCoordinates.from_dict(geo_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


