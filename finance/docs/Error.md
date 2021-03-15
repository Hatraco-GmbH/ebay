# Error

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Identifies the type of erro. | [optional] 
**domain** | **str** | Name for the primary system where the error occurred. This is relevant for application errors. | [optional] 
**error_id** | **int** | A unique number to identify the error. | [optional] 
**input_ref_ids** | **list[str]** | An array of request elements most closely associated to the error. | [optional] 
**long_message** | **str** | A more detailed explanation of the error. | [optional] 
**message** | **str** | Information on how to correct the problem, in the end user&#x27;s terms and language where applicable. | [optional] 
**output_ref_ids** | **list[str]** | An array of request elements most closely associated to the error. | [optional] 
**parameters** | [**list[ErrorParameter]**](ErrorParameter.md) | An array of name/value pairs that describe details the error condition. These are useful when multiple errors are returned. | [optional] 
**subdomain** | **str** | Further helps indicate which subsystem the error is coming from. System subcategories include: Initialization, Serialization, Security, Monitoring, Rate Limiting, etc. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

