from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_condition_descriptor_constraint import ItemConditionDescriptorConstraint
    from ..models.item_condition_descriptor_value import ItemConditionDescriptorValue


T = TypeVar("T", bound="ItemConditionDescriptor")


@_attrs_define
class ItemConditionDescriptor:
    """This type is used to display the possible condition descriptors and condition values applicable for a specified
    category. It also returns usage requirements, maximum length, cardinality, and help text.

        Attributes:
            condition_descriptor_constraint (Union[Unset, ItemConditionDescriptorConstraint]): This type specifies the
                constraints on a condition descriptor, such as the maximum length, default condition descriptor value ID,
                cardinality, mode, usage, and applicable descriptor IDs.
            condition_descriptor_help_text (Union[Unset, str]): A description of the condition descriptor that directs a
                user to its condition descriptor values.<br><br> For example, the help text for <code>Card Condition</code> is
                <code>Select ungraded condition</code>.
            condition_descriptor_id (Union[Unset, str]): The unique identification number of a condition descriptor
                associated with with a <b>conditionDescriptorName</b>. <br><br>For example, <code>40001</code> is the ID for
                <code>Card Condition</code>.<br><br>These IDs are used in the addItem family of calls of the <b>Trading API</b>
                to provide condition descriptor names for the item. These IDs are used by the inventoryItem family of calls of
                the <b>Inventory API</b> to provide condition descriptor names for the item.
            condition_descriptor_name (Union[Unset, str]): The human-readable label for the condition descriptor associated
                with the <b>conditionDescriptorID</b>. <br><br>For example, <code>Card Condition</code> is the condition
                descriptor name for ID <code>40001</code>
            condition_descriptor_values (Union[Unset, List['ItemConditionDescriptorValue']]): This array shows the possible
                values that map to the corresponding <b>conditionDescriptorName</b> values. Constraint information and help text
                are also shown for each value. <br><br>For example, The ID <code>40001</code> is ID for the condition descriptor
                <code>card condition</code>. The ID <code>400012</code> is the ID for the <code>Very Good</code> card condition
                value.
    """

    condition_descriptor_constraint: Union[Unset, "ItemConditionDescriptorConstraint"] = UNSET
    condition_descriptor_help_text: Union[Unset, str] = UNSET
    condition_descriptor_id: Union[Unset, str] = UNSET
    condition_descriptor_name: Union[Unset, str] = UNSET
    condition_descriptor_values: Union[Unset, List["ItemConditionDescriptorValue"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition_descriptor_constraint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.condition_descriptor_constraint, Unset):
            condition_descriptor_constraint = self.condition_descriptor_constraint.to_dict()

        condition_descriptor_help_text = self.condition_descriptor_help_text

        condition_descriptor_id = self.condition_descriptor_id

        condition_descriptor_name = self.condition_descriptor_name

        condition_descriptor_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.condition_descriptor_values, Unset):
            condition_descriptor_values = []
            for condition_descriptor_values_item_data in self.condition_descriptor_values:
                condition_descriptor_values_item = condition_descriptor_values_item_data.to_dict()
                condition_descriptor_values.append(condition_descriptor_values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if condition_descriptor_constraint is not UNSET:
            field_dict["conditionDescriptorConstraint"] = condition_descriptor_constraint
        if condition_descriptor_help_text is not UNSET:
            field_dict["conditionDescriptorHelpText"] = condition_descriptor_help_text
        if condition_descriptor_id is not UNSET:
            field_dict["conditionDescriptorId"] = condition_descriptor_id
        if condition_descriptor_name is not UNSET:
            field_dict["conditionDescriptorName"] = condition_descriptor_name
        if condition_descriptor_values is not UNSET:
            field_dict["conditionDescriptorValues"] = condition_descriptor_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_condition_descriptor_constraint import ItemConditionDescriptorConstraint
        from ..models.item_condition_descriptor_value import ItemConditionDescriptorValue

        d = src_dict.copy()
        _condition_descriptor_constraint = d.pop("conditionDescriptorConstraint", UNSET)
        condition_descriptor_constraint: Union[Unset, ItemConditionDescriptorConstraint]
        if isinstance(_condition_descriptor_constraint, Unset):
            condition_descriptor_constraint = UNSET
        else:
            condition_descriptor_constraint = ItemConditionDescriptorConstraint.from_dict(
                _condition_descriptor_constraint
            )

        condition_descriptor_help_text = d.pop("conditionDescriptorHelpText", UNSET)

        condition_descriptor_id = d.pop("conditionDescriptorId", UNSET)

        condition_descriptor_name = d.pop("conditionDescriptorName", UNSET)

        condition_descriptor_values = []
        _condition_descriptor_values = d.pop("conditionDescriptorValues", UNSET)
        for condition_descriptor_values_item_data in _condition_descriptor_values or []:
            condition_descriptor_values_item = ItemConditionDescriptorValue.from_dict(
                condition_descriptor_values_item_data
            )

            condition_descriptor_values.append(condition_descriptor_values_item)

        item_condition_descriptor = cls(
            condition_descriptor_constraint=condition_descriptor_constraint,
            condition_descriptor_help_text=condition_descriptor_help_text,
            condition_descriptor_id=condition_descriptor_id,
            condition_descriptor_name=condition_descriptor_name,
            condition_descriptor_values=condition_descriptor_values,
        )

        item_condition_descriptor.additional_properties = d
        return item_condition_descriptor

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
