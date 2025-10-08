# Document

This type provides an array of one or more regulatory documents associated with a listing for Regulatory Compliance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | The unique identifier of a regulatory document associated with the listing.&lt;br&gt;&lt;br&gt;This value can be found in the response of the &lt;a href&#x3D;\&quot;/api-docs/commerce/media/resources/document/methods/createDocument\&quot; target&#x3D;\&quot;_blank\&quot;&gt;createDocument&lt;/a&gt; method of the Media API. | [optional] 

## Example

```python
from ebayinventory.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


