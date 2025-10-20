# CreateDocumentResponse

This type provides information about the created document ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | The unique identifier of the document to be uploaded.&lt;br&gt;&lt;br&gt;This value is returned in the response and &lt;b&gt;location&lt;/b&gt; header of the &lt;b&gt;createDocument&lt;/b&gt; and &lt;b&gt;createDocumentFromUrl&lt;/b&gt; methods. This ID can be used with the &lt;b&gt;getDocument&lt;/b&gt; and &lt;b&gt;uploadDocument&lt;/b&gt; methods, and to add an uploaded document to a listing. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/inventory/managing-document-media.html#add-documents\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Adding documents to listings&lt;/a&gt; for more information.  | [optional] 
**document_status** | **str** | The status of the document resource.&lt;br&gt;&lt;br&gt;For example, the value &lt;code&gt;PENDING_UPLOAD&lt;/code&gt; is the initial state when the reference to the document has been created using the &lt;b&gt;createDocument&lt;/b&gt; method. When creating a document using the &lt;b&gt;createDocumentFromUrl&lt;/b&gt; method, the initial state will be &lt;code&gt;SUBMITTED&lt;/code&gt;. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/commerce/media/types/api:DocumentStatusEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**document_type** | **str** | The type of the document uploaded. For example, &lt;code&gt;USER_GUIDE_OR_MANUAL&lt;/code&gt;. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/commerce/media/types/api:DocumentTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**languages** | **List[str]** | This array shows the language(s) used in the document. | [optional] 

## Example

```python
from ebaymedia.models.create_document_response import CreateDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocumentResponse from a JSON string
create_document_response_instance = CreateDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateDocumentResponse.to_json())

# convert the object into a dict
create_document_response_dict = create_document_response_instance.to_dict()
# create an instance of CreateDocumentResponse from a dict
create_document_response_from_dict = CreateDocumentResponse.from_dict(create_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


