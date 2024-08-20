from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingStructurePolicy")


@_attrs_define
class ListingStructurePolicy:
    """
    Attributes:
        category_id (Union[Unset, str]): The category ID to which the listing-structure policy applies.
        category_tree_id (Union[Unset, str]): A value that indicates the root node of the category tree used for the
            response set. Each marketplace is based on a category tree whose root node is indicated by this unique category
            ID value. All category policy information returned by this call pertains to the categories included below this
            root node of the tree.    <br><br>A <i>category tree</i> is a hierarchical framework of eBay categories that
            begins at the root node of the tree and extends to include all the child nodes in the tree. Each child node in
            the tree is an eBay category that is represented by a unique <b>categoryId</b> value. Within a category tree,
            the root node has no parent node and <i>leaf nodes</i> are nodes that have no child nodes.
        variations_supported (Union[Unset, bool]): This flag denotes whether or not the associated category supports
            listings with item variations. If set to <code>true</code>, the category does support item variations.
    """

    category_id: Union[Unset, str] = UNSET
    category_tree_id: Union[Unset, str] = UNSET
    variations_supported: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category_id = self.category_id

        category_tree_id = self.category_tree_id

        variations_supported = self.variations_supported

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_tree_id is not UNSET:
            field_dict["categoryTreeId"] = category_tree_id
        if variations_supported is not UNSET:
            field_dict["variationsSupported"] = variations_supported

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category_id = d.pop("categoryId", UNSET)

        category_tree_id = d.pop("categoryTreeId", UNSET)

        variations_supported = d.pop("variationsSupported", UNSET)

        listing_structure_policy = cls(
            category_id=category_id,
            category_tree_id=category_tree_id,
            variations_supported=variations_supported,
        )

        listing_structure_policy.additional_properties = d
        return listing_structure_policy

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
