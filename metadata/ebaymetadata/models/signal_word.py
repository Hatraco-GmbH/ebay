from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignalWord")


@_attrs_define
class SignalWord:
    """A type that describes signal words for hazardous materials labels.

    Attributes:
        signal_word_id (Union[Unset, str]): The identifier of the signal word. For more information, see <a href='/api-
            docs/sell/static/metadata/feature-regulatorhazmatcontainer.html#Signal'>Signal word information</a>.
        signal_word_description (Union[Unset, str]): The description of the signal word localized to the default
            language of the marketplace. For more information, see <a href='/api-docs/sell/static/metadata/feature-
            regulatorhazmatcontainer.html#Signal'>Signal word information</a>.
    """

    signal_word_id: Union[Unset, str] = UNSET
    signal_word_description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        signal_word_id = self.signal_word_id

        signal_word_description = self.signal_word_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signal_word_id is not UNSET:
            field_dict["signalWordId"] = signal_word_id
        if signal_word_description is not UNSET:
            field_dict["signalWordDescription"] = signal_word_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        signal_word_id = d.pop("signalWordId", UNSET)

        signal_word_description = d.pop("signalWordDescription", UNSET)

        signal_word = cls(
            signal_word_id=signal_word_id,
            signal_word_description=signal_word_description,
        )

        signal_word.additional_properties = d
        return signal_word

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
