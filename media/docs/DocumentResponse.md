# DocumentResponse

This type provides information returned about a created document ID, which may or may not have been uploaded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | The unique ID of the document. | [optional] 
**document_metadata** | [**DocumentMetadata**](DocumentMetadata.md) |  | [optional] 
**document_status** | **str** | The status of the document resource.&lt;br&gt;&lt;br&gt;Once a document has been uploaded using the &lt;b&gt;uploadDocument&lt;/b&gt; method, the &lt;b&gt;documentStatus&lt;/b&gt; will be &lt;code&gt;SUBMITTED&lt;/code&gt;. The document will then either be accepted or rejected. Only documents with the status of &lt;code&gt;ACCEPTED&lt;/code&gt; are available to be added to a listing. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/commerce/media/types/api:DocumentStatusEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**document_type** | **str** | The type of the document uploaded. For example, &lt;code&gt;USER_GUIDE_OR_MANUAL&lt;/code&gt;. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/commerce/media/types/api:DocumentTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**languages** | **List[str]** | This array shows the language(s) used in the document. | [optional] 

## Example

```python
from ebaymedia.models.document_response import DocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentResponse from a JSON string
document_response_instance = DocumentResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentResponse.to_json())

# convert the object into a dict
document_response_dict = document_response_instance.to_dict()
# create an instance of DocumentResponse from a dict
document_response_from_dict = DocumentResponse.from_dict(document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


