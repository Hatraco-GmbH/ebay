from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.return_policy import ReturnPolicy


T = TypeVar("T", bound="ReturnPolicyResponse")


@_attrs_define
class ReturnPolicyResponse:
    """
    Attributes:
        return_policies (Union[Unset, List['ReturnPolicy']]): A list of elements, where each contains a category ID and
            a flag that indicates whether or not listings in that category require a return policy.
        warnings (Union[Unset, List['Error']]): A list of the warnings that were generated as a result of the request.
            This field is not returned if no warnings were generated by the request.
    """

    return_policies: Union[Unset, List["ReturnPolicy"]] = UNSET
    warnings: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_policies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.return_policies, Unset):
            return_policies = []
            for return_policies_item_data in self.return_policies:
                return_policies_item = return_policies_item_data.to_dict()
                return_policies.append(return_policies_item)

        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if return_policies is not UNSET:
            field_dict["returnPolicies"] = return_policies
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error
        from ..models.return_policy import ReturnPolicy

        d = src_dict.copy()
        return_policies = []
        _return_policies = d.pop("returnPolicies", UNSET)
        for return_policies_item_data in _return_policies or []:
            return_policies_item = ReturnPolicy.from_dict(return_policies_item_data)

            return_policies.append(return_policies_item)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = Error.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        return_policy_response = cls(
            return_policies=return_policies,
            warnings=warnings,
        )

        return_policy_response.additional_properties = d
        return return_policy_response

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
