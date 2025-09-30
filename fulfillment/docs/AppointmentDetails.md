# AppointmentDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appointment_end_time** | **str** | The date and time the appointment ends, formatted as an &lt;a href&#x3D;\&quot;https://www.iso.org/iso-8601-date-and-time-format.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 8601&lt;/a&gt; string, which is based on the 24-hour Coordinated Universal Time (UTC) clock. Required for tire installation. &lt;br&gt;&lt;br&gt;&lt;b&gt;Format:&lt;/b&gt; &lt;code&gt;[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z&lt;/code&gt; &lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;2022-10-28T00:00:00.000Z&lt;/code&gt; | [optional] 
**appointment_start_time** | **str** | The date and time the appointment begins, formatted as an &lt;a href&#x3D;\&quot;https://www.iso.org/iso-8601-date-and-time-format.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 8601&lt;/a&gt; string, which is based on the 24-hour Coordinated Universal Time (UTC) clock.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Format:&lt;/b&gt; &lt;code&gt;[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z&lt;/code&gt; &lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;2022-10-28T00:10:00.000Z&lt;/code&gt; | [optional] 
**appointment_status** | **str** | The status of the appointment. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AppointmentStatusEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**appointment_type** | **str** | The type of appointment. MACRO appointments only have a start time (not bounded with end time). TIME_SLOT appointments have a period (both start time and end time). Required for tire installation. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AppointmentTypeEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**appointment_window** | **str** | Appointment window for MACRO appointments. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AppointmentWindowEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**service_provider_appointment_date** | **str** | Service provider date of the appointment (no time stamp). Returned only for MACRO appointment types. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

