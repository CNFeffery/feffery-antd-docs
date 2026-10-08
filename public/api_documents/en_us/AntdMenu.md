- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- expandIcon (dict; optional):
    Custom expand icon. Dictionary configuration is recommended only for `mode='inline'`.

    `expandIcon` is a list of or a singular dash component, string
    or number | dict with keys:

    - expand (a list of or a singular dash component, string or number; optional):
        The icon for expanding.

    - collapse (a list of or a singular dash component, string or number; optional):
        The icon for collapsing.

- menuItems (list; optional):
    The data structure of the navigation menu.

- menuItemKeyToTitle (dict with strings as keys and values of type a list of or a singular dash component, string or number; optional):
    Define component-type menu item titles for specified nodes, with a higher priority than the title attribute of the corresponding node in `menuItems`.

- menuItemKeyToIcon (dict with strings as keys and values of type a list of or a singular dash component, string or number; optional):
    Component used as a menu item icon. Takes precedence over the corresponding icon in menuItems.

- mode (a value equal to: 'vertical', 'horizontal', 'inline'; default 'vertical'):
    Display mode. Supported values: `'vertical'`, `'horizontal'`, `'inline'`. Default: `'vertical'`.

- theme (a value equal to: 'light', 'dark'; default 'light'):
    Color theme. Supported values: `'light'`, `'dark'`. Default: `'light'`.

- currentKey (string; optional):
    Monitor or set the key value of the currently selected menu item.

- currentItem (dict; optional):
    Monitor the information of the currently selected menu item.

- currentKeyPath (list; optional):
    Monitor the key value path information of the currently selected menu item.

- currentItemPath (list; optional):
    Monitor the path information of the currently selected menu item.

- openKeys (list of strings; optional):
    Monitor or set the key values of the currently expanded submenu items.

- onlyExpandCurrentSubMenu (boolean; default False):
    Whether to only expand the parent menu of the currently selected item. Default value: `False`.

- defaultOpenKeys (list of strings; optional):
    The key values of the menu items that are expanded by default.

- defaultSelectedKey (string; optional)

- renderCollapsedButton (boolean; default False):
    Whether to render the menu collapse state control button. Default value: `False`.

- popupContainer (a value equal to: 'parent', 'body'; default 'body'):
    Container anchoring strategy for the expanded menu. Supported values: `'parent'`, `'body'`. Default: `'body'`.

- inlineCollapsed (boolean; optional):
    Whether the current menu is collapsed, only effective in inline mode. Default value: `False`.

- inlineIndent (number; default 24):
    The pixel indentation width of the submenu relative to the upper level in inline mode. Default value: `24`.

- triggerSubMenuAction (a value equal to: 'hover', 'click'; default 'hover'):
    Trigger for opening or closing a `SubMenu`. Has no effect when `mode='inline'`. Supported values: `'hover'`, `'click'`, `mode='inline'`. Default: `'hover'`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.

- persistence (boolean | string | number; optional):
    Whether to enable persistence for the current component.

- persisted_props (list of a value equal to: 'currentKey', 'openKeys's; optional):
    Component properties whose values are persisted. Supported values: `'currentKey'`, `'openKeys'`. Default: `['currentKey', 'openKeys']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Storage type for persisted properties. Default: `'local'`.
