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
from ebayfinance.api.transfer_api import TransferApi  # noqa: E501
from ebayfinance.rest import ApiException


class TestTransferApi(unittest.TestCase):
    """TransferApi unit test stubs"""

    def setUp(self):
        self.api = TransferApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_transfer(self):
        """Test case for get_transfer

        """
        pass


if __name__ == '__main__':
    unittest.main()
