# ListingDuration

This type identifies the kind of listing and its duration periods.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_values** | **List[str]** | This array defines the supported time duration options available for the listing type. | [optional] 
**listing_type** | **str** | The enumerated value returned in this field indicates the listing type for the duration value(s). For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:ListingTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from ebaymetadata.models.listing_duration import ListingDuration

# TODO update the JSON string below
json = "{}"
# create an instance of ListingDuration from a JSON string
listing_duration_instance = ListingDuration.from_json(json)
# print the JSON string representation of the object
print(ListingDuration.to_json())

# convert the object into a dict
listing_duration_dict = listing_duration_instance.to_dict()
# create an instance of ListingDuration from a dict
listing_duration_from_dict = ListingDuration.from_dict(listing_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


