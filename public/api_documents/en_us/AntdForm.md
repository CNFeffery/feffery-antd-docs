- id (string; optional):
    The unique identifier for the component.

- key (string; optional):
    Updates the `key` value of the current component, which can force a redraw of the component.

- children (a list of or a singular dash component, string or number; optional):
    The component type, embedding related `AntdFormItem` components or common form input components.

- style (dict; optional):
    The CSS style of the current component.

- className (string | dict; optional):
    The CSS class name of the current component, supporting [dynamic CSS](/advanced-classname).

- layout (a value equal to: 'horizontal', 'vertical', 'inline'; default 'horizontal'):
    The form layout mode, with options `'horizontal'`, `'vertical'`, `'inline'`.
    Default value: `'horizontal'`.

- labelCol (dict; optional):
    Configures the label part of the form item.

    `labelCol` is a dict with keys:

    - span (number; optional):
        The fraction of the total width (total of 24) that the label part occupies.

    - offset (number; optional):
        The fraction of the width that the label part is offset to the right.

    - flex (string | number; optional):
        Similar to the flex property in CSS, used to more flexibly control the width occupied by the label part.

- wrapperCol (dict; optional):
    Configures the control part of the form item.

    `wrapperCol` is a dict with keys:

    - span (number; optional):
        The fraction of the total width (total of 24) that the control part occupies.

    - offset (number; optional):
        The fraction of the width that the control part is offset to the right.

    - flex (string | number; optional):
        Similar to the flex property in CSS, used to more flexibly control the width occupied by the control part.

- colon (boolean; default True):
    When `layout='horizontal'`, controls whether to add a colon at the end of the label part of the form item.

- labelAlign (a value equal to: 'left', 'right'; default 'right'):
    The text alignment of the label part of the form item, with options `'left'`, `'right'`. Default value: `'right'`.

- labelWrap (boolean; default False):
    Whether to allow wrapping for excessively long form item labels. Default value: `False`.

- enableBatchControl (boolean; default False):
    Whether to enable batch control functionality for the form, which may result in some performance loss. Default value: `False`.

- values (dict; optional):
    When `enableBatchControl=True`, can be used to listen to or set the input value changes of internal form input components, after which the `defaultValue`, `value` parameters of the internal form input components will become ineffective.

- validateStatuses (dict with strings as keys and values of type a value equal to: 'success', 'warning', 'error', 'validating'; optional):
    When `enableBatchControl=True`, can be used to uniformly set the `validateStatus` values of internal `AntdFormItem` components, with keys as the `label` values of the corresponding `AntdFormItem` components, with lower priority than the `validateStatus` values of each `AntdFormItem` component.

- helps (dict with strings as keys and values of type a list of or a singular dash component, string or number; optional):
    When `enableBatchControl=True`, can be used to uniformly set the `help` values of internal `AntdFormItem` components, with keys as the `label` values of the corresponding `AntdFormItem` components, with lower priority than the `help` values of each `AntdFormItem` component.

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
