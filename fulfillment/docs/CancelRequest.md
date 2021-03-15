# CancelRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_completed_date** | **str** | The date and time that the order cancellation was completed, if applicable. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned until the cancellation request has actually been approved by the seller. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z | [optional] 
**cancel_initiator** | **str** | This string value indicates the party who made the initial cancellation request. Typically, either the &#x27;Buyer&#x27; or &#x27;Seller&#x27;. If a cancellation request has been made, this field should be returned. | [optional] 
**cancel_reason** | **str** | The reason why the cancelInitiator initiated the cancellation request. Cancellation reasons for a buyer might include &#x27;order placed by mistake&#x27; or &#x27;order won&#x27;t arrive in time&#x27;. For a seller, a typical cancellation reason is &#x27;out of stock&#x27;. If a cancellation request has been made, this field should be returned. | [optional] 
**cancel_requested_date** | **str** | The date and time that the order cancellation was requested. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is returned for each cancellation request. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z | [optional] 
**cancel_request_id** | **str** | The unique identifier of the order cancellation request. This field is returned for each cancellation request. | [optional] 
**cancel_request_state** | **str** | The current stage or condition of the cancellation request. This field is returned for each cancellation request. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:CancelRequestStateEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

