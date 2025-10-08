# Weight

This type is used to specify the weight (and the unit used to measure that weight) of a shipping package. The <strong>weight</strong> container is conditionally required if the seller will be offering calculated shipping rates to determine shipping cost, or is using flat-rate costs, but charging a weight surcharge. See the <a href=\"https://pages.ebay.com/help/pay/calculated-shipping.html \" target=\"_blank\">Calculated shipping</a> help page for more information on calculated shipping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | The unit of measurement used to specify the weight of a shipping package. Both the &lt;strong&gt;unit&lt;/strong&gt; and &lt;strong&gt;value&lt;/strong&gt; fields are required if the &lt;strong&gt;weight&lt;/strong&gt; container is used. If the English system of measurement is being used, the applicable values for weight units are &lt;code&gt;POUND&lt;/code&gt; and &lt;code&gt;OUNCE&lt;/CODE&gt;. If the metric system of measurement is being used, the applicable values for weight units are &lt;code&gt;KILOGRAM&lt;/code&gt; and &lt;code&gt;GRAM&lt;/code&gt;. The metric system is used by most countries outside of the US. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:WeightUnitOfMeasureEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**value** | **float** | The actual weight (in the measurement unit specified in the &lt;strong&gt;unit&lt;/strong&gt; field) of the shipping package. Both the &lt;strong&gt;unit&lt;/strong&gt; and &lt;strong&gt;value&lt;/strong&gt; fields are required if the &lt;strong&gt;weight&lt;/strong&gt; container is used. If a shipping package weighed 20.5 ounces, the container would look as follows: &lt;br&gt;&lt;pre&gt;\&quot;weight\&quot;: {&lt;br&gt; \&quot;value\&quot;: 20.5,&lt;br&gt; \&quot;unit\&quot;: \&quot;OUNCE\&quot;&lt;br&gt; }&lt;/pre&gt; | [optional] 

## Example

```python
from ebayinventory.models.weight import Weight

# TODO update the JSON string below
json = "{}"
# create an instance of Weight from a JSON string
weight_instance = Weight.from_json(json)
# print the JSON string representation of the object
print(Weight.to_json())

# convert the object into a dict
weight_dict = weight_instance.to_dict()
# create an instance of Weight from a dict
weight_from_dict = Weight.from_dict(weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


