- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, dropdown menu trigger anchor element.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- wrapperStyle (dict; optional):
    The CSS style of the anchor element's parent container.

- wrapperClassName (string | dict; optional):
    The CSS class name of the anchor element's parent container.

- title (string; optional):
    The title content of the dropdown menu trigger element, effective when the children parameter is not set.

- buttonMode (boolean; default False):
    Whether the dropdown menu trigger element is rendered as a button, effective when the children parameter is not set. Default value: `False`.

- buttonProps (dict; optional):
    Further configuration for the button form of the dropdown menu trigger element.

    `buttonProps` is a dict with keys:

    - icon (a list of or a singular dash component, string or number; optional):
        Button icon. Supports components.

    - size (a value equal to: 'small', 'middle', 'large'; optional):
        Button size specification, options include `'small'`, `'middle'`, `'large'`. Default value: `'middle'`.

    - type (a value equal to: 'default', 'primary', 'ghost', 'dashed', 'link', 'text'; optional):
        Button type, options include `'default'`, `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`. Default value: `'default'`.

    - danger (boolean; optional):
        Whether the button displays a danger style. Default value: `False`.

    - style (dict; optional):
        Button CSS style.

    - className (string; optional):
        Button CSS class name.

- freePosition (boolean; default False):
    Whether to enable free position mode. Default value: `False`.

- freePositionStyle (dict; optional):
    CSS style for the anchor position when free position mode is enabled.

- freePositionClassName (string; optional):
    CSS class name for the anchor position when free position mode is enabled.

- clickedKey (string; optional):
    Listening to the key value of the clicked dropdown menu option.

- nClicks (number; default 0):
    Listening to the cumulative number of times the dropdown menu option has been clicked. Default value: `0`.

- menuItems (list of dicts; optional):
    `menuItems` is a list of dicts with keys:

    - title (a list of or a singular dash component, string or number; optional):
        Component type, node title.

    - extra (a list of or a singular dash component, string or number; optional):
        Additional content. Supports components.

    - href (string; optional):
        Node link address.

    - target (string; optional):
        Node link jump behavior.

    - disabled (boolean; optional):
        Whether the node is disabled. Default value: `False`.

    - icon (string; optional):
        Node prefix icon name, associated with `iconRenderer` method, same as AntdIcon's icon parameter under `'AntdIcon'` method, represents the icon's CSS class name under `'fontawesome'` method.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
        The rendering method of the prefix icon, options include `'AntdIcon'`, `'fontawesome'`. Default value: `'AntdIcon'`.

    - key (string; optional):
        Unique key value of the node.

    - isDivider (boolean; optional):
        Whether the node is rendered as a divider.

    - children (list; optional):
        Submenu items for building a cascading menu.

- selectable (boolean; default False):
    Whether menu items can be selected. Default value: `False`.

- multiple (boolean; default False):
    Whether menu items can be selected multiple times. Default value: `False`.

- selectedKeys (list of strings; optional):
    Set or listen to the key values of the currently selected menu items.

- nonSelectableKeys (list of strings; optional):
    Setting an array of key values for non-selectable items. Default value: `[]`.

- arrow (boolean; default False):
    Whether the dropdown menu renders an arrow. Default value: `False`.

- disabled (boolean; default False):
    Whether to disable the component's functionality. Default value: `False`.

- overlayClassName (string | dict; optional):
    The CSS class name of the dropdown menu container, supports [dynamic CSS](/advanced-classname).

- overlayStyle (dict; optional):
    CSS style of dropdown container.

- placement (a value equal to: 'bottomLeft', 'bottomCenter', 'bottomRight', 'topLeft', 'topCenter', 'topRight'; optional):
    The direction in which the dropdown menu pops up, options include `'bottomLeft'`, `'bottomCenter'`, `'bottomRight'`, `'topLeft'`, `'topCenter'`, `'topRight'`.

- trigger (a value equal to: 'click', 'hover'; default 'hover'):
    The trigger method for displaying the dropdown menu, options include `'click'`, `'hover'`. Default value: `'hover'`.

- autoAdjustOverflow (boolean; default True):
    Whether the dropdown menu automatically adjusts its position when it is obscured. Default value: `True`.

- visible (boolean; default False):
    Listening to or setting whether the dropdown menu is expanded. Default value: `False`.

- popupContainer (a value equal to: 'parent', 'body'; default 'body'):
    The anchor strategy for the dropdown menu's expansion layer, options include `'parent'`, `'body'`. Default value: `'body'`.

- batchPropsNames (list of strings; optional):
    List of property names to be included in batch property listening. Default value: `[]`.

- batchPropsValues (dict; optional):
    Batch listening for property values corresponding to the current batchPropsNames.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
