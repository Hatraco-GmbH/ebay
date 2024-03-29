# AspectValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**localized_value** | **str** | The localized value of this aspect. Note: This value is always localized for the specified marketplace. | [optional] 
**value_constraints** | [**list[ValueConstraint]**](ValueConstraint.md) | Not returned if the value of the localizedValue field can always be selected for this aspect of the specified category. Contains a list of the dependencies that identify when the value of the localizedValue field is available for the current aspect. Each dependency specifies the values of another aspect of the same category (a control aspect), for which the current value of the current aspect can also be selected by the seller. Example: A shirt is available in three sizes and three colors, but only the Small and Medium sizes come in Green. Thus for the Color aspect, the value Green is constrained by its dependency on Size (the control aspect). Only when the Size aspect value is Small or Medium, can the Color aspect value of Green be selected by the seller. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


