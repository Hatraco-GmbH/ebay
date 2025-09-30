# OrderLineItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**donations** | [**list[Fee]**](Fee.md) | The list of donations applied to the line item.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note: &lt;/b&gt;Currently, this array is only returned if the seller chooses to donate a percentage of the sales proceeds to a charitable organization registered with the eBay for Charity program.&lt;/span&gt; | [optional] 
**fee_basis_amount** | [**Amount**](Amount.md) |  | [optional] 
**line_item_id** | **str** | The unique identifier of an order line item. | [optional] 
**marketplace_fees** | [**list[Fee]**](Fee.md) | An array of all fees accrued for the order line item and deducted from a seller payout. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

