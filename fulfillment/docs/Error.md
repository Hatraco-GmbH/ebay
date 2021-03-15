# Error

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The context or source of this error or warning. | [optional] 
**domain** | **str** | The name of the domain containing the service or application. For example, sell is a domain. | [optional] 
**error_id** | **int** | A positive integer that uniquely identifies the specific error condition that occurred. Your application can use these values as error code identifiers in your customized error-handling algorithms. | [optional] 
**input_ref_ids** | **list[str]** | A list of one or more specific request elements (if any) associated with the error or warning. The format of these strings depends on the request payload format. For JSON, use JSONPath notation. | [optional] 
**long_message** | **str** | An expanded version of the message field. Maximum length: 200 characters | [optional] 
**message** | **str** | A message about the error or warning which is device agnostic and readable by end users and application developers. It explains what the error or warning is, and how to fix it (in a general sense). If applicable, the value is localized to the end user&#x27;s requested locale. Maximum length: 50 characters | [optional] 
**output_ref_ids** | **list[str]** | A list of one or more specific response elements (if any) associated with the error or warning. The format of these strings depends on the request payload format. For JSON, use JSONPath notation. | [optional] 
**parameters** | [**list[ErrorParameter]**](ErrorParameter.md) | Contains a list of name/value pairs that provide additional information concerning this error or warning. Each item in the list is an input parameter that contributed to the error or warning condition. | [optional] 
**subdomain** | **str** | The name of the domain&#x27;s subsystem or subdivision. For example, fulfillment is a subdomain in the sell domain. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

