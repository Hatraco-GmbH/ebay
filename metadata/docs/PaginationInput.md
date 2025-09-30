# PaginationInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The max number of items, from the current result set, returned on a single page.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; For &lt;b&gt;getProductCompatibilities&lt;/b&gt;, the max value is 100. If no &lt;b&gt;limit&lt;/b&gt; is specified, this field defaults to the max value.&lt;/span&gt; | [optional] 
**offset** | **int** | The number of items that will be skipped in the result set before returning the first item in the paginated response.&lt;br&gt;&lt;br&gt;Combine &lt;b&gt;offset&lt;/b&gt; with &lt;b&gt;limit&lt;/b&gt; to control the items returned in the response. For example, if you supply an offset of 10 and a limit of 20, the first page of the response contains items 11-30 from the complete result set.&lt;br&gt;&lt;br&gt;&lt;b&gt;Default:&lt;/b&gt; 0 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

