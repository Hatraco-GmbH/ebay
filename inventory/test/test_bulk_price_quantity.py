# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import ebayinventory
from ebayinventory.models.bulk_price_quantity import BulkPriceQuantity  # noqa: E501
from ebayinventory.rest import ApiException


class TestBulkPriceQuantity(unittest.TestCase):
    """BulkPriceQuantity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBulkPriceQuantity(self):
        """Test BulkPriceQuantity"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ebayinventory.models.bulk_price_quantity.BulkPriceQuantity()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
