- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- styles (dict; optional):
    Fine-grained CSS styles for child elements.

    `styles` is a dict with keys:

    - mask (dict; optional):
        CSS styles for the mask element.

    - content (dict; optional):
        CSS styles for the container element.

    - wrapper (dict; optional):
        CSS styles for the wrapper element.

    - header (dict; optional):
        CSS styles for the header element.

    - body (dict; optional):
        CSS styles for the body element.

    - footer (dict; optional):
        CSS styles for the footer element.

- classNames (dict; optional):
    Fine-grained CSS class names for child elements.

    `classNames` is a dict with keys:

    - mask (string; optional):
        CSS class name for the mask element.

    - content (string; optional):
        CSS class name for the container element.

    - wrapper (string; optional):
        CSS class name for the wrapper element.

    - header (string; optional):
        CSS class name for the header element.

    - body (string; optional):
        CSS class name for the body element.

    - footer (string; optional):
        CSS class name for the footer element.

- title (a list of or a singular dash component, string or number; optional):
    Title content. Supports components.

- visible (boolean; default True):
    Set or monitor popup card visibility. Default: `True`.

- width (number | string; optional):
    Popup card width in pixels.

- transitionType (a value equal to: 'none', 'fade', 'zoom', 'zoom-big', 'zoom-big-fast', 'slide-up', 'slide-down', 'slide-left', 'slide-right', 'move-up', 'move-down', 'move-left', 'move-right'; default 'fade'):
    Card show/hide animation. Supported values: `'none'`, `'fade'`, `'zoom'`, `'zoom-big'`, `'zoom-big-fast'`, `'slide-up'`, `'slide-down'`, `'slide-left'`, `'slide-right'`, `'move-up'`, `'move-down'`, `'move-left'`, `'move-right'`. Default: `'fade'`.

- forceRender (boolean; default False):
    Whether to render card content before the card is first shown. Default: `False`.

- destroyOnClose (boolean; default True):
    Whether to destroy card content after closing. Default: `True`.

- closable (boolean; default True):
    Whether to show the close button in the upper-right corner. Default: `True`.

- closeIconType (a value equal to: 'default', 'outlined', 'two-tone'; default 'default'):
    Close button icon type. Supported values: `'default'`, `'outlined'`, `'two-tone'`. Default: `'default'`.

- draggable (boolean; default False):
    Whether the component is draggable. Default: `False`.

- dragClassName (string | dict; optional):
    CSS class name for the draggable header area.

- zIndex (number; default 1000):
    Popup card z-index. Default: `1000`.

- loading (boolean; default False):
    Whether to show the entire component as loading. Default: `False`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
