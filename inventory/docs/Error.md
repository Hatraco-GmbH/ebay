# Error

This type is used to express detailed information on errors and warnings that may occur with a call request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | This string value indicates the error category. There are three categories of errors: request errors, application errors, and system errors.  | [optional] 
**domain** | **str** | The name of the domain in which the error or warning occurred. | [optional] 
**error_id** | **int** | A unique code that identifies the particular error or warning that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms. | [optional] 
**input_ref_ids** | **List[str]** | An array of one or more reference IDs which identify the specific request element(s) most closely associated to the error or warning, if any. | [optional] 
**long_message** | **str** | A detailed description of the condition that caused the error or warning, and information on what to do to correct the problem. | [optional] 
**message** | **str** | A description of the condition that caused the error or warning. | [optional] 
**output_ref_ids** | **List[str]** | An array of one or more reference IDs which identify the specific response element(s) most closely associated to the error or warning, if any. | [optional] 
**parameters** | [**List[ErrorParameter]**](ErrorParameter.md) | Various warning and error messages return one or more variables that contain contextual information about the error or waring. This is often the field or value that triggered the error or warning. | [optional] 
**subdomain** | **str** | The name of the subdomain in which the error or warning occurred. | [optional] 

## Example

```python
from ebayinventory.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


