- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- value (string; optional):
    Decoded QR code content.

- type (a value equal to: 'canvas', 'svg'; default 'canvas'):
    QR code renderer. Supported values: `'canvas'`, `'svg'`. Default: `'canvas'`.

- icon (string; optional):
    URL of the image embedded in the QR code.

- size (number; default 160):
    QR code side length in pixels. Default: `160`.

- iconSize (dict; default 40):
    Side length of the embedded QR code image in pixels. Default: `40`.

    `iconSize` is a number | dict with keys:

    - width (number; optional)

    - height (number; optional)

- color (string; default '#000'):
    QR code color. Default: `'#000'`.

- bgColor (string; default 'transparent'):
    QR code background color. Default: `'transparent'`.

- bordered (boolean; default True):
    Whether to show a border around the QR code. Default: `True`.

- errorLevel (a value equal to: 'L', 'M', 'Q', 'H'; default 'M'):
    QR code error correction level. Supported values: `'L'`, `'M'`, `'Q'`, `'H'`. Default: `'M'`.

- status (a value equal to: 'active', 'expired', 'loading', 'scanned'; default 'active'):
    QR code status. Supported values: `'active'`, `'expired'`, `'loading'`, `'scanned'`. Default: `'active'`.

- expires (number; optional):
    QR code expiry time in seconds. Changes the status to `'expired'` when reached.

- autoSpin (boolean; default False):
    Whether to enter the `loading` state while `value` is being updated by a callback. Default: `False`.

- refreshClicks (number; default 0):
    Cumulative refresh button clicks; only applies when `status` is `'expired'`. Default: `0`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
