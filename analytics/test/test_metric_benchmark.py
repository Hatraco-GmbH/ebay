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

from __future__ import absolute_import

import os
import sys
import unittest

import ebayanalytics
from ebayanalytics.rest import ApiException
from ebayanalytics.models.metric_benchmark import MetricBenchmark


class TestMetricBenchmark(unittest.TestCase):
    """ MetricBenchmark unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricBenchmark(self):
        """
        Test MetricBenchmark
        """
        model = ebayanalytics.models.metric_benchmark.MetricBenchmark()


if __name__ == '__main__':
    unittest.main()
