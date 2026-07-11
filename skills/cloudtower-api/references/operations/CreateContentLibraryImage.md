# POST /v2/api/upload-content-library-image

**Resource:** [ContentLibraryImage](../resources/ContentLibraryImage.md)
**Operation ID:** `CreateContentLibraryImage`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `multipart/form-data`

**Schema** (inline):

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `file` | string (binary) | Yes |  |
| `clusters` | string | Yes |  |
| `name` | string | No |  |
| `size` | string | No |  |
| `size_unit` | string | No |  |
| `description` | string | No |  |
| `upload_task_id` | string | No |  |

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 304 | Not modified |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [UploadTask](../schemas/Upload/UploadTask.md)

## Security

- **Authorization**
