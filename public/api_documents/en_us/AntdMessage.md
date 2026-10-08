- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string; optional):
    CSS class name of the component.

- content (string; optional):
    Message content.

- type (a value equal to: 'default', 'success', 'error', 'info', 'warning'; default 'default'):
    Message type. Supported values: `'default'`, `'success'`, `'error'`, `'info'`, `'warning'`. Default: 'default'.

- duration (number; default 3):
    Seconds before the message closes automatically. Set to `0` to keep it open. Default: `3`.

- top (number; default 8):
    Distance of the message from the top in pixels. Default: `8`.

- maxCount (number; optional):
    Maximum number of messages shown simultaneously.

- icon (string; optional):
    Custom prefix icon name, equivalent to the `AntdIcon` `icon` property.

- iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; default 'AntdIcon'):
    Renderer for custom prefix icons. Supported values: `'AntdIcon'`, `'fontawesome'`.
