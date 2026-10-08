- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, child elements within the divider.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- innerTextOrientation (a value equal to: 'left', 'center', 'right'; default 'center'):
    Alignment of the child elements, options include `'left'`, `'center'`, `'right'`. Default value: `'center'`.

- isDashed (boolean; default False):
    Whether to render as a dashed line. Default value: `False`.

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    Direction of the divider, options include `'horizontal'`, `'vertical'`. Default value: `'horizontal'`.

- fontSize (string | number; optional):
    Font size of the child elements.

- lineColor (string; optional):
    Color of the divider line.

- fontStyle (string; optional):
    Font style of the child elements.

- fontWeight (string; optional):
    Font weight of the child elements.

- fontFamily (string; optional):
    Font of the child elements.

- fontColor (string; optional):
    Font color of the child elements.

- variant (a value equal to: 'dashed', 'dotted', 'solid'; default 'solid'):
    Variant of the divider, options include `'dashed'` (dashed line), `'dotted'` (dotted line), `'solid'` (solid line). Default value: `'solid'`.

- plain (boolean; default True):
    Whether the text is displayed as normal body text. Default: `True`.

- size (a value equal to: 'small', 'middle', 'large'; optional):
    Gap size. Only applies when ``direction='horizontal'``. Supported values: `'small'`, `'middle'`, `'large'`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
