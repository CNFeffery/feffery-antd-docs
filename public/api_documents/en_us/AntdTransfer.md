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

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- dataSource (list of dicts; optional):
    Option definitions.

    `dataSource` is a list of dicts with keys:

    - key (string | number; optional):
        Unique option ID.

    - title (a list of or a singular dash component, string or number; optional):
        Option title. Supports components.

    - disabled (boolean; optional):
        Whether to disable the current option. Default: `False`.

- selectionsIcon (a list of or a singular dash component, string or number; optional):
    Custom dropdown icon. Supports components.

- height (string | number; optional):
    Overall transfer component height.

- pagination (dict; default False):
    Option pagination settings. Default: `False`.

    `pagination` is a boolean | dict with keys:

    - pageSize (number; optional):
        Maximum number of options per page.

- oneWay (boolean; default False):
    Whether to enable one-way transfer mode. Default: `False`.

- operations (list of a list of or a singular dash component, string or numbers; default ['', '']):
    Content of the left/right move buttons. Default: `['', '']`.

- showSearch (boolean; default False):
    Whether to show the search input. Default: `False`.

- optionFilterMode (a value equal to: 'case-insensitive', 'case-sensitive', 'regex'; default 'case-insensitive'):
    Search matching mode: `'case-insensitive'`, `'case-sensitive'`, or `'regex'`. Default: `'case-insensitive'`.

- showSelectAll (boolean; default True):
    Whether to show the Select all checkbox. Default: `True`.

- titles (list of a list of or a singular dash component, string or numbers; optional):
    Titles of the left and right panels.

- targetKeys (list of number | strings; optional):
    Monitor or set selected item `key` values in the right panel.

- moveDirection (a value equal to: 'left', 'right'; optional):
    Direction of the most recent transfer operation. Supported values: `'left'`, `'right'`.

- moveKeys (list of number | strings; optional):
    Item `key` values involved in the most recent transfer operation.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- status (a value equal to: 'error', 'warning'; optional):
    Control the validation state. Options are `'error'`, `'warning'`.

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

- persisted_props (list of a value equal to: 'targetKeys's; optional):
    Properties whose values are persisted. Supported values: `'targetKeys'`. Default: `['targetKeys']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
