# Offer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_counter_offer** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, the buyer is allowed to make a counter-offer to the seller&#x27;s offer. | [optional] 
**buyer** | [**User**](User.md) |  | [optional] 
**creation_date** | **str** | The date and time when the seller&#x27;s offer was created.  &lt;br&gt;&lt;br&gt;The returned timestamp is formatted as an &lt;a href&#x3D;\&quot;https://www.iso.org/iso-8601-date-and-time-format.html\&quot; title&#x3D;\&quot;https://www.iso.org\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 8601&lt;/a&gt; string, which is based on the 24-hour Coordinated Universal Time (UTC) clock.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Format:&lt;/b&gt; &lt;code&gt;[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z&lt;/code&gt; &lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;2018-08-20T07:09:00.000Z&lt;/code&gt; | [optional] 
**initiated_by** | **str** | The eBay &lt;b&gt;UserName&lt;/b&gt; of the user (seller) who initiated the offer. | [optional] 
**last_modified_date** | **str** | The date and time when the offer was last modified.  &lt;br&gt;&lt;br&gt;The returned timestamp is formatted as an &lt;a href&#x3D;\&quot;http://www.iso.org/iso/home/standards/iso8601.htm\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 8601&lt;/a&gt; string. | [optional] 
**message** | **str** | A seller-defined message related to the offer being made. This message is sent to the list of \&quot;interested\&quot; buyers along with the offer message from eBay. | [optional] 
**offer_duration** | [**TimeDuration**](TimeDuration.md) |  | [optional] 
**offered_items** | [**list[OfferedItem]**](OfferedItem.md) | The list of items associated with the offer. &lt;br&gt;&lt;br&gt;Currently, the offer list is restricted to a single offer. | [optional] 
**offer_id** | **str** | A unique eBay-assigned identifier for the offer. | [optional] 
**offer_status** | **str** | The current state, or status, of an offer.  &lt;br&gt;&lt;br&gt;Status states include &lt;code&gt;PENDING&lt;/code&gt;, &lt;code&gt;COUNTERED&lt;/code&gt;, &lt;code&gt;ACCEPTED&lt;/code&gt;, and &lt;code&gt;DECLINED&lt;/code&gt;. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/negotiation/types/api:OfferStatusEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**offer_type** | **str** | The type of offer being made. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/negotiation/types/api:OfferTypeEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**revision** | **str** | A unique, eBay-assigned ID for the revision of the offer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

