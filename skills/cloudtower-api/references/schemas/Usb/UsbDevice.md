# UsbDevice

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `binded` | boolean | Yes |  |
| `description` | string | Yes |  |
| `host` | [NestedHost](../Nested/NestedHost.md) | Yes |  |
| `id` | string | Yes |  |
| `local_created_at` | string | Yes |  |
| `local_id` | string | Yes |  |
| `manufacturer` | string | Yes |  |
| `name` | string | Yes |  |
| `size` | integer (int64) | Yes |  |
| `status` | [UsbDeviceStatus](../Usb/UsbDeviceStatus.md) | Yes |  |
| `usb_type` | string | Yes |  |
| `entityAsyncStatus` | any | No |  |
| `vms` | Array of [NestedVm](../Nested/NestedVm.md) | No |  |
| `vm` | any | No |  |

