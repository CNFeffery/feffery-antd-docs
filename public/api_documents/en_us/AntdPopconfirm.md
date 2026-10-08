- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Confirmation popup target element. Supports components.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- styles (dict; optional):
    Fine-grained CSS styles for child elements.

    `styles` is a dict with keys:

    - root (dict; optional):
        CSS styles for the root element, including the arrow and content.

    - body (dict; optional):
        CSS styles for the body element.

- classNames (dict; optional):
    Fine-grained CSS class names for child elements.

    `classNames` is a dict with keys:

    - root (string; optional):
        CSS class name for the root element, including the arrow and content.

    - body (string; optional):
        CSS class name for the body element.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- icon (a list of or a singular dash component, string or number; optional):
    Hint icon. Supports components.

- title (a list of or a singular dash component, string or number; optional):
    Title content. Supports components.

- description (a list of or a singular dash component, string or number; optional):
    Description content. Supports components.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- placement (a value equal to: 'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight', 'leftTop', 'leftBottom', 'rightTop', 'rightBottom'; default 'top'):
    Confirmation popup placement. Supported values: `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`, `'leftTop'`, `'leftBottom'`, `'rightTop'`, `'rightBottom'`. Default: `'top'`.

- mouseEnterDelay (number; default 0.1):
    Delay in seconds between mouse enter and showing the confirmation popup. Default: `0.1`.

- mouseLeaveDelay (number; default 0.1):
    Delay in seconds between mouse leave and hiding the confirmation popup. Default: `0.1`.

- okText (a list of or a singular dash component, string or number; optional):
    Confirm button content. Supports components.

- okButtonProps (dict; optional):
    Confirm button settings.

    `okButtonProps` is a dict with keys:

    - size (a value equal to: 'small', 'middle', 'large'; optional):
        Button size specification, options include `'small'`, `'middle'`, `'large'`. Default value: `'middle'`.

    - type (a value equal to: 'primary', 'ghost', 'dashed', 'link', 'text', 'default'; optional):
        Button type, options include `'default'`, `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`. Default value: `'default'`.

    - danger (boolean; optional):
        Whether the button displays a danger style. Default value: `False`.

    - disabled (boolean; optional):
        Whether the button presents a disabled state. Default value: `False`.

    - shape (a value equal to: 'circle', 'round'; optional):
        The shape of the button, with options `'default'`, `'circle'`, `'round'`. Default value: `'default'`.

    - style (dict; optional):
        Button CSS style.

    - className (string; optional):
        Button CSS class name.

- cancelText (a list of or a singular dash component, string or number; optional):
    Cancel button content. Supports components.

- cancelButtonProps (dict; optional):
    Cancel button settings.

    `cancelButtonProps` is a dict with keys:

    - size (a value equal to: 'small', 'middle', 'large'; optional):
        Button size specification, options include `'small'`, `'middle'`, `'large'`. Default value: `'middle'`.

    - type (a value equal to: 'primary', 'ghost', 'dashed', 'link', 'text', 'default'; optional):
        Button type, options include `'default'`, `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`. Default value: `'default'`.

    - danger (boolean; optional):
        Whether the button displays a danger style. Default value: `False`.

    - disabled (boolean; optional):
        Whether the button presents a disabled state. Default value: `False`.

    - shape (a value equal to: 'circle', 'round'; optional):
        The shape of the button, with options `'default'`, `'circle'`, `'round'`. Default value: `'default'`.

    - style (dict; optional):
        Button CSS style.

    - className (string; optional):
        Button CSS class name.

- showCancel (boolean; default True):
    Whether to show the cancel button. Default: `True`.

- confirmCounts (number; default 0):
    Cumulative number of Confirm button clicks. Default: `0`.

- cancelCounts (number; default 0):
    Cumulative number of Cancel button clicks. Default: `0`.

- trigger (a value equal to: 'hover', 'focus', 'click' | list of a value equal to: 'hover', 'focus', 'click's; default 'click'):
    Confirmation popup triggers. Multiple triggers can be combined. Supported values: `'hover'`, `'focus'`, `'click'`. Default: `'click'`.

- zIndex (number; optional):
    Confirmation popup z-index.

- arrow (a value equal to: 'show', 'hide', 'center'; default 'show'):
    Arrow display mode. Supported values: `'show'`, `'hide'`, `'center'`. Default: `'show'`.

- fresh (boolean; default False):
    Whether to keep the content updated. Default: `False`.

- open (boolean; default False):
    Monitor or set confirmation popup visibility. Default: `False`.

- permanent (boolean; default False):
    Whether to keep the confirmation popup's visibility fixed. Default: `False`.

- popupContainer (a value equal to: 'parent', 'body'; default 'body'):
    Parent container strategy for rendering the popup. Supported values: `'parent'`, `'body'`. Default: `'body'`.

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
