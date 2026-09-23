# ebaymedia.PostOrderApi

All URIs are relative to *https://apim.ebay.com/commerce/media/v1_beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_post_order_document**](PostOrderApi.md#download_post_order_document) | **GET** /post_order/document/{document_id} | 
[**remove_post_order_document**](PostOrderApi.md#remove_post_order_document) | **DELETE** /post_order/document/{document_id} | 
[**upload_post_order_document**](PostOrderApi.md#upload_post_order_document) | **POST** /post_order/document | 


# **download_post_order_document**
> List[str] download_post_order_document(document_id)

This method downloads the  file associated with the specified document ID. Access depends on the document’s state:<ul><li>SUBMITTED: Only the document owner can download it </li><li>PUBLISHED: The document is no longer restricted to the owner and can be downloaded by authorized parties involved in the specific post‑order flow based on the <strong>documentUsageType</strong></li></ul><p><span class="tablenote"><span style="color:#004680"><strong>Note: </strong>This method is currently restricted and requires a special <strong>OAuth scope</strong> not available to all users.</span></p><p><span class="tablenote"><span style="color:#004680"><strong>Note: </strong>After a document is uploaded (but not yet published), its status is <strong>SUBMITTED</strong>. Once its identifier is linked to a post‑order entity through an eBay GraphQL mutation, the status changes to <strong>PUBLISHED</strong>. A post-order entity is part of eBay's order management for activities after purchase (such as returns).</span></p><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><strong><span style="color: #dd1e31;" class="mcFormatColor">Important! </span></strong></span></span>The document must be in the <strong>SUBMITTED</strong>  or <strong>PUBLISHED</strong> state to be downloadable. All documents (published or submitted) expire and become inaccessible after their expiration date.</p></div>

### Example

* OAuth Authentication (api_auth):

```python
import ebaymedia
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
    api_instance = ebaymedia.PostOrderApi(api_client)
    document_id = 'document_id_example' # str | This path parameter is the unique identifier of the document associated with the file to be downloaded. This ID was returned in the <a href=\"/develop/guides-v2/using-ebay-restful-apis#responseheaders\" target=\"_blank\">Location response header</a> when calling the <strong><a href=\"/develop/api/sell/media_api#sell-media_api-post_order-uploadpostorderdocument\">uploadPostOrderDocument</a></strong> method to upload the document.

    try:
        api_response = api_instance.download_post_order_document(document_id)
        print("The response of PostOrderApi->download_post_order_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostOrderApi->download_post_order_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| This path parameter is the unique identifier of the document associated with the file to be downloaded. This ID was returned in the &lt;a href&#x3D;\&quot;/develop/guides-v2/using-ebay-restful-apis#responseheaders\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Location response header&lt;/a&gt; when calling the &lt;strong&gt;&lt;a href&#x3D;\&quot;/develop/api/sell/media_api#sell-media_api-post_order-uploadpostorderdocument\&quot;&gt;uploadPostOrderDocument&lt;/a&gt;&lt;/strong&gt; method to upload the document. | 

### Return type

**List[str]**

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_post_order_document**
> remove_post_order_document(document_id)

This method deletes a previously uploaded document by its document ID. Only documents in <strong>SUBMITTED</strong> state can be removed; documents in the <strong>PUBLISHED</strong> state cannot be deleted.<p><span class="tablenote"><span style="color:#004680"><strong>Note: </strong>This method is currently restricted and requires a special <strong>OAuth scope</strong> not available to all users.</span></p><p><span class="tablenote"><span style="color:#004680"><strong>Note: </strong>After a document is uploaded (but not yet published), its status is <strong>SUBMITTED</strong>. When its identifier is associated with a post‑order entity through an eBay GraphQL mutation, the status changes to <strong>PUBLISHED</strong>. A post-order entity is part of eBay's order management for activities after purchase (such as returns).</span></p><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><strong><span style="color: #dd1e31;" class="mcFormatColor">Important! </span></strong></span></span>All documents, whether submitted or published, expire and become inaccessible after their expiration date.</p></div> 

### Example

* OAuth Authentication (api_auth):

```python
import ebaymedia
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
    api_instance = ebaymedia.PostOrderApi(api_client)
    document_id = 'document_id_example' # str | This path parameter is the unique identifier of the document associated with the file to be deleted. This ID was returned in the <a href=\"/develop/guides-v2/using-ebay-restful-apis#responseheaders\">Location response header</a> when calling the <strong><a href=\"/develop/api/sell/media_api#sell-media_api-post_order-uploadpostorderdocument\">uploadPostOrderDocument</a></strong> method to upload the document.

    try:
        api_instance.remove_post_order_document(document_id)
    except Exception as e:
        print("Exception when calling PostOrderApi->remove_post_order_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| This path parameter is the unique identifier of the document associated with the file to be deleted. This ID was returned in the &lt;a href&#x3D;\&quot;/develop/guides-v2/using-ebay-restful-apis#responseheaders\&quot;&gt;Location response header&lt;/a&gt; when calling the &lt;strong&gt;&lt;a href&#x3D;\&quot;/develop/api/sell/media_api#sell-media_api-post_order-uploadpostorderdocument\&quot;&gt;uploadPostOrderDocument&lt;/a&gt;&lt;/strong&gt; method to upload the document. | 

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_post_order_document**
> object upload_post_order_document(content_type)

This method uploads a document for post‑order processes (for example, a seller providing a return shipping label).<p> Supported file types include .PDF, .JPEG/.JPG, .BMP, .GIF and .PNG, with a maximum file size of 5&nbsp;MB&nbsp;(5,242,880&nbsp;bytes).<p><span class="tablenote"><span style="color:#004680"><strong>Note: </strong>This method is currently restricted and requires a special <strong>OAuth scope</strong> not available to all users.</span></p><p><span class="tablenote"><span style="color:#004680"><strong>Note: </strong>Animated and multi-page PNG files are not currently supported. For multi-page content, use PDF. The maximum number of pages allowed varies by the <strong>documentUsageType</strong>.</span></p><p>Send a multipart/form‑data request with:</p><ul><li><strong>file</strong>: the document file, set <code>key: file</code></li><li><strong>documentUsageType</strong>: for example, <code>RETURN_SHIPPING_LABEL</code></li><li><strong>entityType</strong>: for example, <code>RETURNS</code></li><li><strong>entityId</strong>: the unique identifier for the post-order entity</li></ul><p>A successful call returns the HTTP Status Code <strong>201 Created</strong> with the document ID in the <strong>Location header</strong> (no response body is returned). The document’s initial state is <strong>SUBMITTED</strong>. When its identifier is associated with a post-order entity through an eBay GraphQL mutation, the state changes to <strong>PUBLISHED</strong>. </p><p><span class="tablenote"><span style="color:#004680"><strong>Note: </strong>A post-order entity is part of eBay's order management for activities after purchase (such as returns).</span></p><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><strong><span style="color: #dd1e31;" class="mcFormatColor">Important! </span></strong></span></span><br><ul><li>Capture and retain the <strong>documentId</strong> in the response's <a href="/develop/guides-v2/using-ebay-restful-apis#responseheaders" target="_blank">Location header</a>. It is required to use the other <strong>post_order</strong> methods and to associate the document with a post-order entity. The location response header contains the URI of the newly created document ID in the format:<br><code> https://apiz.ebay.com/commerce/media/v1_beta/post_order/document/{documentId}</code></li><li>All documents (published or submitted) expire and become inaccessible after their expiration date.</li><li>All <strong>POST</strong> methods in the <strong>Media API</strong>, including this method, are subject to short-duration, user-level rate limits: 50 requests per 5 seconds.</li></ul></p></div>

### Example

* OAuth Authentication (api_auth):

```python
import ebaymedia
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
    api_instance = ebaymedia.PostOrderApi(api_client)
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <strong>multipart/form-data</strong>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.

    try:
        api_response = api_instance.upload_post_order_document(content_type)
        print("The response of PostOrderApi->upload_post_order_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostOrderApi->upload_post_order_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;strong&gt;multipart/form-data&lt;/strong&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 

### Return type

**object**

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

