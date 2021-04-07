# coding: utf-8

"""
     Seller Service Metrics API 

    The Analytics API provides data and information about a seller and their eBay business. The resources and methods in this API let sellers review information on their listing performance, metrics on their customer service performance, and details on their eBay seller performance rating. The three resources in the Analytics API provide the following data and information: Customer Service Metric &ndash; Returns data on a seller's customer service performance as compared to other seller's in the same peer group. Traffic Report &ndash; Returns data that shows how buyers are engaging with a seller's listings. Seller Standards Profile &ndash; Returns data pertaining to a seller's performance rating. Sellers can use the data and information returned by the various Analytics API methods to determine where they can make improvements to increase sales and how they might improve their seller status as viewed by eBay buyers. For details on using this API, see Analyzing seller performance.

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Error(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, category=None, domain=None, error_id=None, input_ref_ids=None, long_message=None, message=None, output_ref_ids=None, parameters=None, subdomain=None):
        """
        Error - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category': 'str',
            'domain': 'str',
            'error_id': 'int',
            'input_ref_ids': 'list[str]',
            'long_message': 'str',
            'message': 'str',
            'output_ref_ids': 'list[str]',
            'parameters': 'list[ErrorParameter]',
            'subdomain': 'str'
        }

        self.attribute_map = {
            'category': 'category',
            'domain': 'domain',
            'error_id': 'errorId',
            'input_ref_ids': 'inputRefIds',
            'long_message': 'longMessage',
            'message': 'message',
            'output_ref_ids': 'outputRefIds',
            'parameters': 'parameters',
            'subdomain': 'subdomain'
        }

        self._category = category
        self._domain = domain
        self._error_id = error_id
        self._input_ref_ids = input_ref_ids
        self._long_message = long_message
        self._message = message
        self._output_ref_ids = output_ref_ids
        self._parameters = parameters
        self._subdomain = subdomain

    @property
    def category(self):
        """
        Gets the category of this Error.
        Identifies whether the error was in the REQUEST or happened when running the APPLICATION.

        :return: The category of this Error.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Error.
        Identifies whether the error was in the REQUEST or happened when running the APPLICATION.

        :param category: The category of this Error.
        :type: str
        """

        self._category = category

    @property
    def domain(self):
        """
        Gets the domain of this Error.
        The primary system where the error occurred. This is relevant for application errors. For Analytics errors, it always has the value API_ANALYTICS.

        :return: The domain of this Error.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this Error.
        The primary system where the error occurred. This is relevant for application errors. For Analytics errors, it always has the value API_ANALYTICS.

        :param domain: The domain of this Error.
        :type: str
        """

        self._domain = domain

    @property
    def error_id(self):
        """
        Gets the error_id of this Error.
        A positive integer that uniquely identifies the specific error condition that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms. Traffic report error IDs range from 50001 to 50500.

        :return: The error_id of this Error.
        :rtype: int
        """
        return self._error_id

    @error_id.setter
    def error_id(self, error_id):
        """
        Sets the error_id of this Error.
        A positive integer that uniquely identifies the specific error condition that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms. Traffic report error IDs range from 50001 to 50500.

        :param error_id: The error_id of this Error.
        :type: int
        """

        self._error_id = error_id

    @property
    def input_ref_ids(self):
        """
        Gets the input_ref_ids of this Error.
        Identifies specific request elements associated with the error, if any. inputRefId's response is format specific. For JSON, use JSONPath notation.

        :return: The input_ref_ids of this Error.
        :rtype: list[str]
        """
        return self._input_ref_ids

    @input_ref_ids.setter
    def input_ref_ids(self, input_ref_ids):
        """
        Sets the input_ref_ids of this Error.
        Identifies specific request elements associated with the error, if any. inputRefId's response is format specific. For JSON, use JSONPath notation.

        :param input_ref_ids: The input_ref_ids of this Error.
        :type: list[str]
        """

        self._input_ref_ids = input_ref_ids

    @property
    def long_message(self):
        """
        Gets the long_message of this Error.
        A more detailed explanation of the error than given in the message error field.

        :return: The long_message of this Error.
        :rtype: str
        """
        return self._long_message

    @long_message.setter
    def long_message(self, long_message):
        """
        Sets the long_message of this Error.
        A more detailed explanation of the error than given in the message error field.

        :param long_message: The long_message of this Error.
        :type: str
        """

        self._long_message = long_message

    @property
    def message(self):
        """
        Gets the message of this Error.
        Information on how to correct the problem, in the end user's terms and language where applicable. Its value is at most 50 characters long. If applicable, the value is localized in the end user's requested locale.

        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Error.
        Information on how to correct the problem, in the end user's terms and language where applicable. Its value is at most 50 characters long. If applicable, the value is localized in the end user's requested locale.

        :param message: The message of this Error.
        :type: str
        """

        self._message = message

    @property
    def output_ref_ids(self):
        """
        Gets the output_ref_ids of this Error.
        Identifies specific response elements associated with the error, if any. Path format is the same as inputRefId.

        :return: The output_ref_ids of this Error.
        :rtype: list[str]
        """
        return self._output_ref_ids

    @output_ref_ids.setter
    def output_ref_ids(self, output_ref_ids):
        """
        Sets the output_ref_ids of this Error.
        Identifies specific response elements associated with the error, if any. Path format is the same as inputRefId.

        :param output_ref_ids: The output_ref_ids of this Error.
        :type: list[str]
        """

        self._output_ref_ids = output_ref_ids

    @property
    def parameters(self):
        """
        Gets the parameters of this Error.
        This optional list of name/value pairs that contain context-specific ErrorParameter objects, with each item in the list being a parameter (or input field name) that caused an error condition. Each ErrorParameter object consists of two fields, a name and a value.

        :return: The parameters of this Error.
        :rtype: list[ErrorParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this Error.
        This optional list of name/value pairs that contain context-specific ErrorParameter objects, with each item in the list being a parameter (or input field name) that caused an error condition. Each ErrorParameter object consists of two fields, a name and a value.

        :param parameters: The parameters of this Error.
        :type: list[ErrorParameter]
        """

        self._parameters = parameters

    @property
    def subdomain(self):
        """
        Gets the subdomain of this Error.
        If present, indicates which subsystem in which the error occurred.

        :return: The subdomain of this Error.
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """
        Sets the subdomain of this Error.
        If present, indicates which subsystem in which the error occurred.

        :param subdomain: The subdomain of this Error.
        :type: str
        """

        self._subdomain = subdomain

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other