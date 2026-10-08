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

- addonBefore (a list of or a singular dash component, string or number; optional):
    Before-addon content. Supports components.

- addonAfter (a list of or a singular dash component, string or number; optional):
    After-addon content. Supports components.

- prefix (a list of or a singular dash component, string or number; optional):
    Component type, embedded prefix content.

- suffix (a list of or a singular dash component, string or number; optional):
    Embedded suffix content. Supports components.

- autoFocus (boolean; default False):
    Whether to automatically gain focus. Default: `False`.

- controls (boolean; default True):
    Whether to show numeric increment/decrement buttons. Default: `True`.

- keyboard (boolean; default True):
    Whether the up/down arrow keys adjust the numeric value. Default: `True`.

- min (number | string; optional):
    Minimum allowed numeric input; unrestricted by default.

- max (number | string; optional):
    Maximum allowed numeric input; unrestricted by default.

- step (number | string; optional):
    Numeric step size.

- precision (number; optional):
    Numeric precision.

- stringMode (boolean; default False):
    Whether to use string mode to preserve high-precision numeric input. In this mode, `min`, `max`, `step`, `value`, and `defaultValue` must be strings. Default: `False`.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):
    Current component size specification. Options are `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

- bordered (boolean; default True):
    Whether to show the border. When set to `True`, it is equivalent to `variant='outlined'`. Default: `True`.

- variant (a value equal to: 'outlined', 'borderless', 'filled', 'underlined'; optional):
    Variant type. Options are `'outlined'`, `'borderless'`, `'filled'`, `'underlined'`. Among them, `'outlined'` is equivalent to `bordered=True`, but with higher priority.

- placeholder (string; optional):
    Placeholder text content for the input box.

- value (number | string; optional):
    Monitor or set the entered value.

- defaultValue (number | string; optional):
    The initial input value.

- debounceValue (number | string; optional):
    Debounced entered value.

- debounceWait (number; default 0):
    Debounce delay duration, in milliseconds. Default: `0`.

- nSubmit (number; default 0):
    Cumulative Enter key presses while the input is focused. Default: `0`.

- status (a value equal to: 'error', 'warning'; optional):
    Control the validation state. Options are `'error'`, `'warning'`.

- readOnly (boolean; optional):
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

- persisted_props (list of a value equal to: 'value's; default ['value']):
    Properties whose values are persisted. Supported values: `'value'`. Default: `['value']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
