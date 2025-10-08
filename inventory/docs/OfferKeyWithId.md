# OfferKeyWithId

This type is used by the <strong>getListingFees</strong> call to indicate the unpublished offer(s) for which expected listing fees will be retrieved. The user passes in one or more <strong>offerId</strong> values (a maximum of 250). See the <a href=\"https://pages.ebay.com/help/sell/fees.html \" target=\"_blank\">Standard selling fees</a> help page for more information on listing fees.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | The unique identifier of an unpublished offer for which expected listing fees will be retrieved. One to 250 &lt;strong&gt;offerId&lt;/strong&gt; values can be passed in to the &lt;strong&gt;offers&lt;/strong&gt; container for one &lt;strong&gt;getListingFees&lt;/strong&gt; call. &lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/offer/methods/getOffers\&quot;&gt;getOffers&lt;/a&gt; method to retrieve offer IDs.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Errors will occur if &lt;strong&gt;offerId&lt;/strong&gt; values representing published offers are passed in.&lt;/span&gt; | [optional] 

## Example

```python
from ebayinventory.models.offer_key_with_id import OfferKeyWithId

# TODO update the JSON string below
json = "{}"
# create an instance of OfferKeyWithId from a JSON string
offer_key_with_id_instance = OfferKeyWithId.from_json(json)
# print the JSON string representation of the object
print(OfferKeyWithId.to_json())

# convert the object into a dict
offer_key_with_id_dict = offer_key_with_id_instance.to_dict()
# create an instance of OfferKeyWithId from a dict
offer_key_with_id_from_dict = OfferKeyWithId.from_dict(offer_key_with_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


