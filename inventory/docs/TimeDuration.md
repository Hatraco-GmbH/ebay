# TimeDuration

This type is used to indicate the fulfillment time for an In-Store Pickup order, or for an order than will be shipped to the buyer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | This enumeration value indicates the time unit used to specify the fulfillment time, such as &lt;code&gt;BUSINESS_DAY&lt;/code&gt;. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:TimeDurationUnitEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**value** | **int** | The integer value in this field, along with the time unit in the &lt;strong&gt;unit&lt;/strong&gt; field, will indicate the fulfillment time.&lt;br&gt;&lt;br&gt;For standard orders that will be shipped, this value will indicate the expected fulfillment time if the inventory item is shipped from the inventory location. If the value of this field is &lt;code&gt;4&lt;/code&gt;, and the value of the &lt;strong&gt;unit&lt;/strong&gt; field is &lt;code&gt;BUSINESS_DAY&lt;/code&gt;, then the estimated delivery date after purchase is 4 business days. | [optional] 

## Example

```python
from ebayinventory.models.time_duration import TimeDuration

# TODO update the JSON string below
json = "{}"
# create an instance of TimeDuration from a JSON string
time_duration_instance = TimeDuration.from_json(json)
# print the JSON string representation of the object
print(TimeDuration.to_json())

# convert the object into a dict
time_duration_dict = time_duration_instance.to_dict()
# create an instance of TimeDuration from a dict
time_duration_from_dict = TimeDuration.from_dict(time_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


