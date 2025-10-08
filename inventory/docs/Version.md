# Version

This type is used to show the version number and instance of the service or API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**Version**](Version.md) |  | [optional] 
**version** | **str** | The version number of the service or API. | [optional] 

## Example

```python
from ebayinventory.models.version import Version

# TODO update the JSON string below
json = "{}"
# create an instance of Version from a JSON string
version_instance = Version.from_json(json)
# print the JSON string representation of the object
print(Version.to_json())

# convert the object into a dict
version_dict = version_instance.to_dict()
# create an instance of Version from a dict
version_from_dict = Version.from_dict(version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


