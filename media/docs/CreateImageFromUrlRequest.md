# CreateImageFromUrlRequest

A type that provides the location of the image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | The image URL of the self-hosted picture to upload to eBay Picture Services (EPS). In addition to the picture requirements in &lt;a href&#x3D;\&quot;https://www.ebay.com/help/policies/listing-policies/picture-policy?id&#x3D;4370\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Picture policy&lt;/a&gt;, the provided URL must be secured using HTTPS (HTTP is not permitted). For more information, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/inventory/managing-image-media.html#image-requirements\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Image requirements&lt;/a&gt;. | [optional] 

## Example

```python
from ebaymedia.models.create_image_from_url_request import CreateImageFromUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImageFromUrlRequest from a JSON string
create_image_from_url_request_instance = CreateImageFromUrlRequest.from_json(json)
# print the JSON string representation of the object
print(CreateImageFromUrlRequest.to_json())

# convert the object into a dict
create_image_from_url_request_dict = create_image_from_url_request_instance.to_dict()
# create an instance of CreateImageFromUrlRequest from a dict
create_image_from_url_request_from_dict = CreateImageFromUrlRequest.from_dict(create_image_from_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


