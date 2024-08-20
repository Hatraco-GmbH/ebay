from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_condition import ItemCondition


T = TypeVar("T", bound="ItemConditionPolicy")


@_attrs_define
class ItemConditionPolicy:
    """
    Attributes:
        category_id (Union[Unset, str]): The category ID to which the item-condition policy applies.
        category_tree_id (Union[Unset, str]): A value that indicates the root node of the category tree used for the
            response set. Each marketplace is based on a category tree whose root node is indicated by this unique category
            ID value. All category policy information returned by this call pertains to the categories included below this
            root node of the tree.    <br><br>A <i>category tree</i> is a hierarchical framework of eBay categories that
            begins at the root node of the tree and extends to include all the child nodes in the tree. Each child node in
            the tree is an eBay category that is represented by a unique <b>categoryId</b> value. Within a category tree,
            the root node has no parent node and <i>leaf nodes</i> are nodes that have no child nodes.
        item_condition_required (Union[Unset, bool]): This flag denotes whether or not you must list the item condition
            in a listing for the specified category. If set to <code>true</code>, you must specify an item condition for the
            associated category.
        item_conditions (Union[Unset, List['ItemCondition']]): The item-condition values allowed in the
            category.<br><br><span class="tablenote"><b>Note:</b> The ‘Seller Refurbished’ item condition (condition ID
            2500) has been replaced by the 'Excellent - Refurbished', 'Very Good - Refurbished', and 'Good - Refurbished'
            item conditions in a select number of eBay marketplaces and categories. See the <a href="/api-
            docs/sell/static/metadata/condition-id-values.html#Category " target="_blank "> eBay Refurbished Program -
            Category and marketplace support</a> topic for more details.<br/><br/>Similar to the ‘Certified Refurbished’
            item condition (condition ID 2000), a seller’s OAuth user token will have to be used instead of an OAuth
            application token, since each seller must  go through an application and qualification process before using any
            of these new refurbished item conditions in supported categories. If a seller is not qualified to use the new
            refurbished item conditions, these item condition values will not be returned by
            <b>getItemConditionPolicies</b>.</span>
    """

    category_id: Union[Unset, str] = UNSET
    category_tree_id: Union[Unset, str] = UNSET
    item_condition_required: Union[Unset, bool] = UNSET
    item_conditions: Union[Unset, List["ItemCondition"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category_id = self.category_id

        category_tree_id = self.category_tree_id

        item_condition_required = self.item_condition_required

        item_conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_conditions, Unset):
            item_conditions = []
            for item_conditions_item_data in self.item_conditions:
                item_conditions_item = item_conditions_item_data.to_dict()
                item_conditions.append(item_conditions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_tree_id is not UNSET:
            field_dict["categoryTreeId"] = category_tree_id
        if item_condition_required is not UNSET:
            field_dict["itemConditionRequired"] = item_condition_required
        if item_conditions is not UNSET:
            field_dict["itemConditions"] = item_conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_condition import ItemCondition

        d = src_dict.copy()
        category_id = d.pop("categoryId", UNSET)

        category_tree_id = d.pop("categoryTreeId", UNSET)

        item_condition_required = d.pop("itemConditionRequired", UNSET)

        item_conditions = []
        _item_conditions = d.pop("itemConditions", UNSET)
        for item_conditions_item_data in _item_conditions or []:
            item_conditions_item = ItemCondition.from_dict(item_conditions_item_data)

            item_conditions.append(item_conditions_item)

        item_condition_policy = cls(
            category_id=category_id,
            category_tree_id=category_tree_id,
            item_condition_required=item_condition_required,
            item_conditions=item_conditions,
        )

        item_condition_policy.additional_properties = d
        return item_condition_policy

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
