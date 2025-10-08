# OfferPriceQuantity

This type is used by the <strong>offers</strong> container in a <strong>Bulk Update Price and Quantity</strong> call to update the current price and/or quantity of one or more offers associated with a specific inventory item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_quantity** | **int** | This field is used if the seller wants to modify the current quantity of the inventory item that will be available for purchase in the offer (identified by the corresponding &lt;strong&gt;offerId&lt;/strong&gt; value).&lt;br&gt;&lt;br&gt;This value represents the quantity of the item that is available in the marketplace specified within the offer, not the total quantity available. Because of this, this value should not exceed the value specified in the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/inventory_item/methods/bulkUpdatePriceQuantity#request.requests.shipToLocationAvailability.quantity\&quot;&gt;&lt;b&gt;quantity&lt;/b&gt;&lt;/a&gt; field of the &lt;b&gt;shipToLocationAvailability&lt;/b&gt; container (the total available quantity of the item across all marketplaces).&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; To ensure that the available quantity allocated to a specific marketplace doesn&#39;t exceed the total available stock, the quantity specified on a listing will be the minimum value between this field and the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/inventory_item/methods/bulkUpdatePriceQuantity#request.requests.shipToLocationAvailability.quantity\&quot;&gt;&lt;b&gt;quantity&lt;/b&gt;&lt;/a&gt; field.&lt;/span&gt;&lt;br&gt;Either the &lt;strong&gt;availableQuantity&lt;/strong&gt; field or the &lt;strong&gt;price&lt;/strong&gt; container is required, but not necessarily both. | [optional] 
**offer_id** | **str** | This field is the unique identifier of the offer. If an &lt;strong&gt;offers&lt;/strong&gt; container is used to update one or more offers associated to a specific inventory item, the &lt;strong&gt;offerId&lt;/strong&gt; value is required in order to identify the offer to update with a modified price and/or quantity.&lt;br&gt;&lt;br&gt;The seller can use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/offer/methods/getOffers\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getOffers&lt;/a&gt; method (passing in the correct SKU value as a query parameter) to retrieve &lt;strong&gt;offerId&lt;/strong&gt; values for offers associated with the SKU. | [optional] 
**price** | [**Amount**](Amount.md) |  | [optional] 

## Example

```python
from ebayinventory.models.offer_price_quantity import OfferPriceQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of OfferPriceQuantity from a JSON string
offer_price_quantity_instance = OfferPriceQuantity.from_json(json)
# print the JSON string representation of the object
print(OfferPriceQuantity.to_json())

# convert the object into a dict
offer_price_quantity_dict = offer_price_quantity_instance.to_dict()
# create an instance of OfferPriceQuantity from a dict
offer_price_quantity_from_dict = OfferPriceQuantity.from_dict(offer_price_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


