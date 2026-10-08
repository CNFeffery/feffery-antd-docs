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

- optionsMode (a value equal to: 'tree', 'flat'; default 'tree'):
    The rendering mode corresponding to the `options` format, options include `'tree'` (tree mode), `'flat'` (flat mode). Default value: `'tree'`.

- options (list; required):
    Defines the data structure required for constructing cascade selection, consistent with `optionsMode`.

- optionsNodeKeyToLabel (dict with strings as keys and values of type a list of or a singular dash component, string or number; optional):
    For specified nodes in the cascade structure, defines the component-type content that serves as the title, with higher priority than the corresponding `label` value in `options`.

- optionFilterProp (a value equal to: 'value', 'label'; default 'label'):
    The target field for option keyword search, options include `'value'`, `'label'`. Default value: `'label'`.

- panelMode (boolean; default False):
    Whether to enable the embedded panel mode. Default value: `False`.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- changeOnSelect (boolean; default False):
    Whether to update the selected value when any node in the cascade selection is chosen. Default value: `False`.

- size (a value equal to: 'small', 'middle', 'large'; optional):
    Current component size specification. Options are `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

- bordered (boolean; default True):
    Whether to show the border. When set to `True`, it is equivalent to `variant='outlined'`. Default: `True`.

- variant (a value equal to: 'outlined', 'borderless', 'filled', 'underlined'; optional):
    Variant type. Options are `'outlined'`, `'borderless'`, `'filled'`, `'underlined'`. Among them, `'outlined'` is equivalent to `bordered=True`, but with higher priority.

- placeholder (string; optional):
    Placeholder text content for the input box.

- placement (a value equal to: 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'; default 'bottomLeft'):
    The direction in which the selection menu expands, options include `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, `'topRight'`. Default value: `'bottomLeft'`.

- value (list of string | numbers | list of list of string | numberss; optional):
    Listen to or set the selected value(s).

- defaultValue (list of string | numbers | list of list of string | numberss; optional):
    Initial selected value(s).

- multiple (boolean; default False):
    Whether to enable multi-selection mode. Default value: `False`.

- maxTagCount (number | a value equal to: 'responsive'; optional):
    The maximum number of selected values displayed when `multiple=True`.

- expandTrigger (a value equal to: 'click', 'hover'; default 'click'):
    The trigger method for expanding the selection menu, options include `'click'`, `'hover'`. Default value: `'click'`.

- status (a value equal to: 'error', 'warning'; optional):
    Control the validation state. Options are `'error'`, `'warning'`.

- allowClear (boolean; default True):
    Whether to allow one-click clearing of selected values. Default: `True`.

- autoFocus (boolean; default False):
    Whether to automatically gain focus. Default: `False`.

- showCheckedStrategy (a value equal to: 'show-parent', 'show-child'; optional):
    The strategy for filling in the selected options, options include `'show-parent'`, `'show-child'`.

- prefix (a list of or a singular dash component, string or number; optional):
    Component type, embedded prefix content.

- suffixIcon (a list of or a singular dash component, string or number; optional):
    Custom suffix icon content for the selection box.

- readOnly (boolean; optional):
    Whether to render as read-only. Default: `False`.

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

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'value's; optional):
    Several property names for which the persistence feature is enabled. Options are `'value'`. Default: `['value']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
