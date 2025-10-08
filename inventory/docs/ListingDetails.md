# ListingDetails

This type is used by the <strong>listing</strong> container in the <strong>getOffer</strong> and <strong>getOffers</strong> calls to provide the eBay listing ID, the listing status, and quantity sold for the offer. The <strong>listing</strong> container is only returned for published offers, and is not returned for unpublished offers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_id** | **str** | The unique identifier of the eBay listing that is associated with the published offer.  | [optional] 
**listing_on_hold** | **bool** | Indicates if a listing is on hold due to an eBay policy violation.&lt;br&gt;&lt;p&gt;If a listing is put on hold, users are unable to view the listing details, the listing is hidden from search, and all attempted purchases, offers, and bids for the listing are blocked. eBay, however, gives sellers the opportunity to address violations and get listings fully reinstated. A listing will be ended if a seller does not address a violation, or if the violation can not be rectified.&lt;/p&gt;&lt;br&gt;&lt;p&gt;If a listing is fixable, the seller should be able to view the listing details and this boolean will be returned as true.&lt;/p&gt;&lt;br&gt;&lt;p&gt;Once a listing is fixed, this boolean will no longer be returned.&lt;/p&gt; | [optional] 
**listing_status** | **str** | The enumeration value returned in this field indicates the status of the listing that is associated with the published offer. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:ListingStatusEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**sold_quantity** | **int** | This integer value indicates the quantity of the product that has been sold for the published offer. | [optional] 

## Example

```python
from ebayinventory.models.listing_details import ListingDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ListingDetails from a JSON string
listing_details_instance = ListingDetails.from_json(json)
# print the JSON string representation of the object
print(ListingDetails.to_json())

# convert the object into a dict
listing_details_dict = listing_details_instance.to_dict()
# create an instance of ListingDetails from a dict
listing_details_from_dict = ListingDetails.from_dict(listing_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


