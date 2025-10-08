# SameDayShippingCutOffTimes

This type is used by the <b>createInventoryLocation</b> call to specify cut-off time(s) for an inventory location, as well as any overrides for these times.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overrides** | [**List[Overrides]**](Overrides.md) | This container can be used to override the existing cut-off time(s), specified in the &lt;b&gt;weeklySchedule&lt;/b&gt; container, for a specific date or date range. | [optional] 
**weekly_schedule** | [**List[WeeklySchedule]**](WeeklySchedule.md) | This container is used to specify the weekly schedule for shipping and handling cut-off times. A cut-off time is required for each business day that the fulfillment center operates. Any orders made after the specified &lt;b&gt;cutOffTime&lt;/b&gt; on the specified day(s) of the week will be handled on the next day. | [optional] 

## Example

```python
from ebayinventory.models.same_day_shipping_cut_off_times import SameDayShippingCutOffTimes

# TODO update the JSON string below
json = "{}"
# create an instance of SameDayShippingCutOffTimes from a JSON string
same_day_shipping_cut_off_times_instance = SameDayShippingCutOffTimes.from_json(json)
# print the JSON string representation of the object
print(SameDayShippingCutOffTimes.to_json())

# convert the object into a dict
same_day_shipping_cut_off_times_dict = same_day_shipping_cut_off_times_instance.to_dict()
# create an instance of SameDayShippingCutOffTimes from a dict
same_day_shipping_cut_off_times_from_dict = SameDayShippingCutOffTimes.from_dict(same_day_shipping_cut_off_times_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


