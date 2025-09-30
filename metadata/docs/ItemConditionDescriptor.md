# ItemConditionDescriptor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_descriptor_constraint** | [**ItemConditionDescriptorConstraint**](ItemConditionDescriptorConstraint.md) |  | [optional] 
**condition_descriptor_help_text** | **str** | A description of the condition descriptor that directs a user to its condition descriptor values.&lt;br&gt;&lt;br&gt; For example, the help text for &lt;code&gt;Card Condition&lt;/code&gt; is &lt;code&gt;Select ungraded condition&lt;/code&gt;. | [optional] 
**condition_descriptor_id** | **str** | The unique identification number of a condition descriptor associated with with a &lt;b&gt;conditionDescriptorName&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For example, &lt;code&gt;40001&lt;/code&gt; is the ID for &lt;code&gt;Card Condition&lt;/code&gt;.&lt;br&gt;&lt;br&gt;These IDs are used in the addItem family of calls of the &lt;b&gt;Trading API&lt;/b&gt; to provide condition descriptor names for the item. These IDs are used by the inventoryItem family of calls of the &lt;b&gt;Inventory API&lt;/b&gt; to provide condition descriptor names for the item. | [optional] 
**condition_descriptor_name** | **str** | The human-readable label for the condition descriptor associated with the &lt;b&gt;conditionDescriptorID&lt;/b&gt;. &lt;br&gt;&lt;br&gt;For example, &lt;code&gt;Card Condition&lt;/code&gt; is the condition descriptor name for ID &lt;code&gt;40001&lt;/code&gt; | [optional] 
**condition_descriptor_values** | [**list[ItemConditionDescriptorValue]**](ItemConditionDescriptorValue.md) | This array shows the possible values that map to the corresponding &lt;b&gt;conditionDescriptorName&lt;/b&gt; values. Constraint information and help text are also shown for each value. &lt;br&gt;&lt;br&gt;For example, The ID &lt;code&gt;40001&lt;/code&gt; is ID for the condition descriptor &lt;code&gt;card condition&lt;/code&gt;. The ID &lt;code&gt;400012&lt;/code&gt; is the ID for the &lt;code&gt;Very Good&lt;/code&gt; card condition value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

