# BulkPriceQuantityResponse

This type is use by the base response payload of the <strong>bulkUpdatePriceQuantity</strong> call. The <strong>bulkUpdatePriceQuantity</strong> call response will return an HTTP status code, offer ID, and SKU value for each offer/inventory item being updated, as well as an <strong>errors</strong> and/or <strong>warnings</strong> container if any errors or warnings are triggered while trying to update those offers/inventory items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**List[PriceQuantityResponse]**](PriceQuantityResponse.md) | This container will return an HTTP status code, offer ID, and SKU value for each offer/inventory item being updated, as well as an &lt;strong&gt;errors&lt;/strong&gt; and/or &lt;strong&gt;warnings&lt;/strong&gt; container if any errors or warnings are triggered while trying to update those offers/inventory items. | [optional] 

## Example

```python
from ebayinventory.models.bulk_price_quantity_response import BulkPriceQuantityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPriceQuantityResponse from a JSON string
bulk_price_quantity_response_instance = BulkPriceQuantityResponse.from_json(json)
# print the JSON string representation of the object
print(BulkPriceQuantityResponse.to_json())

# convert the object into a dict
bulk_price_quantity_response_dict = bulk_price_quantity_response_instance.to_dict()
# create an instance of BulkPriceQuantityResponse from a dict
bulk_price_quantity_response_from_dict = BulkPriceQuantityResponse.from_dict(bulk_price_quantity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


