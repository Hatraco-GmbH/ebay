# CountryPolicy

This type specifies custom product compliance and/or take-back policies that apply to a specified country.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | The two-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166-1&lt;/a&gt; country code identifying the country to which the policy or policies specified in the corresponding policyIds array will apply. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/ba:CountryCodeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**policy_ids** | **List[str]** | An array of custom policy identifiers that apply to the country specified by &lt;a href&#x3D;\&quot;#request.listingPolicies.regionalProductCompliancePolicies.countryPolicies.country\&quot;&gt;listingPolicies.regionalTakeBackPolicies.countryPolicies.country&lt;/a&gt;.&lt;br&gt;&lt;br&gt;Product compliance and take-back policy information may be returned using the following methods:&lt;ul&gt;&lt;li&gt;&lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/custom_policy/methods/getCustomPolicies \&quot; target&#x3D;\&quot;_blank\&quot;&gt;getCustomPolicies&lt;/a&gt;&lt;br&gt;&lt;br&gt;Set &lt;code&gt;policy_types&lt;/code&gt; to:&lt;ul&gt;&lt;li&gt;&lt;code&gt;PRODUCT_COMPLIANCE&lt;/code&gt; for product compliance policies&lt;/li&gt;&lt;li&gt;&lt;code&gt;TAKE_BACK&lt;/code&gt; for takeback policies&lt;/li&gt;&lt;/ul&gt;&lt;br&gt;This returns the list of specified policies and corresponding &lt;b&gt;customPolicyId&lt;/b&gt; values a seller has created.&lt;/li&gt;&lt;li&gt;&lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/custom_policy/methods/getCustomPolicy \&quot; target&#x3D;\&quot;_blank\&quot;&gt;getCustomPolicy&lt;/a&gt; with &lt;code&gt;custom_policy_id &#x3D; customPolicyId&lt;/code&gt;&lt;br&gt;&lt;br&gt;Returns the details of the policy specified by &lt;b&gt;customPolicyId&lt;/b&gt;&lt;/li&gt;&lt;/ul&gt;For information about creating and managing custom policies, refer to the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/methods#h2-custom_policy \&quot; target&#x3D;\&quot;_blank\&quot;&gt;custom_policy&lt;/a&gt; resource in the &lt;b&gt;Sell Account&lt;/b&gt; API. | [optional] 

## Example

```python
from ebayinventory.models.country_policy import CountryPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of CountryPolicy from a JSON string
country_policy_instance = CountryPolicy.from_json(json)
# print the JSON string representation of the object
print(CountryPolicy.to_json())

# convert the object into a dict
country_policy_dict = country_policy_instance.to_dict()
# create an instance of CountryPolicy from a dict
country_policy_from_dict = CountryPolicy.from_dict(country_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


