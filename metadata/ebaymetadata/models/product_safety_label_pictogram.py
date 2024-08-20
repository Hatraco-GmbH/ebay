from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductSafetyLabelPictogram")


@_attrs_define
class ProductSafetyLabelPictogram:
    """A type that describes pictograms for product safety labels.

    Attributes:
        pictogram_description (Union[Unset, str]): The description of the pictogram localized to the default language of
            the marketplace.
        pictogram_id (Union[Unset, str]): The identifier of the pictogram.
        pictogram_url (Union[Unset, str]): The URL of the pictogram.
    """

    pictogram_description: Union[Unset, str] = UNSET
    pictogram_id: Union[Unset, str] = UNSET
    pictogram_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pictogram_description = self.pictogram_description

        pictogram_id = self.pictogram_id

        pictogram_url = self.pictogram_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pictogram_description is not UNSET:
            field_dict["pictogramDescription"] = pictogram_description
        if pictogram_id is not UNSET:
            field_dict["pictogramId"] = pictogram_id
        if pictogram_url is not UNSET:
            field_dict["pictogramUrl"] = pictogram_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pictogram_description = d.pop("pictogramDescription", UNSET)

        pictogram_id = d.pop("pictogramId", UNSET)

        pictogram_url = d.pop("pictogramUrl", UNSET)

        product_safety_label_pictogram = cls(
            pictogram_description=pictogram_description,
            pictogram_id=pictogram_id,
            pictogram_url=pictogram_url,
        )

        product_safety_label_pictogram.additional_properties = d
        return product_safety_label_pictogram

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
