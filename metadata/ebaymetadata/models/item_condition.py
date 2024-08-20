from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_condition_descriptor import ItemConditionDescriptor


T = TypeVar("T", bound="ItemCondition")


@_attrs_define
class ItemCondition:
    """<span class="tablenote"><b>Note: </b>In all eBay marketplaces, Condition ID 2000 now maps to an item condition of
    'Certified Refurbished', and not 'Manufacturer Refurbished'. To list an item as 'Certified Refurbished', a seller
    must be pre-qualified by eBay for this feature. Any seller who is not eligible for this feature will be blocked if
    they try to create a new listing or revise an existing listing with this item condition. Any active listings on any
    eBay marketplace that had 'Manufacturer Refurbished' as the item condition should have been automatically updated by
    eBay to the 'Seller Refurbished' item condition (Condition ID 2500). <br><br> Any seller that is interested in
    eligibility requirements to list with 'Certified Refurbished' should see the <a href="https://pages.ebay.com/seller-
    center/listing-and-marketing/certified-refurbished-program.html " target="_blank">Certified refurbished program</a>
    page in Seller Center. </span>

        Attributes:
            condition_description (Union[Unset, str]): The human-readable label for the condition (e.g., "New"). This value
                is typically localized for each site.  <br><br>Note that the display name can vary by category. For example, the
                description for condition ID <code>1000</code> could be called "New: with Tags" in one category and "Brand New"
                in another. For details on condition IDs and descriptions, see <a href='/api-
                docs/sell/static/metadata/condition-id-values.html'>Item condition ID and name values</a>.
            condition_descriptors (Union[Unset, List['ItemConditionDescriptor']]): This array contains the possible
                condition descriptors and condition descriptor values applicable for the specified category. It also returns
                usage requirements, maximum length, cardinality, and help text.<br><br><span class="tablenote"><b>Note:</b> This
                array is only returned for categories that support condition descriptors.</span>
            condition_help_text (Union[Unset, str]): A detailed description of the condition denoted by the
                <b>conditionID</b> and <b>conditionDescription</b>.
            condition_id (Union[Unset, str]): The ID value of the selected item condition. For information on the supported
                condition ID values, see <a href='/api-docs/sell/static/metadata/condition-id-values.html'>Item condition ID and
                name values</a>.
            usage (Union[Unset, str]): The value returned in this field indicates if there are any usage restrictions or
                requirements for the corresponding item condition in the corresponding category.<br><br><span
                class="tablenote"><b>Note:</b> Currently, the only supported value is 'RESTRICTED', and this field will only be
                returned for the following conditions: 2000, 2010, 2020, 2030. Sellers must be pre-approved to use any of these
                item conditions.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-
                docs/sell/metadata/types/sel:UsageEnum'>eBay API documentation</a>
    """

    condition_description: Union[Unset, str] = UNSET
    condition_descriptors: Union[Unset, List["ItemConditionDescriptor"]] = UNSET
    condition_help_text: Union[Unset, str] = UNSET
    condition_id: Union[Unset, str] = UNSET
    usage: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition_description = self.condition_description

        condition_descriptors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.condition_descriptors, Unset):
            condition_descriptors = []
            for condition_descriptors_item_data in self.condition_descriptors:
                condition_descriptors_item = condition_descriptors_item_data.to_dict()
                condition_descriptors.append(condition_descriptors_item)

        condition_help_text = self.condition_help_text

        condition_id = self.condition_id

        usage = self.usage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if condition_description is not UNSET:
            field_dict["conditionDescription"] = condition_description
        if condition_descriptors is not UNSET:
            field_dict["conditionDescriptors"] = condition_descriptors
        if condition_help_text is not UNSET:
            field_dict["conditionHelpText"] = condition_help_text
        if condition_id is not UNSET:
            field_dict["conditionId"] = condition_id
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_condition_descriptor import ItemConditionDescriptor

        d = src_dict.copy()
        condition_description = d.pop("conditionDescription", UNSET)

        condition_descriptors = []
        _condition_descriptors = d.pop("conditionDescriptors", UNSET)
        for condition_descriptors_item_data in _condition_descriptors or []:
            condition_descriptors_item = ItemConditionDescriptor.from_dict(condition_descriptors_item_data)

            condition_descriptors.append(condition_descriptors_item)

        condition_help_text = d.pop("conditionHelpText", UNSET)

        condition_id = d.pop("conditionId", UNSET)

        usage = d.pop("usage", UNSET)

        item_condition = cls(
            condition_description=condition_description,
            condition_descriptors=condition_descriptors,
            condition_help_text=condition_help_text,
            condition_id=condition_id,
            usage=usage,
        )

        item_condition.additional_properties = d
        return item_condition

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
