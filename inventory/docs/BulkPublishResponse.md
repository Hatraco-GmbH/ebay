# BulkPublishResponse

This type is used by the base response of the <strong>bulkPublishOffer</strong> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**List[OfferResponseWithListingId]**](OfferResponseWithListingId.md) | A node is returned under the &lt;strong&gt;responses&lt;/strong&gt; container to indicate the success or failure of each offer that the seller was attempting to publish. | [optional] 

## Example

```python
from ebayinventory.models.bulk_publish_response import BulkPublishResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPublishResponse from a JSON string
bulk_publish_response_instance = BulkPublishResponse.from_json(json)
# print the JSON string representation of the object
print(BulkPublishResponse.to_json())

# convert the object into a dict
bulk_publish_response_dict = bulk_publish_response_instance.to_dict()
# create an instance of BulkPublishResponse from a dict
bulk_publish_response_from_dict = BulkPublishResponse.from_dict(bulk_publish_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


