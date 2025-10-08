# RegionalProductCompliancePolicies

This type lists regional product compliance policies to be used by an offer when it is published and converted to a listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_policies** | [**List[CountryPolicy]**](CountryPolicy.md) | The array of country-specific product compliance policies to be used by an offer when it is published and converted to a listing. | [optional] 

## Example

```python
from ebayinventory.models.regional_product_compliance_policies import RegionalProductCompliancePolicies

# TODO update the JSON string below
json = "{}"
# create an instance of RegionalProductCompliancePolicies from a JSON string
regional_product_compliance_policies_instance = RegionalProductCompliancePolicies.from_json(json)
# print the JSON string representation of the object
print(RegionalProductCompliancePolicies.to_json())

# convert the object into a dict
regional_product_compliance_policies_dict = regional_product_compliance_policies_instance.to_dict()
# create an instance of RegionalProductCompliancePolicies from a dict
regional_product_compliance_policies_from_dict = RegionalProductCompliancePolicies.from_dict(regional_product_compliance_policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


