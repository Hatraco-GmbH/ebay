# FundingSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **str** | The brand name of the credit card or the name of the financial institution that is the source of payment. This field may not be populated for other funding sources. | [optional] 
**memo** | **str** | This field provides a note about the funding source. If the seller&#x27;s credit card or bank account is the funding source, this field might contain the last four digits of the credit card or bank account. This field may also be returned as null. | [optional] 
**type** | **str** | The string value returned here indicates the funding source. Possible values include the following:&lt;ul&gt;&lt;li&gt;&lt;code&gt;AVAILABLE_FUNDS&lt;/code&gt;: transfer is funded with seller payout funds&lt;/li&gt;&lt;li&gt;&lt;code&gt;CREDIT_CARD&lt;/code&gt;: transfer is funded with seller&#x27;s credit card&lt;/li&gt;&lt;li&gt;&lt;code&gt;BANK&lt;/code&gt;: transfer is funded with a direct debit to seller&#x27;s bank account on file with eBay&lt;/li&gt;&lt;li&gt;&lt;code&gt;PAY_UPON_INVOICE&lt;/code&gt;: eBay will bill the seller for the transfer on the monthly invoice&lt;/li&gt;&lt;/ul&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

