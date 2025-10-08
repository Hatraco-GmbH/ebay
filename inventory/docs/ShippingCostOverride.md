# ShippingCostOverride

This type is used if the seller wants to override the shipping costs or surcharge associated with a specific domestic or international shipping service option defined in the fulfillment listing policy that is being applied toward the offer. The shipping-related costs that can be overridden include the shipping cost to ship one item, the shipping cost to ship each additional item (if multiple quantity are purchased), and the shipping surcharge applied to the shipping service option.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_shipping_cost** | [**Amount**](Amount.md) |  | [optional] 
**priority** | **int** | The integer value input into this field, along with the &lt;strong&gt;shippingServiceType&lt;/strong&gt; value, sets which domestic or international shipping service option in the fulfillment policy will be modified with updated shipping costs. Specifically, the &lt;strong&gt;shippingCostOverrides.shippingServiceType&lt;/strong&gt; value in a &lt;strong&gt;createOffer&lt;/strong&gt; or &lt;strong&gt;updateOffer&lt;/strong&gt; call must match the &lt;strong&gt;shippingOptions.optionType&lt;/strong&gt; value in a fulfillment listing policy, and the &lt;strong&gt;shippingCostOverrides.priority&lt;/strong&gt; value in a &lt;strong&gt;createOffer&lt;/strong&gt; or &lt;strong&gt;updateOffer&lt;/strong&gt; call must match the &lt;strong&gt;shippingOptions.shippingServices.sortOrderId&lt;/strong&gt; value in a fulfillment listing policy.&lt;br&gt;&lt;br&gt;This field is always required when overriding the shipping costs of a shipping service option, and will be always be returned for each shipping service option whose costs are being overridden. | [optional] 
**shipping_cost** | [**Amount**](Amount.md) |  | [optional] 
**shipping_service_type** | **str** | This enumerated value indicates whether the shipping service specified in the &lt;strong&gt;priority&lt;/strong&gt; field is a domestic or an international shipping service option. To override the shipping costs for a specific domestic shipping service in the fulfillment listing policy, this field should be set to &lt;code&gt;DOMESTIC&lt;/code&gt;, and to override the shipping costs for each international shipping service, this field should be set to &lt;code&gt;INTERNATIONAL&lt;/code&gt;. This value, along with &lt;strong&gt;priority&lt;/strong&gt; value, sets which domestic or international shipping service option in the fulfillment policy that will be modified with updated shipping costs. Specifically, the &lt;strong&gt;shippingCostOverrides.shippingServiceType&lt;/strong&gt; value in a &lt;strong&gt;createOffer&lt;/strong&gt; or &lt;strong&gt;updateOffer&lt;/strong&gt; call must match the &lt;strong&gt;shippingOptions.optionType&lt;/strong&gt; value in a fulfillment listing policy, and the &lt;strong&gt;shippingCostOverrides.priority&lt;/strong&gt; value in a &lt;strong&gt;createOffer&lt;/strong&gt; or &lt;strong&gt;updateOffer&lt;/strong&gt; call must match the &lt;strong&gt;shippingOptions.shippingServices.sortOrderId&lt;/strong&gt; value in a fulfillment listing policy.&lt;br&gt;&lt;br&gt;This field is always required when overriding the shipping costs of a shipping service option, and will be always be returned for each shipping service option whose costs are being overridden. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:ShippingServiceTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**surcharge** | [**Amount**](Amount.md) |  | [optional] 

## Example

```python
from ebayinventory.models.shipping_cost_override import ShippingCostOverride

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingCostOverride from a JSON string
shipping_cost_override_instance = ShippingCostOverride.from_json(json)
# print the JSON string representation of the object
print(ShippingCostOverride.to_json())

# convert the object into a dict
shipping_cost_override_dict = shipping_cost_override_instance.to_dict()
# create an instance of ShippingCostOverride from a dict
shipping_cost_override_from_dict = ShippingCostOverride.from_dict(shipping_cost_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


