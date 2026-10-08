- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- name (string; optional):
    Used with `AntdForm` for batch value collection/control, serving as the field name of the current form item, with `id` as the default value.

- enableBatchControl (boolean; default True):
    Controls whether the current component participates in the effective `AntdForm` batch value collection/control feature. Default: `True`.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- options (list of dicts; optional):
    `options` is a list of string | number | dict with keys:

    `options` is a list of string | number | dict with keys:

    - label (a list of or a singular dash component, string or number; optional):
        Component type, the label content of the current selection box.

    - value (string | number; optional):
        The corresponding value of the current selection box.

    - disabled (boolean; optional):
        Whether to disable the current selection box. Default value: `False`.

- value (list of string | numbers; optional):
    Listen to or set the selected value(s).

- readOnly (boolean; default False):
    Whether to render as read-only. Default: `False`.

- batchPropsNames (list of strings; optional):
    Property names to include in [batch property monitoring](/batch-props-values).

- batchPropsValues (dict; optional):
    Values of the properties specified by `batchPropsNames`.

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
