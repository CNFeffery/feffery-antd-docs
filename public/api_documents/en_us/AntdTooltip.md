- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Tooltip target element. Supports components.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- styles (dict; optional):
    Fine-grained CSS styles for child elements.

    `styles` is a dict with keys:

    - root (dict; optional):
        CSS styles for the root element, including the arrow and content.

    - body (dict; optional):
        CSS styles for the body element.

- classNames (dict; optional):
    Fine-grained CSS class names for child elements.

    `classNames` is a dict with keys:

    - root (string; optional):
        CSS class name for the root element, including the arrow and content.

    - body (string; optional):
        CSS class name for the body element.

- title (a list of or a singular dash component, string or number; optional):
    Tooltip content. Supports components.

- placement (a value equal to: 'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'; default 'top'):
    Tooltip placement. Supported values: `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`, `'leftTop'`, `'leftBottom'`, `'rightTop'`, `'rightBottom'`. Default: `'top'`.

- color (string; optional):
    Background color.

- mouseEnterDelay (number; default 0.1):
    Delay in seconds between mouse enter and showing the tooltip. Default: `0.1`.

- mouseLeaveDelay (number; default 0.1):
    Delay in seconds between mouse leave and hiding the tooltip. Default: `0.1`.

- trigger (a value equal to: 'hover', 'focus', 'click' | list of a value equal to: 'hover', 'focus', 'click's; default 'hover'):
    Trigger events; multiple triggers can be combined. Supported values: `'hover'`, `'focus'`, `'click'`. Default: `'hover'`.

- zIndex (number; optional):
    Tooltip z-index.

- arrow (a value equal to: 'show', 'hide', 'center'; default 'show'):
    Tooltip arrow display mode. Supported values: `'show'`, `'hide'`, `'center'`. Default: `'show'`.

- fresh (boolean; default False):
    Whether to always keep the content updated. Default: `False`.

- open (boolean; default False):
    Monitor or set tooltip visibility. Default: `False`.

- permanent (boolean; default False):
    Whether to keep the tooltip fixed in its `open` state. Default: `False`.

- popupContainer (a value equal to: 'parent', 'body'; default 'body'):
    Container anchoring strategy for the tooltip popup. Supported values: `'parent'`, `'body'`. Default: `'body'`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading.
