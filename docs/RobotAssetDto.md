# RobotAssetDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The asset name. | 
**value_type** | **str** | Defines the type of value stored by the asset. | [optional] 
**string_value** | **str** | The value of the asset when the value type is Text. Empty when the value type is not Text. | [optional] 
**bool_value** | **bool** | The value of the asset when the value type is Bool. False when the value type is not Bool. | [optional] 
**int_value** | **int** | The value of the asset when the value type is Integer. 0 when the value type is not Integer. | [optional] 
**credential_username** | **str** | The user name when the value type is Credential. Empty when the value type is not Credential. | [optional] 
**credential_password** | **str** | The password when the value type is Credential. Empty when the value type is not Credential. | [optional] 
**external_name** | **str** | Contains the value of the key in the external store used to store the credentials. | [optional] 
**credential_store_id** | **int** | The Credential Store used to store the credentials. | [optional] 
**key_value_list** | [**list[CustomKeyValuePair]**](CustomKeyValuePair.md) | A collection of key value pairs when the type is KeyValueList. Empty when the value type is not KeyValueList. | [optional] 
**connection_data** | [**CredentialsConnectionData**](CredentialsConnectionData.md) |  | [optional] 
**id** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


