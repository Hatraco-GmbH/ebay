# EvaluationCycle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** | End date and time of the transaction lookback range. All timestamps are based on Mountain Standard Time (MST). The timestamp is formatted as an ISO 8601 string, which is based on the 24-hour Coordinated Universal Time (UTC) clock. | [optional] 
**evaluation_date** | **str** | The ISO-8601 date and time at which the seller was evaluated for this customer service metric rating. | [optional] 
**evaluation_type** | **str** | This field specifies the transaction lookback period used for the evaluation. The evaluation_type value specified in the request is returned in this field. There are two possible values: CURRENT &amp;ndash; A monthly evaluation that occurs on the 20th of every month. PROJECTED &amp;ndash; A daily evaluation that provides a projection of how the seller is currently performing with regards to the upcoming evaluation period. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/analytics/types/api:EvaluationTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**start_date** | **str** | The start date and time of the transaction lookback range. All timestamps are based on Mountain Standard Time (MST). The timestamp is formatted as an ISO 8601 string, which is based on the 24-hour Coordinated Universal Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2018-08-04T07:09:00.000Z | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


