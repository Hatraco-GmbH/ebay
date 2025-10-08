# MotorsListingPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The unique identifier of the eBay leaf category for which metadata is being returned. | [optional] 
**category_tree_id** | **str** | The unique identifier of the category tree. | [optional] 
**deposit_supported** | **bool** | This field is returned as &lt;code&gt;true&lt;/code&gt; if the corresponding category supports the use of a deposit/down payment on a motor vehicle listing. In an AddItem call, the seller can configure a down payment for a motor vehicle listing using the PaymentDetails container. | [optional] 
**ebay_motors_pro_ad_format_enabled** | **str** | Indicates whether or not eBay Motors Pro sellers can use classified ads in this category to sell their vehicles. This element is applicable for eBay Motors Pro users. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:AdFormatEnabledEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**ebay_motors_pro_auto_accept_enabled** | **bool** | Indicates whether or not the category supports the Best Offer Auto Accept feature for eBay Motors Pro listings. This element is for eBay Motors Pro users. | [optional] 
**ebay_motors_pro_auto_decline_enabled** | **bool** | Indicates whether or not the category allows auto-decline for Best Offers for eBay Motors Classified Ad listings. This element is for eBay Motors Pro users. | [optional] 
**ebay_motors_pro_best_offer_enabled** | **str** | This enumerated value indicates whether or not Best Offer features are supported for eBay Motors Classified Ad listings in this category. This element is for eBay Motors Pro users. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:ClassifiedAdBestOfferEnabledEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**ebay_motors_pro_company_name_enabled** | **bool** | Indicates whether this category supports including the company name in the seller&#39;s contact information. This element is for eBay Motors Pro users. | [optional] 
**ebay_motors_pro_contact_by_address_enabled** | **bool** | Indicates whether this category supports including the address in the seller&#39;s contact information. This element is for eBay Motors Pro users. | [optional] 
**ebay_motors_pro_contact_by_email_enabled** | **bool** | Indicates whether this category supports including an email address in the seller&#39;s contact information. This element is for eBay Motors Pro users. | [optional] 
**ebay_motors_pro_contact_by_phone_enabled** | **bool** | Indicates whether this category supports including the telephone in the seller&#39;s contact information. This element is for eBay Motors Pro users. | [optional] 
**ebay_motors_pro_counter_offer_enabled** | **bool** | Indicates whether counter offers are allowed on Best Offers for this category in an eBay Motors Classified Ad listing. This element is for eBay Motors Pro users. | [optional] 
**ebay_motors_pro_payment_method_check_out_enabled** | **str** | This enumerated value indicates whether this category supports that the payment method should be displayed to the user for this category in an eBay Motors Classified Ad listing. Even if enabled, checkout may or may not be enabled. This element is for eBay Motors Pro users. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:ClassifiedAdPaymentMethodEnabledEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**ebay_motors_pro_phone_count** | **int** | Indicates the number of phone numbers that can be included through contact information for this category. This element is for eBay Motors Pro users. | [optional] 
**ebay_motors_pro_seller_contact_details_enabled** | **bool** | Indicates whether this category allows seller-level contact information for eBay Motors Classified Ad listings. A value of true means seller-level contact information is available for Classified Ad listings. This element is for eBay Motors Pro users. | [optional] 
**ebay_motors_pro_shipping_method_enabled** | **bool** | Indicates if shipping options should be displayed to the user for this category in an eBay Motors Classified Ad listing. This element is for eBay Motors Pro users. | [optional] 
**ebay_motors_pro_street_count** | **int** | This field indicates the number of street addresses allowed in contact information for this category. This element is for eBay Motors Pro users. | [optional] 
**epid_supported** | **bool** | If returned as &lt;code&gt;true&lt;/code&gt;, this indicates the category supports the use of an eBay Product ID (e.g. ePID) to identify which motorcycles and/or scooters are compatible with a motor vehicle part or accessory. ePIDs can only be used to identify motorcycles and scooters on the Germany and UK sites. | [optional] 
**k_type_supported** | **bool** | This field indicates whether or not the category supports the use of a K type to identify the cars and trucks compatible with a motor vehicle part or accessory. Only the AU, DE, ES, FR, IT, and UK marketplaces support the use of K types. See &lt;a href&#x3D;\&quot;/api-docs/user-guides/static/trading-user-guide/manually-specify-compatibility.html#ktype\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Compatibility by K type&lt;/a&gt; for more information | [optional] 
**local_listing_distances** | [**List[LocalListingDistance]**](LocalListingDistance.md) | This array shows the supported distances (in miles) for different types of Local Market subscription types in this category. Motor vehicle listings will be shown to buyers located within these proximities of the vehicle&#39;s location. | [optional] 
**local_market_ad_format_enabled** | **str** | Specifies whether this category supports Motor Local Market Classified Ad listings. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:AdFormatEnabledEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**local_market_auto_accept_enabled** | **bool** | Specifies whether this category supports auto-accept for Best Offers for Motors Local Market Classified Ads. | [optional] 
**local_market_auto_decline_enabled** | **bool** | Specifies whether this category supports auto-decline for Best Offers for Motors Local Market Classified Ads. | [optional] 
**local_market_best_offer_enabled** | **str** | Indicates if Best Offer is enabled/required for Motors Local Market Classified Ad listings in this category.  For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:ClassifiedAdBestOfferEnabledEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**local_market_company_name_enabled** | **bool** | Indicates whether the category supports the seller&#39;s company name being specified when using Motors Local Market classified ads. | [optional] 
**local_market_contact_by_address_enabled** | **bool** | Indicates whether this category supports including the address in the seller&#39;s contact information. | [optional] 
**local_market_contact_by_email_enabled** | **bool** | Indicates whether the category supports including an email address in the seller&#39;s contact information.  | [optional] 
**local_market_contact_by_phone_enabled** | **bool** | Indicates whether this category supports including the telephone in the seller&#39;s contact information. | [optional] 
**local_market_counter_offer_enabled** | **bool** | Indicates whether counter offers are allowed on Best Offers for this category for Motors Local Market Classified Ad listings. | [optional] 
**local_market_non_subscription** | **bool** | Indicates whether the category supports a seller creating a Motors Local Market listing without a subscription. This feature is only available to licensed vehicle dealers. | [optional] 
**local_market_payment_method_check_out_enabled** | **str** | Indicates if the payment method should be displayed to the user for this category in an Motors Local Market Classified Ad listing. Even if enabled, checkout may or may not be enabled. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:ClassifiedAdPaymentMethodEnabledEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**local_market_phone_count** | **int** | Indicates the number of phone numbers that can be included through contact information for this category. | [optional] 
**local_market_premium_subscription** | **bool** | Indicates whether the category supports the Premium level subscription Motors Local Market listings. This feature is only available to licensed vehicle dealers. | [optional] 
**local_market_regular_subscription** | **bool** | Indicates whether the category supports the Regular level subscription to Motors Local Market listings. This feature is only available to licensed vehicle dealers. | [optional] 
**local_market_seller_contact_details_enabled** | **bool** | Specifies the whether this category allows seller-level contact information for Motors Local Market Classified Ad listings. | [optional] 
**local_market_shipping_method_enabled** | **bool** | Indicates if shipping methods should be displayed to the user for this category in an Motors Local Market Classified Ad listing. Even if enabled, checkout may or may not be enabled. | [optional] 
**local_market_speciality_subscription** | **bool** | Indicates whether the category supports the Speciality level subscription to Motors Local Market listings. This feature is only available to licensed vehicle dealers. | [optional] 
**local_market_street_count** | **int** | Indicates which address option is enabled for the seller&#39;s contact information. | [optional] 
**max_granular_fitment_count** | **int** | Indicates the maximum number of compatible applications allowed per item when adding or revising items with compatibilities provided at the most detailed granularity. For example, in Car and Truck Parts on the US site, the most granular application would include Year, Make, Model, Trim, and Engine. | [optional] 
**max_item_compatibility** | **int** | Indicates the maximum number of compatible applications allowed per item when adding or revising items. This is relevant for specifying parts compatibility by application manually only. See &lt;a href&#x3D;\&quot;/api-docs/user-guides/static/trading-user-guide/manually-specify-compatibility.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Specify parts compatibility manually&lt;/a&gt; and &lt;a href&#x3D;\&quot;/api-docs/sell/static/inventory/managing-product-compatibility.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Managing product compatibility&lt;/a&gt; for more information. | [optional] 
**min_item_compatibility** | **int** | Indicates the minimum number of required compatible applications for listing items. A value of &lt;code&gt;0&lt;/code&gt; indicates it is not mandatory to specify parts compatibilities when listing. | [optional] 
**non_subscription** | **str** | The value in this field indicates whether the category supports Motors Local Market listings if the seller does not have a vehicle subscription. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:GeographicExposureEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**premium_subscription** | **str** | The value in this field indicates whether the category supports Motors Local Market listings if the seller has a Premium vehicle subscription. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:GeographicExposureEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**regular_subscription** | **str** | The value in this field indicates whether the category supports Motors Local Market listings if the seller has a Regular vehicle subscription. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:GeographicExposureEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**seller_provided_title_supported** | **bool** | This field is returned as &lt;code&gt;true&lt;/code&gt; if the corresponding category supports the use of a seller-provided title for a motor vehicle listing on the US or Canada Motors marketplaces. A seller-provided title is a descriptive title, given by the seller, that appears below eBay&#39;s pre-filled listing title for the motor vehicle. Visually, the seller-provided title is similar to a subtitle on other types of eBay listings (non-vehicle). A seller-provided title can assist in helping buyers discover the vehicle. | [optional] 
**speciality_subscription** | **str** | The value in this field indicates whether the category supports Motors Local Market listings if the seller has a Specialty vehicle subscription. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/metadata/types/sel:GeographicExposureEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**vin_supported** | **bool** | Indicates if Vehicle Identification Number is supported. | [optional] 
**vrm_supported** | **bool** | Indicates if Vehicle Registration Mark is supported. | [optional] 

## Example

```python
from ebaymetadata.models.motors_listing_policy import MotorsListingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of MotorsListingPolicy from a JSON string
motors_listing_policy_instance = MotorsListingPolicy.from_json(json)
# print the JSON string representation of the object
print(MotorsListingPolicy.to_json())

# convert the object into a dict
motors_listing_policy_dict = motors_listing_policy_instance.to_dict()
# create an instance of MotorsListingPolicy from a dict
motors_listing_policy_from_dict = MotorsListingPolicy.from_dict(motors_listing_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


