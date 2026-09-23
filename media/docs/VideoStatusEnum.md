# VideoStatusEnum

An enumerated value indicating the video's status. The available status values are <code>PENDING_UPLOAD</code>, <code>PROCESSING</code>, <code>PROCESSING_FAILED</code>, <code>BLOCKED</code>, and <code>LIVE</code>. | - **PENDING_UPLOAD**: The video is pending upload. The video is being associated with a video ID and has not been uploaded yet. - **PROCESSING**: After a video upload is successfully completed, the status will show as PROCESSING until the video reaches one of the terminal states of <code>LIVE</code>, <code>BLOCKED</code>, or <code>PROCESSING_FAILED</code>. - **PROCESSING_FAILED**: The video failed to process. If processing fails, it could be because the file is corrupted, is too large, or its size doesn't match what was provided in the metadata. Refer to the error messages to determine the cause of the video's failure to upload. - **BLOCKED**: The video is blocked. A video might be BLOCKED if it contains malware, or if it is blocked by the video moderation feature. - **LIVE**: The video is live. When the status of the video is <code>LIVE</code>, this indicates the file has been processed and uploaded successfully. The <strong>playList</strong> providing URLs for the video in DASH and HLS streaming video protocols will only be generated if the video uploads successfully.

## Enum

* `PENDING_UPLOAD` (value: `'PENDING_UPLOAD'`)

* `PROCESSING` (value: `'PROCESSING'`)

* `PROCESSING_FAILED` (value: `'PROCESSING_FAILED'`)

* `BLOCKED` (value: `'BLOCKED'`)

* `LIVE` (value: `'LIVE'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


