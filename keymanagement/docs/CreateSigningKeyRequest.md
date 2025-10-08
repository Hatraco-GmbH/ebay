# CreateSigningKeyRequest

This request creates a new signing key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing_key_cipher** | **str** | The enumerated value for the cipher to be used to create the signing key. Refer to &lt;a href&#x3D; \&quot;/api-docs/developer/key-management/types/api:SigningKeyCipher\&quot; target&#x3D; \&quot;_blank\&quot;&gt;SigningKeyCiper&lt;/a&gt; for the list of supported enum values. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/developer/key_management/types/api:SigningKeyCipher&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from keymanagement.models.create_signing_key_request import CreateSigningKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSigningKeyRequest from a JSON string
create_signing_key_request_instance = CreateSigningKeyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSigningKeyRequest.to_json())

# convert the object into a dict
create_signing_key_request_dict = create_signing_key_request_instance.to_dict()
# create an instance of CreateSigningKeyRequest from a dict
create_signing_key_request_from_dict = CreateSigningKeyRequest.from_dict(create_signing_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


