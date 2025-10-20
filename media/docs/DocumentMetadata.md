# DocumentMetadata

This type provides information about the <b>documentId</b>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The name of the file including its extension (for example, &lt;code&gt;drone_user_warranty.pdf&lt;/code&gt;). | [optional] 
**file_size** | **str** | The size, in bytes, of the document content. | [optional] 
**file_type** | **str** | The type of the file uploaded. Supported file types include the following: &lt;code&gt;pdf&lt;/code&gt;, &lt;code&gt;jpeg&lt;/code&gt;, &lt;code&gt;jpg&lt;/code&gt;, and &lt;code&gt;png&lt;/code&gt;. | [optional] 

## Example

```python
from ebaymedia.models.document_metadata import DocumentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentMetadata from a JSON string
document_metadata_instance = DocumentMetadata.from_json(json)
# print the JSON string representation of the object
print(DocumentMetadata.to_json())

# convert the object into a dict
document_metadata_dict = document_metadata_instance.to_dict()
# create an instance of DocumentMetadata from a dict
document_metadata_from_dict = DocumentMetadata.from_dict(document_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


