- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Updates the `key` value of the current component, which can force a redraw of the current component.

- children (a list of or a singular dash component, string or number; optional):
    Component type, nested elements.

- style (dict; optional):
    CSS styles for the current component.

- className (string | dict; optional):
    CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

- name (string; optional):
    Used in conjunction with the `AntdForm` form batch value collection/control feature, serving as the field name for the current form item, with `id` as the default value.

- checked (boolean; optional):
    Listens to or sets whether it is checked.

- defaultChecked (boolean; optional):
    Whether it is checked by default.

- bordered (boolean; default True):
    Whether to display a border. Default value: `True`.

- disabled (boolean; default False):
    Whether to disable the current component. Default value: `False`.

- size (a value equal to: 'small', 'default', 'large'; default 'default'):
    The size specification of the current component, with options `'small'`, `'default'`, `'large'`. Default value: `'default'`.

- value (number | string; optional):
    The value of the currently selected card.

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

- persisted_props (list of a value equal to: 'checked's; default ['checked']):
    The names of several properties that are enabled for property persistence, with the option `'checked'`. Default value: `['checked']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    The storage type for property persistence, with options `'local'` (local persistence), `'session'` (session persistence), `'memory'` (memory persistence).
    Default value: `'local'`.
