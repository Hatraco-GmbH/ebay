# ebaymedia.ImageApi

All URIs are relative to *https://apim.ebay.com/commerce/media/v1_beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image_from_file**](ImageApi.md#create_image_from_file) | **POST** /image/create_image_from_file | 
[**create_image_from_url**](ImageApi.md#create_image_from_url) | **POST** /image/create_image_from_url | 
[**get_image**](ImageApi.md#get_image) | **GET** /image/{image_id} | 


# **create_image_from_file**
> ImageResponse create_image_from_file(content_type)

This method uploads a picture file to eBay Picture Services (EPS) using multipart/form-data. <p>All images must comply with eBay's picture requirements, such as dimension and file size restrictions. For more information, see <a href="https://www.ebay.com/help/policies/listing-policies/picture-policy?id=4370"  target="_blank">Picture policy</a>. The image formats supported are <strong>JPG</strong>, <strong>GIF</strong>, <strong>PNG</strong>, <strong>BMP</strong>, <strong>TIFF</strong>, <strong>AVIF</strong>, <strong>HEIC</strong>, and <strong>WEBP</strong>. For more information, see <a href="/api-docs/sell/static/inventory/managing-image-media.html#image-requirements" target="_blank">Image requirements</a>.</p><p><span class="tablenote"><strong>Note:</strong> Animated GIF, and multi-page PNG/TIFF files, are not supported. Any animation effect of supported formats will be lost upon upload.</span></p><p>This call does not have a JSON Request payload but uploads the file as form-data. For example:<br /> <pre> image: &quot;sample_picture.jpg&quot; </pre>See <strong>Samples</strong> for information.</p><p><span class="tablenote"><strong>Note:</strong> You must use a <strong>Content-Type</strong> header with its value set to 'multipart/form-data'.</span></p><p>When an EPS image is successfully created, the method returns the HTTP Status Code <code>201 Created</code>. The method also returns the getImage URI in the <strong>Location</strong> response header.</p><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><strong><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></strong></span></span> Make sure to capture the image ID URI returned in the response <a href="/develop/guides-v2/using-ebay-restful-apis#responseheaders" target="_blank">Location header</a> provided in the following format:</p><p><code>https://apim.ebay.com/commerce/media/v1_beta/image/<em>{image_id}</em></code> </p><p>You can capture the entire URI, or just save the <code>{image_id}</code> only. Pass the <code>{image_id}</code> as a path parameter in the <strong><a href="/develop/api/sell/media_api#sell-media_api-image-getimage" >getImage</a></strong> method to return the value needed to associate an image to a listing using the Trading and Inventory APIs.</p></div><p>See <a href="/api-docs/sell/static/inventory/managing-image-media.html" target="_blank">Managing images</a> for additional details.</p><br/><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><strong><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></strong></span></span>All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds. </p></div>

### Example

* OAuth Authentication (api_auth):

```python
import ebaymedia
from ebaymedia.models.image_response import ImageResponse
from ebaymedia.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apim.ebay.com/commerce/media/v1_beta
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymedia.Configuration(
    host = "https://apim.ebay.com/commerce/media/v1_beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymedia.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymedia.ImageApi(api_client)
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <strong>multipart/form-data</strong>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.

    try:
        api_response = api_instance.create_image_from_file(content_type)
        print("The response of ImageApi->create_image_from_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->create_image_from_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;strong&gt;multipart/form-data&lt;/strong&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 

### Return type

[**ImageResponse**](ImageResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location -  <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_from_url**
> ImageResponse create_image_from_url(content_type, create_image_from_url_request)

This method uploads a picture to eBay Picture Services (EPS) from the specified URL. Specify the location of the picture on an external web server through the <strong>imageUrl</strong> field. <p>All images must comply with eBay’s picture requirements, such as dimension and file size restrictions. For more information, see <a href="https://www.ebay.com/help/policies/listing-policies/picture-policy?id=4370" target="_blank">Picture policy</a>. The image formats supported are <strong>JPG</strong>, <strong>GIF</strong>, <strong>PNG</strong>, <strong>BMP</strong>, <strong>TIFF</strong>, <strong>AVIF</strong>, <strong>HEIC</strong>, and <strong>WEBP</strong>. In addition, the provided URL must be secured using HTTPS (HTTP is not permitted). For more information, see <a href="/api-docs/sell/static/inventory/managing-image-media.html#image-requirements" target="_blank">Image requirements</a>.</p><p><span class="tablenote"><strong>Note:</strong> Animated GIF, and multi-page PNG/TIFF files, are not supported. Any animation effect of supported formats will be lost upon upload.</span></p><p>When an EPS image is successfully created, the method returns the HTTP Status Code <code>201 Created</code>. The method also returns the getImage URI in the <strong>Location</strong> response header.</p><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><strong><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></strong></span></span> Make sure to capture the image ID URI returned in the response <a href="/develop/guides-v2/using-ebay-restful-apis#responseheaders" target="_blank">Location header</a> provided in the following format:</p><p><code>https://apim.ebay.com/commerce/media/v1_beta/image/<em>{image_id}</em></code> </p><p>You can capture the entire URI, or just save the <code>{image_id}</code> only. Pass the <code>{image_id}</code> as a path parameter in the <strong><a href="/develop/api/sell/media_api#sell-media_api-image-getimage" >getImage</a></strong> method to return the value needed to associate an image to a listing using the Trading and Inventory APIs.</p></div><p>See <a href="/api-docs/sell/static/inventory/managing-image-media.html" target="_blank">Managing images</a> for additional details.</p><br/><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><strong><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></strong></span></span>All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds. </p></div>

### Example

* OAuth Authentication (api_auth):

```python
import ebaymedia
from ebaymedia.models.create_image_from_url_request import CreateImageFromUrlRequest
from ebaymedia.models.image_response import ImageResponse
from ebaymedia.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apim.ebay.com/commerce/media/v1_beta
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymedia.Configuration(
    host = "https://apim.ebay.com/commerce/media/v1_beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymedia.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymedia.ImageApi(api_client)
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <strong>application/json</strong>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    create_image_from_url_request = ebaymedia.CreateImageFromUrlRequest() # CreateImageFromUrlRequest | 

    try:
        api_response = api_instance.create_image_from_url(content_type, create_image_from_url_request)
        print("The response of ImageApi->create_image_from_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->create_image_from_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;strong&gt;application/json&lt;/strong&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **create_image_from_url_request** | [**CreateImageFromUrlRequest**](CreateImageFromUrlRequest.md)|  | 

### Return type

[**ImageResponse**](ImageResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location -  <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image**
> ImageResponse get_image(image_id)

This method retrieves an EPS image URL and its expiration details for the unique identifier specified in the path parameter <strong>image_id</strong>. Use the retrieved EPS image URL to add the image to a listing through the <strong>Inventory API</strong> or the <strong>Trading API</strong>. See <a href="/api-docs/sell/static/inventory/managing-image-media.html"  target="_blank">Managing images</a> for additional details.<br><br><span class="tablenote"><strong>Note:</strong> If a user inputs a valid <strong>image_id</strong> as a path parameter but the EPS image associated with that ID has expired, the call will fail and a <strong>404 Not Found</strong> status code will be returned.</span>

### Example

* OAuth Authentication (api_auth):

```python
import ebaymedia
from ebaymedia.models.image_response import ImageResponse
from ebaymedia.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apim.ebay.com/commerce/media/v1_beta
# See configuration.py for a list of all supported configuration parameters.
configuration = ebaymedia.Configuration(
    host = "https://apim.ebay.com/commerce/media/v1_beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ebaymedia.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ebaymedia.ImageApi(api_client)
    image_id = 'image_id_example' # str | This path parameter is the unique identifier of a created image. Use the value returned in the location header of the method used to create the image (<strong>createImageFromFile</strong> or <strong>createImageFromUrl</strong>, as applicable).

    try:
        api_response = api_instance.get_image(image_id)
        print("The response of ImageApi->get_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| This path parameter is the unique identifier of a created image. Use the value returned in the location header of the method used to create the image (&lt;strong&gt;createImageFromFile&lt;/strong&gt; or &lt;strong&gt;createImageFromUrl&lt;/strong&gt;, as applicable). | 

### Return type

[**ImageResponse**](ImageResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

