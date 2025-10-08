# PublishResponse

This type is used by the base response payload of the <strong>publishOffer</strong> and <strong>publishOfferByInventoryItemGroup</strong> calls.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_id** | **str** | The unique identifier of the newly created eBay listing. This field is returned if the single offer (if &lt;strong&gt;publishOffer&lt;/strong&gt; call was used) or group of offers in an inventory item group (if &lt;strong&gt;publishOfferByInventoryItemGroup&lt;/strong&gt; call was used) was successfully converted into an eBay listing. | [optional] 
**warnings** | [**List[Error]**](Error.md) | This container will contain an array of errors and/or warnings if any occur when a &lt;strong&gt;publishOffer&lt;/strong&gt; or &lt;strong&gt;publishOfferByInventoryItemGroup&lt;/strong&gt; call is made. | [optional] 

## Example

```python
from ebayinventory.models.publish_response import PublishResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublishResponse from a JSON string
publish_response_instance = PublishResponse.from_json(json)
# print the JSON string representation of the object
print(PublishResponse.to_json())

# convert the object into a dict
publish_response_dict = publish_response_instance.to_dict()
# create an instance of PublishResponse from a dict
publish_response_from_dict = PublishResponse.from_dict(publish_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


