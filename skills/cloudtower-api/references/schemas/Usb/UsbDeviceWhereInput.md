# UsbDeviceWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [UsbDeviceWhereInput](../Usb/UsbDeviceWhereInput.md) | No |  |
| `NOT` | Array of [UsbDeviceWhereInput](../Usb/UsbDeviceWhereInput.md) | No |  |
| `OR` | Array of [UsbDeviceWhereInput](../Usb/UsbDeviceWhereInput.md) | No |  |
| `binded` | boolean | No |  |
| `binded_not` | boolean | No |  |
| `description` | string | No |  |
| `description_contains` | string | No |  |
| `description_ends_with` | string | No |  |
| `description_gt` | string | No |  |
| `description_gte` | string | No |  |
| `description_in` | string[] | No |  |
| `description_lt` | string | No |  |
| `description_lte` | string | No |  |
| `description_not` | string | No |  |
| `description_not_contains` | string | No |  |
| `description_not_ends_with` | string | No |  |
| `description_not_in` | string[] | No |  |
| `description_not_starts_with` | string | No |  |
| `description_starts_with` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `host` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `id` | string | No |  |
| `id_contains` | string | No |  |
| `id_ends_with` | string | No |  |
| `id_gt` | string | No |  |
| `id_gte` | string | No |  |
| `id_in` | string[] | No |  |
| `id_lt` | string | No |  |
| `id_lte` | string | No |  |
| `id_not` | string | No |  |
| `id_not_contains` | string | No |  |
| `id_not_ends_with` | string | No |  |
| `id_not_in` | string[] | No |  |
| `id_not_starts_with` | string | No |  |
| `id_starts_with` | string | No |  |
| `local_created_at` | string | No |  |
| `local_created_at_gt` | string | No |  |
| `local_created_at_gte` | string | No |  |
| `local_created_at_in` | string[] | No |  |
| `local_created_at_lt` | string | No |  |
| `local_created_at_lte` | string | No |  |
| `local_created_at_not` | string | No |  |
| `local_created_at_not_in` | string[] | No |  |
| `local_id` | string | No |  |
| `local_id_contains` | string | No |  |
| `local_id_ends_with` | string | No |  |
| `local_id_gt` | string | No |  |
| `local_id_gte` | string | No |  |
| `local_id_in` | string[] | No |  |
| `local_id_lt` | string | No |  |
| `local_id_lte` | string | No |  |
| `local_id_not` | string | No |  |
| `local_id_not_contains` | string | No |  |
| `local_id_not_ends_with` | string | No |  |
| `local_id_not_in` | string[] | No |  |
| `local_id_not_starts_with` | string | No |  |
| `local_id_starts_with` | string | No |  |
| `manufacturer` | string | No |  |
| `manufacturer_contains` | string | No |  |
| `manufacturer_ends_with` | string | No |  |
| `manufacturer_gt` | string | No |  |
| `manufacturer_gte` | string | No |  |
| `manufacturer_in` | string[] | No |  |
| `manufacturer_lt` | string | No |  |
| `manufacturer_lte` | string | No |  |
| `manufacturer_not` | string | No |  |
| `manufacturer_not_contains` | string | No |  |
| `manufacturer_not_ends_with` | string | No |  |
| `manufacturer_not_in` | string[] | No |  |
| `manufacturer_not_starts_with` | string | No |  |
| `manufacturer_starts_with` | string | No |  |
| `name` | string | No |  |
| `name_contains` | string | No |  |
| `name_ends_with` | string | No |  |
| `name_gt` | string | No |  |
| `name_gte` | string | No |  |
| `name_in` | string[] | No |  |
| `name_lt` | string | No |  |
| `name_lte` | string | No |  |
| `name_not` | string | No |  |
| `name_not_contains` | string | No |  |
| `name_not_ends_with` | string | No |  |
| `name_not_in` | string[] | No |  |
| `name_not_starts_with` | string | No |  |
| `name_starts_with` | string | No |  |
| `size` | integer (int64) | No |  |
| `size_gt` | integer (int64) | No |  |
| `size_gte` | integer (int64) | No |  |
| `size_in` | integer[] | No |  |
| `size_lt` | integer (int64) | No |  |
| `size_lte` | integer (int64) | No |  |
| `size_not` | integer (int64) | No |  |
| `size_not_in` | integer[] | No |  |
| `status` | [UsbDeviceStatus](../Usb/UsbDeviceStatus.md) | No |  |
| `status_in` | Array of [UsbDeviceStatus](../Usb/UsbDeviceStatus.md) | No |  |
| `status_not` | [UsbDeviceStatus](../Usb/UsbDeviceStatus.md) | No |  |
| `status_not_in` | Array of [UsbDeviceStatus](../Usb/UsbDeviceStatus.md) | No |  |
| `usb_type` | string | No |  |
| `usb_type_contains` | string | No |  |
| `usb_type_ends_with` | string | No |  |
| `usb_type_gt` | string | No |  |
| `usb_type_gte` | string | No |  |
| `usb_type_in` | string[] | No |  |
| `usb_type_lt` | string | No |  |
| `usb_type_lte` | string | No |  |
| `usb_type_not` | string | No |  |
| `usb_type_not_contains` | string | No |  |
| `usb_type_not_ends_with` | string | No |  |
| `usb_type_not_in` | string[] | No |  |
| `usb_type_not_starts_with` | string | No |  |
| `usb_type_starts_with` | string | No |  |
| `vms_every` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vms_none` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vms_some` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |

