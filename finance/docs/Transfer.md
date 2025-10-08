# Transfer

This type is the base response type used by <code>TRANSFER</code> transaction type that is returned in the response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**funding_source** | [**FundingSource**](FundingSource.md) |  | [optional] 
**transaction_date** | **str** | This timestamp indicates the date/time of the transfer. The following (UTC) format is used: &lt;code&gt;YYYY-MM-DDTHH:MM:SS.SSSZ&lt;/code&gt;. For example, &lt;code&gt;2020-08-04T19:09:02.768Z&lt;/code&gt; | [optional] 
**transfer_amount** | [**Amount**](Amount.md) |  | [optional] 
**transfer_detail** | [**TransferDetail**](TransferDetail.md) |  | [optional] 
**transfer_id** | **str** | The unique identifier of the &lt;code&gt;TRANSFER&lt;/code&gt; transaction type. This is the same value that was passed into the end of the call URI. | [optional] 

## Example

```python
from ebayfinance.models.transfer import Transfer

# TODO update the JSON string below
json = "{}"
# create an instance of Transfer from a JSON string
transfer_instance = Transfer.from_json(json)
# print the JSON string representation of the object
print(Transfer.to_json())

# convert the object into a dict
transfer_dict = transfer_instance.to_dict()
# create an instance of Transfer from a dict
transfer_from_dict = Transfer.from_dict(transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


