# TaxIdentifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxpayer_id** | **str** | This value is the unique tax ID associated with the buyer. The type of tax identification is shown in the taxIdentifierType field. | [optional] 
**tax_identifier_type** | **str** | This enumeration value indicates the type of tax identification being used for the buyer. The different tax types are defined in the TaxIdentifierTypeEnum type. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:TaxIdentifierTypeEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**issuing_country** | **str** | This two-letter code indicates the country that issued the buyer&#x27;s tax ID. The country that the two-letter code represents can be found in the CountryCodeEnum type, or in the ISO 3166 standard. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CountryCodeEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

