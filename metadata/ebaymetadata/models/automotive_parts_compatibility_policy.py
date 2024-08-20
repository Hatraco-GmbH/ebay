from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutomotivePartsCompatibilityPolicy")


@_attrs_define
class AutomotivePartsCompatibilityPolicy:
    """
    Attributes:
        category_id (Union[Unset, str]): The category ID to which the automotive-parts-compatibility policies apply.
        category_tree_id (Union[Unset, str]): A value that indicates the root node of the category tree used for the
            response set. Each marketplace is based on a category tree whose root node is indicated by this unique category
            ID value. All category policy information returned by this call pertains to the categories included below this
            root node of the tree.    <br><br>A <i>category tree</i> is a hierarchical framework of eBay categories that
            begins at the root node of the tree and extends to include all the child nodes in the tree. Each child node in
            the tree is an eBay category that is represented by a unique <b>categoryId</b> value. Within a category tree,
            the root node has no parent node and <i>leaf nodes</i> are nodes that have no child nodes.
        compatibility_based_on (Union[Unset, str]): Indicates whether the category supports parts compatibility by
            either <code>ASSEMBLY</code> or by <code>SPECIFICATION</code>. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/sell/metadata/types/sel:CompatibilityTypeEnum'>eBay API
            documentation</a>
        compatible_vehicle_types (Union[Unset, List[str]]): Indicates the compatibility classification of the part based
            on high-level vehicle types.
        max_number_of_compatible_vehicles (Union[Unset, int]): Specifies the maximum number of compatible vehicle-
            applications allowed per item.
    """

    category_id: Union[Unset, str] = UNSET
    category_tree_id: Union[Unset, str] = UNSET
    compatibility_based_on: Union[Unset, str] = UNSET
    compatible_vehicle_types: Union[Unset, List[str]] = UNSET
    max_number_of_compatible_vehicles: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category_id = self.category_id

        category_tree_id = self.category_tree_id

        compatibility_based_on = self.compatibility_based_on

        compatible_vehicle_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.compatible_vehicle_types, Unset):
            compatible_vehicle_types = self.compatible_vehicle_types

        max_number_of_compatible_vehicles = self.max_number_of_compatible_vehicles

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_tree_id is not UNSET:
            field_dict["categoryTreeId"] = category_tree_id
        if compatibility_based_on is not UNSET:
            field_dict["compatibilityBasedOn"] = compatibility_based_on
        if compatible_vehicle_types is not UNSET:
            field_dict["compatibleVehicleTypes"] = compatible_vehicle_types
        if max_number_of_compatible_vehicles is not UNSET:
            field_dict["maxNumberOfCompatibleVehicles"] = max_number_of_compatible_vehicles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category_id = d.pop("categoryId", UNSET)

        category_tree_id = d.pop("categoryTreeId", UNSET)

        compatibility_based_on = d.pop("compatibilityBasedOn", UNSET)

        compatible_vehicle_types = cast(List[str], d.pop("compatibleVehicleTypes", UNSET))

        max_number_of_compatible_vehicles = d.pop("maxNumberOfCompatibleVehicles", UNSET)

        automotive_parts_compatibility_policy = cls(
            category_id=category_id,
            category_tree_id=category_tree_id,
            compatibility_based_on=compatibility_based_on,
            compatible_vehicle_types=compatible_vehicle_types,
            max_number_of_compatible_vehicles=max_number_of_compatible_vehicles,
        )

        automotive_parts_compatibility_policy.additional_properties = d
        return automotive_parts_compatibility_policy

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
