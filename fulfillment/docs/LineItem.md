# LineItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_promotions** | [**list[AppliedPromotion]**](AppliedPromotion.md) | This array contains information about one or more sales promotions or discounts applied to the line item. It is always returned, but will be returned as an empty array if no special sales promotions or discounts apply to the order line item. | [optional] 
**delivery_cost** | [**DeliveryCost**](DeliveryCost.md) |  | [optional] 
**discounted_line_item_cost** | [**Amount**](Amount.md) |  | [optional] 
**ebay_collect_and_remit_taxes** | [**list[EbayCollectAndRemitTax]**](EbayCollectAndRemitTax.md) | This container will be returned if the order line item is subject to a &#x27;Collect and Remit&#x27; tax that eBay will collect and remit to the proper taxing authority on the buyer&#x27;s behalf. &#x27;Collect and Remit&#x27; tax includes US state-mandated sales tax and &#x27;Goods and Services&#x27; tax (collected in Australia and New Zealand). The amount of this tax is shown in the amount field, and the type of tax is shown in the taxType field. eBay will display the tax type and amount during checkout in accordance with the buyer&#x27;s address, and handle collection and remittance of the tax without requiring the seller to take any action. | [optional] 
**gift_details** | [**GiftDetails**](GiftDetails.md) |  | [optional] 
**legacy_item_id** | **str** | The eBay-generated legacy listing item ID of the listing. Note that the unique identifier of a listing in REST-based APIs is called the listingId instead. | [optional] 
**legacy_variation_id** | **str** | The unique identifier of a single variation within a multiple-variation listing. This field is only returned if the line item purchased was from a multiple-variation listing. | [optional] 
**line_item_cost** | [**Amount**](Amount.md) |  | [optional] 
**line_item_fulfillment_instructions** | [**LineItemFulfillmentInstructions**](LineItemFulfillmentInstructions.md) |  | [optional] 
**line_item_fulfillment_status** | **str** | This enumeration value indicates the current fulfillment status of the line item. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:LineItemFulfillmentStatusEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**line_item_id** | **str** | This is the unique identifier of an eBay order line item. This field is created as soon as there is a commitment to buy from the seller. | [optional] 
**listing_marketplace_id** | **str** | The unique identifier of the eBay marketplace where the line item was listed. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:MarketplaceIdEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**properties** | [**LineItemProperties**](LineItemProperties.md) |  | [optional] 
**purchase_marketplace_id** | **str** | The unique identifier of the eBay marketplace where the line item was listed. Often, the listingMarketplaceId and the purchaseMarketplaceId identifier are the same, but there are occasions when an item will surface on multiple eBay marketplaces. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:MarketplaceIdEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**quantity** | **int** | The number of units of the line item in the order. These are represented as a group by a single lineItemId. | [optional] 
**refunds** | [**list[LineItemRefund]**](LineItemRefund.md) | This array is always returned, but is returned as an empty array unless the seller has submitted a partial or full refund to the buyer for the order. If a refund has occurred, the refund amount and refund date will be shown for each refund. | [optional] 
**sku** | **str** | Seller-defined Stock-Keeping Unit (SKU). This inventory identifier must be unique within the seller&#x27;s eBay inventory. SKUs are optional when listing in the legacy/Trading API system, but SKUs are required when listing items through the Inventory API model. | [optional] 
**sold_format** | **str** | The eBay listing type of the line item. The most common listing types are AUCTION and FIXED_PRICE. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:SoldFormatEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**taxes** | [**list[Tax]**](Tax.md) | Contains a list of taxes applied to the line item, if any. This array is always returned, but will be returned as empty if no taxes are applicable to the line item, or if the seller is opted in to eBay managed payments. | [optional] 
**title** | **str** | The title of the listing. | [optional] 
**total** | [**Amount**](Amount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

