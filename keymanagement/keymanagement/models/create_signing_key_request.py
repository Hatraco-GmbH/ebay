# coding: utf-8

"""
    Key Management API

    Due to regulatory requirements applicable to our EU/UK sellers, for certain APIs, developers need to add digital signatures to the respective HTTP call. The Key Management API creates keypairs that are required when creating digital signatures for the following APIs:<ul><li>All methods in the <a href=\"/api-docs/sell/finances/resources/methods \" target=\"_blank \">Finances API</a></li><li><a href=\"/api-docs/sell/fulfillment/resources/order/methods/issueRefund \" target=\"_blank \">issueRefund</a> in the Fulfillment API</li><li><a href=\"/Devzone/XML/docs/Reference/eBay/GetAccount.html \" target=\"_blank \">GetAccount</a> in the Trading API</li><li>The following methods in the Post-Order API:<ul><li><a href=\"/Devzone/post-order/post-order_v2_inquiry-inquiryid_issue_refund__post.html \" target=\"_blank \">Issue Inquiry Refund</a></li><li><a href=\"/Devzone/post-order/post-order_v2_casemanagement-caseid_issue_refund__post.html \" target=\"_blank \">Issue case refund</a></li><li><a href=\"/Devzone/post-order/post-order_v2_return-returnid_issue_refund__post.html \" target=\"_blank \">Issue return refund</a></li><li><a href=\"/Devzone/post-order/post-order_v2_return-returnid_decide__post.html \" target=\"_blank \">Process Return Request</a></li><li><a href=\"/devzone/post-order/post-order_v2_cancellation-cancelid_approve__post.html \" target=\"_blank \">Approve Cancellation Request</a></li><li><a href=\"/devzone/post-order/post-order_v2_cancellation__post.html \" target=\"_blank \">Create Cancellation Request</a></li></ul></li></ul><span class=\"tablenote\"><b>Note:</b> For additional information about keypairs and creating Message Signatures, refer to <a href= \"/develop/guides/digital-signatures-for-apis \" target= \"_blank \">Digital Signatures for APIs</a>.</span>  # noqa: E501

    OpenAPI spec version: v1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from keymanagement.configuration import Configuration


class CreateSigningKeyRequest(object):
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
        'signing_key_cipher': 'str'
    }

    attribute_map = {
        'signing_key_cipher': 'signingKeyCipher'
    }

    def __init__(self, signing_key_cipher=None, _configuration=None):  # noqa: E501
        """CreateSigningKeyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._signing_key_cipher = None
        self.discriminator = None

        if signing_key_cipher is not None:
            self.signing_key_cipher = signing_key_cipher

    @property
    def signing_key_cipher(self):
        """Gets the signing_key_cipher of this CreateSigningKeyRequest.  # noqa: E501

        The enumerated value for the cipher to be used to create the signing key. Refer to <a href= \"/api-docs/developer/key-management/types/api:SigningKeyCipher\" target= \"_blank\">SigningKeyCiper</a> for the list of supported enum values. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/developer/key_management/types/api:SigningKeyCipher'>eBay API documentation</a>  # noqa: E501

        :return: The signing_key_cipher of this CreateSigningKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._signing_key_cipher

    @signing_key_cipher.setter
    def signing_key_cipher(self, signing_key_cipher):
        """Sets the signing_key_cipher of this CreateSigningKeyRequest.

        The enumerated value for the cipher to be used to create the signing key. Refer to <a href= \"/api-docs/developer/key-management/types/api:SigningKeyCipher\" target= \"_blank\">SigningKeyCiper</a> for the list of supported enum values. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/developer/key_management/types/api:SigningKeyCipher'>eBay API documentation</a>  # noqa: E501

        :param signing_key_cipher: The signing_key_cipher of this CreateSigningKeyRequest.  # noqa: E501
        :type: str
        """

        self._signing_key_cipher = signing_key_cipher

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
        if issubclass(CreateSigningKeyRequest, dict):
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
        if not isinstance(other, CreateSigningKeyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSigningKeyRequest):
            return True

        return self.to_dict() != other.to_dict()
