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

- treeDataMode (a value equal to: 'tree', 'flat'; default 'tree'):
    Format of `treeData`: `'tree'` for nested data or `'flat'` for flat data. Default: `'tree'`.

- treeData (list; required):
    Tree data structure, matching `treeDataMode`.

- treeNodeKeyToTitle (dict with strings as keys and values of type a list of or a singular dash component, string or number; optional):
    Component titles for specified tree nodes. Takes precedence over the corresponding `title` in `treeData`.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):
    Current component size specification. Options are `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

- bordered (boolean; default True):
    Whether to show the border. When set to `True`, it is equivalent to `variant='outlined'`. Default: `True`.

- variant (a value equal to: 'outlined', 'borderless', 'filled', 'underlined'; optional):
    Variant: 'outlined', 'borderless', 'filled', or `'underlined'`. 'outlined' is equivalent to bordered=True; this setting takes precedence over bordered.

- placeholder (string; optional):
    Placeholder text content for the input box.

- placement (a value equal to: 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'; default 'bottomLeft'):
    The direction in which the selection menu expands, options include `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, `'topRight'`. Default value: `'bottomLeft'`.

- treeLine (boolean; default False):
    Whether to show connecting lines. Default: `False`.

- value (string | number | list of string | numbers; optional):
    Listen to or set the selected value(s).

- defaultValue (string | number | list of string | numbers; optional):
    Initial selected value(s).

- maxCount (number; optional):
    Maximum selections when `multiple=True`. `maxCount` has no effect if `showCheckedStrategy='show-all'` with `treeCheckStrictly=False`, or if `showCheckedStrategy='show-parent'`.

- maxTagCount (number | a value equal to: 'responsive'; optional):
    Maximum number of visible selected-value tags when `multiple=True`.

- maxTagPlaceholder (a list of or a singular dash component, string or number; optional):
    Content shown for hidden selected-value tags when `multiple=True`.

- maxTagTextLength (number; optional):
    Maximum displayed text length of selected-value tags when `multiple=True`.

- listHeight (number; default 256):
    Maximum selection menu height in pixels. Default: `256`.

- multiple (boolean; default False):
    Whether to enable multi-selection mode. Default value: `False`.

- suffixIcon (a list of or a singular dash component, string or number; optional):
    Custom selection input suffix icon. Supports components.

- switcherIcon (a list of or a singular dash component, string or number; optional):
    Custom tree node expand/collapse icon. Supports components.

- treeCheckable (boolean; default False):
    Whether tree nodes can be checked. Default: `False`.

- treeCheckStrictly (boolean; default False):
    Whether node selection is independent of descendant selection. Default: `False`.

- treeDefaultExpandAll (boolean; default False):
    Whether all nodes are initially expanded. Default: `False`.

- treeDefaultExpandedKeys (list of strings; optional):
    Initial array of expanded node `key` values.

- treeExpandedKeys (list of strings; optional):
    Monitor or set the array of expanded node `key` values.

- virtual (boolean; default True):
    Whether virtual scrolling is enabled. Default: `True`.

- status (a value equal to: 'error', 'warning'; optional):
    Control the validation state. Options are `'error'`, `'warning'`.

- allowClear (boolean; default True):
    Whether to allow one-click clearing of selected values. Default: `True`.

- treeNodeFilterProp (a value equal to: 'title', 'value'; default 'value'):
    Field searched using the input text. Supported values: `'value'`, `'title'`. Default: `'value'`.

- treeNodeFilterMode (a value equal to: 'case-insensitive', 'case-sensitive', 'regex'; default 'case-insensitive'):
    Search matching mode: `'case-insensitive'`, `'case-sensitive'`, or `'regex'`. Default: `'case-insensitive'`.

- autoClearSearchValue (boolean; default True):
    Whether to clear the search input after selection when `multiple=True`. Default: `True`.

- showCheckedStrategy (a value equal to: 'show-all', 'show-parent', 'show-child'; default 'show-all'):
    Strategy for displaying selected items in the search input. Supported values: `'show-all'`, `'show-parent'`, `'show-child'`. Default: `'show-all'`.

- dropdownBefore (a list of or a singular dash component, string or number; optional):
    Component type, prefix content of the selection menu.

- dropdownAfter (a list of or a singular dash component, string or number; optional):
    Component type, suffix content of the selection menu.

- prefix (a list of or a singular dash component, string or number; optional):
    Component type, embedded prefix content.

- readOnly (boolean; optional):
    Whether to render as read-only. Default: `False`.

- enableAsyncLoad (boolean; default False):
    Whether to load children asynchronously. Nodes that have no `children` and do not set `isLeaf` to `True` can expand and trigger `loadingNode` updates. Default: `False`.

- loadingNode (dict; optional):
    Node expansion event that requests asynchronous data loading.

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

- loading_state (dict; optional)

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
