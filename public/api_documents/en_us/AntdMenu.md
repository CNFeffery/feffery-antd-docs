- id (string; optional):
    Unique identifier for the component.

- aria-* (string; optional):
    Wildcard for attributes in the `aria-*` format.

- className (string | dict; optional):
    The CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

- currentItem (dict; optional):
    Monitor the information of the currently selected menu item.

- currentItemPath (list; optional):
    Monitor the path information of the currently selected menu item.

- currentKey (string; optional):
    Monitor or set the key value of the currently selected menu item.

- currentKeyPath (list; optional):
    Monitor the key value path information of the currently selected menu item.

- data-* (string; optional):
    Wildcard for attributes in the `data-*` format.

- defaultOpenKeys (list of strings; optional):
    The key values of the menu items that are expanded by default.

- defaultSelectedKey (string; optional)

- expandIcon (dict; optional):
    Custom expansion icon, it is recommended to use a dictionary type only when `mode='inline'`.

    `expandIcon` is a list of or a singular dash component, string or number | dict with keys:

    - collapse (a list of or a singular dash component, string or number; optional):
        The icon for collapsing.

    - expand (a list of or a singular dash component, string or number; optional):
        The icon for expanding.

- inlineCollapsed (boolean; default False):
    Whether the current menu is collapsed, only effective in inline mode. Default value: `False`.

- inlineIndent (number; default 24):
    The pixel indentation width of the submenu relative to the upper level in inline mode. Default value: `24`.

- key (string; optional):
    Update the `key` value of the current component to force a redraw of the current component.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- menuItemKeyToTitle (dict with strings as keys and values of type a list of or a singular dash component, string or number; optional):
    Define component-type menu item titles for specified nodes, with a higher priority than the title attribute of the corresponding node in `menuItems`.

- menuItems (list; optional):
    The data structure of the navigation menu.

- mode (a value equal to: 'vertical', 'horizontal', 'inline'; default 'vertical'):
    The display mode, with options `vertical`, `horizontal`, `inline`. Default value: `vertical`.

- onlyExpandCurrentSubMenu (boolean; default False):
    Whether to only expand the parent menu of the currently selected item. Default value: `False`.

- openKeys (list of strings; optional):
    Monitor or set the key values of the currently expanded submenu items.

- persisted_props (list of a value equal to: 'currentKey', 'openKeys's; default ['currentKey', 'openKeys']):
    An array of property values that are enabled for persistence in the current component, with options `currentKey`, `openKeys`.
    Default value: `['currentKey', 'openKeys']`.

- persistence (boolean | string | number; optional):
    Whether to enable persistence for the current component.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    The type of persistent storage for the properties of the current component. Default value: `local`.

- popupContainer (a value equal to: 'parent', 'body'; default 'body'):
    The anchoring strategy for the menu expansion layer, with options `parent`, `body`. Default value: `body`.

- renderCollapsedButton (boolean; default False):
    Whether to render the menu collapse state control button. Default value: `False`.

- style (dict; optional):
    The CSS style of the current component.

- theme (a value equal to: 'light', 'dark'; default 'light'):
    The theme, with options `light`, `dark`. Default value: `light`.

- triggerSubMenuAction (a value equal to: 'hover', 'click'; default 'hover'):
    The trigger behavior for the `SubMenu` to expand/close, with options `hover`, `click`, which is invalid when `mode='inline'`.
    Default value: `hover`.
