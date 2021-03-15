# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: 1.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SellerFundsSummaryResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'available_funds': 'Amount',
        'funds_on_hold': 'Amount',
        'processing_funds': 'Amount',
        'total_funds': 'Amount'
    }

    attribute_map = {
        'available_funds': 'availableFunds',
        'funds_on_hold': 'fundsOnHold',
        'processing_funds': 'processingFunds',
        'total_funds': 'totalFunds'
    }

    def __init__(self, available_funds=None, funds_on_hold=None, processing_funds=None, total_funds=None):  # noqa: E501
        """SellerFundsSummaryResponse - a model defined in Swagger"""  # noqa: E501
        self._available_funds = None
        self._funds_on_hold = None
        self._processing_funds = None
        self._total_funds = None
        self.discriminator = None
        if available_funds is not None:
            self.available_funds = available_funds
        if funds_on_hold is not None:
            self.funds_on_hold = funds_on_hold
        if processing_funds is not None:
            self.processing_funds = processing_funds
        if total_funds is not None:
            self.total_funds = total_funds

    @property
    def available_funds(self):
        """Gets the available_funds of this SellerFundsSummaryResponse.  # noqa: E501


        :return: The available_funds of this SellerFundsSummaryResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._available_funds

    @available_funds.setter
    def available_funds(self, available_funds):
        """Sets the available_funds of this SellerFundsSummaryResponse.


        :param available_funds: The available_funds of this SellerFundsSummaryResponse.  # noqa: E501
        :type: Amount
        """

        self._available_funds = available_funds

    @property
    def funds_on_hold(self):
        """Gets the funds_on_hold of this SellerFundsSummaryResponse.  # noqa: E501


        :return: The funds_on_hold of this SellerFundsSummaryResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._funds_on_hold

    @funds_on_hold.setter
    def funds_on_hold(self, funds_on_hold):
        """Sets the funds_on_hold of this SellerFundsSummaryResponse.


        :param funds_on_hold: The funds_on_hold of this SellerFundsSummaryResponse.  # noqa: E501
        :type: Amount
        """

        self._funds_on_hold = funds_on_hold

    @property
    def processing_funds(self):
        """Gets the processing_funds of this SellerFundsSummaryResponse.  # noqa: E501


        :return: The processing_funds of this SellerFundsSummaryResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._processing_funds

    @processing_funds.setter
    def processing_funds(self, processing_funds):
        """Sets the processing_funds of this SellerFundsSummaryResponse.


        :param processing_funds: The processing_funds of this SellerFundsSummaryResponse.  # noqa: E501
        :type: Amount
        """

        self._processing_funds = processing_funds

    @property
    def total_funds(self):
        """Gets the total_funds of this SellerFundsSummaryResponse.  # noqa: E501


        :return: The total_funds of this SellerFundsSummaryResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._total_funds

    @total_funds.setter
    def total_funds(self, total_funds):
        """Sets the total_funds of this SellerFundsSummaryResponse.


        :param total_funds: The total_funds of this SellerFundsSummaryResponse.  # noqa: E501
        :type: Amount
        """

        self._total_funds = total_funds

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SellerFundsSummaryResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SellerFundsSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
