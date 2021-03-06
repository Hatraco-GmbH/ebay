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
from ebayinventory.api.location_api import LocationApi  # noqa: E501
from ebayinventory.rest import ApiException


class TestLocationApi(unittest.TestCase):
    """LocationApi unit test stubs"""

    def setUp(self):
        self.api = LocationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_inventory_location(self):
        """Test case for create_inventory_location

        """
        pass

    def test_delete_inventory_location(self):
        """Test case for delete_inventory_location

        """
        pass

    def test_disable_inventory_location(self):
        """Test case for disable_inventory_location

        """
        pass

    def test_enable_inventory_location(self):
        """Test case for enable_inventory_location

        """
        pass

    def test_get_inventory_location(self):
        """Test case for get_inventory_location

        """
        pass

    def test_get_inventory_locations(self):
        """Test case for get_inventory_locations

        """
        pass

    def test_update_inventory_location(self):
        """Test case for update_inventory_location

        """
        pass


if __name__ == '__main__':
    unittest.main()
