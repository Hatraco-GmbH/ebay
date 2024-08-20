from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeDuration")


@_attrs_define
class TimeDuration:
    """A complex type that specifies a period of time using a specified time-measurement unit.

    Attributes:
        unit (Union[Unset, str]): A time-measurement unit that specifies a singular period of time.  <br><br>A span of
            time is defined when you apply the value specified in the <b>value</b> field to the value specified for
            <b>unit</b>.  <br><br>Time-measurement units can be YEAR, MONTH, DAY, and so on. See <b>TimeDurationUnitEnum</b>
            for a complete list of possible time-measurement units. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/sell/metadata/types/ba:TimeDurationUnitEnum'>eBay API
            documentation</a>
        value (Union[Unset, int]): An integer that represents an amount of time, as measured by the time-measurement
            unit specified in the <b>unit</b> field.
    """

    unit: Union[Unset, str] = UNSET
    value: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit = self.unit

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit is not UNSET:
            field_dict["unit"] = unit
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit = d.pop("unit", UNSET)

        value = d.pop("value", UNSET)

        time_duration = cls(
            unit=unit,
            value=value,
        )

        time_duration.additional_properties = d
        return time_duration

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
