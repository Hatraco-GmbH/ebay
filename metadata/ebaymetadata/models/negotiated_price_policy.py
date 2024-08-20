from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NegotiatedPricePolicy")


@_attrs_define
class NegotiatedPricePolicy:
    """
    Attributes:
        best_offer_auto_accept_enabled (Union[Unset, bool]): This flag denotes whether or not the category supports the
            setting of a price at which best offers are automatically accepted. If set to <code>true</code>, the category
            does support the setting of an automatic price for best-offers.
        best_offer_auto_decline_enabled (Union[Unset, bool]): This flag denotes whether or not the category supports the
            setting of an auto-decline price for best offers. If set to <code>true</code>, the category does support the
            setting of an automatic-decline price for best-offers.
        best_offer_counter_enabled (Union[Unset, bool]): This flag denotes whether or not the category supports the
            setting for an automatic counter-offer on best offers. If set to <code>true</code>, the category does support
            the setting of an automatic counter-offer price for best-offers.
        category_id (Union[Unset, str]): The category ID to which the negotiated-price policies apply.
        category_tree_id (Union[Unset, str]): A value that indicates the root node of the category tree used for the
            response set. Each marketplace is based on a category tree whose root node is indicated by this unique category
            ID value. All category policy information returned by this call pertains to the categories included below this
            root node of the tree.    <br><br>A <i>category tree</i> is a hierarchical framework of eBay categories that
            begins at the root node of the tree and extends to include all the child nodes in the tree. Each child node in
            the tree is an eBay category that is represented by a unique <b>categoryId</b> value. Within a category tree,
            the root node has no parent node and <i>leaf nodes</i> are nodes that have no child nodes.
    """

    best_offer_auto_accept_enabled: Union[Unset, bool] = UNSET
    best_offer_auto_decline_enabled: Union[Unset, bool] = UNSET
    best_offer_counter_enabled: Union[Unset, bool] = UNSET
    category_id: Union[Unset, str] = UNSET
    category_tree_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        best_offer_auto_accept_enabled = self.best_offer_auto_accept_enabled

        best_offer_auto_decline_enabled = self.best_offer_auto_decline_enabled

        best_offer_counter_enabled = self.best_offer_counter_enabled

        category_id = self.category_id

        category_tree_id = self.category_tree_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if best_offer_auto_accept_enabled is not UNSET:
            field_dict["bestOfferAutoAcceptEnabled"] = best_offer_auto_accept_enabled
        if best_offer_auto_decline_enabled is not UNSET:
            field_dict["bestOfferAutoDeclineEnabled"] = best_offer_auto_decline_enabled
        if best_offer_counter_enabled is not UNSET:
            field_dict["bestOfferCounterEnabled"] = best_offer_counter_enabled
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_tree_id is not UNSET:
            field_dict["categoryTreeId"] = category_tree_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        best_offer_auto_accept_enabled = d.pop("bestOfferAutoAcceptEnabled", UNSET)

        best_offer_auto_decline_enabled = d.pop("bestOfferAutoDeclineEnabled", UNSET)

        best_offer_counter_enabled = d.pop("bestOfferCounterEnabled", UNSET)

        category_id = d.pop("categoryId", UNSET)

        category_tree_id = d.pop("categoryTreeId", UNSET)

        negotiated_price_policy = cls(
            best_offer_auto_accept_enabled=best_offer_auto_accept_enabled,
            best_offer_auto_decline_enabled=best_offer_auto_decline_enabled,
            best_offer_counter_enabled=best_offer_counter_enabled,
            category_id=category_id,
            category_tree_id=category_tree_id,
        )

        negotiated_price_policy.additional_properties = d
        return negotiated_price_policy

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
