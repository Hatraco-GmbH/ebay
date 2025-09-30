# ProductRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_property_filters** | [**list[PropertyFilterInner]**](PropertyFilterInner.md) | This array is used to filter the properties of an application, such as a vehicle&#x27;s make or model, that will be returned in the response.&lt;br&gt;&lt;br&gt;Application property filters are specified as name-value pairs. Only products compatible with these name-value pairs will be returned. | [optional] 
**dataset** | **list[str]** | This array defines the type of properties that are returned for the catalog-enabled category.&lt;br&gt;&lt;br&gt;For example, if you specify &lt;code&gt;Searchable&lt;/code&gt;, the compatibility details will contain properties that can be used to search for products, such as make or model.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This field cannot be used alongside &lt;b&gt;dataPropertyName&lt;/b&gt;. If both are used, an error will occur.&lt;/span&gt;&lt;br&gt;&lt;b&gt;Valid values:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;&lt;code&gt;DisplayableProductDetails&lt;/code&gt;: Properties for use in a user interface to describe products.&lt;/li&gt;&lt;li&gt;&lt;code&gt;DisplayableSearchResults&lt;/code&gt;: Properties for use in results for product searches.&lt;/li&gt;&lt;li&gt;&lt;code&gt;Searchable&lt;/code&gt;: Properties for use in searches.&lt;/li&gt;&lt;li&gt;&lt;code&gt;Sortable&lt;/code&gt;: Properties that are suitable for sorting.&lt;/li&gt;&lt;/ul&gt;&lt;br&gt;&lt;b&gt;Default:&lt;/b&gt; &lt;code&gt;DisplayableSearchResults&lt;/code&gt; | [optional] 
**dataset_property_name** | **list[str]** | This comma-delimted array can be used to define the specific property name(s) that will be returned in the response.&lt;br&gt;&lt;br&gt;For example, if you specify &lt;code&gt;Engine&lt;/code&gt;, the result set will only contain engines that are compatible with the input criteria.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This array cannot be used alongside &lt;b&gt;dataset&lt;/b&gt;. If both are used, an error will occur.&lt;/span&gt; | [optional] 
**disabled_product_filter** | [**DisabledProductFilter**](DisabledProductFilter.md) |  | [optional] 
**pagination_input** | [**PaginationInput**](PaginationInput.md) |  | [optional] 
**product_identifier** | [**ProductIdentifier**](ProductIdentifier.md) |  | [optional] 
**sort_orders** | [**list[SortOrderInner]**](SortOrderInner.md) | This array controls the sort order of compatibility properties. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

