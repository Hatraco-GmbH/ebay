# EnergyEfficiencyLabel

This type provides information about the energy efficiency for certain durable goods.<br><br><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span> When providing energy efficiency information on an appliance or smartphones and tablets listing, the energy efficiency <b>rating</b> and <b>range</b> of the item must be specified through the the <a href= \"/api-docs/sell/inventory/resources/inventory_item/methods/bulkCreateOrReplaceInventoryItem#request.requests.product.aspects\" target=\"_blank\">aspects</a> field when creating the inventory item record. Use the <a href= \"/api-docs/commerce/taxonomy/resources/category_tree/methods/getItemAspectsForCategory\" target=\"_blank\">getItemAspectsForCategory</a> method of the Taxonomy API to retrieve applicable rating and range values for a specified category.</p></div>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_description** | **str** | A brief verbal summary of the information included on the Energy Efficiency Label for an item.&lt;br&gt;&lt;br&gt;For example, &lt;i&gt;On a scale of A to G the rating is E.&lt;/i&gt; | [optional] 
**image_url** | **str** | The URL to the Energy Efficiency Label image that is applicable to an item. | [optional] 
**product_information_sheet** | **str** | The URL to the Product Information Sheet that provides complete manufacturer-provided efficiency information about an item. | [optional] 

## Example

```python
from ebayinventory.models.energy_efficiency_label import EnergyEfficiencyLabel

# TODO update the JSON string below
json = "{}"
# create an instance of EnergyEfficiencyLabel from a JSON string
energy_efficiency_label_instance = EnergyEfficiencyLabel.from_json(json)
# print the JSON string representation of the object
print(EnergyEfficiencyLabel.to_json())

# convert the object into a dict
energy_efficiency_label_dict = energy_efficiency_label_instance.to_dict()
# create an instance of EnergyEfficiencyLabel from a dict
energy_efficiency_label_from_dict = EnergyEfficiencyLabel.from_dict(energy_efficiency_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


