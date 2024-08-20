from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemConditionDescriptorConstraint")


@_attrs_define
class ItemConditionDescriptorConstraint:
    """This type specifies the constraints on a condition descriptor, such as the maximum length, default condition
    descriptor value ID, cardinality, mode, usage, and applicable descriptor IDs.

        Attributes:
            applicable_to_condition_descriptor_ids (Union[Unset, List[str]]): This array is returned if the corresponding
                condition descriptor requires that one or more other associated condition descriptors must also be specified in
                a listing. The condition descriptor IDs for the associated condition descriptors are returned here.<br><br>For
                example, the <code>Grade</code> and <code>Grader</code> condition descriptors must always be specified together
                in a listing for Graded cards.
            cardinality (Union[Unset, str]): The value returned in this field indicates whether a condition descriptor can
                have a single value or multiple values. For implementation help, refer to <a
                href='https://developer.ebay.com/api-docs/sell/metadata/types/sel:CardinalityEnum'>eBay API documentation</a>
            default_condition_descriptor_value_id (Union[Unset, str]): The default condition descriptor value that will be
                set if there are multiple values.
            max_length (Union[Unset, int]): The maximum characters allowed for a condition descriptor. This field is only
                returned/applicable for condition descriptors that allow free text for condition descriptor values.
            mode (Union[Unset, str]): The value returned in this field indicates whether the supported values for a
                condition descriptor are predefined or if the seller manually specified the value.<br><br><span
                class="tablenote"><b>Note:</b> <code>FREE_TEXT</code> is currently only applicable to the Certification Number
                condition descriptor.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-
                docs/sell/metadata/types/sel:ModeEnum'>eBay API documentation</a>
            usage (Union[Unset, str]): This value indicates whether or not the condition descriptor is required for the item
                condition. Currently, this field is only returned if the condition descriptor is required for the item
                condition. For implementation help, refer to <a href='https://developer.ebay.com/api-
                docs/sell/metadata/types/sel:DescriptorUsageEnum'>eBay API documentation</a>
    """

    applicable_to_condition_descriptor_ids: Union[Unset, List[str]] = UNSET
    cardinality: Union[Unset, str] = UNSET
    default_condition_descriptor_value_id: Union[Unset, str] = UNSET
    max_length: Union[Unset, int] = UNSET
    mode: Union[Unset, str] = UNSET
    usage: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        applicable_to_condition_descriptor_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.applicable_to_condition_descriptor_ids, Unset):
            applicable_to_condition_descriptor_ids = self.applicable_to_condition_descriptor_ids

        cardinality = self.cardinality

        default_condition_descriptor_value_id = self.default_condition_descriptor_value_id

        max_length = self.max_length

        mode = self.mode

        usage = self.usage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applicable_to_condition_descriptor_ids is not UNSET:
            field_dict["applicableToConditionDescriptorIds"] = applicable_to_condition_descriptor_ids
        if cardinality is not UNSET:
            field_dict["cardinality"] = cardinality
        if default_condition_descriptor_value_id is not UNSET:
            field_dict["defaultConditionDescriptorValueId"] = default_condition_descriptor_value_id
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if mode is not UNSET:
            field_dict["mode"] = mode
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        applicable_to_condition_descriptor_ids = cast(List[str], d.pop("applicableToConditionDescriptorIds", UNSET))

        cardinality = d.pop("cardinality", UNSET)

        default_condition_descriptor_value_id = d.pop("defaultConditionDescriptorValueId", UNSET)

        max_length = d.pop("maxLength", UNSET)

        mode = d.pop("mode", UNSET)

        usage = d.pop("usage", UNSET)

        item_condition_descriptor_constraint = cls(
            applicable_to_condition_descriptor_ids=applicable_to_condition_descriptor_ids,
            cardinality=cardinality,
            default_condition_descriptor_value_id=default_condition_descriptor_value_id,
            max_length=max_length,
            mode=mode,
            usage=usage,
        )

        item_condition_descriptor_constraint.additional_properties = d
        return item_condition_descriptor_constraint

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
