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

- label (a list of or a singular dash component, string or number; optional):
    Component type, label content.

- autoFocus (boolean; default False):
    Whether to automatically gain focus. Default: `False`.

- checked (boolean; default False):
    To monitor or set whether the current checkbox is checked. Default value: `False`.

- indeterminate (boolean; default False):
    Whether to force rendering in an indeterminate state, which only affects the style and is unrelated to the checked state. Default value: `False`.

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

- persisted_props (list of a value equal to: 'checked's; optional):
    Several property names for which the persistence feature is enabled. Options are `'checked'`. Default: `['checked']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
