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


class DimensionMetric(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, dimension=None, metrics=None):
        """
        DimensionMetric - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'dimension': 'Dimension',
            'metrics': 'list[Metric]'
        }

        self.attribute_map = {
            'dimension': 'dimension',
            'metrics': 'metrics'
        }

        self._dimension = dimension
        self._metrics = metrics

    @property
    def dimension(self):
        """
        Gets the dimension of this DimensionMetric.


        :return: The dimension of this DimensionMetric.
        :rtype: Dimension
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """
        Sets the dimension of this DimensionMetric.


        :param dimension: The dimension of this DimensionMetric.
        :type: Dimension
        """

        self._dimension = dimension

    @property
    def metrics(self):
        """
        Gets the metrics of this DimensionMetric.
        This is a list of Metric elements where each element contains data and information related to the transactions grouped by the associated dimension.

        :return: The metrics of this DimensionMetric.
        :rtype: list[Metric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this DimensionMetric.
        This is a list of Metric elements where each element contains data and information related to the transactions grouped by the associated dimension.

        :param metrics: The metrics of this DimensionMetric.
        :type: list[Metric]
        """

        self._metrics = metrics

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
