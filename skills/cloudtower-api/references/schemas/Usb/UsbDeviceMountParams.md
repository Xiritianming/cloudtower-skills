# UsbDeviceMountParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [UsbDeviceWhereInput](../Usb/UsbDeviceWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vms` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vm_id` | string | No |  |

