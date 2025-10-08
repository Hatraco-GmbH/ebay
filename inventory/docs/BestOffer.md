# BestOffer

This type is used by the <strong>bestOfferTerms</strong> container, which is used if the seller would like to support the Best Offer feature on their listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_accept_price** | [**Amount**](Amount.md) |  | [optional] 
**auto_decline_price** | [**Amount**](Amount.md) |  | [optional] 
**best_offer_enabled** | **bool** | This field indicates whether or not the Best Offer feature is enabled for the listing. A seller can enable the Best Offer feature for a listing as long as the category supports the Best Offer feature.&lt;br&gt;&lt;br&gt;The seller includes this field and sets its value to &lt;code&gt;true&lt;/code&gt; to enable Best Offer feature.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Best Offer is not available for multi-variation listings.&lt;/span&gt; | [optional] 

## Example

```python
from ebayinventory.models.best_offer import BestOffer

# TODO update the JSON string below
json = "{}"
# create an instance of BestOffer from a JSON string
best_offer_instance = BestOffer.from_json(json)
# print the JSON string representation of the object
print(BestOffer.to_json())

# convert the object into a dict
best_offer_dict = best_offer_instance.to_dict()
# create an instance of BestOffer from a dict
best_offer_from_dict = BestOffer.from_dict(best_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


