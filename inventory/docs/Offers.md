# Offers

This type is used by the base response of the <strong>getOffers</strong> call, and it is an array of one or more of the seller's offers, along with pagination data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | This is the URL to the current page of offers. | [optional] 
**limit** | **int** | This integer value is the number of offers that will be displayed on each results page. | [optional] 
**next** | **str** | This is the URL to the next page of offers. This field will only be returned if there are additional offers to view. | [optional] 
**offers** | [**List[EbayOfferDetailsWithAll]**](EbayOfferDetailsWithAll.md) | This container is an array of one or more of the seller&#39;s offers for the SKU value that is passed in through the required &lt;strong&gt;sku&lt;/strong&gt; query parameter.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; Currently, the Inventory API does not support the same SKU across multiple eBay marketplaces.&lt;/span&gt;&lt;br&gt;&lt;strong&gt;Max Occurs:&lt;/strong&gt; 25 | [optional] 
**prev** | **str** | This is the URL to the previous page of offers. This field will only be returned if there are previous offers to view. | [optional] 
**size** | **int** | This integer value indicates the number of offers being displayed on the current page of results. This number will generally be the same as the &lt;strong&gt;limit&lt;/strong&gt; value if there are additional pages of results to view.  &lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The same SKU can be offered through an auction and a fixed-price listing concurrently. If this is the case, &lt;b&gt;getOffers&lt;/b&gt; will return two offers and this value will be &lt;code&gt;2&lt;/code&gt;. Otherwise, only one offer will be returned and this value will be &lt;code&gt;1&lt;/code&gt;.&lt;/span&gt; | [optional] 
**total** | **int** | This integer value is the total number of offers that exist for the specified SKU value. Based on this number and on the &lt;strong&gt;limit&lt;/strong&gt; value, the seller may have to toggle through multiple pages to view all offers. &lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The same SKU can be offered through an auction and a fixed-price listing concurrently. If this is the case, &lt;b&gt;getOffers&lt;/b&gt; will return two offers, so this value would be &lt;code&gt;2&lt;/code&gt;. Otherwise, only one offer will be returned and this value will be &lt;code&gt;1&lt;/code&gt;.&lt;/span&gt; | [optional] 

## Example

```python
from ebayinventory.models.offers import Offers

# TODO update the JSON string below
json = "{}"
# create an instance of Offers from a JSON string
offers_instance = Offers.from_json(json)
# print the JSON string representation of the object
print(Offers.to_json())

# convert the object into a dict
offers_dict = offers_instance.to_dict()
# create an instance of Offers from a dict
offers_from_dict = Offers.from_dict(offers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


