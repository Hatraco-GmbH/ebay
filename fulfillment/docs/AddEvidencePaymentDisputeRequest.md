# AddEvidencePaymentDisputeRequest

This type is used by the request payload of the <strong>addEvidence</strong> method. The <strong>addEvidence</strong> method is used to create a new evidence set against a payment dispute with one or more evidence files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_type** | **str** | This field is used to indicate the type of evidence being provided through one or more evidence files. All evidence files (if more than one) should be associated with the evidence type passed in this field.&lt;br&gt;&lt;br&gt;See the &lt;a href&#x3D;\&quot;/api-docs/sell/fulfillment/types/api:EvidenceTypeEnum\&quot; target&#x3D;\&quot;_blank \&quot;&gt;EvidenceTypeEnum&lt;/a&gt; type for the supported evidence types. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/fulfillment/types/api:EvidenceTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**files** | [**List[FileEvidence]**](FileEvidence.md) | This array is used to specify one or more evidence files that will become part of a new evidence set associated with a payment dispute. At least one evidence file must be specified in the &lt;strong&gt;files&lt;/strong&gt; array. | [optional] 
**line_items** | [**List[OrderLineItems]**](OrderLineItems.md) | This array identifies the order line item(s) for which the evidence file(s) will be applicable.&lt;br&gt;&lt;Br&gt;These values are returned under the &lt;strong&gt;evidenceRequests.lineItems&lt;/strong&gt; array in the &lt;a href&#x3D;\&quot;/api-docs/sell/fulfillment/resources/payment_dispute/methods/getPaymentDispute\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getPaymentDispute&lt;/a&gt; response. | [optional] 

## Example

```python
from ebayfulfillment.models.add_evidence_payment_dispute_request import AddEvidencePaymentDisputeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddEvidencePaymentDisputeRequest from a JSON string
add_evidence_payment_dispute_request_instance = AddEvidencePaymentDisputeRequest.from_json(json)
# print the JSON string representation of the object
print(AddEvidencePaymentDisputeRequest.to_json())

# convert the object into a dict
add_evidence_payment_dispute_request_dict = add_evidence_payment_dispute_request_instance.to_dict()
# create an instance of AddEvidencePaymentDisputeRequest from a dict
add_evidence_payment_dispute_request_from_dict = AddEvidencePaymentDisputeRequest.from_dict(add_evidence_payment_dispute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


