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

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- format (string; default 'HH:mm:ss'):
    Time display format. See [reference](https://day.js.org/docs/en/display/format). Default: `'HH:mm:ss'`.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- hourStep (number; default 1):
    Interval between hour options. Default: `1`.

- minuteStep (number; default 1):
    Interval between minute options. Default: `1`.

- secondStep (number; default 1):
    Interval between second options. Default: `1`.

- use12Hours (boolean; default False):
    Whether to use a 12-hour clock. When `True`, the default `format` becomes `'h:mm:ss a'`. Default: `False`.

- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):
    Current component size specification. Options are `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

- bordered (boolean; default True):
    Whether to show the border. When set to `True`, it is equivalent to `variant='outlined'`. Default: `True`.

- variant (a value equal to: 'outlined', 'borderless', 'filled', 'underlined'; optional):
    Variant type. Options are `'outlined'`, `'borderless'`, `'filled'`, `'underlined'`. Among them, `'outlined'` is equivalent to `bordered=True`, but with higher priority.

- placeholder (string; optional):
    Placeholder text content for the input box.

- placement (a value equal to: 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'; default 'bottomLeft'):
    Direction in which the selection panel expands. Options are `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, `'topRight'` Default: `'bottomLeft'`.

- value (string; optional):
    Listen to or set the selected value, corresponding to `format`.

- defaultValue (string; optional):
    Initial selected value, corresponding to `format`.

- status (a value equal to: 'error', 'warning'; optional):
    Control the validation state. Options are `'error'`, `'warning'`.

- allowClear (boolean; default True):
    Whether to allow one-click clearing of selected values. Default: `True`.

- autoFocus (boolean; default False):
    Whether to automatically gain focus. Default: `False`.

- readOnly (boolean; optional):
    Whether to render as read-only. Default: `False`.

- extraFooter (a list of or a singular dash component, string or number; optional):
    Component type, extra footer content.

- showNow (boolean; default True):
    Whether to show the Now shortcut button. Default: `True`.

- prefix (a list of or a singular dash component, string or number; optional):
    Component type, embedded prefix content.

- suffixIcon (a list of or a singular dash component, string or number; optional):
    Custom suffix icon content for the selection box.

- popupContainer (a value equal to: 'parent', 'body'; default 'body'):
    Anchoring strategy for the related popup layer. Options are `'parent'`, `'body'`. Default: `'body'`.

- batchPropsNames (list of strings; optional):
    Property names to include in [batch property monitoring](/batch-props-values).

- batchPropsValues (dict; optional):
    Values of the properties specified by `batchPropsNames`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.

- needConfirm (boolean; default False):
    Whether confirmation is required. When `False`, losing focus confirms the selection. Default: `False`.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading.

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'value's; optional):
    Several property names for which the persistence feature is enabled. Options are `'value'`. Default: `['value']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
