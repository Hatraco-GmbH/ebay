# ExtendedProducerResponsibility

This type provides IDs for the producer or importer related to the new item, packaging, added documentation, or an eco-participation fee. In some markets, such as in France, this may be the importer of the item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eco_participation_fee** | [**Amount**](Amount.md) |  | [optional] 
**producer_product_id** | **str** | &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;b&gt;THIS FIELD IS DEPRECATED AND NO LONGER SUPPORTED.&lt;/b&gt; For sellers selling on the eBay France Marketplace, Extended Producer Responsibility ID fields are no longer set at the listing level. Instead, sellers must provide these IDs for each applicable category in their My eBay accounts. The URL will be based on the seller&#39;s home/registration site, and will use this pattern: https://accountsettings./epr-fr. Sellers based in the US will use &lt;a href&#x3D;\&quot;https://accountsettings.ebay.com/epr-fr\&quot; target&#x3D;\&quot;_blank\&quot;&gt;https://accountsettings.ebay.com/epr-fr&lt;/a&gt;, sellers based in France will use &lt;a href&#x3D;\&quot;https://accountsettings.ebay.fr/epr-fr\&quot; target&#x3D;\&quot;_blank\&quot;&gt;https://accountsettings.ebay.fr/epr-fr&lt;/a&gt;, and so on.&lt;/span&gt; | [optional] 
**product_documentation_id** | **str** | &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;b&gt;THIS FIELD IS DEPRECATED AND NO LONGER SUPPORTED.&lt;/b&gt; For sellers selling on the eBay France Marketplace, Extended Producer Responsibility ID fields are no longer set at the listing level. Instead, sellers must provide these IDs for each applicable category in their My eBay accounts. The URL will be based on the seller&#39;s home/registration site, and will use this pattern: https://accountsettings./epr-fr. Sellers based in the US will use &lt;a href&#x3D;\&quot;https://accountsettings.ebay.com/epr-fr\&quot; target&#x3D;\&quot;_blank\&quot;&gt;https://accountsettings.ebay.com/epr-fr&lt;/a&gt;, sellers based in France will use &lt;a href&#x3D;\&quot;https://accountsettings.ebay.fr/epr-fr\&quot; target&#x3D;\&quot;_blank\&quot;&gt;https://accountsettings.ebay.fr/epr-fr&lt;/a&gt;, and so on.&lt;/span&gt; | [optional] 
**product_package_id** | **str** | &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;b&gt;THIS FIELD IS DEPRECATED AND NO LONGER SUPPORTED.&lt;/b&gt; For sellers selling on the eBay France Marketplace, Extended Producer Responsibility ID fields are no longer set at the listing level. Instead, sellers must provide these IDs for each applicable category in their My eBay accounts. The URL will be based on the seller&#39;s home/registration site, and will use this pattern: https://accountsettings./epr-fr. Sellers based in the US will use &lt;a href&#x3D;\&quot;https://accountsettings.ebay.com/epr-fr\&quot; target&#x3D;\&quot;_blank\&quot;&gt;https://accountsettings.ebay.com/epr-fr&lt;/a&gt;, sellers based in France will use &lt;a href&#x3D;\&quot;https://accountsettings.ebay.fr/epr-fr\&quot; target&#x3D;\&quot;_blank\&quot;&gt;https://accountsettings.ebay.fr/epr-fr&lt;/a&gt;, and so on.&lt;/span&gt; | [optional] 
**shipment_package_id** | **str** | &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;b&gt;THIS FIELD IS DEPRECATED AND NO LONGER SUPPORTED.&lt;/b&gt; For sellers selling on the eBay France Marketplace, Extended Producer Responsibility ID fields are no longer set at the listing level. Instead, sellers must provide these IDs for each applicable category in their My eBay accounts. The URL will be based on the seller&#39;s home/registration site, and will use this pattern: https://accountsettings./epr-fr. Sellers based in the US will use &lt;a href&#x3D;\&quot;https://accountsettings.ebay.com/epr-fr\&quot; target&#x3D;\&quot;_blank\&quot;&gt;https://accountsettings.ebay.com/epr-fr&lt;/a&gt;, sellers based in France will use &lt;a href&#x3D;\&quot;https://accountsettings.ebay.fr/epr-fr\&quot; target&#x3D;\&quot;_blank\&quot;&gt;https://accountsettings.ebay.fr/epr-fr&lt;/a&gt;, and so on.&lt;/span&gt; | [optional] 

## Example

```python
from ebayinventory.models.extended_producer_responsibility import ExtendedProducerResponsibility

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedProducerResponsibility from a JSON string
extended_producer_responsibility_instance = ExtendedProducerResponsibility.from_json(json)
# print the JSON string representation of the object
print(ExtendedProducerResponsibility.to_json())

# convert the object into a dict
extended_producer_responsibility_dict = extended_producer_responsibility_instance.to_dict()
# create an instance of ExtendedProducerResponsibility from a dict
extended_producer_responsibility_from_dict = ExtendedProducerResponsibility.from_dict(extended_producer_responsibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


