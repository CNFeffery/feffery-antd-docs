- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the `key` value of the current component to force a redraw of the component.

- style (dict; optional):
    CSS styles for the current component.

- className (string | dict; optional):
    CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

- name (string; optional):
    Used in conjunction with the `AntdForm` form for batch value collection/control, serving as the field name for the current form item, with `id` as the default value.

- disabled (boolean; default False):
    Whether to disable the current component. Default value: `False`.

- options (list of dicts; optional):
    Defines the data structure required to construct a combo box.

    `options` is a list of string | number | dict with keys:

    - disabled (boolean; optional):
        Whether to disable the current selection box. Default value: `False`.

    - label (a list of or a singular dash component, string or number; optional):
        Component type, the label content of the current selection box.

    - value (string | number; optional):
        The corresponding value of the current selection box.

- value (list of string | numbers; optional):
    To listen for or set the selected value.

- readOnly (boolean; default False):
    Whether to render in read-only state. Default value: `False`.

- batchPropsNames (list of strings; optional):
    Several property names to be included in [batch property listening](/batch-props-values).

- batchPropsValues (dict; optional):
    Listens to the values of several properties specified in `batchPropsNames`.

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- loading_state (dict; optional):
    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'value's; default ['value']):
    Several property names for the property persistence feature, with the option `'value'`. Default value: `['value']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Property persistence storage type, with options `'local'` (local persistence), `'session'` (session persistence), `'memory'` (memory persistence).
    Default value: `'local'`.
