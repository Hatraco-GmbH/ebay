# FeeSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fees** | [**list[Fee]**](Fee.md) | This container is an array of listing fees that can be expected to be applied to an offer on the specified eBay marketplace (marketplaceId value). Many fee types will get returned even when they are 0.0. See the Standard selling fees help page for more information on listing fees. | [optional] 
**marketplace_id** | **str** | This is the unique identifier of the eBay site for which listing fees for the offer are applicable. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/inventory/types/slr:MarketplaceEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**warnings** | [**list[Error]**](Error.md) | This container will contain an array of errors and/or warnings when a call is made, and errors and/or warnings occur. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

