- children (a list of or a singular dash component, string or number; optional):
    Component type, dropdown menu trigger anchor element.

- id (string; optional):
    Unique ID for the component.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- arrow (boolean; default False):
    Whether the dropdown menu renders an arrow. Default value: `False`.

- autoAdjustOverflow (boolean; default True):
    Whether the dropdown menu automatically adjusts its position when it is obscured. Default value: `True`.

- batchPropsNames (list of strings; optional):
    Attribute names to be included in batch property listening. Default value: `[]`.

- batchPropsValues (dict; optional):
    Batch listening to attribute values corresponding to the current batchPropsNames.

- buttonMode (boolean; default False):
    Whether the dropdown menu trigger element is rendered as a button, effective when the children parameter is not set. Default value: `False`.

- buttonProps (dict; optional):
    Further configuration for the button form of the dropdown menu trigger element.

    `buttonProps` is a dict with keys:

    - className (string; optional):
        Button CSS class name.

    - danger (boolean; optional):
        Whether the button displays a danger style. Default value: `False`.

    - size (a value equal to: 'small', 'middle', 'large'; optional):
        Button size specification, options include `'small'`, `'middle'`, `'large'`. Default value: `'middle'`.

    - style (dict; optional):
        Button CSS style.

    - type (a value equal to: 'default', 'primary', 'ghost', 'dashed', 'link', 'text'; optional):
        Button type, options include `'default'`, `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`.
        Default value: `'default'`.

- className (string | dict; optional):
    The current component's CSS class name, supports [dynamic CSS](/advanced-classname).

- clickedKey (string; optional):
    Listening to the key value of the clicked dropdown menu option.

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- disabled (boolean; default False):
    Whether to disable the component's functionality. Default value: `False`.

- freePosition (boolean; default False):
    Whether to enable free position mode. Default value: `False`.

- freePositionClassName (string; optional):
    CSS class name for the anchor position when free position mode is enabled.

- freePositionStyle (dict; optional):
    CSS style for the anchor position when free position mode is enabled.

- key (string; optional):
    Update the `key` value of the current component to force a redraw of the current component.

- loading_state (dict; optional):

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- menuItems (list of dicts; optional):
    The data structure of the dropdown menu.

    `menuItems` is a list of dicts with keys:

    - disabled (boolean; optional):
        Whether the node is disabled. Default value: `False`.

    - href (string; optional):
        Node link address.

    - icon (string; optional):
        Node prefix icon name, associated with `iconRenderer` method, same as AntdIcon's icon parameter under `'AntdIcon'` method, represents the icon's CSS class name under `'fontawesome'` method.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
        The rendering method of the prefix icon, options include `'AntdIcon'`, `'fontawesome'`. Default value: `'AntdIcon'`.

    - isDivider (boolean; optional):
        Whether the node is rendered as a divider.

    - key (string; optional):
        Unique key value of the node.

    - target (string; optional):
        Node link jump behavior.

    - title (a list of or a singular dash component, string or number; optional):
        Component type, node title.

- multiple (boolean; default False):
    Whether menu items can be selected multiple times. Default value: `False`.

- nClicks (number; default 0):
    Listening to the cumulative number of times the dropdown menu option has been clicked. Default value: `0`.

- nonSelectableKeys (list of strings; optional):
    Setting an array of key values for non-selectable items. Default value: `[]`.

- overlayClassName (string | dict; optional):
    The CSS class name of the dropdown menu container, supports [dynamic CSS](/advanced-classname).

- overlayStyle (dict; optional):
    The CSS style of the dropdown menu container.

- placement (a value equal to: 'bottomLeft', 'bottomCenter', 'bottomRight', 'topLeft', 'topCenter', 'topRight'; optional):
    The direction in which the dropdown menu pops up, options include `'bottomLeft'`, `'bottomCenter'`, `'bottomRight'`, `'topLeft'`, `'topCenter'`, `'topRight'`.

- popupContainer (a value equal to: 'parent', 'body'; default 'body'):
    The anchor strategy for the dropdown menu's expansion layer, options include `'parent'`, `'body'`. Default value: `'body'`.

- selectable (boolean; default False):
    Whether menu items can be selected. Default value: `False`.

- selectedKeys (list of strings; optional):
    Set or listen to the key values of the currently selected menu items.

- style (dict; optional):
    The current component's CSS style.

- title (string; optional):
    The title content of the dropdown menu trigger element, effective when the children parameter is not set.

- trigger (a value equal to: 'click', 'hover'; default 'hover'):
    The trigger method for displaying the dropdown menu, options include `'click'`, `'hover'`. Default value: `'hover'`.

- visible (boolean; default False):
    Listening to or setting whether the dropdown menu is expanded. Default value: `False`.

- wrapperClassName (string | dict; optional):
    The CSS class name of the anchor element's parent container.

- wrapperStyle (dict; optional):
    The CSS style of the anchor element's parent container.
