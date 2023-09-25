# azure_speech_api.DefaultApi

All URIs are relative to *https://cognitiveuseprod.cognitiveservices.azure.com/speechtotext/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datasets_commit_blocks**](DefaultApi.md#datasets_commit_blocks) | **POST** /datasets/{id}/blocks:commit | Commit Block List
[**datasets_create**](DefaultApi.md#datasets_create) | **POST** /datasets | Create Dataset
[**datasets_delete**](DefaultApi.md#datasets_delete) | **DELETE** /datasets/{id} | Delete Dataset
[**datasets_get**](DefaultApi.md#datasets_get) | **GET** /datasets/{id} | Get Dataset
[**datasets_get_blocks**](DefaultApi.md#datasets_get_blocks) | **GET** /datasets/{id}/blocks | Get Uploaded Blocks
[**datasets_get_file**](DefaultApi.md#datasets_get_file) | **GET** /datasets/{id}/files/{fileId} | Get Dataset File
[**datasets_list**](DefaultApi.md#datasets_list) | **GET** /datasets | Get Datasets
[**datasets_list_files**](DefaultApi.md#datasets_list_files) | **GET** /datasets/{id}/files | Get Dataset Files
[**datasets_list_supported_locales**](DefaultApi.md#datasets_list_supported_locales) | **GET** /datasets/locales | Get Supported Locales for Datasets
[**datasets_update**](DefaultApi.md#datasets_update) | **PATCH** /datasets/{id} | Update Dataset
[**datasets_upload**](DefaultApi.md#datasets_upload) | **POST** /datasets/upload | Upload Dataset From Form
[**datasets_upload_block**](DefaultApi.md#datasets_upload_block) | **PUT** /datasets/{id}/blocks | Upload Data Block
[**endpoints_create**](DefaultApi.md#endpoints_create) | **POST** /endpoints | Create Endpoint
[**endpoints_delete**](DefaultApi.md#endpoints_delete) | **DELETE** /endpoints/{id} | Delete Endpoint
[**endpoints_delete_base_model_log**](DefaultApi.md#endpoints_delete_base_model_log) | **DELETE** /endpoints/base/{locale}/files/logs/{logId} | Delete Base Model Endpoint Log
[**endpoints_delete_base_model_logs**](DefaultApi.md#endpoints_delete_base_model_logs) | **DELETE** /endpoints/base/{locale}/files/logs | Delete All Base Model Endpoint Logs
[**endpoints_delete_log**](DefaultApi.md#endpoints_delete_log) | **DELETE** /endpoints/{id}/files/logs/{logId} | Delete Custom Model Endpoint Log
[**endpoints_delete_logs**](DefaultApi.md#endpoints_delete_logs) | **DELETE** /endpoints/{id}/files/logs | Delete All Custom Model Endpoint Logs
[**endpoints_get**](DefaultApi.md#endpoints_get) | **GET** /endpoints/{id} | Get Endpoint
[**endpoints_get_base_model_log**](DefaultApi.md#endpoints_get_base_model_log) | **GET** /endpoints/base/{locale}/files/logs/{logId} | Get Base Model Endpoint Log
[**endpoints_get_log**](DefaultApi.md#endpoints_get_log) | **GET** /endpoints/{id}/files/logs/{logId} | Get Custom Model Endpoint Log
[**endpoints_list**](DefaultApi.md#endpoints_list) | **GET** /endpoints | Get Endpoints
[**endpoints_list_base_model_logs**](DefaultApi.md#endpoints_list_base_model_logs) | **GET** /endpoints/base/{locale}/files/logs | Get Base Model Logs
[**endpoints_list_logs**](DefaultApi.md#endpoints_list_logs) | **GET** /endpoints/{id}/files/logs | Get Endpoint Logs
[**endpoints_list_supported_locales**](DefaultApi.md#endpoints_list_supported_locales) | **GET** /endpoints/locales | Get Supported Locales for Endpoints
[**endpoints_update**](DefaultApi.md#endpoints_update) | **PATCH** /endpoints/{id} | Update Endpoint
[**evaluations_create**](DefaultApi.md#evaluations_create) | **POST** /evaluations | Create Evaluation
[**evaluations_delete**](DefaultApi.md#evaluations_delete) | **DELETE** /evaluations/{id} | Delete Evaluation
[**evaluations_get**](DefaultApi.md#evaluations_get) | **GET** /evaluations/{id} | Get Evaluation
[**evaluations_get_file**](DefaultApi.md#evaluations_get_file) | **GET** /evaluations/{id}/files/{fileId} | Get Evaluation File
[**evaluations_list**](DefaultApi.md#evaluations_list) | **GET** /evaluations | Get Evaluations
[**evaluations_list_files**](DefaultApi.md#evaluations_list_files) | **GET** /evaluations/{id}/files | Get Evaluation Files
[**evaluations_list_supported_locales**](DefaultApi.md#evaluations_list_supported_locales) | **GET** /evaluations/locales | Get Supported Locales for Evaluations
[**evaluations_update**](DefaultApi.md#evaluations_update) | **PATCH** /evaluations/{id} | Update Evaluation
[**health_status_get**](DefaultApi.md#health_status_get) | **GET** /healthstatus | Get Health Status
[**models_copy_to**](DefaultApi.md#models_copy_to) | **POST** /models/{id}:copyto | Copy Model
[**models_create**](DefaultApi.md#models_create) | **POST** /models | Create Model
[**models_delete**](DefaultApi.md#models_delete) | **DELETE** /models/{id} | Delete Model
[**models_get_base_model**](DefaultApi.md#models_get_base_model) | **GET** /models/base/{id} | Get Base Model
[**models_get_base_model_manifest**](DefaultApi.md#models_get_base_model_manifest) | **GET** /models/base/{id}/manifest | Get Base Model Manifest
[**models_get_custom_model**](DefaultApi.md#models_get_custom_model) | **GET** /models/{id} | Get Model
[**models_get_custom_model_manifest**](DefaultApi.md#models_get_custom_model_manifest) | **GET** /models/{id}/manifest | Get Model Manifest
[**models_get_file**](DefaultApi.md#models_get_file) | **GET** /models/{id}/files/{fileId} | Get Model File
[**models_list_base_models**](DefaultApi.md#models_list_base_models) | **GET** /models/base | Get Base Models
[**models_list_custom_models**](DefaultApi.md#models_list_custom_models) | **GET** /models | Get Models
[**models_list_files**](DefaultApi.md#models_list_files) | **GET** /models/{id}/files | Get Model Files
[**models_list_supported_locales**](DefaultApi.md#models_list_supported_locales) | **GET** /models/locales | Get Supported Locales for Models
[**models_update**](DefaultApi.md#models_update) | **PATCH** /models/{id} | Update Model
[**projects_create**](DefaultApi.md#projects_create) | **POST** /projects | Create Project
[**projects_delete**](DefaultApi.md#projects_delete) | **DELETE** /projects/{id} | Delete Project
[**projects_get**](DefaultApi.md#projects_get) | **GET** /projects/{id} | Get Project
[**projects_list**](DefaultApi.md#projects_list) | **GET** /projects | Get Projects
[**projects_list_datasets**](DefaultApi.md#projects_list_datasets) | **GET** /projects/{id}/datasets | Get Datasets for Project
[**projects_list_endpoints**](DefaultApi.md#projects_list_endpoints) | **GET** /projects/{id}/endpoints | Get Endpoints for Project
[**projects_list_evaluations**](DefaultApi.md#projects_list_evaluations) | **GET** /projects/{id}/evaluations | Get Evaluations for Project
[**projects_list_models**](DefaultApi.md#projects_list_models) | **GET** /projects/{id}/models | Get Models for Project
[**projects_list_supported_locales**](DefaultApi.md#projects_list_supported_locales) | **GET** /projects/locales | Get Supported Locales for Projects
[**projects_list_transcriptions**](DefaultApi.md#projects_list_transcriptions) | **GET** /projects/{id}/transcriptions | Get Transcriptions for Project
[**projects_update**](DefaultApi.md#projects_update) | **PATCH** /projects/{id} | Update Project
[**transcriptions_create**](DefaultApi.md#transcriptions_create) | **POST** /transcriptions | Create Transcription
[**transcriptions_delete**](DefaultApi.md#transcriptions_delete) | **DELETE** /transcriptions/{id} | Delete Transcription
[**transcriptions_get**](DefaultApi.md#transcriptions_get) | **GET** /transcriptions/{id} | Get Transcription
[**transcriptions_get_file**](DefaultApi.md#transcriptions_get_file) | **GET** /transcriptions/{id}/files/{fileId} | Get Transcription File
[**transcriptions_list**](DefaultApi.md#transcriptions_list) | **GET** /transcriptions | Get Transcriptions
[**transcriptions_list_files**](DefaultApi.md#transcriptions_list_files) | **GET** /transcriptions/{id}/files | Get Transcription Files
[**transcriptions_list_supported_locales**](DefaultApi.md#transcriptions_list_supported_locales) | **GET** /transcriptions/locales | Get Supported Locales for Transcriptions
[**transcriptions_update**](DefaultApi.md#transcriptions_update) | **PATCH** /transcriptions/{id} | Update Transcription
[**web_hooks_create**](DefaultApi.md#web_hooks_create) | **POST** /webhooks | Create Web Hook
[**web_hooks_delete**](DefaultApi.md#web_hooks_delete) | **DELETE** /webhooks/{id} | Delete Web Hook
[**web_hooks_get**](DefaultApi.md#web_hooks_get) | **GET** /webhooks/{id} | Get Web Hook
[**web_hooks_list**](DefaultApi.md#web_hooks_list) | **GET** /webhooks | Get Web Hooks
[**web_hooks_ping**](DefaultApi.md#web_hooks_ping) | **POST** /webhooks/{id}:ping | Ping Web Hook
[**web_hooks_test**](DefaultApi.md#web_hooks_test) | **POST** /webhooks/{id}:test | Test Web Hook
[**web_hooks_update**](DefaultApi.md#web_hooks_update) | **PATCH** /webhooks/{id} | Update Web Hook

# **datasets_commit_blocks**
> datasets_commit_blocks(id, body=body)

Commit Block List

Commit block list to complete the upload of the dataset.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the dataset.
body = [azure_speech_api.CommitBlocksEntry()] # list[CommitBlocksEntry] | The list of blocks that compile the dataset. (optional)

try:
    # Commit Block List
    api_instance.datasets_commit_blocks(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->datasets_commit_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the dataset. | 
 **body** | [**list[CommitBlocksEntry]**](CommitBlocksEntry.md)| The list of blocks that compile the dataset. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_create**
> Dataset datasets_create(body=body)

Create Dataset

Uploads and creates a new dataset by getting the data from a specified URL or starts waiting for data blocks to be uploaded.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
body = azure_speech_api.Dataset() # Dataset | Definition for the new dataset. (optional)

try:
    # Create Dataset
    api_response = api_instance.datasets_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->datasets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dataset**](Dataset.md)| Definition for the new dataset. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_delete**
> datasets_delete(id)

Delete Dataset

Deletes the specified dataset.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the dataset.

try:
    # Delete Dataset
    api_instance.datasets_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->datasets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the dataset. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_get**
> Dataset datasets_get(id)

Get Dataset

Gets the dataset identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the dataset.

try:
    # Get Dataset
    api_response = api_instance.datasets_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->datasets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the dataset. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_get_blocks**
> UploadedBlocks datasets_get_blocks(id)

Get Uploaded Blocks

Gets the list of uploaded blocks for this dataset.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the dataset.

try:
    # Get Uploaded Blocks
    api_response = api_instance.datasets_get_blocks(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->datasets_get_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the dataset. | 

### Return type

[**UploadedBlocks**](UploadedBlocks.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_get_file**
> File datasets_get_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Dataset File

Gets one specific file (identified with fileId) from a dataset (identified with id).

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the dataset.
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the file.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)

try:
    # Get Dataset File
    api_response = api_instance.datasets_get_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->datasets_get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the dataset. | 
 **file_id** | [**str**](.md)| Format - uuid. The identifier of the file. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_list**
> PaginatedDatasets datasets_list(skip=skip, top=top, filter=filter)

Get Datasets

Gets a list of datasets for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available datasets.              <ul><li><b>Supported properties:</b> displayName, description, createdDateTime, lastActionDateTime, status, locale, kind.                </li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=createdDateTime gt 2022-02-01T11:00:00Z and displayName eq 'My dataset'```</li></ul> (optional)

try:
    # Get Datasets
    api_response = api_instance.datasets_list(skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->datasets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available datasets.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; displayName, description, createdDateTime, lastActionDateTime, status, locale, kind.                &lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;createdDateTime gt 2022-02-01T11:00:00Z and displayName eq &#x27;My dataset&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedDatasets**](PaginatedDatasets.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_list_files**
> PaginatedFiles datasets_list_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top, filter=filter)

Get Dataset Files

Gets the files of the dataset identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the dataset.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available files.              <ul><li><b>Supported properties:</b> name, createdDateTime, kind.</li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=name eq 'myaudio.wav' and kind eq 'Audio'```</li></ul> (optional)

try:
    # Get Dataset Files
    api_response = api_instance.datasets_list_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->datasets_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the dataset. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available files.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; name, createdDateTime, kind.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;name eq &#x27;myaudio.wav&#x27; and kind eq &#x27;Audio&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_list_supported_locales**
> DatasetLocales datasets_list_supported_locales()

Get Supported Locales for Datasets

Gets a list of supported locales for datasets.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))

try:
    # Get Supported Locales for Datasets
    api_response = api_instance.datasets_list_supported_locales()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->datasets_list_supported_locales: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DatasetLocales**](DatasetLocales.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_update**
> Dataset datasets_update(id, body=body)

Update Dataset

Updates the mutable details of the dataset identified by its ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the dataset.
body = azure_speech_api.DatasetUpdate() # DatasetUpdate | The updated values for the dataset. (optional)

try:
    # Update Dataset
    api_response = api_instance.datasets_update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->datasets_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the dataset. | 
 **body** | [**DatasetUpdate**](DatasetUpdate.md)| The updated values for the dataset. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_upload**
> Dataset datasets_upload(project, display_name, description, locale, kind, custom_properties, data, email)

Upload Dataset From Form

Uploads data and creates a new dataset.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
project = 'project_example' # str | 
display_name = 'display_name_example' # str | 
description = 'description_example' # str | 
locale = 'locale_example' # str | 
kind = 'kind_example' # str | 
custom_properties = 'custom_properties_example' # str | 
data = 'data_example' # str | 
email = 'email_example' # str | 

try:
    # Upload Dataset From Form
    api_response = api_instance.datasets_upload(project, display_name, description, locale, kind, custom_properties, data, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->datasets_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
 **display_name** | **str**|  | 
 **description** | **str**|  | 
 **locale** | **str**|  | 
 **kind** | **str**|  | 
 **custom_properties** | **str**|  | 
 **data** | **str**|  | 
 **email** | **str**|  | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_upload_block**
> datasets_upload_block(blockid, id, body=body)

Upload Data Block

Upload a block of data for the dataset. The maximum size of the block is 8MiB.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
blockid = 'blockid_example' # str | A valid Base64 string value that identifies the block. Prior to encoding, the string must be less than or equal to 64 bytes in size. For a given blob, the length of the value specified for the blockid parameter must be the same size for each block. Note that the Base64 string must be URL-encoded.
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the dataset.
body = azure_speech_api.Object() # Object |  (optional)

try:
    # Upload Data Block
    api_instance.datasets_upload_block(blockid, id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->datasets_upload_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockid** | **str**| A valid Base64 string value that identifies the block. Prior to encoding, the string must be less than or equal to 64 bytes in size. For a given blob, the length of the value specified for the blockid parameter must be the same size for each block. Note that the Base64 string must be URL-encoded. | 
 **id** | [**str**](.md)| Format - uuid. The identifier of the dataset. | 
 **body** | **Object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_create**
> Endpoint endpoints_create(body=body)

Create Endpoint

Creates a new endpoint.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
body = azure_speech_api.Endpoint() # Endpoint | The details of the endpoint. (optional)

try:
    # Create Endpoint
    api_response = api_instance.endpoints_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Endpoint**](Endpoint.md)| The details of the endpoint. | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_delete**
> endpoints_delete(id)

Delete Endpoint

Deletes the endpoint identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the endpoint.

try:
    # Delete Endpoint
    api_instance.endpoints_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the endpoint. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_delete_base_model_log**
> endpoints_delete_base_model_log(locale, log_id)

Delete Base Model Endpoint Log

Deletes one audio or transcription log that have been stored when using the default base model of a given language.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
locale = 'locale_example' # str | The language used to select the default base model.
log_id = 'log_id_example' # str | The identifier of the log.

try:
    # Delete Base Model Endpoint Log
    api_instance.endpoints_delete_base_model_log(locale, log_id)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_delete_base_model_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The language used to select the default base model. | 
 **log_id** | **str**| The identifier of the log. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_delete_base_model_logs**
> endpoints_delete_base_model_logs(locale, end_date=end_date)

Delete All Base Model Endpoint Logs

Deletion process is done asynchronously and can take up to one day depending on the amount of log files.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
locale = 'locale_example' # str | The language used to select the default base model.
end_date = 'end_date_example' # str | The end date of the audio logs deletion (specific day, UTC).              Expected format: \"yyyy-mm-dd\". For instance, \"2023-03-15\" results in deleting all logs on March 15th, 2023 and before.              Deletes all existing logs when date is not specified. (optional)

try:
    # Delete All Base Model Endpoint Logs
    api_instance.endpoints_delete_base_model_logs(locale, end_date=end_date)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_delete_base_model_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The language used to select the default base model. | 
 **end_date** | **str**| The end date of the audio logs deletion (specific day, UTC).              Expected format: \&quot;yyyy-mm-dd\&quot;. For instance, \&quot;2023-03-15\&quot; results in deleting all logs on March 15th, 2023 and before.              Deletes all existing logs when date is not specified. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_delete_log**
> endpoints_delete_log(id, log_id)

Delete Custom Model Endpoint Log

Deletes one audio or transcription log that have been stored for a given endpoint.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the endpoint.
log_id = 'log_id_example' # str | The identifier of the log.

try:
    # Delete Custom Model Endpoint Log
    api_instance.endpoints_delete_log(id, log_id)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_delete_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the endpoint. | 
 **log_id** | **str**| The identifier of the log. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_delete_logs**
> endpoints_delete_logs(id, end_date=end_date)

Delete All Custom Model Endpoint Logs

The deletion process is done asynchronously and can take up to one day depending on the amount of log files.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the endpoint.
end_date = 'end_date_example' # str | The end date of the audio logs deletion (specific day, UTC).              Expected format: \"yyyy-mm-dd\". For instance, \"2023-03-15\" results in deleting all logs on March 15th, 2023 and before.              Deletes all existing logs when date is not specified. (optional)

try:
    # Delete All Custom Model Endpoint Logs
    api_instance.endpoints_delete_logs(id, end_date=end_date)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_delete_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the endpoint. | 
 **end_date** | **str**| The end date of the audio logs deletion (specific day, UTC).              Expected format: \&quot;yyyy-mm-dd\&quot;. For instance, \&quot;2023-03-15\&quot; results in deleting all logs on March 15th, 2023 and before.              Deletes all existing logs when date is not specified. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_get**
> Endpoint endpoints_get(id)

Get Endpoint

Gets the endpoint identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the endpoint.

try:
    # Get Endpoint
    api_response = api_instance.endpoints_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_get_base_model_log**
> File endpoints_get_base_model_log(locale, log_id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Base Model Endpoint Log

Gets a specific audio or transcription log for the default base model in a given language.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
locale = 'locale_example' # str | The language used to select the default base model.
log_id = 'log_id_example' # str | The identifier of the log.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)

try:
    # Get Base Model Endpoint Log
    api_response = api_instance.endpoints_get_base_model_log(locale, log_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_get_base_model_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The language used to select the default base model. | 
 **log_id** | **str**| The identifier of the log. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_get_log**
> File endpoints_get_log(id, log_id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Custom Model Endpoint Log

Gets a specific audio or transcription log for a given endpoint.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the endpoint.
log_id = 'log_id_example' # str | The identifier of the log.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)

try:
    # Get Custom Model Endpoint Log
    api_response = api_instance.endpoints_get_log(id, log_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_get_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the endpoint. | 
 **log_id** | **str**| The identifier of the log. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_list**
> PaginatedEndpoints endpoints_list(skip=skip, top=top, filter=filter)

Get Endpoints

Gets the list of endpoints for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available endpoints.              <ul><li><b>Supported properties:</b> displayName, description, createdDateTime, lastActionDateTime, status, locale.                </li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=locale eq 'en-US'```</li></ul> (optional)

try:
    # Get Endpoints
    api_response = api_instance.endpoints_list(skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available endpoints.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; displayName, description, createdDateTime, lastActionDateTime, status, locale.                &lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;locale eq &#x27;en-US&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedEndpoints**](PaginatedEndpoints.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_list_base_model_logs**
> PaginatedFiles endpoints_list_base_model_logs(locale, sas_validity_in_seconds=sas_validity_in_seconds, skip_token=skip_token, top=top)

Get Base Model Logs

Gets the list of audio and transcription logs that have been stored when using the default base model of a given language.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
locale = 'locale_example' # str | The language used to select the default base model.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)
skip_token = 'skip_token_example' # str | Token to skip logs that were already retrieved in previous requests. Pagination starts from beginning when not defined. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)

try:
    # Get Base Model Logs
    api_response = api_instance.endpoints_list_base_model_logs(locale, sas_validity_in_seconds=sas_validity_in_seconds, skip_token=skip_token, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_list_base_model_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The language used to select the default base model. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 
 **skip_token** | **str**| Token to skip logs that were already retrieved in previous requests. Pagination starts from beginning when not defined. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_list_logs**
> PaginatedFiles endpoints_list_logs(id, sas_validity_in_seconds=sas_validity_in_seconds, skip_token=skip_token, top=top)

Get Endpoint Logs

Gets the list of audio and transcription logs that have been stored for a given endpoint.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the endpoint.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)
skip_token = 'skip_token_example' # str | Token to skip logs that were already retrieved in previous requests. Pagination starts from beginning when not defined. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)

try:
    # Get Endpoint Logs
    api_response = api_instance.endpoints_list_logs(id, sas_validity_in_seconds=sas_validity_in_seconds, skip_token=skip_token, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_list_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the endpoint. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 
 **skip_token** | **str**| Token to skip logs that were already retrieved in previous requests. Pagination starts from beginning when not defined. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_list_supported_locales**
> EndpointsLocalesGet200ApplicationJsonResponse endpoints_list_supported_locales()

Get Supported Locales for Endpoints

Gets a list of supported locales for endpoint creations.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))

try:
    # Get Supported Locales for Endpoints
    api_response = api_instance.endpoints_list_supported_locales()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_list_supported_locales: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EndpointsLocalesGet200ApplicationJsonResponse**](EndpointsLocalesGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_update**
> Endpoint endpoints_update(id, body=body)

Update Endpoint

Updates the metadata of the endpoint identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the endpoint.
body = azure_speech_api.EndpointUpdate() # EndpointUpdate | The updated values for the endpoint. (optional)

try:
    # Update Endpoint
    api_response = api_instance.endpoints_update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->endpoints_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the endpoint. | 
 **body** | [**EndpointUpdate**](EndpointUpdate.md)| The updated values for the endpoint. | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_create**
> Evaluation evaluations_create(body=body)

Create Evaluation

Creates a new evaluation.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
body = azure_speech_api.Evaluation() # Evaluation | The details of the new evaluation. (optional)

try:
    # Create Evaluation
    api_response = api_instance.evaluations_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->evaluations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Evaluation**](Evaluation.md)| The details of the new evaluation. | [optional] 

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_delete**
> evaluations_delete(id)

Delete Evaluation

Deletes the evaluation identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the evaluation.

try:
    # Delete Evaluation
    api_instance.evaluations_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->evaluations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the evaluation. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_get**
> Evaluation evaluations_get(id)

Get Evaluation

Gets the evaluation identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the evaluation.

try:
    # Get Evaluation
    api_response = api_instance.evaluations_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->evaluations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the evaluation. | 

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_get_file**
> File evaluations_get_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Evaluation File

Gets one specific file (identified with fileId) from an evaluation (identified with id).

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the evaluation.
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the file.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)

try:
    # Get Evaluation File
    api_response = api_instance.evaluations_get_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->evaluations_get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the evaluation. | 
 **file_id** | [**str**](.md)| Format - uuid. The identifier of the file. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_list**
> PaginatedEvaluations evaluations_list(skip=skip, top=top, filter=filter)

Get Evaluations

Gets the list of evaluations for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available evaluations.              <ul><li><b>Supported properties:</b> displayName, description, createdDateTime, lastActionDateTime, status and locale.                </li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=displayName eq 'My evaluation'```</li></ul> (optional)

try:
    # Get Evaluations
    api_response = api_instance.evaluations_list(skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->evaluations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available evaluations.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; displayName, description, createdDateTime, lastActionDateTime, status and locale.                &lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;displayName eq &#x27;My evaluation&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedEvaluations**](PaginatedEvaluations.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_list_files**
> PaginatedFiles evaluations_list_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top, filter=filter)

Get Evaluation Files

Gets the files of the evaluation identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the evaluation.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available files.              <ul><li><b>Supported properties:</b> name, createdDateTime, kind.</li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=name eq 'myaudio.wav' and kind eq 'Audio'```</li></ul> (optional)

try:
    # Get Evaluation Files
    api_response = api_instance.evaluations_list_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->evaluations_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the evaluation. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available files.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; name, createdDateTime, kind.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;name eq &#x27;myaudio.wav&#x27; and kind eq &#x27;Audio&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_list_supported_locales**
> EvaluationsLocalesGet200ApplicationJsonResponse evaluations_list_supported_locales()

Get Supported Locales for Evaluations

Gets a list of supported locales for evaluations.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))

try:
    # Get Supported Locales for Evaluations
    api_response = api_instance.evaluations_list_supported_locales()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->evaluations_list_supported_locales: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EvaluationsLocalesGet200ApplicationJsonResponse**](EvaluationsLocalesGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_update**
> Evaluation evaluations_update(id, body=body)

Update Evaluation

Updates the mutable details of the evaluation identified by its id.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the evaluation.
body = azure_speech_api.EvaluationUpdate() # EvaluationUpdate | The object containing the updated fields of the evaluation. (optional)

try:
    # Update Evaluation
    api_response = api_instance.evaluations_update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->evaluations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the evaluation. | 
 **body** | [**EvaluationUpdate**](EvaluationUpdate.md)| The object containing the updated fields of the evaluation. | [optional] 

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_status_get**
> ServiceHealth health_status_get()

Get Health Status

Returns the overall health of the service and optionally of the different subcomponents.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))

try:
    # Get Health Status
    api_response = api_instance.health_status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->health_status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceHealth**](ServiceHealth.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_copy_to**
> CustomModel models_copy_to(id, body=body)

Copy Model

This method can be used to copy a model from one location to another. If the target subscription key belongs to a subscription created for another location, the model will be copied to that location. Only adapted models are allowed to copy to another subscription.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the model that will be copied.
body = azure_speech_api.ModelCopy() # ModelCopy | The body contains the subscription key of the target subscription. (optional)

try:
    # Copy Model
    api_response = api_instance.models_copy_to(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->models_copy_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the model that will be copied. | 
 **body** | [**ModelCopy**](ModelCopy.md)| The body contains the subscription key of the target subscription. | [optional] 

### Return type

[**CustomModel**](CustomModel.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_create**
> CustomModel models_create(body=body)

Create Model

Creates a new model.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
body = azure_speech_api.CustomModel() # CustomModel | The details of the new model. (optional)

try:
    # Create Model
    api_response = api_instance.models_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->models_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomModel**](CustomModel.md)| The details of the new model. | [optional] 

### Return type

[**CustomModel**](CustomModel.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_delete**
> models_delete(id)

Delete Model

Deletes the model identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the model.

try:
    # Delete Model
    api_instance.models_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->models_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the model. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get_base_model**
> BaseModel models_get_base_model(id)

Get Base Model

Gets the base model identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the base model.

try:
    # Get Base Model
    api_response = api_instance.models_get_base_model(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->models_get_base_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the base model. | 

### Return type

[**BaseModel**](BaseModel.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get_base_model_manifest**
> ModelManifest models_get_base_model_manifest(id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Base Model Manifest

Returns an manifest for this base model which can be used in an on-premise container.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The ID of the model to generate a manifest for.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)

try:
    # Get Base Model Manifest
    api_response = api_instance.models_get_base_model_manifest(id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->models_get_base_model_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The ID of the model to generate a manifest for. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 

### Return type

[**ModelManifest**](ModelManifest.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get_custom_model**
> CustomModel models_get_custom_model(id)

Get Model

Gets the model identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the model.

try:
    # Get Model
    api_response = api_instance.models_get_custom_model(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->models_get_custom_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the model. | 

### Return type

[**CustomModel**](CustomModel.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get_custom_model_manifest**
> ModelManifest models_get_custom_model_manifest(id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Model Manifest

Returns an manifest for this model which can be used in an on-premise container.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The ID of the model to generate a manifest for.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)

try:
    # Get Model Manifest
    api_response = api_instance.models_get_custom_model_manifest(id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->models_get_custom_model_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The ID of the model to generate a manifest for. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 

### Return type

[**ModelManifest**](ModelManifest.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get_file**
> File models_get_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Model File

Gets one specific file (identified with fileId) from a model (identified with id).

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the model.
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the file.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)

try:
    # Get Model File
    api_response = api_instance.models_get_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->models_get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the model. | 
 **file_id** | [**str**](.md)| Format - uuid. The identifier of the file. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_list_base_models**
> PaginatedBaseModels models_list_base_models(skip=skip, top=top, filter=filter)

Get Base Models

Gets the list of base models for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available base models.              <ul><li><b>Supported properties: </b> displayName, description, createdDateTime, lastActionDateTime, status, locale.                </li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=status eq 'NotStarted' or status eq 'Running'```</li></ul> (optional)

try:
    # Get Base Models
    api_response = api_instance.models_list_base_models(skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->models_list_base_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available base models.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties: &lt;/b&gt; displayName, description, createdDateTime, lastActionDateTime, status, locale.                &lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;status eq &#x27;NotStarted&#x27; or status eq &#x27;Running&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedBaseModels**](PaginatedBaseModels.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_list_custom_models**
> PaginatedCustomModels models_list_custom_models(skip=skip, top=top, filter=filter)

Get Models

Gets the list of custom models for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available models.              <ul><li><b>Supported properties: </b> displayName, description, createdDateTime, lastActionDateTime, status, locale.                </li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=status eq 'NotStarted' or status eq 'Running'```</li></ul> (optional)

try:
    # Get Models
    api_response = api_instance.models_list_custom_models(skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->models_list_custom_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available models.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties: &lt;/b&gt; displayName, description, createdDateTime, lastActionDateTime, status, locale.                &lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;status eq &#x27;NotStarted&#x27; or status eq &#x27;Running&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedCustomModels**](PaginatedCustomModels.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_list_files**
> PaginatedFiles models_list_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top, filter=filter)

Get Model Files

Gets the files of the model identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the model.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available files.              <ul><li><b>Supported properties:</b> name, createdDateTime, kind.</li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=name eq 'myaudio.wav' and kind eq 'Audio'```</li></ul> (optional)

try:
    # Get Model Files
    api_response = api_instance.models_list_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->models_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the model. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available files.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; name, createdDateTime, kind.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;name eq &#x27;myaudio.wav&#x27; and kind eq &#x27;Audio&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_list_supported_locales**
> ModelsLocalesGet200ApplicationJsonResponse models_list_supported_locales()

Get Supported Locales for Models

Gets a list of supported locales for model adaptation.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))

try:
    # Get Supported Locales for Models
    api_response = api_instance.models_list_supported_locales()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->models_list_supported_locales: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ModelsLocalesGet200ApplicationJsonResponse**](ModelsLocalesGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_update**
> CustomModel models_update(id, body=body)

Update Model

Updates the metadata of the model identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the model.
body = azure_speech_api.ModelUpdate() # ModelUpdate | The updated values for the model. (optional)

try:
    # Update Model
    api_response = api_instance.models_update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->models_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the model. | 
 **body** | [**ModelUpdate**](ModelUpdate.md)| The updated values for the model. | [optional] 

### Return type

[**CustomModel**](CustomModel.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_create**
> Project projects_create(body=body)

Create Project

Creates a new project.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
body = azure_speech_api.Project() # Project | The details of the project. (optional)

try:
    # Create Project
    api_response = api_instance.projects_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Project**](Project.md)| The details of the project. | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_delete**
> projects_delete(id)

Delete Project

Deletes the project identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the project.

try:
    # Delete Project
    api_instance.projects_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the project. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get**
> Project projects_get(id)

Get Project

Gets the project identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the project.

try:
    # Get Project
    api_response = api_instance.projects_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the project. | 

### Return type

[**Project**](Project.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list**
> PaginatedProjects projects_list(skip=skip, top=top, filter=filter)

Get Projects

Gets the list of projects for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available projects.              <ul><li><b>Supported properties:</b> displayName, description, createdDateTime, locale.</li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=displayName eq 'My test'```</li></ul> (optional)

try:
    # Get Projects
    api_response = api_instance.projects_list(skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available projects.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; displayName, description, createdDateTime, locale.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;displayName eq &#x27;My test&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedProjects**](PaginatedProjects.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list_datasets**
> PaginatedDatasets projects_list_datasets(id, skip=skip, top=top, filter=filter)

Get Datasets for Project

Gets the list of datasets for specified project.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the project.
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available datasets.              <ul><li><b>Supported properties:</b> displayName, description, createdDateTime, lastActionDateTime, status, locale, kind.                </li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=createdDateTime gt 2022-02-01T11:00:00Z```</li></ul> (optional)

try:
    # Get Datasets for Project
    api_response = api_instance.projects_list_datasets(id, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_list_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the project. | 
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available datasets.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; displayName, description, createdDateTime, lastActionDateTime, status, locale, kind.                &lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;createdDateTime gt 2022-02-01T11:00:00Z&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedDatasets**](PaginatedDatasets.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list_endpoints**
> PaginatedEndpoints projects_list_endpoints(id, skip=skip, top=top, filter=filter)

Get Endpoints for Project

Gets the list of endpoints for specified project.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the project.
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available endpoints.              <ul><li><b>Supported properties:</b> displayName, description, createdDateTime, lastActionDateTime, status, locale.                </li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=locale eq 'en-US'```</li></ul> (optional)

try:
    # Get Endpoints for Project
    api_response = api_instance.projects_list_endpoints(id, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_list_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the project. | 
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available endpoints.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; displayName, description, createdDateTime, lastActionDateTime, status, locale.                &lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;locale eq &#x27;en-US&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedEndpoints**](PaginatedEndpoints.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list_evaluations**
> PaginatedEvaluations projects_list_evaluations(id, skip=skip, top=top, filter=filter)

Get Evaluations for Project

Gets the list of evaluations for specified project.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the project.
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available evaluations.              <ul><li><b>Supported properties:</b> displayName, description, createdDateTime, lastActionDateTime, status and locale.                </li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=displayName eq 'My evaluation'```</li></ul> (optional)

try:
    # Get Evaluations for Project
    api_response = api_instance.projects_list_evaluations(id, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_list_evaluations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the project. | 
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available evaluations.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; displayName, description, createdDateTime, lastActionDateTime, status and locale.                &lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;displayName eq &#x27;My evaluation&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedEvaluations**](PaginatedEvaluations.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list_models**
> PaginatedCustomModels projects_list_models(id, skip=skip, top=top, filter=filter)

Get Models for Project

Gets the list of models for specified project.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the project.
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available models.              <ul><li><b>Supported properties: </b> displayName, description, createdDateTime, lastActionDateTime, status, locale.                </li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=status eq 'NotStarted' or status eq 'Running'```</li></ul> (optional)

try:
    # Get Models for Project
    api_response = api_instance.projects_list_models(id, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_list_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the project. | 
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available models.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties: &lt;/b&gt; displayName, description, createdDateTime, lastActionDateTime, status, locale.                &lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;status eq &#x27;NotStarted&#x27; or status eq &#x27;Running&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedCustomModels**](PaginatedCustomModels.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list_supported_locales**
> ProjectsLocalesGet200ApplicationJsonResponse projects_list_supported_locales()

Get Supported Locales for Projects

Gets the list of supported locales.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))

try:
    # Get Supported Locales for Projects
    api_response = api_instance.projects_list_supported_locales()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_list_supported_locales: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProjectsLocalesGet200ApplicationJsonResponse**](ProjectsLocalesGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list_transcriptions**
> PaginatedTranscriptions projects_list_transcriptions(id, skip=skip, top=top, filter=filter)

Get Transcriptions for Project

Gets the list of transcriptions for specified project.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the project.
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available transcriptions.              <ul><li><b>Supported properties:</b> displayName, description, createdDateTime, lastActionDateTime, status, locale.                </li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=createdDateTime gt 2022-02-01T11:00:00Z```</li></ul> (optional)

try:
    # Get Transcriptions for Project
    api_response = api_instance.projects_list_transcriptions(id, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_list_transcriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the project. | 
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available transcriptions.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; displayName, description, createdDateTime, lastActionDateTime, status, locale.                &lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;createdDateTime gt 2022-02-01T11:00:00Z&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedTranscriptions**](PaginatedTranscriptions.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_update**
> Project projects_update(id, body=body)

Update Project

Updates the project identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the project.
body = azure_speech_api.ProjectUpdate() # ProjectUpdate | The updated values for the project. (optional)

try:
    # Update Project
    api_response = api_instance.projects_update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the project. | 
 **body** | [**ProjectUpdate**](ProjectUpdate.md)| The updated values for the project. | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_create**
> Transcription transcriptions_create(body=body)

Create Transcription

Creates a new transcription.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
body = azure_speech_api.Transcription() # Transcription | The details of the new transcription. (optional)

try:
    # Create Transcription
    api_response = api_instance.transcriptions_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transcriptions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Transcription**](Transcription.md)| The details of the new transcription. | [optional] 

### Return type

[**Transcription**](Transcription.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_delete**
> transcriptions_delete(id)

Delete Transcription

Deletes the specified transcription task.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the transcription.

try:
    # Delete Transcription
    api_instance.transcriptions_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->transcriptions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the transcription. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_get**
> Transcription transcriptions_get(id)

Get Transcription

Gets the transcription identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the transcription.

try:
    # Get Transcription
    api_response = api_instance.transcriptions_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transcriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the transcription. | 

### Return type

[**Transcription**](Transcription.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_get_file**
> File transcriptions_get_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Transcription File

Gets one specific file (identified with fileId) from a transcription (identified with id).

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the transcription.
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the file.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)

try:
    # Get Transcription File
    api_response = api_instance.transcriptions_get_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transcriptions_get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the transcription. | 
 **file_id** | [**str**](.md)| Format - uuid. The identifier of the file. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_list**
> PaginatedTranscriptions transcriptions_list(skip=skip, top=top, filter=filter)

Get Transcriptions

Gets a list of transcriptions for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available transcriptions.              <ul><li><b>Supported properties:</b> displayName, description, createdDateTime, lastActionDateTime, status, locale.                </li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=createdDateTime gt 2022-02-01T11:00:00Z```</li></ul> (optional)

try:
    # Get Transcriptions
    api_response = api_instance.transcriptions_list(skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transcriptions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available transcriptions.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; displayName, description, createdDateTime, lastActionDateTime, status, locale.                &lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;createdDateTime gt 2022-02-01T11:00:00Z&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedTranscriptions**](PaginatedTranscriptions.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_list_files**
> PaginatedFiles transcriptions_list_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top, filter=filter)

Get Transcription Files

Gets the files of the transcription identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the transcription.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available files.              <ul><li><b>Supported properties:</b> name, createdDateTime, kind.</li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=name eq 'myaudio.wav.json' and kind eq 'Transcription'```</li></ul> (optional)

try:
    # Get Transcription Files
    api_response = api_instance.transcriptions_list_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transcriptions_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the transcription. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available files.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; name, createdDateTime, kind.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;name eq &#x27;myaudio.wav.json&#x27; and kind eq &#x27;Transcription&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_list_supported_locales**
> TranscriptionsLocalesGet200ApplicationJsonResponse transcriptions_list_supported_locales()

Get Supported Locales for Transcriptions

Gets a list of supported locales for offline transcriptions.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))

try:
    # Get Supported Locales for Transcriptions
    api_response = api_instance.transcriptions_list_supported_locales()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transcriptions_list_supported_locales: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TranscriptionsLocalesGet200ApplicationJsonResponse**](TranscriptionsLocalesGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_update**
> Transcription transcriptions_update(id, body=body)

Update Transcription

Updates the mutable details of the transcription identified by its ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the transcription.
body = azure_speech_api.TranscriptionUpdate() # TranscriptionUpdate | The updated values for the transcription. (optional)

try:
    # Update Transcription
    api_response = api_instance.transcriptions_update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transcriptions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the transcription. | 
 **body** | [**TranscriptionUpdate**](TranscriptionUpdate.md)| The updated values for the transcription. | [optional] 

### Return type

[**Transcription**](Transcription.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_create**
> WebHook web_hooks_create(body=body)

Create Web Hook

If the property secret in the configuration is present and contains a non-empty string, it will be used to create a SHA256 hash of the payload with the secret as HMAC key. This hash will be set as X-MicrosoftSpeechServices-Signature header when calling back into the registered URL.              When calling back into the registered URL, the request will contain a X-MicrosoftSpeechServices-Event header containing one of the registered event types. There will be one request per registered event type.              After successfully registering the web hook, it will not be usable until a challenge/response is completed. To do this, a request with the event type challenge will be made with a query parameter called validationToken. Respond to the challenge with a 200 OK containing the value of the validationToken query parameter as the response body. When the challenge/response is successfully completed, the web hook will begin receiving events.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
body = azure_speech_api.WebHook() # WebHook | The details of the new web hook. (optional)

try:
    # Create Web Hook
    api_response = api_instance.web_hooks_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->web_hooks_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebHook**](WebHook.md)| The details of the new web hook. | [optional] 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_delete**
> web_hooks_delete(id)

Delete Web Hook

Deletes the web hook identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the web hook.

try:
    # Delete Web Hook
    api_instance.web_hooks_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->web_hooks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the web hook. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_get**
> WebHook web_hooks_get(id)

Get Web Hook

Gets the web hook identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the web hook.

try:
    # Get Web Hook
    api_response = api_instance.web_hooks_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->web_hooks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the web hook. | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_list**
> PaginatedWebHooks web_hooks_list(skip=skip, top=top, filter=filter)

Get Web Hooks

Gets the list of web hooks for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available hooks.              <ul><li><b>Supported properties:</b> displayName, description, createdDateTime, lastActionDateTime, status and webUrl.</li><li><b>Operators:</b><ul><li>eq, ne are supported for all properties.</li><li>gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.</li><li>and, or, not are supported.</li></ul></li><li><b>Example:</b>```filter=displayName eq 'test'```</li></ul> (optional)

try:
    # Get Web Hooks
    api_response = api_instance.web_hooks_list(skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->web_hooks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available hooks.              &lt;ul&gt;&lt;li&gt;&lt;b&gt;Supported properties:&lt;/b&gt; displayName, description, createdDateTime, lastActionDateTime, status and webUrl.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Operators:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;eq, ne are supported for all properties.&lt;/li&gt;&lt;li&gt;gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.&lt;/li&gt;&lt;li&gt;and, or, not are supported.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;&lt;b&gt;Example:&lt;/b&gt;&#x60;&#x60;&#x60;filter&#x3D;displayName eq &#x27;test&#x27;&#x60;&#x60;&#x60;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**PaginatedWebHooks**](PaginatedWebHooks.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_ping**
> web_hooks_ping(id)

Ping Web Hook

The request body of the POST request sent to the registered web hook URL is of the same shape as in the GET request for a specific hook. The Swagger Schema ID of the model is WebHookV3.              The request will contain a X-MicrosoftSpeechServices-Event header with the value ping. If the web hook was registered with a secret it will contain a X-MicrosoftSpeechServices-Signature header with an SHA256 hash of the payload with the secret as HMAC key. The hash is base64 encoded.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the web hook to ping.

try:
    # Ping Web Hook
    api_instance.web_hooks_ping(id)
except ApiException as e:
    print("Exception when calling DefaultApi->web_hooks_ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the web hook to ping. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_test**
> web_hooks_test(id)

Test Web Hook

The payload will be generated from the last entity that would have invoked the web hook. If no entity is present for none of the registered event types, the POST will respond with 204. If a test request can be made, it will respond with 200. The request will contain a X-MicrosoftSpeechServices-Event header with the respective registered event type. If the web hook was registered with a secret it will contain a X-MicrosoftSpeechServices-Signature header with an SHA256 hash of the payload with the secret as HMAC key. The hash is base64 encoded.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the web hook to ping.

try:
    # Test Web Hook
    api_instance.web_hooks_test(id)
except ApiException as e:
    print("Exception when calling DefaultApi->web_hooks_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the web hook to ping. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_update**
> WebHook web_hooks_update(id, body=body)

Update Web Hook

If the property secret in the configuration is omitted or contains an empty string, future callbacks won't contain X-MicrosoftSpeechServices-Signature headers. If the property contains a non-empty string, it will be used to create a SHA256 hash of the payload with the secret as HMAC key. This hash will be set as X-MicrosoftSpeechServices-Signature header when calling back into the registered URL.              If the URL changes,  the web hook will stop receiving events until a challenge/response is completed. To do this, a request with the event type challenge will be made with a query parameter called validationToken. Respond to the challenge with a 200 OK containing the value of the validationToken query parameter as the response body. When the challenge/response is successfully completed, the web hook will begin receiving events.

### Example
```python
from __future__ import print_function
import time
import azure_speech_api
from azure_speech_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = azure_speech_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = azure_speech_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = azure_speech_api.DefaultApi(azure_speech_api.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Format - uuid. The identifier of the web hook.
body = azure_speech_api.WebHookUpdate() # WebHookUpdate | The updated values for the web hook. (optional)

try:
    # Update Web Hook
    api_response = api_instance.web_hooks_update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->web_hooks_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Format - uuid. The identifier of the web hook. | 
 **body** | [**WebHookUpdate**](WebHookUpdate.md)| The updated values for the web hook. | [optional] 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

