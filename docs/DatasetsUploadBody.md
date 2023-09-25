# DatasetsUploadBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** | The optional string representation of the url of a project. If set, the dataset will be associated with that project. | [optional] 
**display_name** | **str** | The name of this dataset (required). | 
**description** | **str** | Optional description of this dataset. | [optional] 
**locale** | **str** | The locale of this dataset (required). | 
**kind** | **str** | The kind of the dataset (required). Possible values are \&quot;Language\&quot;, \&quot;Acoustic\&quot;, \&quot;Pronunciation\&quot;, \&quot;AudioFiles\&quot;, \&quot;LanguageMarkdown\&quot;. | 
**custom_properties** | **str** | The optional custom properties of this entity. The maximum allowed key length is 64 characters, the maximum allowed value length is 256 characters and the count of allowed entries is 10. | [optional] 
**data** | **str** | For acoustic datasets, a zip file containing the audio data and a text file containing the transcriptions for the audio data. For language datasets, a text file containing the language or pronunciation data. Required in both cases. | [optional] 
**email** | **str** | An optional string containing the email address to send email notifications to in case the operation completes. The value will be removed after successfully sending the email. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

