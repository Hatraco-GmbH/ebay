# Compatibility

This type is used by the <strong>createOrReplaceProductCompatibility</strong> call to associate compatible vehicles to an inventory item. This type is also the base response of the <strong>getProductCompatibility</strong> call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compatible_products** | [**List[CompatibleProduct]**](CompatibleProduct.md) | This container consists of an array of motor vehicles (make, model, year, trim, engine) that are compatible with the motor vehicle part or accessory specified by the sku value. | [optional] 
**sku** | **str** | The seller-defined SKU value of the inventory item that will be associated with the compatible vehicles.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This field is not applicable to the &lt;strong&gt;createOrReplaceProductCompatibility&lt;/strong&gt; method, as the SKU value for the inventory item is passed in as part of the call URI and not in the request payload. It is always returned with the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/inventory_item/product_compatibility/methods/getProductCompatibility\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getProductCompatibility&lt;/a&gt; method.&lt;/span&gt; | [optional] 

## Example

```python
from ebayinventory.models.compatibility import Compatibility

# TODO update the JSON string below
json = "{}"
# create an instance of Compatibility from a JSON string
compatibility_instance = Compatibility.from_json(json)
# print the JSON string representation of the object
print(Compatibility.to_json())

# convert the object into a dict
compatibility_dict = compatibility_instance.to_dict()
# create an instance of Compatibility from a dict
compatibility_from_dict = Compatibility.from_dict(compatibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


