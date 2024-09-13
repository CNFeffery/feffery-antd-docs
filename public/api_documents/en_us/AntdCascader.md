Here is the translation of the provided text into English:

- id (string; optional):
    The unique identifier for the component.

- allowClear (boolean; default True):
    Whether to allow one-click clearing of the selected value. Default value: `True`.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- autoFocus (boolean; default False):
    Whether to automatically focus. Default value: `False`.

- batchPropsNames (list of strings; optional):
    A list of property names to include in [batch property listening](/batch-props-values).

- batchPropsValues (dict; optional):
    Listens to the values of several properties specified in `batchPropsNames`.

- bordered (boolean; default True):
    Whether to display a border, setting it to `True` is equivalent to `variant='outlined'`. Default value: `True`.

- changeOnSelect (boolean; default False):
    Whether to update the selected value when any node in the cascade selection is chosen. Default value: `False`.

- className (string | dict; optional):
    The current component's CSS class name, supports [dynamic CSS](/advanced-classname).

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- defaultValue (list of string | numbers | list of list of string | numbers; optional):
    The initial selected values.

- disabled (boolean; default False):
    Whether to disable the current component. Default value: `False`.

- expandTrigger (a value equal to: 'click', 'hover'; default 'click'):
    The trigger method for expanding the selection menu, options include `'click'`, `'hover'`. Default value: `'click'`.

- key (string; optional):
    Updating the `key` value of the current component can force a redraw of the component.

- loading_state (dict; optional):
    `loading_state` is a dictionary with keys:
    - component_name (string; optional):
        Holds the name of the component that is loading.
    - is_loading (boolean; optional):
        Determines if the component is loading or not.
    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de'; default 'zh-cn'):
    The language of the component's text, options include `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German). Default value: `'zh-cn'`.

- maxTagCount (number | a value equal to: 'responsive'; optional):
    The maximum number of selected values displayed when `multiple=True`.

- multiple (boolean; default False):
    Whether to enable multi-selection mode. Default value: `False`.

- name (string; optional):
    Used in conjunction with the `AntdForm` form batch value collection/control feature, serving as the field name for the current form item, with `id` as the default value.

- optionFilterProp (a value equal to: 'value', 'label'; default 'label'):
    The target field for option keyword search, options include `'value'`, `'label'`. Default value: `'label'`.

- options (list; required):
    Defines the data structure required for constructing cascade selection, consistent with `optionsMode`.

- optionsMode (a value equal to: 'tree', 'flat'; default 'tree'):
    The rendering mode corresponding to the `options` format, options include `'tree'` (tree mode), `'flat'` (flat mode). Default value: `'tree'`.

- optionsNodeKeyToLabel (dict with strings as keys and values of type a list of or a singular dash component, string or number; optional):
    For specified nodes in the cascade structure, defines the component-type content that serves as the title, with higher priority than the corresponding `label` value in `options`.

- panelMode (boolean; default False):
    Whether to enable the embedded panel mode. Default value: `False`.

- persisted_props (list of a value equal to: 'value's; default ['value']):
    The names of several properties that enable attribute persistence, with the option of `'value'`. Default value: `['value']`.

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    The storage type for property persistence, options include `'local'` (local persistence), `'session'` (session persistence), `'memory'` (memory persistence). Default value: `'local'`.

- placeholder (string; optional):
    The placeholder text content of the input box.

- placement (a value equal to: 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'; default 'bottomLeft'):
    The direction in which the selection menu expands, options include `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, `'topRight'`. Default value: `'bottomLeft'`.

- popupClassName (string; optional):
    The CSS class name of the expanded menu.

- popupContainer (a value equal to: 'parent', 'body'; default 'body'):
    The anchoring strategy for the related expansion layer, options include `'parent'`, `'body'`. Default value: `'body'`.

- readOnly (boolean; optional):
    Whether to render in read-only state. Default value: `False`.

- showCheckedStrategy (a value equal to: 'show-parent', 'show-child'; optional):
    The strategy for filling in the selected options, options include `'show-parent'`, `'show-child'`.

- size (a value equal to: 'small', 'middle', 'large'; optional):
    The size specification of the current component, options include `'small'`, `'middle'`, `'large'`. Default value: `'middle'`.

- status (a value equal to: 'error', 'warning'; optional):
    Controls the validation status, options include `'error'`, `'warning'`.

- style (dict; optional):
    The current component's CSS styles.

- value (list of string | numbers | list of list of string | numbers; optional):
    Listens for or sets the selected values.

- variant (a value equal to: 'outlined', 'borderless', 'filled'; optional):
    The variant type, options include `'outlined'`, `'borderless'`, `'filled'`. Where `'outlined'` is equivalent to `bordered=True`, but has higher priority.
