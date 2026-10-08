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

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    Layout direction of the radio buttons. Supported values: `'horizontal'`, `'vertical'`. Default: `'horizontal'`.

- options (list of dicts; optional):
    Option definitions.

    `options` is a list of string | number | dict with keys:

    - label (a list of or a singular dash component, string or number; optional):
        Component type, the label content of the current option.

    - value (string | number; optional):
        The value of the current option.

    - disabled (boolean; optional):
        Whether this option is disabled. Default: `False`.

- block (boolean; default False):
    Whether to fill the parent container. Default: `False`.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):
    Option button size when `optionType='button'`. Supported values: `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

- value (string | number; optional):
    Listen to or set the selected value, corresponding to `format`.

- defaultValue (string | number; optional):
    Initial selected value, corresponding to `format`.

- optionType (a value equal to: 'default', 'button'; default 'default'):
    Option display type. Supported values: `'default'`, `'button'`. Default: `'default'`.

- buttonStyle (a value equal to: 'outline', 'solid'; default 'outline'):
    Option button appearance when `optionType='button'`. Supported values: `'outline'`, `'solid'`. Default: `'outline'`.

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
