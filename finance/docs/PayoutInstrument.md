# PayoutInstrument

This type is used to provide details about one or two of the seller's accounts that are enabled to receive payouts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_last_four_digits** | **str** | This value is the last four digits of the account that the seller uses to receive the payout. This may be the last four digits of a bank account, a debit card, or a payment processor account such as Payoneer. | [optional] 
**instrument_type** | **str** | This value indicates the type of account that received the payout. The value returned in this field may be:&lt;br&gt;&lt;ul&gt;&lt;li&gt;&lt;code&gt;BANK&lt;/code&gt;: indicates that the payout was made to a seller&#39;s bank account.&lt;/li&gt;&lt;li&gt;&lt;code&gt;CARD&lt;/code&gt;: indicates that the payout went to a seller&#39;s debit card&lt;/li&gt;&lt;li&gt;The name of a digital wallet provider or payment processor (e.g., &lt;code&gt;PAYONEER&lt;/code&gt;)&lt;/li&gt;&lt;/ul&gt;&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Only Payoneer is currently supported for sellers in mainland China. Card payouts are not currently available for sellers in mainland China.&lt;/span&gt; | [optional] 
**nickname** | **str** | When &lt;b&gt;instrumentType&lt;/b&gt; returns &lt;code&gt;BANK&lt;/code&gt;, this value is the seller-provided nickname that the seller uses to represent the bank account that receives the payout.&lt;br&gt;&lt;br&gt;When &lt;b&gt;instrumentType&lt;/b&gt; returns &lt;code&gt;CARD&lt;/code&gt;, this value is the debit card network for the debit card that receives the payout.&lt;br&gt;&lt;br&gt;When &lt;b&gt;instrumentType&lt;/b&gt; returns a provider of digital wallet or payment processing services, the value returned is the name of the service provider (e.g., &lt;code&gt;PAYONEER&lt;/code&gt;).&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Card payouts are not currently available for sellers in mainland China.&lt;/span&gt; | [optional] 
**payout_percentage** | **str** | This value indicates the current payout percentage allocated to a payout instrument. For example, &lt;code&gt;50&lt;/code&gt; indicates that 50% of the payout goes to the instrument.&lt;br&gt;&lt;br&gt;This field will be returned even when 100% of the payout funds are going to one payout instrument.&lt;br&gt;&lt;br&gt;This field is only returned to sellers in mainland China. | [optional] 

## Example

```python
from ebayfinance.models.payout_instrument import PayoutInstrument

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutInstrument from a JSON string
payout_instrument_instance = PayoutInstrument.from_json(json)
# print the JSON string representation of the object
print(PayoutInstrument.to_json())

# convert the object into a dict
payout_instrument_dict = payout_instrument_instance.to_dict()
# create an instance of PayoutInstrument from a dict
payout_instrument_from_dict = PayoutInstrument.from_dict(payout_instrument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


