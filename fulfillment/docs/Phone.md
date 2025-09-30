# Phone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  The two-letter, &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166&lt;/a&gt; code associated with the seller&#x27;s phone number. This field is needed if the buyer is located in a different country than the seller. It is also OK to provide if the buyer and seller are both located in the same country&lt;br&gt;&lt;br&gt;See &lt;a href&#x3D;\&quot;/api-docs/sell/fulfillment/types/ba:CountryCodeEnum \&quot; target&#x3D;\&quot;_blank\&quot;&gt;CountryCodeEnum&lt;/a&gt; for a list of supported values. | [optional] 
**number** | **str** | The seller&#x27;s primary phone number associated with the return address. When this number is provided in a &lt;strong&gt;contestPaymentDispute&lt;/strong&gt; or &lt;strong&gt;contestPaymentDispute&lt;/strong&gt; method, it is provided as one continuous numeric string, including the area code. So, if the phone number&#x27;s area code was &#x27;408&#x27;, a number in this field may look something like this: &lt;br&gt;&lt;br&gt;&lt;code&gt;\&quot;number\&quot; : \&quot;4088084356\&quot;&lt;/code&gt;&lt;br&gt;&lt;br&gt;If the buyer is located in a different country than the seller, the seller&#x27;s country code will need to be specified in the &lt;strong&gt;countryCode&lt;/strong&gt; field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

