from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.item_condition_policy import ItemConditionPolicy


T = TypeVar("T", bound="ItemConditionPolicyResponse")


@_attrs_define
class ItemConditionPolicyResponse:
    """
    Attributes:
        item_condition_policies (Union[Unset, List['ItemConditionPolicy']]): A list of category IDs and the policies for
            how to indicate an item's condition in each of the listed categories.
        warnings (Union[Unset, List['Error']]): A list of the warnings that were generated as a result of the request.
            This field is not returned if no warnings were generated by the request.
    """

    item_condition_policies: Union[Unset, List["ItemConditionPolicy"]] = UNSET
    warnings: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_condition_policies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_condition_policies, Unset):
            item_condition_policies = []
            for item_condition_policies_item_data in self.item_condition_policies:
                item_condition_policies_item = item_condition_policies_item_data.to_dict()
                item_condition_policies.append(item_condition_policies_item)

        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_condition_policies is not UNSET:
            field_dict["itemConditionPolicies"] = item_condition_policies
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error
        from ..models.item_condition_policy import ItemConditionPolicy

        d = src_dict.copy()
        item_condition_policies = []
        _item_condition_policies = d.pop("itemConditionPolicies", UNSET)
        for item_condition_policies_item_data in _item_condition_policies or []:
            item_condition_policies_item = ItemConditionPolicy.from_dict(item_condition_policies_item_data)

            item_condition_policies.append(item_condition_policies_item)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = Error.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        item_condition_policy_response = cls(
            item_condition_policies=item_condition_policies,
            warnings=warnings,
        )

        item_condition_policy_response.additional_properties = d
        return item_condition_policy_response

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