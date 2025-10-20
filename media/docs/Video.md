# Video

A response field that retrieves all the metadata for the video, including its <b>title</b>, <b>classification</b>, <b>size</b>, <b>description</b>, <b>status</b>, <b>status message</b> (if any), and <b>expiration date</b>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **List[str]** | The intended use for this video content. Currently, videos can only be added and associated with eBay listings, so the only supported value is &lt;code&gt;ITEM&lt;/code&gt;. | [optional] 
**description** | **str** | The description of the video. The video description is an optional field that can be set using the &lt;a href&#x3D;\&quot; /api-docs/commerce/media/resources/video/methods/createVideo\&quot; target&#x3D;\&quot;_blank\&quot;&gt;createVideo&lt;/a&gt; method. | [optional] 
**expiration_date** | **str** | The date and time when an unused video will expire and be removed from the eBay Video Services server, in Coordinated Universal Time (UTC).&lt;br&gt;&lt;br&gt;As long as a video is being used in an active listing, that video will remain on the server and be accessible. If a video is not being used on an active listing, its expiration date is automatically set to 30 days after the video&#39;s initial upload. | [optional] 
**moderation** | [**Moderation**](Moderation.md) |  | [optional] 
**play_lists** | [**List[Play]**](Play.md) | The playlist created for the uploaded video, which provides the streaming video URLs to play the video. The supported streaming video protocols are DASH (Dynamic Adaptive Streaming over HTTP) and HLS (HTTP Live Streaming). The playlist will only be generated if a video is successfully uploaded with a status of &lt;code&gt;LIVE&lt;/code&gt;. | [optional] 
**size** | **int** | The size, in bytes, of the video content. | [optional] 
**status** | **str** | The status of the current video resource. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/commerce/media/types/api:VideoStatusEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**status_message** | **str** | The &lt;b&gt;statusMessage&lt;/b&gt; field contains additional information on the status. For example, information on why processing might have failed or if the video was blocked. | [optional] 
**thumbnail** | [**Image**](Image.md) |  | [optional] 
**title** | **str** | The title of the video. | [optional] 
**video_id** | **str** | The unique ID of the video. | [optional] 

## Example

```python
from ebaymedia.models.video import Video

# TODO update the JSON string below
json = "{}"
# create an instance of Video from a JSON string
video_instance = Video.from_json(json)
# print the JSON string representation of the object
print(Video.to_json())

# convert the object into a dict
video_dict = video_instance.to_dict()
# create an instance of Video from a dict
video_from_dict = Video.from_dict(video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


