# ProductIdentifier

This type is used to identify a motor vehicle that is compatible with the corresponding inventory item (the SKU that is passed in as part of the call URI). The motor vehicle can be identified through an eBay Product ID or a K-Type value. The <strong>gtin</strong> field (for inputting Global Trade Item Numbers) is for future use only. If a motor vehicle is found in the eBay product catalog, the motor vehicle properties (engine, make, model, trim, and year) will automatically get picked up for that motor vehicle.<br><br><span class=\"tablenote\"> <strong>Note:</strong> Currently, parts compatibility is only applicable for motor vehicles, but it is possible that the Product Compatibility feature is expanded to other (non-vehicle) products in the future.</span>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epid** | **str** | This field can be used if the seller already knows the eBay catalog product ID (ePID) associated with the motor vehicle that is to be added to the compatible product list. If this eBay catalog product ID is found in the eBay product catalog, the motor vehicle properties (e.g. make, model, year, engine, and trim) will automatically get picked up for that motor vehicle. | [optional] 
**gtin** | **str** | This field can be used if the seller knows the Global Trade Item Number for the motor vehicle that is to be added to the compatible product list. If this GTIN value is found in the eBay product catalog, the motor vehicle properties (e.g. make, model, year, engine, and trim will automatically get picked up for that motor vehicle.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; This field is for future use.&lt;/span&gt; | [optional] 
**ktype** | **str** | This field can be used if the seller knows the K Type Number for the motor vehicle that is to be added to the compatible product list. If this K Type value is found in the eBay product catalog, the motor vehicle properties (e.g. make, model, year, engine, and trim) will automatically get picked up for that motor vehicle. &lt;br&gt;&lt;br&gt;Only the AU, DE, ES, FR, IT, and UK marketplaces support the use of K Type Numbers. | [optional] 

## Example

```python
from ebayinventory.models.product_identifier import ProductIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ProductIdentifier from a JSON string
product_identifier_instance = ProductIdentifier.from_json(json)
# print the JSON string representation of the object
print(ProductIdentifier.to_json())

# convert the object into a dict
product_identifier_dict = product_identifier_instance.to_dict()
# create an instance of ProductIdentifier from a dict
product_identifier_from_dict = ProductIdentifier.from_dict(product_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


