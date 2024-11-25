# DocumentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | The unique ID of the document. | [optional] 
**document_metadata** | [**DocumentMetadata**](DocumentMetadata.md) |  | [optional] 
**document_status** | **str** | The status of the document resource.&lt;br&gt;&lt;br&gt;Once a document has been uploaded using the &lt;b&gt;uploadDocument&lt;/b&gt; method, the &lt;b&gt;documentStatus&lt;/b&gt; will be &lt;code&gt;SUBMITTED&lt;/code&gt;. The document will then either be accepted or rejected. Only documents with the status of &lt;code&gt;ACCEPTED&lt;/code&gt; are available to be added to a listing. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/commerce/media/types/api:DocumentStatusEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**document_type** | **str** | The type of the document uploaded. For example, &lt;code&gt;USER_GUIDE_OR_MANUAL&lt;/code&gt;. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/commerce/media/types/api:DocumentTypeEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**languages** | **list[str]** | This array shows the language(s) used in the document. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

