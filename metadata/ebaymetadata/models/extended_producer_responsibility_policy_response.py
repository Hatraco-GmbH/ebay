from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.extended_producer_responsibility_policy import ExtendedProducerResponsibilityPolicy


T = TypeVar("T", bound="ExtendedProducerResponsibilityPolicyResponse")


@_attrs_define
class ExtendedProducerResponsibilityPolicyResponse:
    """A type that defines the response fields for the <b>getExtendedProducerResponsibilityPolicies</b> method.

    Attributes:
        extended_producer_responsibilities (Union[Unset, List['ExtendedProducerResponsibilityPolicy']]): An array of
            response fields detailing the Extended Producer Responsibility policies supported for the specified marketplace.
        warnings (Union[Unset, List['Error']]): A collection of warnings generated for the request.
    """

    extended_producer_responsibilities: Union[Unset, List["ExtendedProducerResponsibilityPolicy"]] = UNSET
    warnings: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        extended_producer_responsibilities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extended_producer_responsibilities, Unset):
            extended_producer_responsibilities = []
            for extended_producer_responsibilities_item_data in self.extended_producer_responsibilities:
                extended_producer_responsibilities_item = extended_producer_responsibilities_item_data.to_dict()
                extended_producer_responsibilities.append(extended_producer_responsibilities_item)

        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extended_producer_responsibilities is not UNSET:
            field_dict["extendedProducerResponsibilities"] = extended_producer_responsibilities
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error
        from ..models.extended_producer_responsibility_policy import ExtendedProducerResponsibilityPolicy

        d = src_dict.copy()
        extended_producer_responsibilities = []
        _extended_producer_responsibilities = d.pop("extendedProducerResponsibilities", UNSET)
        for extended_producer_responsibilities_item_data in _extended_producer_responsibilities or []:
            extended_producer_responsibilities_item = ExtendedProducerResponsibilityPolicy.from_dict(
                extended_producer_responsibilities_item_data
            )

            extended_producer_responsibilities.append(extended_producer_responsibilities_item)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = Error.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        extended_producer_responsibility_policy_response = cls(
            extended_producer_responsibilities=extended_producer_responsibilities,
            warnings=warnings,
        )

        extended_producer_responsibility_policy_response.additional_properties = d
        return extended_producer_responsibility_policy_response

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
