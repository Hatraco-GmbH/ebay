# CustomPolicy

This container defines a seller's custom policy identified by policy ID for the selected eBay marketplace. A successful call returns the requested policy information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_policy_id** | **str** | The unique custom policy identifier for a policy. | [optional] 
**description** | **str** | Contains the seller&#39;s policy and policy terms. Buyers access this information from the View Item page for items to which the policy has been applied.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length:&lt;/b&gt; 15,000 | [optional] 
**label** | **str** | Customer-facing label shown on View Item pages for items to which the policy applies. This seller-defined string is displayed as a system-generated hyperlink pointing to the seller&#39;s policy information.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length:&lt;/b&gt; 65 | [optional] 
**name** | **str** | The seller-defined name for the custom policy. Names must be unique for policies assigned to the same seller and policy type.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This field is visible only to the seller. &lt;/span&gt;&lt;br&gt;&lt;b&gt;Max length:&lt;/b&gt; 65 | [optional] 
**policy_type** | **str** | Specifies the type of Custom Policy being returned. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/account/types/api:CustomPolicyTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from ebayaccount.models.custom_policy import CustomPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPolicy from a JSON string
custom_policy_instance = CustomPolicy.from_json(json)
# print the JSON string representation of the object
print(CustomPolicy.to_json())

# convert the object into a dict
custom_policy_dict = custom_policy_instance.to_dict()
# create an instance of CustomPolicy from a dict
custom_policy_from_dict = CustomPolicy.from_dict(custom_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


