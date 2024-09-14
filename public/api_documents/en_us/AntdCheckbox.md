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

- label (a list of or a singular dash component, string or number; optional):
    Component type, label content.

- autoFocus (boolean; default False):
    Whether to automatically gain focus. Default value: `False`.

- checked (boolean; default False):
    To monitor or set whether the current checkbox is checked. Default value: `False`.

- indeterminate (boolean; default False):
    Whether to force rendering in an indeterminate state, which only affects the style and is unrelated to the checked state. Default value: `False`.

- readOnly (boolean; default False):
    Whether to render in read-only state. Default value: `False`.

- batchPropsNames (list of strings; optional):
    A list of property names to be included in [batch property monitoring](/batch-props-values).

- batchPropsValues (dict; optional):
    Monitor the values of several properties specified in `batchPropsNames`.

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- loading_state (dict; optional):

    `loading_state` is a dictionary with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'checked's; default ['checked']):
    A list of property names for the enabled property persistence feature, with the option of `'checked'`. Default value: `['checked']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    The type of property persistence storage, with options of `'local'` (local persistence), `'session'` (session persistence), `'memory'` (memory persistence).
    Default value: `'local'`.
