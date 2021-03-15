# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import ebayfulfillment
from ebayfulfillment.models.monetary_transaction import MonetaryTransaction  # noqa: E501
from ebayfulfillment.rest import ApiException


class TestMonetaryTransaction(unittest.TestCase):
    """MonetaryTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonetaryTransaction(self):
        """Test MonetaryTransaction"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ebayfulfillment.models.monetary_transaction.MonetaryTransaction()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()