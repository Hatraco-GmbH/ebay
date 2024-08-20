from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegulatoryAttribute")


@_attrs_define
class RegulatoryAttribute:
    """A type that defines the attributes of a regulatory policy.

    Attributes:
        name (Union[Unset, str]): A unique value identifying a specific regulatory attribute. For implementation help,
            refer to <a href='https://developer.ebay.com/api-docs/sell/metadata/types/sel:RegulatoryAttributeEnum'>eBay API
            documentation</a>
        usage (Union[Unset, str]): The enumeration value in this field indicates whether the corresponding attribute is
            recommended or required for the corresponding leaf category. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/sell/metadata/types/sel:GenericUsageEnum'>eBay API documentation</a>
    """

    name: Union[Unset, str] = UNSET
    usage: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        usage = self.usage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        usage = d.pop("usage", UNSET)

        regulatory_attribute = cls(
            name=name,
            usage=usage,
        )

        regulatory_attribute.additional_properties = d
        return regulatory_attribute

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
