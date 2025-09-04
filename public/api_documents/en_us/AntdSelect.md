- id (string; optional):
  Component unique id.

- key (string; optional):
  Update the `key` value of the current component to force re-rendering of the current component F.

- className (string | dict; optional):
  CSS class name of the current component, supports [dynamic css](/advanced-classname).

- popupClassName (string; optional):
  CSS class name for the expanded menu.

- name (string; optional):
  Used with `AntdForm` for batch value collection/control, serving as the field name of the current form item, with `id` as the default value.

- enableBatchControl (boolean; default True):
  Controls whether the current component participates in the effective `AntdForm` batch value collection/control feature. Default: `True`.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru'; default 'zh-cn'):
  Component text locale. Options are `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'ru-ru'` (Russian)
  Default: `'zh-cn'`.

- options (list of dicts; optional):
  Configure dropdown options.

  `options` is a list of string | number | dict with keys:

  - label (a list of or a singular dash component, string or number; required):
    Component type, the label content of the current option.

  - value (string

    Or number; required):
    The value of the current option.

  - disabled (boolean; optional):
    Whether to disable the current option. Default: `False`.

  - colors (list of strings; optional):
    For the color ramp special rendering mode, set the array of color values required to generate the gradient color ramp. | dict with keys:

  - group (a list of or a singular dash component, string or number; optional):
    Component type, the label content of the current group.

  - options (list of dicts; optional):
    Configure options within the current group.

    `options` is a list of dicts with keys:

    - label (a list of or a singular dash component, string or number; required):

      Component type, the label content of the current option.

    - value (string | number; required):

      The value of the current option.

    - disabled (boolean; optional):

      Whether to disable the current option. Default: `False`.

    - colors (list of strings; optional):

      For the color ramp special rendering mode, set the array of color values required to generate the gradient color ramp.s

- listHeight (number; default 256):
  Maximum pixel height of the dropdown menu.

- colorsMode (a value equal to: 'sequential', 'diverging'; default 'sequential'):
  In the color ramp special rendering mode, set the rendering form. Options are `'sequential'`, `'diverging'`.

- colorsNameWidth (number; default 40):
  In the color ramp special rendering mode, set the pixel width of the name part for each option. Default: `40`.

- mode (a value equal to: 'multiple', 'tags'; optional):
  Selection mode. Options are `'multiple'` (multi-select), `'tags'` (free add).

- disabled (boolean; optional):
  Whether to disable the current component. Default: `False`.

- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):
  Current component size specification. Options are `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

- bordered (boolean; default True):
  Whether to show the border. When set to `True`, it is equivalent to `variant='outlined'`. Default: `True`.

- variant (a value equal to: 'outlined', 'borderless', 'filled', 'underlined'; optional):
  Variant type. Options are `'outlined'`, `'borderless'`, `'filled'`, `'underlined'`. Among them, `'outlined'` is equivalent to `bordered=True`, but with higher priority.

- placeholder (string; optional):
  Placeholder text content for the input box.

- placement (a value equal to: 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'; default 'bottomLeft'):
  Direction in which the selection panel expands. Options are `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, `'topRight'`
  Default: `'bottomLeft'`.

- value (string | number | list of string | numbers; optional):
  Listen to or set the selected value(s).

- defaultValue (string | number | list of string | numbers; optional):
  Initial selected value(s).

- maxTagCount (number | a value equal to: 'responsive'; default 5):
  When `multiple=True`, the maximum number of selected values to display. Default: `5`.

- status (a value equal to: 'error', 'warning'; optional):
  Control the validation state. Options are `'error'`, `'warning'`.

- optionFilterProp (a value equal to: 'value', 'label'; default 'value'):
  The target field for searching based on the input in the search box. Options are `'value'`, `'label'`. Default: `'value'`.

- searchValue (string; optional):
  Listen to the content already entered in the search box.

- optionFilterMode (a value equal to: 'case-insensitive', 'case-sensitive', 'regex', 'remote-match'; default 'case-insensitive'):
  Search matching mode. Options are `'case-insensitive'` (case insensitive), `'case-sensitive'` (case sensitive), `'regex'` (regular expression), `'remote-match'` (remote matching mode)
  Default: `'case-insensitive'`.

- debounceSearchValue (string; optional):
  Listen to the content already entered in the search box using a debounced delay.

- debounceWait (number; default 0):
  Debounce delay duration, in milliseconds. Default: `0`.

- autoSpin (boolean; default False):
  Whether to render in a loading state while the current component-related properties are being updated by callbacks. Default: `False`.

- autoClearSearchValue (boolean; default True):
  When `mode` is `'multiple'` or `'tags'`, set whether to automatically clear the content in the search box after selecting an item. Default: `True`.

- emptyContent (a list of or a singular dash component, string or number; optional):
  Component type, custom empty-data state prompt content.

- loadingEmptyContent (a list of or a singular dash component, string or number; optional):
  Component type, custom empty-data state prompt content in the loading state.

- dropdownBefore (a list of or a singular dash component, string or number; optional):
  Component type, prefix content of the selection menu.

- dropdownAfter (a list of or a singular dash component, string or number; optional):
  Component type, suffix content of the selection menu.

- prefix (a list of or a singular dash component, string or number; optional):
  Component type, embedded prefix content.

- suffixIcon (a list of or a singular dash component, string or number; optional):
  Custom suffix icon content for the selection box.

- allowClear (boolean; default True):
  Whether to allow one-click clearing of selected values. Default: `True`.

- autoFocus (boolean; default False):
  Whether to automatically gain focus. Default: `False`.

- popupMatchSelectWidth (boolean; default True):
  Whether the selection menu has the same width as the selection box. When set to `False`, virtual scrolling will be disabled. Default: `True`.

- readOnly (boolean; optional):
  Whether to render as read-only. Default: `False`.

- maxCount (number; optional):
  Effective in `'multiple'` and `'tags'` modes, limits the upper bound of the number of selected items.

- popupContainer (a value equal to: 'parent', 'body'; default 'body'):
  Anchoring strategy for the related popup layer. Options are `'parent'`, `'body'`. Default: `'body'`.

- batchPropsNames (list of strings; optional):
  Several property names that need to be included in [batch property listening](/batch-props-values).

- batchPropsValues (dict; optional):
  Listen to several property values specified in `batchPropsNames`.

- data-_ (string; optional):
  Wildcard attributes in `data-_` format.

- aria-_ (string; optional):
  Wildcard attributes in `aria-_` format.

- persistence (boolean | string | number; optional):
  Whether to enable [prop persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'value's; optional):
  Several property names for which the persistence feature is enabled. Options are `'value'`. Default: `['value']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
  Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence)
  Default: `'local'`.
