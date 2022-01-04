# coding: utf-8

"""
    Taxonomy API

    Use the Taxonomy API to discover the most appropriate eBay categories under which sellers can offer inventory items for sale, and the most likely categories under which buyers can browse or search for items to purchase. In addition, the Taxonomy API provides metadata about the required and recommended category aspects to include in listings, and also has two operations to retrieve parts compatibility information.

    OpenAPI spec version: v1.0.0
    
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


class CategorySuggestion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, category=None, category_tree_node_ancestors=None, category_tree_node_level=None, relevancy=None):
        """
        CategorySuggestion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category': 'Category',
            'category_tree_node_ancestors': 'list[AncestorReference]',
            'category_tree_node_level': 'int',
            'relevancy': 'str'
        }

        self.attribute_map = {
            'category': 'category',
            'category_tree_node_ancestors': 'categoryTreeNodeAncestors',
            'category_tree_node_level': 'categoryTreeNodeLevel',
            'relevancy': 'relevancy'
        }

        self._category = category
        self._category_tree_node_ancestors = category_tree_node_ancestors
        self._category_tree_node_level = category_tree_node_level
        self._relevancy = relevancy

    @property
    def category(self):
        """
        Gets the category of this CategorySuggestion.


        :return: The category of this CategorySuggestion.
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this CategorySuggestion.


        :param category: The category of this CategorySuggestion.
        :type: Category
        """

        self._category = category

    @property
    def category_tree_node_ancestors(self):
        """
        Gets the category_tree_node_ancestors of this CategorySuggestion.
        An ordered list of category references that describes the location of the suggested category in the specified category tree. The list identifies the category's ancestry as a sequence of parent nodes, from the current node's immediate parent to the root node of the category tree. Note: The root node of a full default category tree includes categoryId and categoryName fields, but their values should not be relied upon. They provide no useful information for application development.

        :return: The category_tree_node_ancestors of this CategorySuggestion.
        :rtype: list[AncestorReference]
        """
        return self._category_tree_node_ancestors

    @category_tree_node_ancestors.setter
    def category_tree_node_ancestors(self, category_tree_node_ancestors):
        """
        Sets the category_tree_node_ancestors of this CategorySuggestion.
        An ordered list of category references that describes the location of the suggested category in the specified category tree. The list identifies the category's ancestry as a sequence of parent nodes, from the current node's immediate parent to the root node of the category tree. Note: The root node of a full default category tree includes categoryId and categoryName fields, but their values should not be relied upon. They provide no useful information for application development.

        :param category_tree_node_ancestors: The category_tree_node_ancestors of this CategorySuggestion.
        :type: list[AncestorReference]
        """

        self._category_tree_node_ancestors = category_tree_node_ancestors

    @property
    def category_tree_node_level(self):
        """
        Gets the category_tree_node_level of this CategorySuggestion.
        The absolute level of the category tree node in the hierarchy of its category tree. Note: The root node of any full category tree is always at level 0.

        :return: The category_tree_node_level of this CategorySuggestion.
        :rtype: int
        """
        return self._category_tree_node_level

    @category_tree_node_level.setter
    def category_tree_node_level(self, category_tree_node_level):
        """
        Sets the category_tree_node_level of this CategorySuggestion.
        The absolute level of the category tree node in the hierarchy of its category tree. Note: The root node of any full category tree is always at level 0.

        :param category_tree_node_level: The category_tree_node_level of this CategorySuggestion.
        :type: int
        """

        self._category_tree_node_level = category_tree_node_level

    @property
    def relevancy(self):
        """
        Gets the relevancy of this CategorySuggestion.
        This field is reserved for internal or future use.

        :return: The relevancy of this CategorySuggestion.
        :rtype: str
        """
        return self._relevancy

    @relevancy.setter
    def relevancy(self, relevancy):
        """
        Sets the relevancy of this CategorySuggestion.
        This field is reserved for internal or future use.

        :param relevancy: The relevancy of this CategorySuggestion.
        :type: str
        """

        self._relevancy = relevancy

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
