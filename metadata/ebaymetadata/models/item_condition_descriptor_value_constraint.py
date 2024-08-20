from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemConditionDescriptorValueConstraint")


@_attrs_define
class ItemConditionDescriptorValueConstraint:
    """This type shows the constraints on a condition descriptor value, such as any associated condition descriptor ID and
    condition descriptor value IDs required for a listing.

        Attributes:
            applicable_to_condition_descriptor_id (Union[Unset, str]): This string is returned if the corresponding
                condition descriptor value requires an associated condition descriptor that must also be specified in a listing.
                The condition descriptor ID for the associated condition descriptors is returned here.
            applicable_to_condition_descriptor_value_ids (Union[Unset, List[str]]): This array is returned if the
                corresponding condition descriptor value is required for one or more associated condition descriptor values that
                must also be specified in a listing. The condition descriptor values IDs for the associated condition descriptor
                values are returned here.
    """

    applicable_to_condition_descriptor_id: Union[Unset, str] = UNSET
    applicable_to_condition_descriptor_value_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        applicable_to_condition_descriptor_id = self.applicable_to_condition_descriptor_id

        applicable_to_condition_descriptor_value_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.applicable_to_condition_descriptor_value_ids, Unset):
            applicable_to_condition_descriptor_value_ids = self.applicable_to_condition_descriptor_value_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applicable_to_condition_descriptor_id is not UNSET:
            field_dict["applicableToConditionDescriptorId"] = applicable_to_condition_descriptor_id
        if applicable_to_condition_descriptor_value_ids is not UNSET:
            field_dict["applicableToConditionDescriptorValueIds"] = applicable_to_condition_descriptor_value_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        applicable_to_condition_descriptor_id = d.pop("applicableToConditionDescriptorId", UNSET)

        applicable_to_condition_descriptor_value_ids = cast(
            List[str], d.pop("applicableToConditionDescriptorValueIds", UNSET)
        )

        item_condition_descriptor_value_constraint = cls(
            applicable_to_condition_descriptor_id=applicable_to_condition_descriptor_id,
            applicable_to_condition_descriptor_value_ids=applicable_to_condition_descriptor_value_ids,
        )

        item_condition_descriptor_value_constraint.additional_properties = d
        return item_condition_descriptor_value_constraint

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
