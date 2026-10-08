- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- popupClassName (string; optional):
    CSS class name for the expanded menu.

- name (string; optional):
    Used with `AntdForm` for batch value collection/control, serving as the field name of the current form item, with `id` as the default value.

- enableBatchControl (boolean; default True):
    Controls whether the current component participates in the effective `AntdForm` batch value collection/control feature. Default: `True`.

- autoSize (dict; default False):
    Automatic input height settings. Default: `False`.

    `autoSize` is a boolean | dict with keys:

    - minRows (number; optional):
        Minimum number of input rows.

    - maxRows (number; optional):
        Maximum number of input rows.

- prefix (string; default '@'):
    Keyword that opens the selection menu. Default: `'@'`.

- value (string; optional):
    Monitor or set the entered value.

- defaultValue (string; optional):
    The initial input value.

- options (list of dicts; required):
    Required. Selection menu items.

    `options` is a list of dicts with keys:

    - label (a list of or a singular dash component, string or number; optional):
        Component type, the label content of the current option.

    - value (string; optional):
        The value of the current option.

- selectedOptions (list of strings; optional):
    Selected item values in the input content.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- placement (a value equal to: 'top', 'bottom'; default 'bottom'):
    Selection menu placement. Supported values: `'top'`, `'bottom'`. Default: `'bottom'`.

- bordered (boolean; default True):
    Whether to show the border. When set to `True`, it is equivalent to `variant='outlined'`. Default: `True`.

- variant (a value equal to: 'outlined', 'borderless', 'filled', 'underlined'; optional):
    Variant type. Options are `'outlined'`, `'borderless'`, `'filled'`, `'underlined'`. Among them, `'outlined'` is equivalent to `bordered=True`, but with higher priority.

- placeholder (string; optional):
    Placeholder text content for the input box.

- status (a value equal to: 'error', 'warning'; optional):
    Control the validation state. Options are `'error'`, `'warning'`.

- autoFocus (boolean; default False):
    Whether to automatically gain focus. Default: `False`.

- popupContainer (a value equal to: 'parent', 'body'; optional):
    Anchoring strategy for the related popup layer. Options are `'parent'`, `'body'`. Default: `'body'`.

- batchPropsNames (list of strings; optional):
    Property names to include in [batch property monitoring](/batch-props-values).

- batchPropsValues (dict; optional):
    Values of the properties specified by `batchPropsNames`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
