# Video

A response field that retrieves all the metadata for the video, including its <strong>title</strong>, <strong>classification</strong>, <strong>size</strong>, <strong>description</strong>, <strong>status</strong>, <strong>status message</strong> (if any), and <strong>expiration date</strong>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | [**List[Classification]**](Classification.md) | The intended use for this video content. Currently, videos can only be added and associated with eBay listings, so the only supported value is &lt;code&gt;ITEM&lt;/code&gt;. This array is always returned. | [optional] 
**description** | **str** | The description of the video. The video description is an optional field that can be set using the &lt;a href&#x3D;\&quot; /develop/api/sell/media_api#sell-media_api-video-createvideo\&quot;&gt;createVideo&lt;/a&gt; method. | [optional] 
**expiration_date** | **str** | The date and time when an unused video will expire and be removed from the eBay Video Services server, in Coordinated Universal Time (UTC).&lt;br&gt;&lt;br&gt;As long as a video is being used in an active listing, that video will remain on the server and be accessible. If a video is not being used on an active listing, its expiration date is automatically set to 30 days after the video&#39;s initial upload. | [optional] 
**moderation** | [**Moderation**](Moderation.md) | The video moderation information that is returned if a video is blocked by moderators.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#478415\&quot;&gt;&lt;strong&gt;Tip:&lt;/strong&gt;&lt;/span&gt; See &lt;a href&#x3D;\&quot;https://www.ebay.com/help/selling/listings/creating-managing-listings/add-video-to-listing?id&#x3D;5272#section2\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Video moderation and restrictions&lt;/a&gt; in the eBay Seller Center for details about video moderation.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;If the video status is &lt;code&gt;BLOCKED&lt;/code&gt;, ensure that the video complies with eBay&#39;s video formatting and content guidelines. Afterwards, begin the video creation and upload procedure anew using the &lt;strong&gt;createVideo&lt;/strong&gt; and &lt;strong&gt;uploadVideo&lt;/strong&gt; methods. | [optional] 
**play_lists** | [**List[Play]**](Play.md) | The playlist created for the uploaded video, which provides the streaming video URLs to play the video. The supported streaming video protocols are DASH (Dynamic Adaptive Streaming over HTTP) and HLS (HTTP Live Streaming). The playlist will only be generated if a video is successfully uploaded with a status of &lt;code&gt;LIVE&lt;/code&gt;. | [optional] 
**size** | **int** | The size, in bytes, of the video content. This field is always returned. | [optional] 
**status** | [**VideoStatusEnum**](VideoStatusEnum.md) | The status of the current video resource. | [optional] 
**status_message** | **str** | The &lt;strong&gt;statusMessage&lt;/strong&gt; field contains additional information on the status. For example, information on why processing might have failed or if the video was blocked. | [optional] 
**thumbnail** | [**Image**](Image.md) | The URL of the thumbnail image of the video. The thumbnail image&#39;s URL must be an eBayPictureURL (EPS URL). | [optional] 
**title** | **str** | The title of the video. This field is always returned. | [optional] 
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


