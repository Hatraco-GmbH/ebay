# Moderation

A container that provides video moderation information when calling the <strong>getVideo</strong> method.<br /><br />This container is returned if the specified video has been blocked by moderators.<br /><br /><span class=\"tablenote\"><span style=\"color:#478415\"><strong>Tip:</strong></span> See <a href=\"https://www.ebay.com/help/selling/listings/creating-managing-listings/add-video-to-listing?id=5272#section2\" target=\"_blank\">Video moderation and restrictions</a> in the eBay Seller Center for details about video moderation.</span>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reject_reasons** | **List[str]** | The reason(s) why the specified video was blocked by moderators. | [optional] 

## Example

```python
from ebaymedia.models.moderation import Moderation

# TODO update the JSON string below
json = "{}"
# create an instance of Moderation from a JSON string
moderation_instance = Moderation.from_json(json)
# print the JSON string representation of the object
print(Moderation.to_json())

# convert the object into a dict
moderation_dict = moderation_instance.to_dict()
# create an instance of Moderation from a dict
moderation_from_dict = Moderation.from_dict(moderation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


