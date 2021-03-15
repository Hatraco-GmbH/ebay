# OperatingHours

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week_enum** | **str** | A dayOfWeekEnum value is required for each day of the week that the store location has regular operating hours. This field is returned if operating hours are defined for the store location. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/inventory/types/api:DayOfWeekEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**intervals** | [**list[Interval]**](Interval.md) | This container is used to define the opening and closing times of a store&#x27;s working day (defined in the dayOfWeekEnum field). An intervals container is needed for each day of the week that the store location is open. If a store location closes for lunch (or any other period during the day) and then reopens, multiple open and close pairs are needed This container is returned if operating hours are defined for the store location. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

