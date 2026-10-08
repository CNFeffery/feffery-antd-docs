- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- classNames (dict; optional):
    CSS class names for individual child elements.

    `classNames` is a dict with keys:

    - header (string; optional):
        CSS class name for the header element.

    - body (string; optional):
        CSS class name for the body element.

    - footer (string; optional):
        CSS class name for the footer element.

    - mask (string; optional):
        CSS class name for the mask element.

    - content (string; optional):
        CSS class name for the drawer container.

- styles (dict; optional):
    CSS styles for individual child elements.

    `styles` is a dict with keys:

    - header (dict; optional):
        CSS styles for the header element.

    - body (dict; optional):
        CSS styles for the body element.

    - footer (dict; optional):
        CSS styles for the footer element.

    - mask (dict; optional):
        CSS styles for the mask element.

    - content (dict; optional):
        CSS styles for the drawer container.

- rootStyle (dict; optional):
    CSS styles for the drawer root, including its mask. Setting `containerId` or `containerSelector` automatically sets `position` to `absolute`.

- visible (boolean; default False):
    Monitor or set drawer visibility. Default: `False`.

- title (a list of or a singular dash component, string or number; optional):
    Drawer title. Supports components.

- placement (a value equal to: 'left', 'right', 'top', 'bottom'; default 'right'):
    Drawer placement. Supported values: `'left'`, `'right'`, `'top'`, `'bottom'`. Default: `'right'`.

- closable (boolean; default True):
    Whether to show the close button. Default: `True`.

- forceRender (boolean; default False):
    Whether to render drawer content in advance. Default: `False`.

- destroyOnClose (boolean; default False):
    Whether to destroy drawer content when closed. Default: `False`.

- width (number | string; default 256):
    Drawer width in pixels when `placement` is `'left'` or `'right'`. Default: `256`.

- height (number | string; default 256):
    Drawer height in pixels when `placement` is `'top'` or `'bottom'`. Default: `256`.

- mask (boolean; default True):
    Whether to show the mask. Default: `True`.

- maskClosable (boolean; default True):
    Whether clicking the mask closes the drawer. Default: `True`.

- zIndex (number; default 1000):
    Drawer `z-index`. Default: `1000`.

- loading (boolean; default False):
    Whether to show the loading state. Default: `False`.

- extra (a list of or a singular dash component, string or number; optional):
    Additional action area elements. Supports components.

- footer (a list of or a singular dash component, string or number; optional):
    Footer elements. Supports components.

- containerId (string; optional):
    ID of a local container whose `position` is `relative`.

- containerSelector (string; optional):
    JavaScript code string locating the container in complex layouts. `containerId` takes precedence.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
