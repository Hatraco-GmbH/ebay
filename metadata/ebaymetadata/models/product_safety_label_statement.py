from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductSafetyLabelStatement")


@_attrs_define
class ProductSafetyLabelStatement:
    """A type that describes statements for product safety labels.

    Attributes:
        statement_description (Union[Unset, str]): The description of the statement localized to the default language of
            the marketplace.
        statement_id (Union[Unset, str]): The identifier of the statement.
    """

    statement_description: Union[Unset, str] = UNSET
    statement_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        statement_description = self.statement_description

        statement_id = self.statement_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if statement_description is not UNSET:
            field_dict["statementDescription"] = statement_description
        if statement_id is not UNSET:
            field_dict["statementId"] = statement_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        statement_description = d.pop("statementDescription", UNSET)

        statement_id = d.pop("statementId", UNSET)

        product_safety_label_statement = cls(
            statement_description=statement_description,
            statement_id=statement_id,
        )

        product_safety_label_statement.additional_properties = d
        return product_safety_label_statement

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
