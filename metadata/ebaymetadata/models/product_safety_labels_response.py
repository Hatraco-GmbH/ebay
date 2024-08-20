from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_safety_label_pictogram import ProductSafetyLabelPictogram
    from ..models.product_safety_label_statement import ProductSafetyLabelStatement


T = TypeVar("T", bound="ProductSafetyLabelsResponse")


@_attrs_define
class ProductSafetyLabelsResponse:
    """A type that defines the response fields for the <b>getProductSafetyLabels</b> method.

    Attributes:
        pictograms (Union[Unset, List['ProductSafetyLabelPictogram']]): This array contains a list of pictograms of
            product safety labels  for the specified marketplace.
        statements (Union[Unset, List['ProductSafetyLabelStatement']]): This array contains available product safety
            labels statements for the specified marketplace.
    """

    pictograms: Union[Unset, List["ProductSafetyLabelPictogram"]] = UNSET
    statements: Union[Unset, List["ProductSafetyLabelStatement"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pictograms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pictograms, Unset):
            pictograms = []
            for pictograms_item_data in self.pictograms:
                pictograms_item = pictograms_item_data.to_dict()
                pictograms.append(pictograms_item)

        statements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.statements, Unset):
            statements = []
            for statements_item_data in self.statements:
                statements_item = statements_item_data.to_dict()
                statements.append(statements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pictograms is not UNSET:
            field_dict["pictograms"] = pictograms
        if statements is not UNSET:
            field_dict["statements"] = statements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_safety_label_pictogram import ProductSafetyLabelPictogram
        from ..models.product_safety_label_statement import ProductSafetyLabelStatement

        d = src_dict.copy()
        pictograms = []
        _pictograms = d.pop("pictograms", UNSET)
        for pictograms_item_data in _pictograms or []:
            pictograms_item = ProductSafetyLabelPictogram.from_dict(pictograms_item_data)

            pictograms.append(pictograms_item)

        statements = []
        _statements = d.pop("statements", UNSET)
        for statements_item_data in _statements or []:
            statements_item = ProductSafetyLabelStatement.from_dict(statements_item_data)

            statements.append(statements_item)

        product_safety_labels_response = cls(
            pictograms=pictograms,
            statements=statements,
        )

        product_safety_labels_response.additional_properties = d
        return product_safety_labels_response

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
