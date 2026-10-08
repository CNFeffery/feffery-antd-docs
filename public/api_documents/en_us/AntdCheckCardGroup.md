- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, containing several `AntdCheckCard` related components.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- name (string; optional):
    Used with `AntdForm` for batch value collection/control, serving as the field name of the current form item, with `id` as the default value.

- enableBatchControl (boolean; default True):
    Controls whether the current component participates in the effective `AntdForm` batch value collection/control feature. Default: `True`.

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
    Whether to disable the current component. Default: `False`.

- size (a value equal to: 'small', 'default', 'large'; default 'default'):
    The size specification of the current component, with options `'small'`, `'default'`, `'large'`. Default value: `'default'`.

- readOnly (boolean; default False):
    Whether to render as read-only. Default: `False`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'value's; optional):
    Several property names for which the persistence feature is enabled. Options are `'value'`. Default: `['value']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
