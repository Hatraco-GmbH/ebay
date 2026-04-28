# Program

The seller program to opt in to when part of an <b>optInToProgram</b> request, or out of when part of an  <b>optOutOfProgram</b> request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_type** | **str** | The seller program to opt in to when part of an &lt;b&gt;optInToProgram&lt;/b&gt; request, or out of when part of an  &lt;b&gt;optOutOfProgram&lt;/b&gt; request. When returned in an &lt;b&gt;getOptedInPrograms&lt;/b&gt; response, a separate &lt;b&gt;programType&lt;/b&gt; field is returned for each seller program that the seller is opted in to. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/account/types/api:ProgramTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 

## Example

```python
from ebayaccount.models.program import Program

# TODO update the JSON string below
json = "{}"
# create an instance of Program from a JSON string
program_instance = Program.from_json(json)
# print the JSON string representation of the object
print(Program.to_json())

# convert the object into a dict
program_dict = program_instance.to_dict()
# create an instance of Program from a dict
program_from_dict = Program.from_dict(program_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


