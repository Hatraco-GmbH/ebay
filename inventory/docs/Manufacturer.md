# Manufacturer

This type provides name and contact information about the manufacturer of the item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The first line of the product manufacturer&#39;s street address.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 180 characters | [optional] 
**address_line2** | **str** | The second line of the product manufacturer&#39;s street address. This field is not always used, but can be used for secondary address information such as &#39;Suite Number&#39; or &#39;Apt Number&#39;.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 180 characters | [optional] 
**city** | **str** | The city of the product manufacturer&#39;s street address.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 64 characters | [optional] 
**company_name** | **str** | The company name of the product manufacturer.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 100 characters | [optional] 
**contact_url** | **str** | The contact URL of the product manufacturer.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 250 characters | [optional] 
**country** | **str** | This defines the list of valid country codes, adapted from http://www.iso.org/iso/country_codes, ISO 3166-1 country code. List elements take the following form to identify a two-letter code with a short name in English, a three-digit code, and a three-letter code: For example, the entry for Japan includes Japan, 392, JPN. Short codes provide uniform recognition, avoiding language-dependent country names. The number code is helpful where Latin script may be problematic. Not all listed codes are universally recognized as countries, for example: code AQ is Antarctica, 010, ATA For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/ba:CountryCodeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**email** | **str** | The product manufacturer&#39;s business email address.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 180 characters | [optional] 
**phone** | **str** | The product manufacturer&#39;s business phone number.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 64 characters | [optional] 
**postal_code** | **str** | The postal code of the product manufacturer&#39;s street address.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 9 characters | [optional] 
**state_or_province** | **str** | The state or province of the product manufacturer&#39;s street address.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length&lt;/b&gt;: 64 characters | [optional] 

## Example

```python
from ebayinventory.models.manufacturer import Manufacturer

# TODO update the JSON string below
json = "{}"
# create an instance of Manufacturer from a JSON string
manufacturer_instance = Manufacturer.from_json(json)
# print the JSON string representation of the object
print(Manufacturer.to_json())

# convert the object into a dict
manufacturer_dict = manufacturer_instance.to_dict()
# create an instance of Manufacturer from a dict
manufacturer_from_dict = Manufacturer.from_dict(manufacturer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


