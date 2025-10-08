# BulkPriceQuantity

This type is used by the base request payload of the <strong>bulkUpdatePriceQuantity</strong> call. The <strong>bulkUpdatePriceQuantity</strong> call allows the seller to update the total 'ship-to-home' quantity of one or more inventory items (up to 25) and/or to update the price and/or quantity of one or more specific published offers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[PriceQuantity]**](PriceQuantity.md) | This container is used by the seller to update the total &#39;ship-to-home&#39; quantity of one or more inventory items (up to 25) and/or to update the price and/or quantity of one or more specific published offers. | [optional] 

## Example

```python
from ebayinventory.models.bulk_price_quantity import BulkPriceQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPriceQuantity from a JSON string
bulk_price_quantity_instance = BulkPriceQuantity.from_json(json)
# print the JSON string representation of the object
print(BulkPriceQuantity.to_json())

# convert the object into a dict
bulk_price_quantity_dict = bulk_price_quantity_instance.to_dict()
# create an instance of BulkPriceQuantity from a dict
bulk_price_quantity_from_dict = BulkPriceQuantity.from_dict(bulk_price_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


