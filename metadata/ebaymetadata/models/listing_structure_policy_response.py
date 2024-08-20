from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.listing_structure_policy import ListingStructurePolicy


T = TypeVar("T", bound="ListingStructurePolicyResponse")


@_attrs_define
class ListingStructurePolicyResponse:
    """
    Attributes:
        listing_structure_policies (Union[Unset, List['ListingStructurePolicy']]): Returns a list of category IDs plus a
            flag indicating whether or not each listed category supports item variations.
        warnings (Union[Unset, List['Error']]): A list of the warnings that were generated as a result of the request.
            This field is not returned if no warnings were generated by the request.
    """

    listing_structure_policies: Union[Unset, List["ListingStructurePolicy"]] = UNSET
    warnings: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        listing_structure_policies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.listing_structure_policies, Unset):
            listing_structure_policies = []
            for listing_structure_policies_item_data in self.listing_structure_policies:
                listing_structure_policies_item = listing_structure_policies_item_data.to_dict()
                listing_structure_policies.append(listing_structure_policies_item)

        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if listing_structure_policies is not UNSET:
            field_dict["listingStructurePolicies"] = listing_structure_policies
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error
        from ..models.listing_structure_policy import ListingStructurePolicy

        d = src_dict.copy()
        listing_structure_policies = []
        _listing_structure_policies = d.pop("listingStructurePolicies", UNSET)
        for listing_structure_policies_item_data in _listing_structure_policies or []:
            listing_structure_policies_item = ListingStructurePolicy.from_dict(listing_structure_policies_item_data)

            listing_structure_policies.append(listing_structure_policies_item)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = Error.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        listing_structure_policy_response = cls(
            listing_structure_policies=listing_structure_policies,
            warnings=warnings,
        )

        listing_structure_policy_response.additional_properties = d
        return listing_structure_policy_response

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