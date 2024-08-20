from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extended_producer_responsibility import ExtendedProducerResponsibility


T = TypeVar("T", bound="ExtendedProducerResponsibilityPolicy")


@_attrs_define
class ExtendedProducerResponsibilityPolicy:
    """A type that defines the Extended Producer Responsibility policy.

    Attributes:
        category_id (Union[Unset, str]): The unique identifier for the category under which the policy applies.
        category_tree_id (Union[Unset, str]): The unique identifier for the category tree under which the policy
            applies.
        supported_attributes (Union[Unset, List['ExtendedProducerResponsibility']]): The details regarding the
            attributes included in the policy, such as their usage guidelines and whether they can be specified at the
            listing variation level.
    """

    category_id: Union[Unset, str] = UNSET
    category_tree_id: Union[Unset, str] = UNSET
    supported_attributes: Union[Unset, List["ExtendedProducerResponsibility"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category_id = self.category_id

        category_tree_id = self.category_tree_id

        supported_attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.supported_attributes, Unset):
            supported_attributes = []
            for supported_attributes_item_data in self.supported_attributes:
                supported_attributes_item = supported_attributes_item_data.to_dict()
                supported_attributes.append(supported_attributes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_tree_id is not UNSET:
            field_dict["categoryTreeId"] = category_tree_id
        if supported_attributes is not UNSET:
            field_dict["supportedAttributes"] = supported_attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.extended_producer_responsibility import ExtendedProducerResponsibility

        d = src_dict.copy()
        category_id = d.pop("categoryId", UNSET)

        category_tree_id = d.pop("categoryTreeId", UNSET)

        supported_attributes = []
        _supported_attributes = d.pop("supportedAttributes", UNSET)
        for supported_attributes_item_data in _supported_attributes or []:
            supported_attributes_item = ExtendedProducerResponsibility.from_dict(supported_attributes_item_data)

            supported_attributes.append(supported_attributes_item)

        extended_producer_responsibility_policy = cls(
            category_id=category_id,
            category_tree_id=category_tree_id,
            supported_attributes=supported_attributes,
        )

        extended_producer_responsibility_policy.additional_properties = d
        return extended_producer_responsibility_policy

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
