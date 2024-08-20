from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sales_tax_jurisdiction import SalesTaxJurisdiction


T = TypeVar("T", bound="SalesTaxJurisdictions")


@_attrs_define
class SalesTaxJurisdictions:
    """This complex type contains a list of sales-tax jurisdictions.

    Attributes:
        sales_tax_jurisdictions (Union[Unset, List['SalesTaxJurisdiction']]): A list of sales-tax jurisdictions.
    """

    sales_tax_jurisdictions: Union[Unset, List["SalesTaxJurisdiction"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sales_tax_jurisdictions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sales_tax_jurisdictions, Unset):
            sales_tax_jurisdictions = []
            for sales_tax_jurisdictions_item_data in self.sales_tax_jurisdictions:
                sales_tax_jurisdictions_item = sales_tax_jurisdictions_item_data.to_dict()
                sales_tax_jurisdictions.append(sales_tax_jurisdictions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sales_tax_jurisdictions is not UNSET:
            field_dict["salesTaxJurisdictions"] = sales_tax_jurisdictions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sales_tax_jurisdiction import SalesTaxJurisdiction

        d = src_dict.copy()
        sales_tax_jurisdictions = []
        _sales_tax_jurisdictions = d.pop("salesTaxJurisdictions", UNSET)
        for sales_tax_jurisdictions_item_data in _sales_tax_jurisdictions or []:
            sales_tax_jurisdictions_item = SalesTaxJurisdiction.from_dict(sales_tax_jurisdictions_item_data)

            sales_tax_jurisdictions.append(sales_tax_jurisdictions_item)

        sales_tax_jurisdictions = cls(
            sales_tax_jurisdictions=sales_tax_jurisdictions,
        )

        sales_tax_jurisdictions.additional_properties = d
        return sales_tax_jurisdictions

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
