# ItemLocation

This type describes the physical location of an order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The two-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166&lt;/a&gt; code representing the country of the address. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CountryCodeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**location** | **str** | Indicates the geographical location of the item (along with the values in the &lt;strong&gt;countryCode&lt;/strong&gt; and &lt;b&gt;postalCode&lt;/b&gt; fields).&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If the item is shipped from a fulfillment center location through the Multi-Warehouse Program, this field will return the geographical location of the fulfillment center closest to the buyer.&lt;/span&gt;&lt;br&gt;This field provides city, province, state, or similar information. | [optional] 
**postal_code** | **str** | The postal code of the address. | [optional] 

## Example

```python
from ebayfulfillment.models.item_location import ItemLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ItemLocation from a JSON string
item_location_instance = ItemLocation.from_json(json)
# print the JSON string representation of the object
print(ItemLocation.to_json())

# convert the object into a dict
item_location_dict = item_location_instance.to_dict()
# create an instance of ItemLocation from a dict
item_location_from_dict = ItemLocation.from_dict(item_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


