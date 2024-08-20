from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_parameter import ErrorParameter


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """A container that defines the elements of error and warning messages.

    Attributes:
        category (Union[Unset, str]): The category type for this error or warning. It takes an ErrorCategory object
            which can have one of three values:<ul><li><code>Application</code>: Indicates an exception or error occurred in
            the application code or at runtime. Examples include catching an exception in a service's business logic, system
            failures, or request errors from a dependency.</li><li><code>Business</code>: Used when your service or a
            dependent service refused to continue processing on the resource because of a business rule violation such as
            "Seller does not ship item to Antarctica" or "Buyer ineligible to purchase an alcoholic item". Business errors
            are not syntactical input errors.</li><li><code>Request</code>: Used when there is anything wrong with the
            request, such as authentication, syntactical errors, rate limiting or missing headers, bad HTTP header values,
            and so on.</li></ul>
        domain (Union[Unset, str]): Name of the domain containing the service or application.
        error_id (Union[Unset, int]): A positive integer that uniquely identifies the specific error condition that
            occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.
        input_ref_ids (Union[Unset, List[str]]): Identifies specific request elements associated with the error, if any.
            inputRefId's response is format specific. For JSON, use <i>JSONPath</i> notation.
        long_message (Union[Unset, str]): An expanded version of message that should be around 100-200 characters long,
            but is not required to be such.
        message (Union[Unset, str]): An end user and app developer friendly device agnostic message. It explains what
            the error or warning is, and how to fix it (in a general sense). Its value is at most 50 characters long. If
            applicable, the value is localized in the end user's requested locale.
        output_ref_ids (Union[Unset, List[str]]): Identifies specific response elements associated with the error, if
            any. Path format is the same as <code>inputRefId</code>.
        parameters (Union[Unset, List['ErrorParameter']]): This optional complex field type contains a list of one or
            more context-specific <code>ErrorParameter</code> objects, with each item in the list entry being a parameter
            (or input field name) that caused an error condition. Each <code>ErrorParameter</code> object consists of two
            fields, a <code>name</code> and a <code>value</code>.
        subdomain (Union[Unset, str]): Name of the domain's subsystem or subdivision. For example, checkout is a
            subdomain in the buying domain.
    """

    category: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    error_id: Union[Unset, int] = UNSET
    input_ref_ids: Union[Unset, List[str]] = UNSET
    long_message: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    output_ref_ids: Union[Unset, List[str]] = UNSET
    parameters: Union[Unset, List["ErrorParameter"]] = UNSET
    subdomain: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category

        domain = self.domain

        error_id = self.error_id

        input_ref_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.input_ref_ids, Unset):
            input_ref_ids = self.input_ref_ids

        long_message = self.long_message

        message = self.message

        output_ref_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.output_ref_ids, Unset):
            output_ref_ids = self.output_ref_ids

        parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        subdomain = self.subdomain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if domain is not UNSET:
            field_dict["domain"] = domain
        if error_id is not UNSET:
            field_dict["errorId"] = error_id
        if input_ref_ids is not UNSET:
            field_dict["inputRefIds"] = input_ref_ids
        if long_message is not UNSET:
            field_dict["longMessage"] = long_message
        if message is not UNSET:
            field_dict["message"] = message
        if output_ref_ids is not UNSET:
            field_dict["outputRefIds"] = output_ref_ids
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if subdomain is not UNSET:
            field_dict["subdomain"] = subdomain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_parameter import ErrorParameter

        d = src_dict.copy()
        category = d.pop("category", UNSET)

        domain = d.pop("domain", UNSET)

        error_id = d.pop("errorId", UNSET)

        input_ref_ids = cast(List[str], d.pop("inputRefIds", UNSET))

        long_message = d.pop("longMessage", UNSET)

        message = d.pop("message", UNSET)

        output_ref_ids = cast(List[str], d.pop("outputRefIds", UNSET))

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = ErrorParameter.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        subdomain = d.pop("subdomain", UNSET)

        error = cls(
            category=category,
            domain=domain,
            error_id=error_id,
            input_ref_ids=input_ref_ids,
            long_message=long_message,
            message=message,
            output_ref_ids=output_ref_ids,
            parameters=parameters,
            subdomain=subdomain,
        )

        error.additional_properties = d
        return error

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
