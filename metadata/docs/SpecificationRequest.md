# SpecificationRequest

This type provides the properties and specifications to use to search for compatibilities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The unique identifier of the eBay leaf category for which compatibility details are being retrieved. This category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility for cars, trucks, or motorcycles.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/marketplace/methods/getAutomotivePartsCompatibilityPolicies\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAutomotivePartsCompatibilityPolicies&lt;/a&gt; method to retrieve a list of categories that support parts compatibility by specification. For the categories in the response that support compatibility by specification, you’ll see &lt;code&gt;SPECIFICATIONS&lt;/code&gt; as the value for the &lt;b&gt;compatibilityBasedOn&lt;/b&gt; field  | [optional] 
**compatibility_property_filters** | [**List[PropertyFilterInner]**](PropertyFilterInner.md) | This comma-delimited array can be used to restrict the number of compatible application name-value pairs returned in the response by specifying the properties that the seller wishes to be included in the response.&lt;br&gt;&lt;br&gt;Only compatible applications with the specified properties will be returned. Properties that can be specified here include make, model, year, and trim. | [optional] 
**dataset** | **str** | This field can be used to define the type of properties that will be returned in the response.&lt;br&gt;&lt;br&gt; For example, if you specify &lt;code&gt;Searchable&lt;/code&gt;, the compatibility details will contain properties that can be used to search for products, such as make or model.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This field cannot be used alongside &lt;b&gt;dataPropertyName&lt;/b&gt;. If both are used, an error will occur.&lt;/span&gt;&lt;br&gt;&lt;b&gt;Valid values:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;&lt;code&gt;DisplayableProductDetails&lt;/code&gt;: Properties for use in a user interface to describe products.&lt;/li&gt;&lt;li&gt;&lt;code&gt;DisplayableSearchResults&lt;/code&gt;: Properties for use in results for product searches.&lt;/li&gt;&lt;li&gt;&lt;code&gt;Searchable&lt;/code&gt;: Properties for use in searches.&lt;/li&gt;&lt;li&gt;&lt;code&gt;Sortable&lt;/code&gt;: Properties that are suitable for sorting.&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Default value:&lt;/b&gt; &lt;code&gt;DisplayableSearchResults&lt;/code&gt; | [optional] 
**dataset_property_name** | **List[str]** | This comma-delimited array can be used to define the specific property name(s) that will be returned in the response.&lt;br&gt;&lt;br&gt;For example, if you specify &lt;code&gt;Engine&lt;/code&gt;, the result set will only contain engines that are compatible with the input criteria.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This array cannot be used alongside &lt;b&gt;dataset&lt;/b&gt;. If both are used, an error will occur.&lt;/span&gt; | [optional] 
**exact_match** | **bool** | This boolean can be used to specify that the compatibilities returned in the response are to be defined by an exact match on the input value of specification properties.&lt;br&gt;&lt;br&gt;By default, an expanded compatibility match is done when it applies, such as for Load Index, where a compatible vehicle is one that has a load index requirement that is less than or equal to the input. By specifying this field as &lt;code&gt;true&lt;/code&gt;, only exact matches are returned. | [optional] 
**pagination_input** | [**PaginationInput**](PaginationInput.md) |  | [optional] 
**sort_orders** | [**List[SortOrderInner]**](SortOrderInner.md) | This array specifies the sorting order of the compatibility properties. Any of the searchable properties can be used to specify search order. Up to 5 levels of sort order may be specified.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; If no sort order is specified through this field, the default sort order of &lt;b&gt;popularity descending&lt;/b&gt; is applied.&lt;/span&gt; | [optional] 
**specifications** | [**List[PropertyFilterInner]**](PropertyFilterInner.md) | This array defines the specifications of the part, in the form of name-value pairs, for which compatible applications will be retrieved. | [optional] 

## Example

```python
from ebaymetadata.models.specification_request import SpecificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationRequest from a JSON string
specification_request_instance = SpecificationRequest.from_json(json)
# print the JSON string representation of the object
print(SpecificationRequest.to_json())

# convert the object into a dict
specification_request_dict = specification_request_instance.to_dict()
# create an instance of SpecificationRequest from a dict
specification_request_from_dict = SpecificationRequest.from_dict(specification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


