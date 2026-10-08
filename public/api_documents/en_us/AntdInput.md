- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- styles (dict; optional):
    Fine-grained CSS styles for child elements.

    `styles` is a dict with keys:

    - input (dict; optional):
        CSS styles for the input element.

    - prefix (dict; optional):
        CSS styles for the prefix container.

    - suffix (dict; optional):
        CSS styles for the suffix container.

    - count (dict; optional):
        CSS styles for the character count element.

    - textarea (dict; optional):
        CSS styles for the textarea element.

- classNames (dict; optional):
    Fine-grained CSS class names for child elements.

    `classNames` is a dict with keys:

    - input (string; optional):
        CSS class name for the input element.

    - prefix (string; optional):
        CSS class name for the prefix container.

    - suffix (string; optional):
        CSS class name for the suffix container.

    - count (string; optional):
        CSS class name for the character count element.

    - textarea (string; optional):
        CSS class name for the textarea element.

- name (string; optional):
    Used with `AntdForm` for batch value collection/control, serving as the field name of the current form item, with `id` as the default value.

- enableBatchControl (boolean; default True):
    Controls whether the current component participates in the effective `AntdForm` batch value collection/control feature. Default: `True`.

- mode (a value equal to: 'default', 'search', 'text-area', 'password'; default 'default'):
    Input mode. Supported values: `'default'`, `'search'`, `'text-area'`, `'password'`. Default: `'default'`.

- autoComplete (a value equal to: 'off', 'on'; default 'on'):
    Browser autocomplete setting. Supported values: `'off'`, `'on'`. Default: `'on'`.

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

- value (string; optional):
    Monitor or set the entered value.

- defaultValue (string; optional):
    The initial input value.

- passwordUseMd5 (boolean; default False):
    Whether MD5 hashing is enabled in `'password'` mode. Default: `False`.

- md5Value (string; optional):
    MD5 hash of the entered value when `passwordUseMd5=True`.

- debounceValue (string; optional):
    Debounced entered value.

- debounceWait (number; default 0):
    Debounce delay duration, in milliseconds. Default: `0`.

- addonBefore (a list of or a singular dash component, string or number; optional):
    Before-addon content. Supports components.

- addonAfter (a list of or a singular dash component, string or number; optional):
    After-addon content. Supports components.

- prefix (a list of or a singular dash component, string or number; optional):
    Component type, embedded prefix content.

- suffix (a list of or a singular dash component, string or number; optional):
    Embedded suffix content. Supports components.

- maxLength (number; optional):
    Maximum number of characters that can be entered.

- showCount (boolean; default False):
    Whether to show the entered character count. Default: `False`.

- countFormat (string; optional):
    Regular expression defining custom character counting rules.

- autoSize (dict; default False):
    Automatic input height settings for `'text-area'` mode. Default: `False`.

    `autoSize` is a boolean | dict with keys:

    - minRows (number; optional):
        Minimum number of input rows.

    - maxRows (number; optional):
        Maximum number of input rows.

- nSubmit (number; default 0):
    Cumulative Enter key presses while the input is focused. Default: `0`.

- nClicksSearch (number; default 0):
    Cumulative search button clicks in `'search'` mode. Default: `0`.

- status (a value equal to: 'error', 'warning'; optional):
    Control the validation state. Options are `'error'`, `'warning'`.

- allowClear (boolean; default False):
    Whether entered values can be cleared with one click. Default: `False`.

- autoFocus (boolean; default False):
    Whether to automatically gain focus. Default: `False`.

- focusing (boolean; optional):
    Whether the input is focused.

- readOnly (boolean; optional):
    Whether to render as read-only. Default: `False`.

- emptyAsNone (boolean; default False):
    Whether an empty input forces `value` to null, normalizing empty strings and null values. Default: `False`.

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

- persisted_props (list of a value equal to: 'value', 'md5Value's; optional):
    Properties whose values are persisted. Supported values: `'value'`, `'md5Value'`. Default: `['value', 'md5Value']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
