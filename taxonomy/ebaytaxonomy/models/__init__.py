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

from __future__ import absolute_import

# import models into model package
from .ancestor_reference import AncestorReference
from .aspect import Aspect
from .aspect_constraint import AspectConstraint
from .aspect_metadata import AspectMetadata
from .aspect_value import AspectValue
from .base_category_tree import BaseCategoryTree
from .category import Category
from .category_aspect import CategoryAspect
from .category_subtree import CategorySubtree
from .category_suggestion import CategorySuggestion
from .category_suggestion_response import CategorySuggestionResponse
from .category_tree import CategoryTree
from .category_tree_node import CategoryTreeNode
from .compatibility_property import CompatibilityProperty
from .compatibility_property_value import CompatibilityPropertyValue
from .get_categories_aspect_response import GetCategoriesAspectResponse
from .get_compatibility_metadata_response import GetCompatibilityMetadataResponse
from .get_compatibility_property_values_response import GetCompatibilityPropertyValuesResponse
from .relevance_indicator import RelevanceIndicator
from .value_constraint import ValueConstraint
