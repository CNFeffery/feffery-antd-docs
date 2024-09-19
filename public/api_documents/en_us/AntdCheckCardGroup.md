- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Updates the `key` value of the current component to force a redraw.

- children (a list of or a singular dash component, string or number; optional):
    Component type, containing several `AntdCheckCard` related components.

- style (dict; optional):
    CSS styles for the current component.

- className (string | dict; optional):
    CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

- name (string; optional):
    Used in conjunction with the `AntdForm` form for batch value collection and control, serving as the field name for the current form item, with `id` as the default value.

- multiple (boolean; default False):
    Whether to enable multiple selection. Default value: `False`.

- allowNoValue (boolean; default True):
    Whether to allow the last option in the current group of selection cards to be deselected. Default value: `True`.

- bordered (boolean; default True):
    Whether to display a border. Default value: `True`.

- value (number | string | list of number | strings; optional):
    Listens to or sets the value of the selected card(s).

- defaultValue (number | string | list of number | strings; optional):
    Initializes the value of the selected card(s).

- disabled (boolean; default False):
    Whether to disable the current component. Default value: `False`.

- size (a value equal to: 'small', 'default', 'large'; default 'default'):
    The size specification of the current component, with options `'small'`, `'default'`, `'large'`. Default value: `'default'`.

- readOnly (boolean; default False):
    Whether to render as read-only. Default value: `False`.

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- loading_state (dict; optional):
    `loading_state` is a dictionary with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'value's; default ['value']):
    The names of several properties that are enabled for property persistence, with the option `'value'`. Default value: `['value']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    The storage type for property persistence, with options `'local'` (local persistence), `'session'` (session persistence), `'memory'` (memory persistence).
    Default value: `'local'`.
