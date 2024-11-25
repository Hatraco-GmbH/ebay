# ebaymedia.VideoApi

All URIs are relative to *https://apim.ebay.com{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_video**](VideoApi.md#create_video) | **POST** /video | 
[**get_video**](VideoApi.md#get_video) | **GET** /video/{video_id} | 
[**upload_video**](VideoApi.md#upload_video) | **POST** /video/{video_id}/upload | 

# **create_video**
> create_video(content_type, body=body)



This method creates a video. When using this method, specify the <b>title</b>, <b>size</b>, and <b>classification</b> of the video to be created. <b>Description</b> is an optional field for this method.<br /><br /><span class=\"tablenote\"><span style=\"color:#478415\"><strong>Tip:</strong></span> See <a href=\"https://www.ebay.com/help/selling/listings/creating-managing-listings/add-video-to-listing?id=5272#section3\" target=\"_blank\">Adding a video to your listing</a> in the eBay Seller Center for details about video formatting requirements and restrictions, or visit the relevant eBay site help pages for the region in which the listings will be posted.</span><br /><br />When a video is successfully created, the method returns the HTTP Status Code <code>201 Created.</code>The method also returns the location response header containing the <b>video ID</b>, which you can use to retrieve the video.<br /><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> There is no ability to edit metadata on videos at this time. There is also no method to delete videos.</span><br /><br />To upload a created video, use the <a href=\" /api-docs/commerce/media/resources/video/methods/uploadVideo\" target=\"_blank\">uploadVideo</a> method.

### Example
```python
from __future__ import print_function
import time
import ebaymedia
from ebaymedia.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaymedia.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaymedia.VideoApi(ebaymedia.ApiClient(configuration))
content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
body = ebaymedia.CreateVideoRequest() # CreateVideoRequest |  (optional)

try:
    api_instance.create_video(content_type, body=body)
except ApiException as e:
    print("Exception when calling VideoApi->create_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **body** | [**CreateVideoRequest**](CreateVideoRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video**
> Video get_video(video_id)



This method retrieves a video's metadata and content given a specified <b>video ID</b>. The method returns the <b>title</b>, <b>size</b>, <b>classification</b>, <b>description</b>, <b>video ID</b>, <b>playList</b>, <b>status</b>, <b>status message</b> (if any), <b>expiration  date</b>, and <b>thumbnail</b> image of the retrieved video. <p>The video’s <b>title</b>, <b>size</b>, <b>classification</b>, and <b>description</b> are set using the <a href=\" /api-docs/commerce/media/resources/video/methods/createVideo\" target=\"_blank\">createVideo</a> method.</p> <p>The video's <b>playList</b> contains two URLs that link to instances of the streaming video based on the supported protocol.</p><p>The <b>status</b> field contains the current status of the video. After a video upload is successfully completed, the video's <b>status</b> will show as <code>PROCESSING</code> until the video reaches one of the terminal states of <code>LIVE</code>, <code>BLOCKED</code> or <code>PROCESSING_FAILED</code>.<p> If a video's processing fails, it could be because the file is corrupted, is too large, or its size doesn’t match what was provided in the metadata. Refer to the error messages to determine the cause of the video’s failure to upload.</p> <p> The <b>status message</b> will indicate why a video was blocked from uploading.</p><p>The video’s <b>expiration date</b> is automatically set to 30 days after the video’s initial creation.<p>The video's <b>thumbnail</b> image is automatically generated when the video is created.

### Example
```python
from __future__ import print_function
import time
import ebaymedia
from ebaymedia.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaymedia.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaymedia.VideoApi(ebaymedia.ApiClient(configuration))
video_id = 'video_id_example' # str | The unique identifier of the video to be retrieved.

try:
    api_response = api_instance.get_video(video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->get_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier of the video to be retrieved. | 

### Return type

[**Video**](Video.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_video**
> upload_video(content_type, video_id, body=body, content_length=content_length, content_range=content_range)



This method associates the specified file with the specified <b>video ID</b> and uploads the input file. After the file has been uploaded the processing of the file begins.<br /><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> The size of the video to be uploaded must exactly match the size of the video's input stream that was set in the <a href=\" /api-docs/commerce/media/resources/video/methods/createVideo\" target=\"_blank\">createVideo</a> method. If the sizes do not match, the video will not upload successfully.</span><br /><br />When a video is successfully uploaded, it returns the HTTP Status Code <code>200 OK</code>.<br /><br />The status flow is <code>PENDING_UPLOAD</code> > <code>PROCESSING</code> > <code>LIVE</code>,  <code>PROCESSING_FAILED</code>, or <code>BLOCKED</code>. After a video upload is successfully completed, the status will show as <code>PROCESSING</code> until the video reaches one of the terminal states of <code>LIVE</code>, <code>BLOCKED</code>, or <code>PROCESSING_FAILED</code>. If the size information (in bytes) provided is incorrect, the API will throw an error.<br /><br /><span class=\"tablenote\"><span style=\"color:#478415\"><strong>Tip:</strong></span> See <a href=\"https://www.ebay.com/help/selling/listings/creating-managing-listings/add-video-to-listing?id=5272#section3\" target=\"_blank\">Adding a video to your listing</a> in the eBay Seller Center for details about video formatting requirements and restrictions, or visit the relevant eBay site help pages for the region in which the listings will be posted.</span><br /><br />To retrieve an uploaded video, use the <a href=\"/api-docs/commerce/media/resources/video/methods/getVideo\" target=\"_blank\">getVideo</a> method.

### Example
```python
from __future__ import print_function
import time
import ebaymedia
from ebaymedia.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebaymedia.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebaymedia.VideoApi(ebaymedia.ApiClient(configuration))
content_type = 'content_type_example' # str | Use this header to specify the content type for the upload. The Content-Type should be set to <code>application/octet-stream</code>.
video_id = 'video_id_example' # str | The unique identifier of the video to be uploaded.
body = ebaymedia.InputStream() # InputStream | The request payload for this method is the input stream for the video source. The input source must be an .mp4 file of the type MPEG-4 Part 10 or Advanced Video Coding (MPEG-4 AVC). (optional)
content_length = 'content_length_example' # str | Use this header to specify the content length for the upload. Use Content-Range: bytes {1}-{2}/{3} and Content-Length:{4} headers.<br /><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> This header is optional and is only required for <i>resumable</i> uploads (when an upload is interrupted and must be resumed from a certain point).</span> (optional)
content_range = 'content_range_example' # str | Use this header to specify the content range for the upload. The Content-Range should be of the following bytes ((?:[0-9]+-[0-9]+)|\\\\\\\\*)/([0-9]+|\\\\\\\\*) pattern.<br /><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> This header is optional and is only required for <i>resumable</i> uploads (when an upload is interrupted and must be resumed from a certain point).</span> (optional)

try:
    api_instance.upload_video(content_type, video_id, body=body, content_length=content_length, content_range=content_range)
except ApiException as e:
    print("Exception when calling VideoApi->upload_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Use this header to specify the content type for the upload. The Content-Type should be set to &lt;code&gt;application/octet-stream&lt;/code&gt;. | 
 **video_id** | **str**| The unique identifier of the video to be uploaded. | 
 **body** | [**InputStream**](InputStream.md)| The request payload for this method is the input stream for the video source. The input source must be an .mp4 file of the type MPEG-4 Part 10 or Advanced Video Coding (MPEG-4 AVC). | [optional] 
 **content_length** | **str**| Use this header to specify the content length for the upload. Use Content-Range: bytes {1}-{2}/{3} and Content-Length:{4} headers.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#004680\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt;&lt;/span&gt; This header is optional and is only required for &lt;i&gt;resumable&lt;/i&gt; uploads (when an upload is interrupted and must be resumed from a certain point).&lt;/span&gt; | [optional] 
 **content_range** | **str**| Use this header to specify the content range for the upload. The Content-Range should be of the following bytes ((?:[0-9]+-[0-9]+)|\\\\\\\\*)/([0-9]+|\\\\\\\\*) pattern.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#004680\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt;&lt;/span&gt; This header is optional and is only required for &lt;i&gt;resumable&lt;/i&gt; uploads (when an upload is interrupted and must be resumed from a certain point).&lt;/span&gt; | [optional] 

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

