# PayoutDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_ids** | **list[str]** | This array indicates the list of true(actual) payout ids associated with a split payout. These values can be used as a path parameter for the &lt;b&gt;getPayout&lt;/b&gt; method to retrieve details on the associated payouts. | [optional] 
**payout_reference** | **str** | This field contains the unique identifier for the Payout Reference. In split-payout cases, this is the unique identifier reference (not true payout). This field is only returned and will show the associated true(actual) payout id(s) when sellers in Mainland China enable split payouts between a Payoneer account and/or a bank account.  This value can be used by the &lt;b&gt;filter&lt;/b&gt; query parameter of the &lt;b&gt;getPayouts&lt;/b&gt; method to get the monetary details of each true(actual) payout associated with the payoutReference. &lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt;Split-payout functionality will &lt;b&gt;only&lt;/b&gt; be available to mainland China sellers.&lt;/span&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

