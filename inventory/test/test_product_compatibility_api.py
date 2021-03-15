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
from ebayinventory.api.product_compatibility_api import ProductCompatibilityApi  # noqa: E501
from ebayinventory.rest import ApiException


class TestProductCompatibilityApi(unittest.TestCase):
    """ProductCompatibilityApi unit test stubs"""

    def setUp(self):
        self.api = ProductCompatibilityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_or_replace_product_compatibility(self):
        """Test case for create_or_replace_product_compatibility

        """
        pass

    def test_delete_product_compatibility(self):
        """Test case for delete_product_compatibility

        """
        pass

    def test_get_product_compatibility(self):
        """Test case for get_product_compatibility

        """
        pass


if __name__ == '__main__':
    unittest.main()