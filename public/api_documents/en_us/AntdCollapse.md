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

    - header (dict; optional):
        CSS styles for the header element.

    - body (dict; optional):
        CSS styles for the body element.

- classNames (dict; optional):
    Fine-grained CSS class names for child elements.

    `classNames` is a dict with keys:

    - header (string; optional):
        CSS class name for the header element.

    - body (string; optional):
        CSS class name for the body element.

- title (a list of or a singular dash component, string or number; optional):
    Title content. Supports components.

- isOpen (boolean; default True):
    Whether the component is expanded. Default: `True`.

- size (a value equal to: 'large', 'middle', 'small'; default 'middle'):
    Component size specification. Options are `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

- bordered (boolean; default True):
    Whether to render borders. Default: `True`.

- showArrow (boolean; default True):
    Whether to render arrows. Default: `True`.

- ghost (boolean; default False):
    Whether to enable the transparent background mode. Default value: `False`.

- collapsible (a value equal to: 'header', 'disabled', 'icon'; optional):
    Collapse trigger: `'header'` for the header area, `'disabled'` to disable collapsing, or `'icon'` for the icon area.

- forceRender (boolean; default False):
    Whether to render the content before its first expansion. Default: `False`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'isOpen's; optional):
    Properties whose values are persisted. Supported values: `'isOpen'`. Default: `['isOpen']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
