# BulkEbayOfferDetailsWithKeys

This type is used by the base request of the <strong>bulkCreateOffer</strong> method, which is used to create up to 25 new offers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[EbayOfferDetailsWithKeys]**](EbayOfferDetailsWithKeys.md) | The details of each offer that is being created is passed in under this container. Up to 25 offers can be created with one &lt;strong&gt;bulkCreateOffer&lt;/strong&gt; call. | [optional] 

## Example

```python
from ebayinventory.models.bulk_ebay_offer_details_with_keys import BulkEbayOfferDetailsWithKeys

# TODO update the JSON string below
json = "{}"
# create an instance of BulkEbayOfferDetailsWithKeys from a JSON string
bulk_ebay_offer_details_with_keys_instance = BulkEbayOfferDetailsWithKeys.from_json(json)
# print the JSON string representation of the object
print(BulkEbayOfferDetailsWithKeys.to_json())

# convert the object into a dict
bulk_ebay_offer_details_with_keys_dict = bulk_ebay_offer_details_with_keys_instance.to_dict()
# create an instance of BulkEbayOfferDetailsWithKeys from a dict
bulk_ebay_offer_details_with_keys_from_dict = BulkEbayOfferDetailsWithKeys.from_dict(bulk_ebay_offer_details_with_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


