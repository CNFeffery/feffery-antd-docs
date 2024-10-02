- id (string; optional):
    The unique identifier for the component.

- key (string; optional):
    Updates the `key` value of the current component, which can force a redraw of the current component.

- children (a list of or a singular dash component, string or number; optional):
    The component type, embedding common form input components.

- style (dict; optional):
    The CSS style of the current component.

- className (string | dict; optional):
    The CSS class name of the current component, supporting [dynamic CSS](/advanced-classname).

- required (boolean; default False):
    Whether to display an additional asterisk (*) indicating a required field. Default value: `False`.

- labelCol (dict; optional):
    Configures the label part of the form item with higher priority than the `labelCol` parameter in the parent `AntdForm`.

    `labelCol` is a dict with keys:

    - span (number; optional):
        The fraction of the total width (total of 24) that the label part occupies.

    - offset (number; optional):
        The fraction of the width that the label part is offset to the right.

    - flex (string | number; optional):
        Similar to the flex property in CSS, used to more flexibly control the width occupied by the label part.

- wrapperCol (dict; optional):
    Configures the control part of the form item with higher priority than the `labelCol` parameter in the parent `AntdForm`.

    `wrapperCol` is a dict with keys:

    - span (number; optional):
        The fraction of the total width (total of 24) that the control part occupies.

    - offset (number; optional):
        The fraction of the width that the control part is offset to the right.

    - flex (string | number; optional):
        Similar to the flex property in CSS, used to more flexibly control the width occupied by the control part.

- colon (boolean; optional):
    When `layout='horizontal'`, controls whether to add a colon at the end of the label part of the form item, with higher priority than the `colon` parameter in the parent `AntdForm`.

- label (a list of or a singular dash component, string or number; optional):
    The component type, the content of the current form item label.

- labelAlign (a value equal to: 'left', 'right'; optional):
    The text alignment of the label part of the form item, with options `'left'`, `'right'`, and higher priority than the `labelAlign` parameter in the parent `AntdForm`.
    Default value: `'right'`.

- tooltip (a list of or a singular dash component, string or number; optional):
    The component type, additional text prompt information after the current form item label content.

- extra (a list of or a singular dash component, string or number; optional):
    The component type, additional prompt information for the current form item.

- validateStatus (a value equal to: 'success', 'warning', 'error', 'validating'; optional):
    Controls the validation status, with options `'success'`, `'warning'`, `'error'`, `'validating'`.

- hasFeedback (boolean; default False):
    Corresponds to the status set by `validateStatus`, used to control whether to display additional status icons. Default value: `False`.

- help (a list of or a singular dash component, string or number; optional):
    The component type, additional explanatory content consistent with the `validateStatus` status.

- hidden (boolean; default False):
    Whether to hide the current field. Default value: `False`.

- layout (a value equal to: 'horizontal', 'vertical'; optional):
    The layout mode of the form item, with options `'horizontal'`, `'vertical'`.

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading.
