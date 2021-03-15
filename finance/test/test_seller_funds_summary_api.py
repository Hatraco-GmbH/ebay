# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: 1.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import ebayfinance
from ebayfinance.api.seller_funds_summary_api import SellerFundsSummaryApi  # noqa: E501
from ebayfinance.rest import ApiException


class TestSellerFundsSummaryApi(unittest.TestCase):
    """SellerFundsSummaryApi unit test stubs"""

    def setUp(self):
        self.api = SellerFundsSummaryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_seller_funds_summary(self):
        """Test case for get_seller_funds_summary

        """
        pass


if __name__ == '__main__':
    unittest.main()