from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pictogram")


@_attrs_define
class Pictogram:
    """A type that describes pictograms for hazardous materials labels.

    Attributes:
        pictogram_id (Union[Unset, str]): The identifier of the pictogram. For sample values, see <a href='/api-
            docs/sell/static/metadata/feature-regulatorhazmatcontainer.html#Pictogra'>Pictogram sample values</a>.
        pictogram_description (Union[Unset, str]): The description of the pictogram localized to the default language of
            the marketplace. For sample values, see <a href='/api-docs/sell/static/metadata/feature-
            regulatorhazmatcontainer.html#Pictogra'>Pictogram sample values</a>.
        pictogram_url (Union[Unset, str]): The URL of the pictogram.
    """

    pictogram_id: Union[Unset, str] = UNSET
    pictogram_description: Union[Unset, str] = UNSET
    pictogram_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pictogram_id = self.pictogram_id

        pictogram_description = self.pictogram_description

        pictogram_url = self.pictogram_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pictogram_id is not UNSET:
            field_dict["pictogramId"] = pictogram_id
        if pictogram_description is not UNSET:
            field_dict["pictogramDescription"] = pictogram_description
        if pictogram_url is not UNSET:
            field_dict["pictogramUrl"] = pictogram_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pictogram_id = d.pop("pictogramId", UNSET)

        pictogram_description = d.pop("pictogramDescription", UNSET)

        pictogram_url = d.pop("pictogramUrl", UNSET)

        pictogram = cls(
            pictogram_id=pictogram_id,
            pictogram_description=pictogram_description,
            pictogram_url=pictogram_url,
        )

        pictogram.additional_properties = d
        return pictogram

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
