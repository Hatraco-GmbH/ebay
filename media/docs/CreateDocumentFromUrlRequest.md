# CreateDocumentFromUrlRequest

This type contains the metadata used to create the document ID when creating a document using a URL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** | The type of the document being created. For example, a &lt;code&gt;USER_GUIDE_OR_MANUAL&lt;/code&gt; or a &lt;code&gt;SAFETY_DATA_SHEET&lt;/code&gt;. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/commerce/media/types/api:DocumentTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**document_url** | **str** | The URL of the document being created.&lt;br&gt;&lt;br&gt;The document referenced by the URL must be a .pdf, .png, .jpg, or .jpeg file, and must be no larger than 10 MB. | [optional] 
**languages** | **List[str]** | This array shows the language(s) used in the document. | [optional] 

## Example

```python
from ebaymedia.models.create_document_from_url_request import CreateDocumentFromUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocumentFromUrlRequest from a JSON string
create_document_from_url_request_instance = CreateDocumentFromUrlRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDocumentFromUrlRequest.to_json())

# convert the object into a dict
create_document_from_url_request_dict = create_document_from_url_request_instance.to_dict()
# create an instance of CreateDocumentFromUrlRequest from a dict
create_document_from_url_request_from_dict = CreateDocumentFromUrlRequest.from_dict(create_document_from_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


