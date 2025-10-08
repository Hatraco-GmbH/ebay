# PriceQuantityResponse

This type is used to display the result for each offer and/or inventory item that the seller attempted to update with a <strong>bulkUpdatePriceQuantity</strong> call. If any errors or warnings occur, the error/warning data is returned at the offer/inventory item level.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Error]**](Error.md) | This array will be returned if there were one or more errors associated with the update to the offer or inventory item record. | [optional] 
**offer_id** | **str** | The unique identifier of the offer that was updated. This field will not be returned in situations where the seller is only updating the total &#39;ship-to-home&#39; quantity of an inventory item record. | [optional] 
**sku** | **str** | This is the seller-defined SKU value of the product. This field is returned whether the seller attempted to update an offer with the SKU value or just attempted to update the total &#39;ship-to-home&#39; quantity of an inventory item record.&lt;br&gt;&lt;br&gt;&lt;strong&gt;Max Length&lt;/strong&gt;: 50&lt;br&gt; | [optional] 
**status_code** | **int** | The value returned in this container will indicate the status of the attempt to update the price and/or quantity of the offer (specified in the corresponding &lt;strong&gt;offerId&lt;/strong&gt; field) or the attempt to update the total &#39;ship-to-home&#39; quantity of an inventory item (specified in the corresponding &lt;strong&gt;sku&lt;/strong&gt; field). For a completely successful update of an offer or inventory item record, a value of &lt;code&gt;200&lt;/code&gt; will appear in this field.  A user can view the &lt;strong&gt;HTTP status codes&lt;/strong&gt; section for information on other status codes that may be returned with the &lt;strong&gt;bulkUpdatePriceQuantity&lt;/strong&gt; method. | [optional] 
**warnings** | [**List[Error]**](Error.md) | This array will be returned if there were one or more warnings associated with the update to the offer or inventory item record. | [optional] 

## Example

```python
from ebayinventory.models.price_quantity_response import PriceQuantityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PriceQuantityResponse from a JSON string
price_quantity_response_instance = PriceQuantityResponse.from_json(json)
# print the JSON string representation of the object
print(PriceQuantityResponse.to_json())

# convert the object into a dict
price_quantity_response_dict = price_quantity_response_instance.to_dict()
# create an instance of PriceQuantityResponse from a dict
price_quantity_response_from_dict = PriceQuantityResponse.from_dict(price_quantity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


