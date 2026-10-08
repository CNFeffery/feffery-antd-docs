- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string; optional):
    CSS class name of the component.

- markClassName (string; optional):
    CSS class name for the watermark layer.

- markStyle (dict; optional):
    CSS styles for the watermark layer.

- content (string | list of strings; optional):
    Watermark content. An array renders multiple lines.

- rotate (number; default -22):
    Watermark rotation angle. Default: `-22`.

- zIndex (number; optional):
    Watermark z-index.

- fontColor (string; optional):
    Watermark text color.

- fontSize (number; default 16):
    Watermark font size. Default: `16`.

- gapX (number; default 212):
    Horizontal gap between watermarks in pixels. Default: `212`.

- gapY (number; default 222):
    Vertical gap between watermarks in pixels. Default: `222`.

- image (string; optional):
    Image watermark URL.

- width (number; optional):
    Image watermark width in pixels.

- height (number; optional):
    Image watermark height in pixels.

- inherit (boolean; default True):
    Whether the watermark also covers popups such as `AntdModal` and `AntdDrawer`. Default: `True`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
