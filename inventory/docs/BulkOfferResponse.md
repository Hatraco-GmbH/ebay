# BulkOfferResponse

This type is used by the base response of the <strong>bulkCreateOffer</strong> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**List[OfferSkuResponse]**](OfferSkuResponse.md) |  | [optional] 

## Example

```python
from ebayinventory.models.bulk_offer_response import BulkOfferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOfferResponse from a JSON string
bulk_offer_response_instance = BulkOfferResponse.from_json(json)
# print the JSON string representation of the object
print(BulkOfferResponse.to_json())

# convert the object into a dict
bulk_offer_response_dict = bulk_offer_response_instance.to_dict()
# create an instance of BulkOfferResponse from a dict
bulk_offer_response_from_dict = BulkOfferResponse.from_dict(bulk_offer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


