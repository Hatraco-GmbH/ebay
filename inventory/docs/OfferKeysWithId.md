# OfferKeysWithId

This type is used by the base request payload of the <strong>getListingFees</strong> call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offers** | [**List[OfferKeyWithId]**](OfferKeyWithId.md) | This container is used to identify one or more (up to 250) unpublished offers for which expected listing fees will be retrieved. The user passes one or more &lt;strong&gt;offerId&lt;/strong&gt; values (maximum of 250) in to this container to identify the unpublished offers in which to retrieve expected listing fees. This call is only applicable for offers in the unpublished state. &lt;br&gt;&lt;br&gt;The call response gives aggregate fee amounts per eBay marketplace, and does not give fee information at the individual offer level. | [optional] 

## Example

```python
from ebayinventory.models.offer_keys_with_id import OfferKeysWithId

# TODO update the JSON string below
json = "{}"
# create an instance of OfferKeysWithId from a JSON string
offer_keys_with_id_instance = OfferKeysWithId.from_json(json)
# print the JSON string representation of the object
print(OfferKeysWithId.to_json())

# convert the object into a dict
offer_keys_with_id_dict = offer_keys_with_id_instance.to_dict()
# create an instance of OfferKeysWithId from a dict
offer_keys_with_id_from_dict = OfferKeysWithId.from_dict(offer_keys_with_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


