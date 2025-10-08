# OperatingHours

This type is used to express the regular operating hours of a merchant's store or fulfillment center during the days of the week.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week_enum** | **str** | A &lt;strong&gt;dayOfWeekEnum&lt;/strong&gt; value is required for each day of the week that the store location has regular operating hours. &lt;br&gt;&lt;br&gt;This field is returned if operating hours are defined for the store location. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/api:DayOfWeekEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**intervals** | [**List[Interval]**](Interval.md) | This container is used to define the opening and closing times of a store location&#39;s working day (defined in the &lt;strong&gt;dayOfWeekEnum&lt;/strong&gt; field). An &lt;strong&gt;intervals&lt;/strong&gt; container is needed for each day of the week that the store location is open. If a store location closes for lunch (or any other period during the day) and then reopens, multiple &lt;strong&gt;open&lt;/strong&gt; and &lt;strong&gt;close&lt;/strong&gt; pairs are needed &lt;br&gt;&lt;br&gt;This container is returned if operating hours are defined for the store location. | [optional] 

## Example

```python
from ebayinventory.models.operating_hours import OperatingHours

# TODO update the JSON string below
json = "{}"
# create an instance of OperatingHours from a JSON string
operating_hours_instance = OperatingHours.from_json(json)
# print the JSON string representation of the object
print(OperatingHours.to_json())

# convert the object into a dict
operating_hours_dict = operating_hours_instance.to_dict()
# create an instance of OperatingHours from a dict
operating_hours_from_dict = OperatingHours.from_dict(operating_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


