from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SalesTaxJurisdiction")


@_attrs_define
class SalesTaxJurisdiction:
    """A unique ID for a sales tax jurisdiction.

    Attributes:
        sales_tax_jurisdiction_id (Union[Unset, str]): The unique ID for a sales-tax jurisdiction.<br><br><div
            class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color:
            #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span
            class="autonumber"><span><b><span style="color: #dd1e31;"
            class="mcFormatColor">Important!</span></b></span></span> When <code>countryCode</code> is set to
            <code>US</code>, IDs for all 50 states, Washington, DC, and all US territories will be returned. However, the
            only <code>salesTaxJurisdictionId</code> values currently supported are:<ul><li><code>AS</code> (American
            Samoa)</li><li><code>GU</code> (Guam</li><li><code>MP</code> Northern Mariana Islands</li><li><code>PW
            (Palau)</li><li><code>VI</code> (US Virgin Islands)</li></ul></p></div>
    """

    sales_tax_jurisdiction_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sales_tax_jurisdiction_id = self.sales_tax_jurisdiction_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sales_tax_jurisdiction_id is not UNSET:
            field_dict["salesTaxJurisdictionId"] = sales_tax_jurisdiction_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sales_tax_jurisdiction_id = d.pop("salesTaxJurisdictionId", UNSET)

        sales_tax_jurisdiction = cls(
            sales_tax_jurisdiction_id=sales_tax_jurisdiction_id,
        )

        sales_tax_jurisdiction.additional_properties = d
        return sales_tax_jurisdiction

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
