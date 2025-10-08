# OfferResponse

This type is used by the response payload of the <strong>createOffer</strong> and <strong>updateOffer</strong> calls. The <strong>offerId</strong> field contains the unique identifier for the offer if the offer is successfully created by the <strong>createOffer</strong> call. The <strong>warnings</strong> field contains any errors and/or warnings that may have been triggered by the call. <p> <span class=\"tablenote\"><strong>Note:</strong> The <strong>offerId</strong> value is only returned with a successful <strong>createOffer</strong> call. This field will not be returned in the <strong>updateOffer </strong> response.</span></p>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | The unique identifier of the offer that was just created with a &lt;strong&gt;createOffer&lt;/strong&gt; call. It is not returned if the &lt;strong&gt;createOffer&lt;/strong&gt; call fails to create an offer. This identifier will be needed for many offer-related calls. &lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The &lt;strong&gt;offerId&lt;/strong&gt; value is only returned with a successful &lt;strong&gt;createOffer&lt;/strong&gt; call. This field will not be returned in the &lt;strong&gt;updateOffer &lt;/strong&gt; response.&lt;/span&gt;&lt;/p&gt; | [optional] 
**warnings** | [**List[Error]**](Error.md) | This container will contain an array of errors and/or warnings when a call is made, and errors and/or warnings occur. | [optional] 

## Example

```python
from ebayinventory.models.offer_response import OfferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponse from a JSON string
offer_response_instance = OfferResponse.from_json(json)
# print the JSON string representation of the object
print(OfferResponse.to_json())

# convert the object into a dict
offer_response_dict = offer_response_instance.to_dict()
# create an instance of OfferResponse from a dict
offer_response_from_dict = OfferResponse.from_dict(offer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


