from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtendedProducerResponsibility")


@_attrs_define
class ExtendedProducerResponsibility:
    """A type that defines the attributes of an Extended Producer Responsibility policy.

    Attributes:
        enabled_for_variations (Union[Unset, bool]): An indication of whether the attribute can be enabled for listing
            variations.<br><br>If the value is <code>true</code>, the attribute may be specified at the variation level.
        name (Union[Unset, str]): The name of the attribute included in the policy. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/sell/metadata/types/sel:ExtendedProducerResponsibilityEnum'>eBay API
            documentation</a>
        usage (Union[Unset, str]): The usage guidelines for the attribute, in the specified marketplace. For
            implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/sell/metadata/types/sel:GenericUsageEnum'>eBay API documentation</a>
    """

    enabled_for_variations: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    usage: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled_for_variations = self.enabled_for_variations

        name = self.name

        usage = self.usage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled_for_variations is not UNSET:
            field_dict["enabledForVariations"] = enabled_for_variations
        if name is not UNSET:
            field_dict["name"] = name
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled_for_variations = d.pop("enabledForVariations", UNSET)

        name = d.pop("name", UNSET)

        usage = d.pop("usage", UNSET)

        extended_producer_responsibility = cls(
            enabled_for_variations=enabled_for_variations,
            name=name,
            usage=usage,
        )

        extended_producer_responsibility.additional_properties = d
        return extended_producer_responsibility

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
