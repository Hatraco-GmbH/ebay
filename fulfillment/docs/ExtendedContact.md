# ExtendedContact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | The company name associated with the buyer or eBay shipping partner. This field is only returned if defined/applicable to the buyer or eBay shipping partner. | [optional] 
**contact_address** | [**Address**](Address.md) |  | [optional] 
**email** | **str** | This field shows the email address of the buyer. The email address of a buyer will be masked 14 days after order creation. This field will still be returned for the order, but it will not contain the buyer&#x27;s email address, but instead, something like &#x27;Invalid Request&#x27;. Note: This field always contains the email address of the buyer even with a Global Shipping Program shipment. | [optional] 
**full_name** | **str** | The full name of the buyer or eBay shipping partner. | [optional] 
**primary_phone** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

