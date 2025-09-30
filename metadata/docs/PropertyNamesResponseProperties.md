# PropertyNamesResponseProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** | This field defines the types of properties are returned for the specified catalog-enabled category.&lt;br&gt;&lt;br&gt;&lt;b&gt;Valid values:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;&lt;code&gt;DisplayableProductDetails&lt;/code&gt;: Properties for use in a user interface to describe products.&lt;/li&gt;&lt;li&gt;&lt;code&gt;DisplayableSearchResults&lt;/code&gt;: Properties for use in results for product searches.&lt;/li&gt;&lt;li&gt;&lt;code&gt;Searchable&lt;/code&gt;: Properties for use in searches.&lt;/li&gt;&lt;li&gt;&lt;code&gt;Sortable&lt;/code&gt;: Properties that are suitable for sorting.&lt;/li&gt;&lt;/ul&gt; | [optional] 
**property_names** | [**list[PropertyNamesResponsePropertyNames]**](PropertyNamesResponsePropertyNames.md) | This array specifies the names of the properties associated with the specified category in the specified marketplace.&lt;br&gt;&lt;br&gt;For example, typical vehicle property names are &#x27;Make&#x27;, &#x27;Model&#x27;, &#x27;Year&#x27;, &#x27;Engine&#x27;, and &#x27;Trim&#x27;, but will vary based on the eBay marketplace and the eBay category. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

