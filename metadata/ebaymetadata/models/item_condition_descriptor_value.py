from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_condition_descriptor_value_constraint import ItemConditionDescriptorValueConstraint


T = TypeVar("T", bound="ItemConditionDescriptorValue")


@_attrs_define
class ItemConditionDescriptorValue:
    """This type displays the possible values for the corresponding condition descriptor, along with help text and
    constraint information.

        Attributes:
            condition_descriptor_value_additional_help_text (Union[Unset, List[str]]): Additional information about the the
                condition of the item that is not included in the <b>conditionDescriptorValueHelpText</b> field.
            condition_descriptor_value_constraints (Union[Unset, List['ItemConditionDescriptorValueConstraint']]): The
                constraints on a condition descriptor value, such as which descriptor value IDs and Descriptor ID it is
                associated with.
            condition_descriptor_value_help_text (Union[Unset, str]): A detailed description of the condition descriptor
                value.
            condition_descriptor_value_id (Union[Unset, str]): The unique identification number of a condition descriptor
                value associated with the <b>conditionDescriptorValueName</b>.
            condition_descriptor_value_name (Union[Unset, str]): The human-readable label for the condition descriptor value
                associated with the <b>conditionDescriptorValueID</b>.
    """

    condition_descriptor_value_additional_help_text: Union[Unset, List[str]] = UNSET
    condition_descriptor_value_constraints: Union[Unset, List["ItemConditionDescriptorValueConstraint"]] = UNSET
    condition_descriptor_value_help_text: Union[Unset, str] = UNSET
    condition_descriptor_value_id: Union[Unset, str] = UNSET
    condition_descriptor_value_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition_descriptor_value_additional_help_text: Union[Unset, List[str]] = UNSET
        if not isinstance(self.condition_descriptor_value_additional_help_text, Unset):
            condition_descriptor_value_additional_help_text = self.condition_descriptor_value_additional_help_text

        condition_descriptor_value_constraints: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.condition_descriptor_value_constraints, Unset):
            condition_descriptor_value_constraints = []
            for condition_descriptor_value_constraints_item_data in self.condition_descriptor_value_constraints:
                condition_descriptor_value_constraints_item = condition_descriptor_value_constraints_item_data.to_dict()
                condition_descriptor_value_constraints.append(condition_descriptor_value_constraints_item)

        condition_descriptor_value_help_text = self.condition_descriptor_value_help_text

        condition_descriptor_value_id = self.condition_descriptor_value_id

        condition_descriptor_value_name = self.condition_descriptor_value_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if condition_descriptor_value_additional_help_text is not UNSET:
            field_dict["conditionDescriptorValueAdditionalHelpText"] = condition_descriptor_value_additional_help_text
        if condition_descriptor_value_constraints is not UNSET:
            field_dict["conditionDescriptorValueConstraints"] = condition_descriptor_value_constraints
        if condition_descriptor_value_help_text is not UNSET:
            field_dict["conditionDescriptorValueHelpText"] = condition_descriptor_value_help_text
        if condition_descriptor_value_id is not UNSET:
            field_dict["conditionDescriptorValueId"] = condition_descriptor_value_id
        if condition_descriptor_value_name is not UNSET:
            field_dict["conditionDescriptorValueName"] = condition_descriptor_value_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_condition_descriptor_value_constraint import ItemConditionDescriptorValueConstraint

        d = src_dict.copy()
        condition_descriptor_value_additional_help_text = cast(
            List[str], d.pop("conditionDescriptorValueAdditionalHelpText", UNSET)
        )

        condition_descriptor_value_constraints = []
        _condition_descriptor_value_constraints = d.pop("conditionDescriptorValueConstraints", UNSET)
        for condition_descriptor_value_constraints_item_data in _condition_descriptor_value_constraints or []:
            condition_descriptor_value_constraints_item = ItemConditionDescriptorValueConstraint.from_dict(
                condition_descriptor_value_constraints_item_data
            )

            condition_descriptor_value_constraints.append(condition_descriptor_value_constraints_item)

        condition_descriptor_value_help_text = d.pop("conditionDescriptorValueHelpText", UNSET)

        condition_descriptor_value_id = d.pop("conditionDescriptorValueId", UNSET)

        condition_descriptor_value_name = d.pop("conditionDescriptorValueName", UNSET)

        item_condition_descriptor_value = cls(
            condition_descriptor_value_additional_help_text=condition_descriptor_value_additional_help_text,
            condition_descriptor_value_constraints=condition_descriptor_value_constraints,
            condition_descriptor_value_help_text=condition_descriptor_value_help_text,
            condition_descriptor_value_id=condition_descriptor_value_id,
            condition_descriptor_value_name=condition_descriptor_value_name,
        )

        item_condition_descriptor_value.additional_properties = d
        return item_condition_descriptor_value

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
