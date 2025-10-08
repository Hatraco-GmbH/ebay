# ShipToLocationAvailabilityWithAll

This type is used to specify the total 'ship-to-home' quantity of the inventory items that will be available for purchase through one or more published offers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_by_format** | [**FormatAllocation**](FormatAllocation.md) |  | [optional] 
**availability_distributions** | [**List[AvailabilityDistribution]**](AvailabilityDistribution.md) | This container is used to set the available quantity of the inventory item at one or more warehouse locations.&lt;br&gt;&lt;br&gt;This container will be returned if the available quantity is set for one or more inventory locations. | [optional] 
**quantity** | **int** | &lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt; Publish offer note: Although this field is not required before an offer can be published to create an active listing, out of stock listings will result if this field is omitted or set to &lt;code&gt;0&lt;/code&gt;.&lt;/p&gt;&lt;/div&gt;&lt;br&gt;This field is used to set the total &#39;ship-to-home&#39; quantity of the inventory item that will be available for purchase through one or more published offers. This field is not immediately required, but &#39;ship-to-home&#39; quantity must be set before an offer of the inventory item can be published.&lt;br&gt;&lt;br&gt;If an existing inventory item is being updated, and the &#39;ship-to-home&#39; quantity already exists for the inventory item record, this field should be included again, even if the value is not changing, or the available quantity data will be lost. | [optional] 

## Example

```python
from ebayinventory.models.ship_to_location_availability_with_all import ShipToLocationAvailabilityWithAll

# TODO update the JSON string below
json = "{}"
# create an instance of ShipToLocationAvailabilityWithAll from a JSON string
ship_to_location_availability_with_all_instance = ShipToLocationAvailabilityWithAll.from_json(json)
# print the JSON string representation of the object
print(ShipToLocationAvailabilityWithAll.to_json())

# convert the object into a dict
ship_to_location_availability_with_all_dict = ship_to_location_availability_with_all_instance.to_dict()
# create an instance of ShipToLocationAvailabilityWithAll from a dict
ship_to_location_availability_with_all_from_dict = ShipToLocationAvailabilityWithAll.from_dict(ship_to_location_availability_with_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


