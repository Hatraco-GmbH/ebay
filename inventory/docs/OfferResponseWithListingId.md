# OfferResponseWithListingId

This type is used to indicate the status of each offer that the user attempted to publish. If an offer is successfully published, an eBay listing ID (also known as an Item ID) is returned. If there is an issue publishing the offer and creating the new eBay listing, the information about why the listing failed should be returned in the <strong>errors</strong> and/or <strong>warnings</strong> containers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Error]**](Error.md) | This container will be returned if there were one or more errors associated with publishing the offer. | [optional] 
**listing_id** | **str** | The unique identifier of the newly-created eBay listing. This field is only returned if the seller successfully published the offer and created the new eBay listing. | [optional] 
**offer_id** | **str** | The unique identifier of the offer that the seller published (or attempted to publish). | [optional] 
**status_code** | **int** | The HTTP status code returned in this field indicates the success or failure of publishing the offer specified in the &lt;strong&gt;offerId&lt;/strong&gt; field. See the &lt;strong&gt;HTTP status codes&lt;/strong&gt; table to see which each status code indicates. | [optional] 
**warnings** | [**List[Error]**](Error.md) | This container will be returned if there were one or more warnings associated with publishing the offer. | [optional] 

## Example

```python
from ebayinventory.models.offer_response_with_listing_id import OfferResponseWithListingId

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponseWithListingId from a JSON string
offer_response_with_listing_id_instance = OfferResponseWithListingId.from_json(json)
# print the JSON string representation of the object
print(OfferResponseWithListingId.to_json())

# convert the object into a dict
offer_response_with_listing_id_dict = offer_response_with_listing_id_instance.to_dict()
# create an instance of OfferResponseWithListingId from a dict
offer_response_with_listing_id_from_dict = OfferResponseWithListingId.from_dict(offer_response_with_listing_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


