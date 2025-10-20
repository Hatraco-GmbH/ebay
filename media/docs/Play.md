# Play

The two streaming video URLs available for a successfully uploaded video with a status of <code>LIVE</code>. The supported streaming video protocols are DASH (Dynamic Adaptive Streaming over HTTP) and HLS (HTTP Live Streaming).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**play_url** | **str** | The playable URL for this video. | [optional] 
**protocol** | **str** | The protocol for the video playlist. Supported protocols are DASH (Dynamic Adaptive Streaming over HTTP) and HLS (HTTP Live Streaming). For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/commerce/media/types/api:ProtocolEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from ebaymedia.models.play import Play

# TODO update the JSON string below
json = "{}"
# create an instance of Play from a JSON string
play_instance = Play.from_json(json)
# print the JSON string representation of the object
print(Play.to_json())

# convert the object into a dict
play_dict = play_instance.to_dict()
# create an instance of Play from a dict
play_from_dict = Play.from_dict(play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


