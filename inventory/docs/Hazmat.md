# Hazmat

This container is used by the seller to provide hazardous material information for the listing.<br><br>The <b>statements</b> element is required to complete the hazmat section of a listing.<br><br>The following elements are optional:<ul><li><b>pictograms</b></li><li><b>signalWord</b></li><li><b>component</b></li></ul>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | This field is used by the seller to provide component information for the listing. For example, component information can provide the specific material of Hazmat concern.&lt;br&gt;&lt;br&gt;&lt;b&gt;Max length:&lt;/b&gt; 120 | [optional] 
**pictograms** | **List[str]** | An array of comma-separated string values listing applicable pictogram code(s) for Hazard Pictogram(s).&lt;br&gt;&lt;br&gt;If your product contains hazardous substances or mixtures, please select the values corresponding to the hazard pictograms that are stated on your product&#39;s Safety Data Sheet. The selected hazard information will be displayed on your listing.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Use the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/marketplace/methods/getHazardousMaterialsLabels \&quot; target&#x3D;\&quot;_blank\&quot;&gt;getHazardousMaterialsLabels&lt;/a&gt; method in the Metadata API to find supported values for a specific marketplace/site. Refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/metadata/feature-regulatorhazmatcontainer.html#Pictogra\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Pictogram sample values&lt;/a&gt; for additional information.&lt;/span&gt; | [optional] 
**signal_word** | **str** | This field sets the signal word for hazardous materials in the listing.&lt;br&gt;&lt;br&gt;If your product contains hazardous substances or mixtures, please select a value corresponding to the signal word that is stated on your product&#39;s Safety Data Sheet. The selected hazard information will be displayed on your listing.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Use the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/marketplace/methods/getHazardousMaterialsLabels \&quot; target&#x3D;\&quot;_blank\&quot;&gt;getHazardousMaterialsLabels&lt;/a&gt; method in the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/methods \&quot; target&#x3D;\&quot;_blank\&quot;&gt;Metadata API&lt;/a&gt; to find supported values for a specific marketplace/site. Refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/metadata/feature-regulatorhazmatcontainer.html#Signal\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Signal word information&lt;/a&gt; for additional information.&lt;/span&gt; | [optional] 
**statements** | **List[str]** | An array of comma-separated string values specifying applicable statement code(s) for hazard statement(s) for the listing.&lt;br&gt;&lt;br&gt;If your product contains hazardous substances or mixtures, please select the values corresponding to the hazard statements that are stated on your product&#39;s Safety Data Sheet. The selected hazard information will be displayed on your listing.&lt;br&gt;&lt;br&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Use the &lt;a href&#x3D;\&quot;/api-docs/sell/metadata/resources/marketplace/methods/getHazardousMaterialsLabels \&quot; target&#x3D;\&quot;_blank\&quot;&gt;getHazardousMaterialsLabels&lt;/a&gt; method in the Metadata API to find supported values for a specific marketplace/site. Refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/metadata/feature-regulatorhazmatcontainer.html#Hazard\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Hazard statement sample values&lt;/a&gt; for additional information.&lt;/span&gt;&lt;br&gt;This field is required if hazardous material information is provided for the listing. | [optional] 

## Example

```python
from ebayinventory.models.hazmat import Hazmat

# TODO update the JSON string below
json = "{}"
# create an instance of Hazmat from a JSON string
hazmat_instance = Hazmat.from_json(json)
# print the JSON string representation of the object
print(Hazmat.to_json())

# convert the object into a dict
hazmat_dict = hazmat_instance.to_dict()
# create an instance of Hazmat from a dict
hazmat_from_dict = Hazmat.from_dict(hazmat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


