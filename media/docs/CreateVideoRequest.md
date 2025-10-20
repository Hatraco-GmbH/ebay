# CreateVideoRequest

The request to create a video, which must contain the video's <b>title</b>, <b>size</b>, and <b>classification</b>. <b>Description</b> is an optional field when creating videos.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **List[str]** | The intended use for this video content. Currently, videos can only be added and associated with eBay listings, so the only supported value is &lt;code&gt;ITEM&lt;/code&gt;. | [optional] 
**description** | **str** | The description of the video. | [optional] 
**size** | **int** | The size, in bytes, of the video content. &lt;br&gt;&lt;br&gt;&lt;b&gt;Max:&lt;/b&gt; 157,286,400 bytes | [optional] 
**title** | **str** | The title of the video. | [optional] 

## Example

```python
from ebaymedia.models.create_video_request import CreateVideoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVideoRequest from a JSON string
create_video_request_instance = CreateVideoRequest.from_json(json)
# print the JSON string representation of the object
print(CreateVideoRequest.to_json())

# convert the object into a dict
create_video_request_dict = create_video_request_instance.to_dict()
# create an instance of CreateVideoRequest from a dict
create_video_request_from_dict = CreateVideoRequest.from_dict(create_video_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


