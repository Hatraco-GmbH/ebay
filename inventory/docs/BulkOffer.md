# BulkOffer

This type is used by the base request of the <strong>bulkPublishOffer</strong> method, which is used to publish up to 25 different offers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[OfferKeyWithId]**](OfferKeyWithId.md) | This container is used to pass in an array of offers to publish. Up to 25 offers can be published with one &lt;strong&gt;bulkPublishOffer&lt;/strong&gt; method. | [optional] 

## Example

```python
from ebayinventory.models.bulk_offer import BulkOffer

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOffer from a JSON string
bulk_offer_instance = BulkOffer.from_json(json)
# print the JSON string representation of the object
print(BulkOffer.to_json())

# convert the object into a dict
bulk_offer_dict = bulk_offer_instance.to_dict()
# create an instance of BulkOffer from a dict
bulk_offer_from_dict = BulkOffer.from_dict(bulk_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


