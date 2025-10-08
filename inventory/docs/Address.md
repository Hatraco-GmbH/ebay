# Address

This type is used to define the physical address of an inventory location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The first line of a street address. This field is required for store and fulfillment center locations. A street address is not required for warehouse locations.&lt;br&gt;&lt;br&gt;This field will be returned if defined for an inventory location. &lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 128 | [optional] 
**address_line2** | **str** | The second line of a street address. This field can be used for additional address information, such as a suite or apartment number. &lt;br&gt;&lt;br&gt;This field will be returned if defined for an inventory location. &lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 128 | [optional] 
**city** | **str** | The city in which the inventory location resides. This field is required for store and fulfillment center locations. For warehouse locations, this field is conditionally required as part of a &lt;strong&gt;city&lt;/strong&gt; and &lt;strong&gt;stateOrProvince&lt;/strong&gt; pair if a &lt;strong&gt;postalCode&lt;/strong&gt; is not provided. If a &lt;strong&gt;postalCode&lt;/strong&gt; is provided, the city is derived from the provided postal code and this field is technically optional.&lt;br&gt;&lt;br&gt;This field is returned if defined for an inventory location. &lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 128 | [optional] 
**country** | **str** | The country in which the address resides, represented as two-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166&lt;/a&gt; country code. For example, &lt;code&gt;US&lt;/code&gt; represents the United States, and &lt;code&gt;DE&lt;/code&gt; represents Germany. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/ba:CountryCodeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**county** | **str** | The county in which the address resides.&lt;br&gt;&lt;br&gt;This field is returned if defined for an inventory location. | [optional] 
**postal_code** | **str** | The postal/zip code of the address. eBay uses postal codes to surface In-Store Pickup items within the vicinity of a buyer&#39;s location, and it also uses postal codes (origin and destination) to estimate shipping costs when the seller uses calculated shipping. This field is required for store and fulfillment center locations. &lt;br&gt;&lt;br&gt;For warehouse locations, this field is conditionally required if a &lt;strong&gt;city&lt;/strong&gt; and &lt;strong&gt;stateOrProvince&lt;/strong&gt; pair is not provided.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt; &lt;strong&gt;Note:&lt;/strong&gt; For warehouse locations, &lt;strong&gt;city&lt;/strong&gt; and &lt;strong&gt;stateOrProvince&lt;/strong&gt; pair can be used instead of a &lt;strong&gt;postalCode&lt;/strong&gt; value, and then the postal code is just derived from the city and state/province.&lt;/span&gt;&lt;br&gt;&lt;br&gt;This field is returned if defined for an inventory location. &lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 16 | [optional] 
**state_or_province** | **str** | The state/province in which the inventory location resides. This field is required for store and fulfillment center locations. For warehouse locations, this field is conditionally required as part of a &lt;strong&gt;city&lt;/strong&gt; and &lt;strong&gt;stateOrProvince&lt;/strong&gt; pair if a &lt;strong&gt;postalCode&lt;/strong&gt; is not provided. If a &lt;strong&gt;postalCode&lt;/strong&gt; is provided, the state or province is derived from the provided zip code and this field is technically optional.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 128 | [optional] 

## Example

```python
from ebayinventory.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


