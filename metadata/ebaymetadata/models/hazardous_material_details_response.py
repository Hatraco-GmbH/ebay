from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hazard_statement import HazardStatement
    from ..models.pictogram import Pictogram
    from ..models.signal_word import SignalWord


T = TypeVar("T", bound="HazardousMaterialDetailsResponse")


@_attrs_define
class HazardousMaterialDetailsResponse:
    """A type that defines the response fields for the <b>getHazardousMaterialsLabels</b> method.

    Attributes:
        signal_words (Union[Unset, List['SignalWord']]): This array contains available hazardous materials signal words
            for the specified marketplace.
        statements (Union[Unset, List['HazardStatement']]): This array contains available hazardous materials hazard
            statements for the specified marketplace.
        pictograms (Union[Unset, List['Pictogram']]): This array contains available hazardous materials hazard
            pictograms for the specified marketplace.
    """

    signal_words: Union[Unset, List["SignalWord"]] = UNSET
    statements: Union[Unset, List["HazardStatement"]] = UNSET
    pictograms: Union[Unset, List["Pictogram"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        signal_words: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.signal_words, Unset):
            signal_words = []
            for signal_words_item_data in self.signal_words:
                signal_words_item = signal_words_item_data.to_dict()
                signal_words.append(signal_words_item)

        statements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.statements, Unset):
            statements = []
            for statements_item_data in self.statements:
                statements_item = statements_item_data.to_dict()
                statements.append(statements_item)

        pictograms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pictograms, Unset):
            pictograms = []
            for pictograms_item_data in self.pictograms:
                pictograms_item = pictograms_item_data.to_dict()
                pictograms.append(pictograms_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signal_words is not UNSET:
            field_dict["signalWords"] = signal_words
        if statements is not UNSET:
            field_dict["statements"] = statements
        if pictograms is not UNSET:
            field_dict["pictograms"] = pictograms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hazard_statement import HazardStatement
        from ..models.pictogram import Pictogram
        from ..models.signal_word import SignalWord

        d = src_dict.copy()
        signal_words = []
        _signal_words = d.pop("signalWords", UNSET)
        for signal_words_item_data in _signal_words or []:
            signal_words_item = SignalWord.from_dict(signal_words_item_data)

            signal_words.append(signal_words_item)

        statements = []
        _statements = d.pop("statements", UNSET)
        for statements_item_data in _statements or []:
            statements_item = HazardStatement.from_dict(statements_item_data)

            statements.append(statements_item)

        pictograms = []
        _pictograms = d.pop("pictograms", UNSET)
        for pictograms_item_data in _pictograms or []:
            pictograms_item = Pictogram.from_dict(pictograms_item_data)

            pictograms.append(pictograms_item)

        hazardous_material_details_response = cls(
            signal_words=signal_words,
            statements=statements,
            pictograms=pictograms,
        )

        hazardous_material_details_response.additional_properties = d
        return hazardous_material_details_response

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
