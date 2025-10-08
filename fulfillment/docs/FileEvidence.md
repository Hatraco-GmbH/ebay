# FileEvidence

This type is used to store the unique identifier of an evidence file. Evidence files are used by seller to contest a payment dispute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | This field is used to identify the evidence file to be uploaded to the evidence set.&lt;br&gt;&lt;br&gt; This file is created with the &lt;a href&#x3D;\&quot;/api-docs/sell/fulfillment/resources/payment_dispute/methods/uploadEvidenceFile\&quot; target&#x3D;\&quot;_blank \&quot;&gt;uploadEvidenceFile&lt;/a&gt; method and can be retrieved using the &lt;a href&#x3D;\&quot;/api-docs/sell/fulfillment/resources/payment_dispute/methods/getPaymentDisputes\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getPaymentDisputes&lt;/a&gt; method. | [optional] 

## Example

```python
from ebayfulfillment.models.file_evidence import FileEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of FileEvidence from a JSON string
file_evidence_instance = FileEvidence.from_json(json)
# print the JSON string representation of the object
print(FileEvidence.to_json())

# convert the object into a dict
file_evidence_dict = file_evidence_instance.to_dict()
# create an instance of FileEvidence from a dict
file_evidence_from_dict = FileEvidence.from_dict(file_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


