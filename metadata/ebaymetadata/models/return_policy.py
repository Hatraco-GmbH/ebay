from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.return_policy_details import ReturnPolicyDetails


T = TypeVar("T", bound="ReturnPolicy")


@_attrs_define
class ReturnPolicy:
    """
    Attributes:
        category_id (Union[Unset, str]): The category ID to which the return policies apply.
        category_tree_id (Union[Unset, str]): A value that indicates the root node of the category tree used for the
            response set. Each marketplace is based on a category tree whose root node is indicated by this unique category
            ID value. All category policy information returned by this call pertains to the categories included below this
            root node of the tree.    <br><br>A <i>category tree</i> is a hierarchical framework of eBay categories that
            begins at the root node of the tree and extends to include all the child nodes in the tree. Each child node in
            the tree is an eBay category that is represented by a unique <b>categoryId</b> value. Within a category tree,
            the root node has no parent node and <i>leaf nodes</i> are nodes that have no child nodes.
        domestic (Union[Unset, ReturnPolicyDetails]): This container defines the category policies that relate to
            domestic and international return policies (the return shipping is made via a domestic or an international
            shipping service, respectively).
        international (Union[Unset, ReturnPolicyDetails]): This container defines the category policies that relate to
            domestic and international return policies (the return shipping is made via a domestic or an international
            shipping service, respectively).
        required (Union[Unset, bool]): If set to <code>true</code>, this flag indicates that you must specify a return
            policy for items listed in the associated category.  <br><br>Note that not accepting returns (setting
            <b>returnsAcceptedEnabled</b> to <code>false</code>) is a valid return policy.
    """

    category_id: Union[Unset, str] = UNSET
    category_tree_id: Union[Unset, str] = UNSET
    domestic: Union[Unset, "ReturnPolicyDetails"] = UNSET
    international: Union[Unset, "ReturnPolicyDetails"] = UNSET
    required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category_id = self.category_id

        category_tree_id = self.category_tree_id

        domestic: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.domestic, Unset):
            domestic = self.domestic.to_dict()

        international: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.international, Unset):
            international = self.international.to_dict()

        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_tree_id is not UNSET:
            field_dict["categoryTreeId"] = category_tree_id
        if domestic is not UNSET:
            field_dict["domestic"] = domestic
        if international is not UNSET:
            field_dict["international"] = international
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.return_policy_details import ReturnPolicyDetails

        d = src_dict.copy()
        category_id = d.pop("categoryId", UNSET)

        category_tree_id = d.pop("categoryTreeId", UNSET)

        _domestic = d.pop("domestic", UNSET)
        domestic: Union[Unset, ReturnPolicyDetails]
        if isinstance(_domestic, Unset):
            domestic = UNSET
        else:
            domestic = ReturnPolicyDetails.from_dict(_domestic)

        _international = d.pop("international", UNSET)
        international: Union[Unset, ReturnPolicyDetails]
        if isinstance(_international, Unset):
            international = UNSET
        else:
            international = ReturnPolicyDetails.from_dict(_international)

        required = d.pop("required", UNSET)

        return_policy = cls(
            category_id=category_id,
            category_tree_id=category_tree_id,
            domestic=domestic,
            international=international,
            required=required,
        )

        return_policy.additional_properties = d
        return return_policy

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
