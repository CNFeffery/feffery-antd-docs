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

- allowClear (boolean; default True):
    Whether clicking the selected rating again clears it. Default: `True`.

- allowHalf (boolean; default False):
    Whether half-star ratings are allowed. Default: `False`.

- count (number; default 5):
    Maximum rating value. Default: `5`.

- tooltips (list of strings; optional):
    Tooltip text for each rating value.

- disabled (boolean; default False):
    Whether the rating is read-only. Default: `False`.

- autoFocus (boolean; default False):
    Whether to automatically gain focus. Default: `False`.

- value (number; optional):
    Listen to or set the selected value(s).

- defaultValue (number; default 0):
    Initial selected value. Default: `0`.

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

- persisted_props (list of a value equal to: 'value's; default ['value']):
    Several property names for which the persistence feature is enabled. Options are `'value'`. Default: `['value']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
