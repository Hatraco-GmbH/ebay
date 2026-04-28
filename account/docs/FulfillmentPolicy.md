# FulfillmentPolicy

This type is used by the <b>fulfillmentPolicy</b> response container, a container which defines a seller's fulfillment policy for a specific marketplace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_types** | [**List[CategoryType]**](CategoryType.md) | This container indicates whether the fulfillment policy applies to motor vehicle listings, or if it applies to non-motor vehicle listings. | [optional] 
**description** | **str** | A seller-defined description of the fulfillment policy. This description is only for the seller&#39;s use, and is not exposed on any eBay pages. This field is returned if set for the policy. &lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 250 | [optional] 
**freight_shipping** | **bool** | If returned as &lt;code&gt;true&lt;/code&gt;, the seller offers freight shipping. Freight shipping can be used for large items over 150 lbs. | [optional] 
**fulfillment_policy_id** | **str** | A unique eBay-assigned ID for the fulfillment policy. This ID is generated when the policy is created. | [optional] 
**global_shipping** | **bool** | &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note&lt;/b&gt;: This field is only applicable for the eBay United Kingdom marketplace (&lt;code&gt;EBAY_GB&lt;/code&gt;).&lt;/span&gt;&lt;br&gt;If returned as &lt;code&gt;true&lt;/code&gt;, eBay&#39;s Global Shipping Program will be used by the seller to ship items to international locations.&lt;br&gt;&lt;br&gt;eBay International Shipping is an account level setting; no field needs to be set in a Fulfillment business policy to enable eBay International Shipping. If a US seller&#39;s account is opted in to eBay International Shipping, this shipping option will be enabled automatically for all listings where international shipping is available. A US seller who is opted in to eBay International Shipping can also specify individual international shipping service options for a Fulfillment business policy. | [optional] 
**handling_time** | [**TimeDuration**](TimeDuration.md) |  | [optional] 
**local_pickup** | **bool** | If returned as &lt;code&gt;true&lt;/code&gt;, local pickup is available for this policy. | [optional] 
**marketplace_id** | **str** | The ID of the eBay marketplace to which this fulfillment policy applies. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**name** | **str** | A seller-defined name for this fulfillment policy. Names must be unique for policies assigned to the same marketplace. &lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 64 | [optional] 
**pickup_drop_off** | **bool** | If returned as &lt;code&gt;true&lt;/code&gt;, the seller offers the \&quot;Click and Collect\&quot; option. &lt;br&gt;&lt;br&gt;Currently, \&quot;Click and Collect\&quot; is available only to large retail merchants the eBay AU, UK, DE, FR, and IT marketplaces. | [optional] 
**shipping_options** | [**List[ShippingOption]**](ShippingOption.md) | This array is used to provide detailed information on the domestic and international shipping options available for the policy. A separate &lt;b&gt;ShippingOption&lt;/b&gt; object covers domestic shipping service options and international shipping service options (if the seller ships to international locations). &lt;br&gt;&lt;br&gt;The &lt;b&gt;optionType&lt;/b&gt; field indicates whether the &lt;b&gt;ShippingOption&lt;/b&gt; object applies to domestic or international shipping, and the &lt;b&gt;costType&lt;/b&gt; field indicates whether flat-rate shipping or calculated shipping will be used. &lt;p&gt;A separate &lt;b&gt;ShippingServices&lt;/b&gt; object is used to specify cost and other details for every available domestic and international shipping service option. &lt;/p&gt; | [optional] 
**ship_to_locations** | [**RegionSet**](RegionSet.md) |  | [optional] 

## Example

```python
from ebayaccount.models.fulfillment_policy import FulfillmentPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of FulfillmentPolicy from a JSON string
fulfillment_policy_instance = FulfillmentPolicy.from_json(json)
# print the JSON string representation of the object
print(FulfillmentPolicy.to_json())

# convert the object into a dict
fulfillment_policy_dict = fulfillment_policy_instance.to_dict()
# create an instance of FulfillmentPolicy from a dict
fulfillment_policy_from_dict = FulfillmentPolicy.from_dict(fulfillment_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


