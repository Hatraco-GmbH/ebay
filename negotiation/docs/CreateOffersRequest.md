# CreateOffersRequest

This complex type contains the fields needed to create an offer to a buyer that is initiated by the seller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_counter_offer** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, the buyer is allowed to make a counter-offer to the seller&#39;s offer.  &lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Currently, you must set this field to &lt;code&gt;false&lt;/code&gt;; counter-offers are not supported in this release.&lt;/span&gt;  &lt;br&gt;&lt;br&gt;&lt;b&gt;Default:&lt;/b&gt; &lt;code&gt;false&lt;/code&gt; | [optional] 
**message** | **str** | A seller-defined message related to the offer being made.  &lt;br&gt;&lt;br&gt;This message is sent to the list of \&quot;interested\&quot; buyers.  &lt;br&gt;&lt;br&gt;To increase the conversion rate of the offers a seller makes to buyers, eBay recommends you always add a customized message to your offers.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Maximum length:&lt;/b&gt; 2,000 characters | [optional] 
**offer_duration** | [**TimeDuration**](TimeDuration.md) |  | [optional] 
**offered_items** | [**List[OfferedItem]**](OfferedItem.md) | An array of objects where each object contains the details of an offer and the ID of the listing on which the offer is being made.  &lt;br&gt;&lt;br&gt;Note that the service does not currently support the creation of multiple offers with a single call to &lt;b&gt;sendOfferToInterestedBuyer&lt;/b&gt;. With this, each request can target only one listing at a time and you must populate this array with a single element that contains the details of one offer. | [optional] 

## Example

```python
from ebaynegotiation.models.create_offers_request import CreateOffersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOffersRequest from a JSON string
create_offers_request_instance = CreateOffersRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOffersRequest.to_json())

# convert the object into a dict
create_offers_request_dict = create_offers_request_instance.to_dict()
# create an instance of CreateOffersRequest from a dict
create_offers_request_from_dict = CreateOffersRequest.from_dict(create_offers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


