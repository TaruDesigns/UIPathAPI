# TransactionResultDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_successful** | **bool** | States if the processing was successful or not. | [optional] 
**processing_exception** | [**ProcessingExceptionDto**](ProcessingExceptionDto.md) |  | [optional] 
**defer_date** | **datetime** | The earliest date and time at which the item is available for processing. If empty the item can be processed as soon as possible. | [optional] 
**due_date** | **datetime** | The latest date and time at which the item should be processed. If empty the item can be processed at any given time. | [optional] 
**output** | **dict(str, object)** | A collection of key value pairs containing custom data resulted after successful processing. | [optional] 
**analytics** | **dict(str, object)** | A collection of key value pairs containing custom data for further analytics processing. | [optional] 
**progress** | **str** | String field which is used to keep track of the business flow progress. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


