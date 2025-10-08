# QuerySigningKeysResponse

This container stores metadata information for all keypairs that are owned by a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing_keys** | [**List[SigningKey]**](SigningKey.md) | An array of metadata information for keypairs owned by a user. | [optional] 

## Example

```python
from keymanagement.models.query_signing_keys_response import QuerySigningKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySigningKeysResponse from a JSON string
query_signing_keys_response_instance = QuerySigningKeysResponse.from_json(json)
# print the JSON string representation of the object
print(QuerySigningKeysResponse.to_json())

# convert the object into a dict
query_signing_keys_response_dict = query_signing_keys_response_instance.to_dict()
# create an instance of QuerySigningKeysResponse from a dict
query_signing_keys_response_from_dict = QuerySigningKeysResponse.from_dict(query_signing_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


