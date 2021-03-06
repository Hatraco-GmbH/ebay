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
from ebayfinance.api.payout_api import PayoutApi  # noqa: E501
from ebayfinance.rest import ApiException


class TestPayoutApi(unittest.TestCase):
    """PayoutApi unit test stubs"""

    def setUp(self):
        self.api = PayoutApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_payout(self):
        """Test case for get_payout

        """
        pass

    def test_get_payout_summary(self):
        """Test case for get_payout_summary

        """
        pass

    def test_get_payouts(self):
        """Test case for get_payouts

        """
        pass


if __name__ == '__main__':
    unittest.main()
