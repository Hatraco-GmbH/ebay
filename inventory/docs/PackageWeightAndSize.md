# PackageWeightAndSize

This type is used to indicate the package type, weight, and dimensions of the shipping package. Package weight and dimensions are required when calculated shipping rates are used, and weight alone is required when flat-rate shipping is used, but with a weight surcharge. See the <a href=\"https://pages.ebay.com/help/pay/calculated-shipping.html \" target=\"_blank\">Calculated shipping</a> help page for more information on calculated shipping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | [**Dimension**](Dimension.md) |  | [optional] 
**package_type** | **str** | This enumeration value indicates the type of shipping package used to ship the inventory item. The supported values for this field can be found in the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/types/slr:PackageTypeEnum\&quot; target&#x3D;\&quot;_blank\&quot;&gt;PackageTypeEnum&lt;/a&gt; type.&lt;br&gt;&lt;br&gt;This field will be returned if the package type is set for the inventory item.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; You can use the &lt;a href&#x3D;\&quot;/Devzone/XML/docs/Reference/eBay/GeteBayDetails.html#Response.ShippingPackageDetails\&quot; target&#x3D;\&quot;_blank\&quot;&gt;GeteBayDetails&lt;/a&gt; Trading API call to retrieve a list of supported package types for a specific marketplace.&lt;/span&gt; For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:PackageTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**shipping_irregular** | **bool** | A value of &lt;code&gt;true&lt;/code&gt; indicates that the package is irregular and cannot go through the stamping machine at the shipping service office. This field applies to calculated shipping only. Irregular packages require special or fragile handling. | [optional] 
**weight** | [**Weight**](Weight.md) |  | [optional] 

## Example

```python
from ebayinventory.models.package_weight_and_size import PackageWeightAndSize

# TODO update the JSON string below
json = "{}"
# create an instance of PackageWeightAndSize from a JSON string
package_weight_and_size_instance = PackageWeightAndSize.from_json(json)
# print the JSON string representation of the object
print(PackageWeightAndSize.to_json())

# convert the object into a dict
package_weight_and_size_dict = package_weight_and_size_instance.to_dict()
# create an instance of PackageWeightAndSize from a dict
package_weight_and_size_from_dict = PackageWeightAndSize.from_dict(package_weight_and_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


