# LineItemFulfillmentInstructions

This type contains the specifications for processing the fulfillment of a line item, including the handling window and the delivery window. These fields provide guidance for <i>eBay Guaranteed Delivery</i> as well as for non-guaranteed delivery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guaranteed_delivery** | **bool** | Although this field is still returned, it can be ignored since eBay Guaranteed Delivery is no longer a supported feature on any marketplace. This field may get removed from the schema in the future. | [optional] 
**max_estimated_delivery_date** | **str** | The estimated latest date and time that the buyer can expect to receive the line item based on the seller&#39;s stated handling time and the transit times of the available shipping service options. The seller must pay extra attention to this date, as a failure to deliver by this date/time can result in a &#39;Late shipment&#39; seller defect, and can affect seller level and Top-Rated Seller status. In addition to the seller defect, buyers will be eligible for a shipping cost refund, and will also be eligible to return the item for a full refund (with no return shipping charge) if they choose. &lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. &lt;br&gt;&lt;br&gt;&lt;b&gt;Format:&lt;/b&gt; &lt;code&gt;[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z&lt;/code&gt; &lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;2015-08-04T19:09:02.768Z&lt;/code&gt;&lt;/span&gt; | [optional] 
**min_estimated_delivery_date** | **str** | The estimated earliest date and time that the buyer can expect to receive the line item based on the seller&#39;s stated handling time and the transit times of the available shipping service options.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. &lt;br&gt;&lt;br&gt;&lt;b&gt;Format:&lt;/b&gt; &lt;code&gt;[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z&lt;/code&gt; &lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;2015-08-04T19:09:02.768Z&lt;/code&gt;&lt;/span&gt; | [optional] 
**ship_by_date** | **str** | The latest date and time by which the seller should ship line item in order to meet the expected delivery window. This timestamp will be set by eBay based on time of purchase and the seller&#39;s stated handling time. The seller must pay extra attention to this date, as a failure to physically ship the line item by this date/time can result in a &#39;Late shipment&#39; seller defect, and can affect seller level and Top-Rated Seller status. In addition to the seller defect, buyers will be eligible for a shipping cost refund, and will also be eligible to return the item for a full refund (with no return shipping charge) if they choose. &lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. &lt;br&gt;&lt;br&gt;&lt;b&gt;Format:&lt;/b&gt; &lt;code&gt;[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z&lt;/code&gt; &lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;2015-08-04T19:09:02.768Z&lt;/code&gt;&lt;/span&gt; | [optional] 

## Example

```python
from ebayfulfillment.models.line_item_fulfillment_instructions import LineItemFulfillmentInstructions

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemFulfillmentInstructions from a JSON string
line_item_fulfillment_instructions_instance = LineItemFulfillmentInstructions.from_json(json)
# print the JSON string representation of the object
print(LineItemFulfillmentInstructions.to_json())

# convert the object into a dict
line_item_fulfillment_instructions_dict = line_item_fulfillment_instructions_instance.to_dict()
# create an instance of LineItemFulfillmentInstructions from a dict
line_item_fulfillment_instructions_from_dict = LineItemFulfillmentInstructions.from_dict(line_item_fulfillment_instructions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


