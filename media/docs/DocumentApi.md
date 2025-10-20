# ebaymedia.DocumentApi

All URIs are relative to *https://apim.ebay.com/commerce/media/v1_beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document**](DocumentApi.md#create_document) | **POST** /document | 
[**create_document_from_url**](DocumentApi.md#create_document_from_url) | **POST** /document/create_document_from_url | 
[**get_document**](DocumentApi.md#get_document) | **GET** /document/{document_id} | 
[**upload_document**](DocumentApi.md#upload_document) | **POST** /document/{document_id}/upload | 


# **create_document**
> CreateDocumentResponse create_document(content_type, create_document_request=create_document_request)

This method stages a document to be uploaded, and requires the type of document to be uploaded, and the language(s) that the document contains. A successful call returns a <b>documentId</b> value that is then used as a path parameter in an <a href=" /api-docs/commerce/media/resources/document/methods/uploadDocument" >uploadDocument</a> call.<p>When a document is successfully created, the method returns the HTTP Status Code <code>201 Created.</code> The method returns <b>documentId</b> in the response payload, which you can use to retrieve the document resource. This ID is also returned in the <b>location</b> header, for convenience.</p><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> Make sure to capture the document ID value returned in the response payload. This value is required to use the other methods in the <b>document</b> resource, and also needed to associate a document to a listing using the Trading and Inventory APIs.</p></div><br><p>To upload a created document, use the document ID returned from this method's response with the <a href=" /api-docs/commerce/media/resources/document/methods/uploadDocument" >uploadDocument</a> method. See <a href="/api-docs/sell/static/inventory/managing-document-media.html" target="_blank">Managing documents</a> for information on creating, uploading, and adding documents to listings.</p><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds.</p></div> 

### Example

* OAuth Authentication (api_auth):

```python
import ebaymedia
from ebaymedia.models.create_document_request import CreateDocumentRequest
from ebaymedia.models.create_document_response import CreateDocumentResponse
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
    api_instance = ebaymedia.DocumentApi(api_client)
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    create_document_request = ebaymedia.CreateDocumentRequest() # CreateDocumentRequest |  (optional)

    try:
        api_response = api_instance.create_document(content_type, create_document_request=create_document_request)
        print("The response of DocumentApi->create_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->create_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **create_document_request** | [**CreateDocumentRequest**](CreateDocumentRequest.md)|  | [optional] 

### Return type

[**CreateDocumentResponse**](CreateDocumentResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document_from_url**
> CreateDocumentResponse create_document_from_url(content_type, create_document_from_url_request=create_document_from_url_request)

This method downloads a document from the provided URL and adds that document to the user's account. This method requires the URL of the document, the type of document to be uploaded, and the language(s) that the document contains. <br><br>When a document is successfully created, the method returns the HTTP Status Code <code>201 Created.</code> The method returns <b>documentId</b> in the response payload, which you can use to retrieve the document resource. This ID is also returned in the <b>location</b> header, for convenience.</p><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> Make sure to capture the document ID value returned in the response payload. This value is required to use the other methods in the <b>document</b> resource, and also needed to associate a document to a listing using the Trading and Inventory APIs.</p></div><br>After creating a document using this method, a <a href="/api-docs/commerce/media/resources/document/methods/getDocument" target="_blank">getDocument</a> call should be made to check for a <b>documentStatus</b> of <code>ACCEPTED</code>. Only documents with this status can be added to a listing. See <a href="/api-docs/sell/static/inventory/managing-document-media.html" target="_blank">Managing documents</a> for more information on creating, uploading, and adding documents to listings.<br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds.</p></div>

### Example

* OAuth Authentication (api_auth):

```python
import ebaymedia
from ebaymedia.models.create_document_from_url_request import CreateDocumentFromUrlRequest
from ebaymedia.models.create_document_response import CreateDocumentResponse
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
    api_instance = ebaymedia.DocumentApi(api_client)
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.
    create_document_from_url_request = ebaymedia.CreateDocumentFromUrlRequest() # CreateDocumentFromUrlRequest |  (optional)

    try:
        api_response = api_instance.create_document_from_url(content_type, create_document_from_url_request=create_document_from_url_request)
        print("The response of DocumentApi->create_document_from_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->create_document_from_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;application/json&lt;/b&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 
 **create_document_from_url_request** | [**CreateDocumentFromUrlRequest**](CreateDocumentFromUrlRequest.md)|  | [optional] 

### Return type

[**CreateDocumentResponse**](CreateDocumentResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> DocumentResponse get_document(document_id)

This method retrieves the current <b>status</b> and metadata of the specified document.<br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> The document ID value returned in the response payload of the <a href="/api-docs/commerce/media/resources/document/methods/createDocument">createDocument</a> method is a required input path parameter for this method.</p></div><p>See <a href="/api-docs/sell/static/inventory/managing-document-media.html" target="_blank">Managing documents</a> for additional information.</p>

### Example

* OAuth Authentication (api_auth):

```python
import ebaymedia
from ebaymedia.models.document_response import DocumentResponse
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
    api_instance = ebaymedia.DocumentApi(api_client)
    document_id = 'document_id_example' # str | The unique identifier of the document for which status and metadata is being retrieved.<br><br>This value is returned in the response of the <a href=\"/api-docs/commerce/media/resources/document/methods/createDocument\" target=\"_blank\">createDocument</a> method.

    try:
        api_response = api_instance.get_document(document_id)
        print("The response of DocumentApi->get_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->get_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The unique identifier of the document for which status and metadata is being retrieved.&lt;br&gt;&lt;br&gt;This value is returned in the response of the &lt;a href&#x3D;\&quot;/api-docs/commerce/media/resources/document/methods/createDocument\&quot; target&#x3D;\&quot;_blank\&quot;&gt;createDocument&lt;/a&gt; method. | 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Uploaded |  -  |
**400** | Bad Request |  -  |
**404** | Document Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document**
> DocumentResponse upload_document(document_id, content_type)

This method associates the specified file with the specified document ID and uploads the input file. After the file has been uploaded, the processing of the file begins. Supported file types include .PDF, .JPEG/.JPG, and .PNG, with a maximum file size of 10 MB (10485760 bytes).<br><br><span class="tablenote"><b>Note:</b> Animated and multi-page PNG files are not currently supported.</span><br><span class="tablenote"><span style="color:#004680"><strong>Note:</strong></span> The document ID value returned in the response of the <a href="/api-docs/commerce/media/resources/document/methods/createDocument">createDocument</a> method is a required input path parameter for this method. This value is also returned in the <b>location</b> header of the <b>createDocument</b> response payload.</span><br>A successful upload returns the HTTP Status Code <code>200 OK</code>.<br><p>See <a href="/api-docs/sell/static/inventory/managing-document-media.html" target="_blank">Managing documents</a> for additional information.</p> <span class="tablenote"><b>Note:</b> You must use a <strong>Content-Type</strong> header with its value set to <b>multipart/form-data</b>.</p></span></p>This call does not have a JSON Request payload but uploads the file as form-data. For example:<br /> <pre>file: @&quot;/C:/Users/.../drone_user_warranty.pdf&quot;</pre>See <a href="/api-docs/commerce/media/resources/document/methods/uploadDocument#h2-samples">Samples</a> for information.<br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds.</p></div>

### Example

* OAuth Authentication (api_auth):

```python
import ebaymedia
from ebaymedia.models.document_response import DocumentResponse
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
    api_instance = ebaymedia.DocumentApi(api_client)
    document_id = 'document_id_example' # str | The unique identifier of the document to be uploaded.<br><br>This value is returned in the response of the <a href=\"/api-docs/commerce/media/resources/document/methods/createDocument\" target=\"_blank\">createDocument</a> method.
    content_type = 'content_type_example' # str | This header indicates the format of the request body provided by the client. Its value should be set to <b>multipart/form-data</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>.

    try:
        api_response = api_instance.upload_document(document_id, content_type)
        print("The response of DocumentApi->upload_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->upload_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The unique identifier of the document to be uploaded.&lt;br&gt;&lt;br&gt;This value is returned in the response of the &lt;a href&#x3D;\&quot;/api-docs/commerce/media/resources/document/methods/createDocument\&quot; target&#x3D;\&quot;_blank\&quot;&gt;createDocument&lt;/a&gt; method. | 
 **content_type** | **str**| This header indicates the format of the request body provided by the client. Its value should be set to &lt;b&gt;multipart/form-data&lt;/b&gt;. &lt;br&gt;&lt;br&gt; For more information, refer to &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank \&quot;&gt;HTTP request headers&lt;/a&gt;. | 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Uploaded |  -  |
**400** | Bad Request |  -  |
**404** | Document Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

