# LocalListingDistance

This type contains the kind of distance and radius of the selling area for Local Market Vehicle listings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distances** | **List[int]** | This array indicates the radius (in miles) of the selling area for Local Market Vehicle listings. | [optional] 
**distance_type** | **str** | This enumerated value indicates the type of local listing distances, such as non-subscription or regular, for items listed by sellers. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:DistanceType&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from ebaymetadata.models.local_listing_distance import LocalListingDistance

# TODO update the JSON string below
json = "{}"
# create an instance of LocalListingDistance from a JSON string
local_listing_distance_instance = LocalListingDistance.from_json(json)
# print the JSON string representation of the object
print(LocalListingDistance.to_json())

# convert the object into a dict
local_listing_distance_dict = local_listing_distance_instance.to_dict()
# create an instance of LocalListingDistance from a dict
local_listing_distance_from_dict = LocalListingDistance.from_dict(local_listing_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


