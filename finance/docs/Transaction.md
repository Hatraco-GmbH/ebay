# Transaction

This type is used to express the details of one of the following monetary transactions: a buyer's payment for an order, a refund to the buyer for a returned item or cancelled order, or a credit issued by eBay to the seller's account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) |  | [optional] 
**booking_entry** | **str** | The enumeration value returned in this field indicates if the monetary transaction amount is a (&lt;code&gt;CREDIT&lt;/code&gt;) or a (&lt;code&gt;DEBIT&lt;/code&gt;) to the seller&#39;s account. Typically, the &lt;code&gt;SALE&lt;/code&gt; and &lt;code&gt;CREDIT&lt;/code&gt; transaction types are credits to the seller&#39;s account, and the &lt;code&gt;REFUND&lt;/code&gt;, &lt;code&gt;DISPUTE&lt;/code&gt;, &lt;code&gt;SHIPPING_LABEL&lt;/code&gt;, and &lt;code&gt;TRANSFER&lt;/code&gt; transaction types are debits to the seller&#39;s account. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/finances/types/pay:BookingEntryEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**buyer** | [**Buyer**](Buyer.md) |  | [optional] 
**e_bay_collected_tax_amount** | [**Amount**](Amount.md) |  | [optional] 
**fee_jurisdiction** | [**FeeJurisdiction**](FeeJurisdiction.md) |  | [optional] 
**fee_type** | **str** | The enumeration value returned in this field indicates the type of fee that was deducted from the seller payout. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/finances/types/api:FeeTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**order_id** | **str** | The unique identifier of the eBay order associated with the monetary transaction. | [optional] 
**order_line_items** | [**List[OrderLineItem]**](OrderLineItem.md) | This array either shows the order line item transactional fees related to a &lt;code&gt;SALE&lt;/code&gt; transaction and deducted from the payout associated with that order, or it shows the transactional fee credits going back to the seller in the case of a &lt;code&gt;REFUND&lt;/code&gt; transaction.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; In certain circumstances, transactional fees like &lt;code&gt;FINAL_VALUE_FEE&lt;/code&gt; and &lt;code&gt;FINAL_VALUE_FEE_FIXED_PER_ORDER&lt;/code&gt; are not deducted from a seller payout, but instead they are billed to the seller&#39;s account as \&quot;non-sale charges\&quot;. When this happens, the &lt;code&gt;SALE&lt;/code&gt; transaction entity will not have these fees under the &lt;b&gt;orderLineItems&lt;/b&gt; array, but they will appear as separate &lt;code&gt;NON_SALE_CHARGE&lt;/code&gt; transactions. When this happens, and you want to see those transactional fees for the order, one thing you can do is make another call to &lt;b&gt;getTransactions&lt;/b&gt; and filter against the &lt;b&gt;orderId&lt;/b&gt;. In the response, you will see the &lt;code&gt;SALE&lt;/code&gt; transaction and the &lt;code&gt;NON_SALE_CHARGE&lt;/code&gt; transactions applied against the order. See &lt;a href&#x3D;\&quot;/api-docs/sell/finances/resources/transaction/methods/getTransactions#s0-1-28-4-7-5-6-Gettransactionalfeesforanorder-5\&quot; &gt;Sample 6: Get transactional fees for an order&lt;/a&gt; and &lt;a href&#x3D;\&quot;/api-docs/sell/finances/resources/transaction/methods/getTransactions#s0-1-28-4-7-5-6-Getnon-salechargesforanorder-9\&quot;&gt;Sample 10: Get non-sale charges for an order&lt;/a&gt; for examples. | [optional] 
**payments_entity** | **str** | This string value indicates the entity that is processing the payment. | [optional] 
**payout_details** | [**PayoutDetails**](PayoutDetails.md) |  | [optional] 
**payout_id** | **str** | The unique identifier of the seller payout associated with the monetary transaction. This identifier is generated once eBay begins processing the payout for the corresponding order. This field will not be returned if eBay has not yet begun processing the payout for an order.&lt;br&gt;&lt;br&gt;This value can be used by the &lt;b&gt;filter&lt;/b&gt; query parameter to get monetary transactions associated with the true(actual) payout associated with the &lt;b&gt;PayoutId&lt;/b&gt;.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; In case of a split payout, always pick the first true(actual) payout id.&lt;/span&gt;  | [optional] 
**references** | [**List[Reference]**](Reference.md) | This field contains reference information for the transaction fee. This includes an ID and the type of ID provided (such as item ID). | [optional] 
**sales_record_reference** | **str** | The Sales Record Number associated with a sales order. Sales Record Numbers are Selling Manager/Selling Manager Pro identifiers that are created at order checkout.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; For all orders originating after February 1, 2020, a value of &lt;code&gt;0&lt;/code&gt; will be returned in this field. The Sales Record Number field has also been removed from Seller Hub. Instead of &lt;strong&gt;salesRecordReference&lt;/strong&gt;, depend on &lt;strong&gt;orderId&lt;/strong&gt; instead as the identifier of the order. The &lt;strong&gt;salesRecordReference&lt;/strong&gt; field has been scheduled for deprecation, and a date for when this field will no longer be returned at all will be announced soon.&lt;/span&gt; | [optional] 
**taxes** | [**List[Tax]**](Tax.md) | This array shows the tax type and amount applicable to the transaction. &lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Currently, this array is only returned for tax charged against a purchased eBay shipping label.&lt;/span&gt; | [optional] 
**total_fee_amount** | [**Amount**](Amount.md) |  | [optional] 
**total_fee_basis_amount** | [**Amount**](Amount.md) |  | [optional] 
**transaction_date** | **str** | This timestamp indicates when the monetary transaction (order purchase, buyer refund, seller credit) occurred. The following (UTC) format is used: &lt;code&gt;YYYY-MM-DDTHH:MM:SS.SSSZ&lt;/code&gt;. For example, &lt;code&gt;2015-08-04T19:09:02.768Z&lt;/code&gt;. | [optional] 
**transaction_id** | **str** | This field, when combined with the &lt;a href&#x3D;\&quot;#response.transactions.transactionType\&quot; &gt;transactionType&lt;/a&gt; field, provide a unique identifier of the monetary transaction. A monetary transaction can be a sales order, an order refund to the buyer, a credit to the seller&#39;s account, a debit to the seller for the purchase of a shipping label, or a transaction where eBay recouped money from the seller if the seller lost a buyer-initiated payment dispute. | [optional] 
**transaction_memo** | **str** | This field applies to shipping label transactions, sales transactions where payout is on hold, and non-sale charge fees. The following are examples of how the field is used for each transaction type:&lt;ul&gt;&lt;li&gt;&lt;b&gt;Shipping label purchase&lt;/b&gt;: the &lt;b&gt;transactionMemo&lt;/b&gt; field gives details about a purchase, a refund, or a price adjustment to the cost of the shipping label.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Sales transactions with funds on hold&lt;/b&gt;: the &lt;b&gt;transactionMemo&lt;/b&gt; field provides information on the reason for the hold or when the hold will be released (e.g., \&quot;Funds on hold. Estimated release on Jun 1\&quot;).&lt;/li&gt;&lt;li&gt;&lt;b&gt;Non-sale charge fees&lt;/b&gt;: the &lt;b&gt;transactionMemo&lt;/b&gt; field will provide the type of fee that was charged, such as Promoted Offsite Fee.&lt;/li&gt;&lt;/ul&gt;This field is only returned if applicable/available. | [optional] 
**transaction_status** | **str** | This enumeration value indicates the current status of the seller payout associated with the monetary transaction. See the &lt;code&gt;TransactionStatusEnum&lt;/code&gt; type for more information on the different states. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/finances/types/pay:TransactionStatusEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**transaction_type** | **str** | This enumeration value indicates the type of monetary transaction. Examples of monetary transactions include a buyer&#39;s payment for an order, a refund to the buyer for a returned item or cancelled order, or a credit issued by eBay to the seller&#39;s account. For a complete list of monetary transaction types within the &lt;strong&gt;Finances API&lt;/strong&gt;, see the &lt;a href&#x3D;\&quot;/api-docs/sell/finances/types/pay:TransactionTypeEnum\&quot;&gt;TransactionTypeEnum&lt;/a&gt; type. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/finances/types/pay:TransactionTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from ebayfinance.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_from_dict = Transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


