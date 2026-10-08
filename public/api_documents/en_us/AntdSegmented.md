- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- options (list of dicts; optional):
    Option settings.

    `options` is a list of string | number | dict with keys:

    - label (a list of or a singular dash component, string or number; optional):
        Option title content. Supports components.

    - value (string | number; required):
        Required. Option value.

    - disabled (boolean; optional):
        Whether to disable the current option. Default: `False`.

    - icon (string; optional):
        Option prefix icon. Uses the `AntdIcon` icon property when `iconRenderer='AntdIcon'`, or a CSS class when `iconRenderer='fontawesome'`.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
        Option prefix icon renderer. Supported values: `'AntdIcon'`, `'fontawesome'`. Default: `'AntdIcon'`.

- value (string | number; optional):
    Monitor or set the selected value.

- defaultValue (string | number; optional):
    Initial selected value.

- block (boolean; default False):
    Whether to fill the parent container. Default: `False`.

- shape (a value equal to: 'default', 'round'; default 'default'):
    Shape. Supported values: `'default'`, `'round'`. Default: `'default'`.

- vertical (boolean; default False):
    Whether to use a vertical layout. Default: `False`.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- size (a value equal to: 'large', 'middle', 'small'; default 'middle'):
    Component size specification. Options are `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

- batchPropsNames (list of strings; optional):
    Property names to include in [batch property monitoring](/batch-props-values).

- batchPropsValues (dict; optional):
    Values of the properties specified by `batchPropsNames`.

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

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'value's; optional):
    Several property names for which the persistence feature is enabled. Options are `'value'`. Default: `['value']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
