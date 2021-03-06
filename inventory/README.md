# ebayinventory
The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.12.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import ebayinventory 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ebayinventory
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import ebayinventory
from ebayinventory.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.BulkInventoryItem() # BulkInventoryItem | Details of the inventories with sku and locale

try:
    api_response = api_instance.bulk_create_or_replace_inventory_item(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryItemApi->bulk_create_or_replace_inventory_item: %s\n" % e)

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.BulkGetInventoryItem() # BulkGetInventoryItem | Details of the inventories with sku and locale

try:
    api_response = api_instance.bulk_get_inventory_item(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryItemApi->bulk_get_inventory_item: %s\n" % e)

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.BulkPriceQuantity() # BulkPriceQuantity | Price and allocation details for the given SKU and Marketplace

try:
    api_response = api_instance.bulk_update_price_quantity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryItemApi->bulk_update_price_quantity: %s\n" % e)

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
body = ebayinventory.InventoryItem() # InventoryItem | Details of the inventory item record.
content_language = 'content_language_example' # str | This request header sets the natural language that will be provided in the field values of the request payload.
sku = 'sku_example' # str | The seller-defined SKU value for the inventory item is required whether the seller is creating a new inventory item, or updating an existing inventory item. This SKU value is passed in at the end of the call URI. SKU values must be unique across the seller's inventory. Max length: 50.

try:
    api_response = api_instance.create_or_replace_inventory_item(body, content_language, sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryItemApi->create_or_replace_inventory_item: %s\n" % e)

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
sku = 'sku_example' # str | This is the seller-defined SKU value of the product whose inventory item record you wish to delete. Max length: 50.

try:
    api_instance.delete_inventory_item(sku)
except ApiException as e:
    print("Exception when calling InventoryItemApi->delete_inventory_item: %s\n" % e)

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
sku = 'sku_example' # str | This is the seller-defined SKU value of the product whose inventory item record you wish to retrieve. Max length: 50.

try:
    api_response = api_instance.get_inventory_item(sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryItemApi->get_inventory_item: %s\n" % e)

# Configure OAuth2 access token for authorization: api_auth
configuration = ebayinventory.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ebayinventory.InventoryItemApi(ebayinventory.ApiClient(configuration))
limit = 'limit_example' # str | The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be an integer from 1 to 100. If this query parameter is not set, up to 100 records will be returned on each page of results. Min: 1, Max: 100 (optional)
offset = 'offset_example' # str | The value passed in this query parameter sets the page number to retrieve. The first page of records has a value of 0, the second page of records has a value of 1, and so on. If this query parameter is not set, its value defaults to 0, and the first page of records is returned. (optional)

try:
    api_response = api_instance.get_inventory_items(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryItemApi->get_inventory_items: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.ebay.com{basePath}*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InventoryItemApi* | [**bulk_create_or_replace_inventory_item**](docs/InventoryItemApi.md#bulk_create_or_replace_inventory_item) | **POST** /bulk_create_or_replace_inventory_item | 
*InventoryItemApi* | [**bulk_get_inventory_item**](docs/InventoryItemApi.md#bulk_get_inventory_item) | **POST** /bulk_get_inventory_item | 
*InventoryItemApi* | [**bulk_update_price_quantity**](docs/InventoryItemApi.md#bulk_update_price_quantity) | **POST** /bulk_update_price_quantity | 
*InventoryItemApi* | [**create_or_replace_inventory_item**](docs/InventoryItemApi.md#create_or_replace_inventory_item) | **PUT** /inventory_item/{sku} | 
*InventoryItemApi* | [**delete_inventory_item**](docs/InventoryItemApi.md#delete_inventory_item) | **DELETE** /inventory_item/{sku} | 
*InventoryItemApi* | [**get_inventory_item**](docs/InventoryItemApi.md#get_inventory_item) | **GET** /inventory_item/{sku} | 
*InventoryItemApi* | [**get_inventory_items**](docs/InventoryItemApi.md#get_inventory_items) | **GET** /inventory_item | 
*InventoryItemGroupApi* | [**create_or_replace_inventory_item_group**](docs/InventoryItemGroupApi.md#create_or_replace_inventory_item_group) | **PUT** /inventory_item_group/{inventoryItemGroupKey} | 
*InventoryItemGroupApi* | [**delete_inventory_item_group**](docs/InventoryItemGroupApi.md#delete_inventory_item_group) | **DELETE** /inventory_item_group/{inventoryItemGroupKey} | 
*InventoryItemGroupApi* | [**get_inventory_item_group**](docs/InventoryItemGroupApi.md#get_inventory_item_group) | **GET** /inventory_item_group/{inventoryItemGroupKey} | 
*ListingApi* | [**bulk_migrate_listing**](docs/ListingApi.md#bulk_migrate_listing) | **POST** /bulk_migrate_listing | 
*LocationApi* | [**create_inventory_location**](docs/LocationApi.md#create_inventory_location) | **POST** /location/{merchantLocationKey} | 
*LocationApi* | [**delete_inventory_location**](docs/LocationApi.md#delete_inventory_location) | **DELETE** /location/{merchantLocationKey} | 
*LocationApi* | [**disable_inventory_location**](docs/LocationApi.md#disable_inventory_location) | **POST** /location/{merchantLocationKey}/disable | 
*LocationApi* | [**enable_inventory_location**](docs/LocationApi.md#enable_inventory_location) | **POST** /location/{merchantLocationKey}/enable | 
*LocationApi* | [**get_inventory_location**](docs/LocationApi.md#get_inventory_location) | **GET** /location/{merchantLocationKey} | 
*LocationApi* | [**get_inventory_locations**](docs/LocationApi.md#get_inventory_locations) | **GET** /location | 
*LocationApi* | [**update_inventory_location**](docs/LocationApi.md#update_inventory_location) | **POST** /location/{merchantLocationKey}/update_location_details | 
*OfferApi* | [**bulk_create_offer**](docs/OfferApi.md#bulk_create_offer) | **POST** /bulk_create_offer | 
*OfferApi* | [**bulk_publish_offer**](docs/OfferApi.md#bulk_publish_offer) | **POST** /bulk_publish_offer | 
*OfferApi* | [**create_offer**](docs/OfferApi.md#create_offer) | **POST** /offer | 
*OfferApi* | [**delete_offer**](docs/OfferApi.md#delete_offer) | **DELETE** /offer/{offerId} | 
*OfferApi* | [**get_listing_fees**](docs/OfferApi.md#get_listing_fees) | **POST** /offer/get_listing_fees | 
*OfferApi* | [**get_offer**](docs/OfferApi.md#get_offer) | **GET** /offer/{offerId} | 
*OfferApi* | [**get_offers**](docs/OfferApi.md#get_offers) | **GET** /offer | 
*OfferApi* | [**publish_offer**](docs/OfferApi.md#publish_offer) | **POST** /offer/{offerId}/publish/ | 
*OfferApi* | [**publish_offer_by_inventory_item_group**](docs/OfferApi.md#publish_offer_by_inventory_item_group) | **POST** /offer/publish_by_inventory_item_group/ | 
*OfferApi* | [**update_offer**](docs/OfferApi.md#update_offer) | **PUT** /offer/{offerId} | 
*OfferApi* | [**withdraw_offer**](docs/OfferApi.md#withdraw_offer) | **POST** /offer/{offerId}/withdraw | 
*OfferApi* | [**withdraw_offer_by_inventory_item_group**](docs/OfferApi.md#withdraw_offer_by_inventory_item_group) | **POST** /offer/withdraw_by_inventory_item_group | 
*ProductCompatibilityApi* | [**create_or_replace_product_compatibility**](docs/ProductCompatibilityApi.md#create_or_replace_product_compatibility) | **PUT** /inventory_item/{sku}/product_compatibility | 
*ProductCompatibilityApi* | [**delete_product_compatibility**](docs/ProductCompatibilityApi.md#delete_product_compatibility) | **DELETE** /inventory_item/{sku}/product_compatibility | 
*ProductCompatibilityApi* | [**get_product_compatibility**](docs/ProductCompatibilityApi.md#get_product_compatibility) | **GET** /inventory_item/{sku}/product_compatibility | 

## Documentation For Models

 - [Address](docs/Address.md)
 - [Amount](docs/Amount.md)
 - [Availability](docs/Availability.md)
 - [AvailabilityDistribution](docs/AvailabilityDistribution.md)
 - [AvailabilityWithAll](docs/AvailabilityWithAll.md)
 - [BaseResponse](docs/BaseResponse.md)
 - [BestOffer](docs/BestOffer.md)
 - [BulkEbayOfferDetailsWithKeys](docs/BulkEbayOfferDetailsWithKeys.md)
 - [BulkGetInventoryItem](docs/BulkGetInventoryItem.md)
 - [BulkGetInventoryItemResponse](docs/BulkGetInventoryItemResponse.md)
 - [BulkInventoryItem](docs/BulkInventoryItem.md)
 - [BulkInventoryItemResponse](docs/BulkInventoryItemResponse.md)
 - [BulkMigrateListing](docs/BulkMigrateListing.md)
 - [BulkMigrateListingResponse](docs/BulkMigrateListingResponse.md)
 - [BulkOffer](docs/BulkOffer.md)
 - [BulkOfferResponse](docs/BulkOfferResponse.md)
 - [BulkPriceQuantity](docs/BulkPriceQuantity.md)
 - [BulkPriceQuantityResponse](docs/BulkPriceQuantityResponse.md)
 - [BulkPublishResponse](docs/BulkPublishResponse.md)
 - [Charity](docs/Charity.md)
 - [Compatibility](docs/Compatibility.md)
 - [CompatibleProduct](docs/CompatibleProduct.md)
 - [Dimension](docs/Dimension.md)
 - [EbayOfferDetailsWithAll](docs/EbayOfferDetailsWithAll.md)
 - [EbayOfferDetailsWithId](docs/EbayOfferDetailsWithId.md)
 - [EbayOfferDetailsWithKeys](docs/EbayOfferDetailsWithKeys.md)
 - [Error](docs/Error.md)
 - [ErrorParameter](docs/ErrorParameter.md)
 - [Fee](docs/Fee.md)
 - [FeeSummary](docs/FeeSummary.md)
 - [FeesSummaryResponse](docs/FeesSummaryResponse.md)
 - [FormatAllocation](docs/FormatAllocation.md)
 - [GeoCoordinates](docs/GeoCoordinates.md)
 - [GetInventoryItem](docs/GetInventoryItem.md)
 - [GetInventoryItemResponse](docs/GetInventoryItemResponse.md)
 - [Interval](docs/Interval.md)
 - [InventoryItem](docs/InventoryItem.md)
 - [InventoryItemGroup](docs/InventoryItemGroup.md)
 - [InventoryItemListing](docs/InventoryItemListing.md)
 - [InventoryItemResponse](docs/InventoryItemResponse.md)
 - [InventoryItemWithSkuLocale](docs/InventoryItemWithSkuLocale.md)
 - [InventoryItemWithSkuLocaleGroupKeys](docs/InventoryItemWithSkuLocaleGroupKeys.md)
 - [InventoryItemWithSkuLocaleGroupid](docs/InventoryItemWithSkuLocaleGroupid.md)
 - [InventoryItems](docs/InventoryItems.md)
 - [InventoryLocation](docs/InventoryLocation.md)
 - [InventoryLocationFull](docs/InventoryLocationFull.md)
 - [InventoryLocationResponse](docs/InventoryLocationResponse.md)
 - [ListingDetails](docs/ListingDetails.md)
 - [ListingPolicies](docs/ListingPolicies.md)
 - [Location](docs/Location.md)
 - [LocationDetails](docs/LocationDetails.md)
 - [LocationResponse](docs/LocationResponse.md)
 - [MigrateListing](docs/MigrateListing.md)
 - [MigrateListingResponse](docs/MigrateListingResponse.md)
 - [NameValueList](docs/NameValueList.md)
 - [OfferKeyWithId](docs/OfferKeyWithId.md)
 - [OfferKeysWithId](docs/OfferKeysWithId.md)
 - [OfferPriceQuantity](docs/OfferPriceQuantity.md)
 - [OfferResponse](docs/OfferResponse.md)
 - [OfferResponseWithListingId](docs/OfferResponseWithListingId.md)
 - [OfferSkuResponse](docs/OfferSkuResponse.md)
 - [Offers](docs/Offers.md)
 - [OperatingHours](docs/OperatingHours.md)
 - [PackageWeightAndSize](docs/PackageWeightAndSize.md)
 - [PickupAtLocationAvailability](docs/PickupAtLocationAvailability.md)
 - [PriceQuantity](docs/PriceQuantity.md)
 - [PriceQuantityResponse](docs/PriceQuantityResponse.md)
 - [PricingSummary](docs/PricingSummary.md)
 - [Product](docs/Product.md)
 - [ProductFamilyProperties](docs/ProductFamilyProperties.md)
 - [ProductIdentifier](docs/ProductIdentifier.md)
 - [PublishByInventoryItemGroupRequest](docs/PublishByInventoryItemGroupRequest.md)
 - [PublishResponse](docs/PublishResponse.md)
 - [ShipToLocationAvailability](docs/ShipToLocationAvailability.md)
 - [ShipToLocationAvailabilityWithAll](docs/ShipToLocationAvailabilityWithAll.md)
 - [ShippingCostOverride](docs/ShippingCostOverride.md)
 - [SpecialHours](docs/SpecialHours.md)
 - [Specification](docs/Specification.md)
 - [Tax](docs/Tax.md)
 - [TimeDuration](docs/TimeDuration.md)
 - [VariesBy](docs/VariesBy.md)
 - [Version](docs/Version.md)
 - [Weight](docs/Weight.md)
 - [WithdrawByInventoryItemGroupRequest](docs/WithdrawByInventoryItemGroupRequest.md)
 - [WithdrawResponse](docs/WithdrawResponse.md)

## Documentation For Authorization


## api_auth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://auth.ebay.com/oauth2/authorize
- **Scopes**: 
 - **https://api.ebay.com/oauth/api_scope/sell.inventory**: View and manage your inventory and offers
 - **https://api.ebay.com/oauth/api_scope/sell.inventory.readonly**: View your inventory and offers


## Author


