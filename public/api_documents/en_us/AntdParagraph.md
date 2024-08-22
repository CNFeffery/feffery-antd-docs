- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- id (string; optional):
    Unique ID for the component.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- className (string | dict; optional):
    The CSS class name for the current component, supports [dynamic CSS class names](/advanced-classname).

- code (boolean; optional):
    Whether to render as code format.

- copyable (boolean; optional):
    Whether to enable the quick copy feature.

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- disabled (boolean; optional):
    Whether to render as disabled.

- ellipsis (dict; default False):
    Configures the ellipsis functionality for content. Set to `False` to disable. Default value: `False`.

    `ellipsis` can be a boolean or a dict with keys:

    - expandable (boolean | a value equal to: 'collapsible'; optional):
        Whether it is expandable.

    - rows (number; optional):
        Maximum number of visible rows.

    - suffix (string; optional):
        Custom suffix after content is ellipsized.

    - symbol (a list of or a singular dash component, string or number; optional):
        Component type, custom content expansion control.

- italic (boolean; optional):
    Whether to render as italic.

- key (string; optional):
    Update the `key` value for the current component, which can force a redraw of the current component.

- loading_state (dict; optional):

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh-cn', 'en-us'; default 'zh-cn'):
    The language of the component's text, options include `'zh-cn'`, `'en-us'`. Default value: `'zh-cn'`.

- mark (boolean; optional):
    Whether to render as highlighted.

- strikethrough (boolean; optional):
    Whether to render as strikethrough.

- strong (boolean; optional):
    Whether to render as bold.

- style (dict; optional):
    The CSS styles for the current component.

- type (a value equal to: 'secondary', 'success', 'warning', 'danger'; optional):
    Sets the special state of the content, options include `'secondary'`, `'success'`, `'warning'`, `'danger'`.

- underline (boolean; optional):
    Whether to render as underlined.
