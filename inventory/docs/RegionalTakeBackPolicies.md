# RegionalTakeBackPolicies

This type lists regional take-back policies to be used by an offer when it is published and converted to a listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_policies** | [**List[CountryPolicy]**](CountryPolicy.md) | The array of country-specific take-back policies to be used by an offer when it is published and converted to a listing. | [optional] 

## Example

```python
from ebayinventory.models.regional_take_back_policies import RegionalTakeBackPolicies

# TODO update the JSON string below
json = "{}"
# create an instance of RegionalTakeBackPolicies from a JSON string
regional_take_back_policies_instance = RegionalTakeBackPolicies.from_json(json)
# print the JSON string representation of the object
print(RegionalTakeBackPolicies.to_json())

# convert the object into a dict
regional_take_back_policies_dict = regional_take_back_policies_instance.to_dict()
# create an instance of RegionalTakeBackPolicies from a dict
regional_take_back_policies_from_dict = RegionalTakeBackPolicies.from_dict(regional_take_back_policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


