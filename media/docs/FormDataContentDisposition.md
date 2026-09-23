# FormDataContentDisposition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_date** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**modification_date** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**parameters** | **Dict[str, str]** |  | [optional] 
**read_date** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from ebaymedia.models.form_data_content_disposition import FormDataContentDisposition

# TODO update the JSON string below
json = "{}"
# create an instance of FormDataContentDisposition from a JSON string
form_data_content_disposition_instance = FormDataContentDisposition.from_json(json)
# print the JSON string representation of the object
print(FormDataContentDisposition.to_json())

# convert the object into a dict
form_data_content_disposition_dict = form_data_content_disposition_instance.to_dict()
# create an instance of FormDataContentDisposition from a dict
form_data_content_disposition_from_dict = FormDataContentDisposition.from_dict(form_data_content_disposition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


