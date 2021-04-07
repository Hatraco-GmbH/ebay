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


class Metric(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, benchmark=None, distributions=None, metric_key=None, value=None):
        """
        Metric - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'benchmark': 'MetricBenchmark',
            'distributions': 'list[MetricDistribution]',
            'metric_key': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'benchmark': 'benchmark',
            'distributions': 'distributions',
            'metric_key': 'metricKey',
            'value': 'value'
        }

        self._benchmark = benchmark
        self._distributions = distributions
        self._metric_key = metric_key
        self._value = value

    @property
    def benchmark(self):
        """
        Gets the benchmark of this Metric.


        :return: The benchmark of this Metric.
        :rtype: MetricBenchmark
        """
        return self._benchmark

    @benchmark.setter
    def benchmark(self, benchmark):
        """
        Sets the benchmark of this Metric.


        :param benchmark: The benchmark of this Metric.
        :type: MetricBenchmark
        """

        self._benchmark = benchmark

    @property
    def distributions(self):
        """
        Gets the distributions of this Metric.
        Returned when metricKey equals COUNT, this field returns an array of seller data where each set of data is grouped according by an overarching basis. When the seller distribution is returned, the numeric value of the associated value container equals the sum of the transactions where the seller meets the criteria of the customer service metric type for the given dimension during the evaluationCycle.

        :return: The distributions of this Metric.
        :rtype: list[MetricDistribution]
        """
        return self._distributions

    @distributions.setter
    def distributions(self, distributions):
        """
        Sets the distributions of this Metric.
        Returned when metricKey equals COUNT, this field returns an array of seller data where each set of data is grouped according by an overarching basis. When the seller distribution is returned, the numeric value of the associated value container equals the sum of the transactions where the seller meets the criteria of the customer service metric type for the given dimension during the evaluationCycle.

        :param distributions: The distributions of this Metric.
        :type: list[MetricDistribution]
        """

        self._distributions = distributions

    @property
    def metric_key(self):
        """
        Gets the metric_key of this Metric.
        This field indicates the customer service metric being returned in the associated metrics container. The field is set as follows: TRANSACTION_COUNT &ndash; When set to this value, the associated value field equals the total number of transactions completed in the seller group for the metric in the given dimension during the associated evaluationCycle. COUNT &ndash; When set to this value, the associated value field is set to the total number of transactions the seller completed that meet the criteria of the customer service metric type for the given dimension that occurred during the evaluationCycle. RATE &ndash; When set to this value, the value of the associated value field is the rate of the customer service metric type in the given dimension during the associated evaluationCycle. Specifically, when metricKey is set to RATE, the associated value field is set to the value of metricKey TRANSACTION_COUNT divided by the value of metricKey COUNT. The returned benchmark.rating for the seller is based on this calculated value.

        :return: The metric_key of this Metric.
        :rtype: str
        """
        return self._metric_key

    @metric_key.setter
    def metric_key(self, metric_key):
        """
        Sets the metric_key of this Metric.
        This field indicates the customer service metric being returned in the associated metrics container. The field is set as follows: TRANSACTION_COUNT &ndash; When set to this value, the associated value field equals the total number of transactions completed in the seller group for the metric in the given dimension during the associated evaluationCycle. COUNT &ndash; When set to this value, the associated value field is set to the total number of transactions the seller completed that meet the criteria of the customer service metric type for the given dimension that occurred during the evaluationCycle. RATE &ndash; When set to this value, the value of the associated value field is the rate of the customer service metric type in the given dimension during the associated evaluationCycle. Specifically, when metricKey is set to RATE, the associated value field is set to the value of metricKey TRANSACTION_COUNT divided by the value of metricKey COUNT. The returned benchmark.rating for the seller is based on this calculated value.

        :param metric_key: The metric_key of this Metric.
        :type: str
        """

        self._metric_key = metric_key

    @property
    def value(self):
        """
        Gets the value of this Metric.
        This field is set to the seller's numeric rating for the associated metricKey for the given dimension during the evaluationCycle. To determine the seller's rating for this metric, the value of this field is compared to the average metric value of the group.

        :return: The value of this Metric.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Metric.
        This field is set to the seller's numeric rating for the associated metricKey for the given dimension during the evaluationCycle. To determine the seller's rating for this metric, the value of this field is compared to the average metric value of the group.

        :param value: The value of this Metric.
        :type: str
        """

        self._value = value

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
