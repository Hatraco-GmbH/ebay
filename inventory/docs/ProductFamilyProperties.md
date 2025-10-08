# ProductFamilyProperties

This type is used to specify the details of a motor vehicle that is compatible with the inventory item specified through the SKU value in the call URI.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **str** | &lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt; The &lt;strong&gt;productFamilyProperties&lt;/strong&gt; container is no longer supported.&lt;/p&gt;&lt;/div&gt; | [optional] 
**make** | **str** | &lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt; The &lt;strong&gt;productFamilyProperties&lt;/strong&gt; container is no longer supported.&lt;/p&gt;&lt;/div&gt; | [optional] 
**model** | **str** | &lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt; The &lt;strong&gt;productFamilyProperties&lt;/strong&gt; container is no longer supported.&lt;/p&gt;&lt;/div&gt; | [optional] 
**trim** | **str** | &lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt; The &lt;strong&gt;productFamilyProperties&lt;/strong&gt; container is no longer supported.&lt;/p&gt;&lt;/div&gt; | [optional] 
**year** | **str** | &lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt; The &lt;strong&gt;productFamilyProperties&lt;/strong&gt; container is no longer supported.&lt;/p&gt;&lt;/div&gt; | [optional] 

## Example

```python
from ebayinventory.models.product_family_properties import ProductFamilyProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ProductFamilyProperties from a JSON string
product_family_properties_instance = ProductFamilyProperties.from_json(json)
# print the JSON string representation of the object
print(ProductFamilyProperties.to_json())

# convert the object into a dict
product_family_properties_dict = product_family_properties_instance.to_dict()
# create an instance of ProductFamilyProperties from a dict
product_family_properties_from_dict = ProductFamilyProperties.from_dict(product_family_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


