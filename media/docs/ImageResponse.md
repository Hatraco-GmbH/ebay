# ImageResponse

A type that provides an image's details including its URL and expiration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_date** | **str** | The date and time when an unused EPS image will expire and be removed from the EPS server, in Coordinated Universal Time (UTC). As long as an EPS image is being used in an active listing, that image will remain on the EPS server and be accessible. | [optional] 
**image_url** | **str** | The EPS URL to access the uploaded image. This URL will be used in listing calls to add the image to a listing. | [optional] 

## Example

```python
from ebaymedia.models.image_response import ImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageResponse from a JSON string
image_response_instance = ImageResponse.from_json(json)
# print the JSON string representation of the object
print(ImageResponse.to_json())

# convert the object into a dict
image_response_dict = image_response_instance.to_dict()
# create an instance of ImageResponse from a dict
image_response_from_dict = ImageResponse.from_dict(image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


