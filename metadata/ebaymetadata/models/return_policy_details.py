from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_duration import TimeDuration


T = TypeVar("T", bound="ReturnPolicyDetails")


@_attrs_define
class ReturnPolicyDetails:
    """This container defines the category policies that relate to domestic and international return policies (the return
    shipping is made via a domestic or an international shipping service, respectively).

        Attributes:
            policy_description_enabled (Union[Unset, bool]): If set to <code>true</code>, this flag indicates you can supply
                a detailed return policy description within your return policy (for example, by populating the
                <b>returnInstructions</b> field in the Account API's <b>createReturnPolicy</b>). User-supplied return policy
                details are allowed only in the DE, ES, FR, and IT marketplaces.
            refund_methods (Union[Unset, List[str]]): A list of refund methods allowed for the associated category.
            return_methods (Union[Unset, List[str]]): A list of return methods allowed for the associated category.
            return_periods (Union[Unset, List['TimeDuration']]): A list of return periods allowed for the associated
                category.  <br><br>Note that different APIs require you to enter the return period in different ways. For
                example, the Account API uses the complex <b>TimeDuration</b> type, which takes two values (a <b>unit</b> and a
                <b>value</b>), whereas the Trading API takes a single value (such as <code>Days_30</code>).
            returns_acceptance_enabled (Union[Unset, bool]): If set to <code>true</code>, this flag indicates the seller can
                configure how they handle domestic returns.
            return_shipping_cost_payers (Union[Unset, List[str]]): A list of allowed values for who pays for the return
                shipping cost.  <br><br>Note that for SNAD returns, the seller is always responsible for the return shipping
                cost.
    """

    policy_description_enabled: Union[Unset, bool] = UNSET
    refund_methods: Union[Unset, List[str]] = UNSET
    return_methods: Union[Unset, List[str]] = UNSET
    return_periods: Union[Unset, List["TimeDuration"]] = UNSET
    returns_acceptance_enabled: Union[Unset, bool] = UNSET
    return_shipping_cost_payers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        policy_description_enabled = self.policy_description_enabled

        refund_methods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.refund_methods, Unset):
            refund_methods = self.refund_methods

        return_methods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.return_methods, Unset):
            return_methods = self.return_methods

        return_periods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.return_periods, Unset):
            return_periods = []
            for return_periods_item_data in self.return_periods:
                return_periods_item = return_periods_item_data.to_dict()
                return_periods.append(return_periods_item)

        returns_acceptance_enabled = self.returns_acceptance_enabled

        return_shipping_cost_payers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.return_shipping_cost_payers, Unset):
            return_shipping_cost_payers = self.return_shipping_cost_payers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy_description_enabled is not UNSET:
            field_dict["policyDescriptionEnabled"] = policy_description_enabled
        if refund_methods is not UNSET:
            field_dict["refundMethods"] = refund_methods
        if return_methods is not UNSET:
            field_dict["returnMethods"] = return_methods
        if return_periods is not UNSET:
            field_dict["returnPeriods"] = return_periods
        if returns_acceptance_enabled is not UNSET:
            field_dict["returnsAcceptanceEnabled"] = returns_acceptance_enabled
        if return_shipping_cost_payers is not UNSET:
            field_dict["returnShippingCostPayers"] = return_shipping_cost_payers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.time_duration import TimeDuration

        d = src_dict.copy()
        policy_description_enabled = d.pop("policyDescriptionEnabled", UNSET)

        refund_methods = cast(List[str], d.pop("refundMethods", UNSET))

        return_methods = cast(List[str], d.pop("returnMethods", UNSET))

        return_periods = []
        _return_periods = d.pop("returnPeriods", UNSET)
        for return_periods_item_data in _return_periods or []:
            return_periods_item = TimeDuration.from_dict(return_periods_item_data)

            return_periods.append(return_periods_item)

        returns_acceptance_enabled = d.pop("returnsAcceptanceEnabled", UNSET)

        return_shipping_cost_payers = cast(List[str], d.pop("returnShippingCostPayers", UNSET))

        return_policy_details = cls(
            policy_description_enabled=policy_description_enabled,
            refund_methods=refund_methods,
            return_methods=return_methods,
            return_periods=return_periods,
            returns_acceptance_enabled=returns_acceptance_enabled,
            return_shipping_cost_payers=return_shipping_cost_payers,
        )

        return_policy_details.additional_properties = d
        return return_policy_details

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
