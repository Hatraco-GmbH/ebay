# GetCurrenciesResponse

This type defines the response fields specifying the default currency for the marketplace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_currency** | [**Currency**](Currency.md) |  | [optional] 
**marketplace_id** | **str** | The ID of the eBay marketplace to which the default currency applies. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/bas:MarketplaceIdEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from ebaymetadata.models.get_currencies_response import GetCurrenciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrenciesResponse from a JSON string
get_currencies_response_instance = GetCurrenciesResponse.from_json(json)
# print the JSON string representation of the object
print(GetCurrenciesResponse.to_json())

# convert the object into a dict
get_currencies_response_dict = get_currencies_response_instance.to_dict()
# create an instance of GetCurrenciesResponse from a dict
get_currencies_response_from_dict = GetCurrenciesResponse.from_dict(get_currencies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


