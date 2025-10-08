# ProductIdentifier

This type defines the supported product identifiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ean** | **str** | The EAN of the item, if applicable. EAN is the European Article Number, a barcode standard for retail product labeling primarily used outside of North America. | [optional] 
**epid** | **str** | The ePID (eBay Product Identifier) of the item, if applicable. ePID is a unique identifier used by eBay to track products in its catalog.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/commerce/catalog/resources/product/methods/getProduct\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getProduct&lt;/a&gt; method of the Catalog API to retrieve the ePID of an item. | [optional] 
**isbn** | **str** | The ISBN of the item, if applicable. ISBN is the International Standard Book Number, a unique identifier for books. | [optional] 
**product_id** | **str** | The product ID of the item, if applicable. The product ID is a general term for a unique identifier assigned to a product. | [optional] 
**upc** | **str** | The UPC of the item, if applicable. UPC stands for Universal Product Code, a unique identifier for products, primarily in North America. | [optional] 

## Example

```python
from ebaymetadata.models.product_identifier import ProductIdentifier

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


