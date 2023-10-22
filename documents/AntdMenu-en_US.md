**id:** *string* or *dict*

　　Used to set the unique ID information for the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for a forced redraw of the component.

**style:** *dict*

　　Used to set the CSS style for the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**menuItems:** `list[dict]`

　　Used to define the navigation menu structure. Each dictionary in the list is used to define the corresponding element in the navigation menu. The available key-value parameters are:

- **component:** *string* - Used to define the role of the current element. Available options are `'Item'` (menu item, user can click to select, should be the terminal node of the entire menu structure), `'SubMenu'` (sub-menu, used to nest the next level of elements, user can click to expand/close), `'ItemGroup'` (menu item group, used to group and display nested elements, similar to the effect of option grouping in `AntdSelect`), `'Divider'` (horizontal divider).

- **props:** *dict* - Used to set other parameters for the current element, including:
  - **key:** *str* - Used to set the unique ID for the current element.
  - **title:** *str* - Used to set the title content for the current element.
  - **disabled:** *bool* (default: `False`) - Used to set whether the current element is disabled.
  - **icon:** *str* - Used to add a prefix icon to the current element, same as the `icon` parameter in `AntdIcon`.
  - **iconRenderer:** *string* type, defaulting to `'AntdIcon'`, is used to define the *rendering method for setting prefix icons for the current element*. Available options include `'AntdIcon'` (built-in icons) and `'fontawesome'` (rendered based on CSS class names).
  - **danger:** *bool* (default: `False`) - Used to set whether to display the current element in a dangerous state. This parameter is only available for `'Item'`.
  - **href:** *str* - Used to set the URL for the current node's link. This parameter is only available for `'Item'`.
  - **target:** *str* - Used to set the target behavior for the current node's link. This parameter is only available for `'Item'`.
- **dashed:** *bool* (default: `False`) - Used to set whether the current horizontal divider element is dashed. This parameter is only available for `'Divider'`.
  
- **children:** `list[dict]` - Used to pass other nested elements inside. This parameter is only available for `'SubMenu'` and `'ItemGroup'`.

　　Users can freely configure any navigation menu structure based on the above parameter hierarchy. Here is an example:

```python
menuItems = [
    {
        'component': 'Item',
        'props': {
            'key': '/home-page',
            'title': 'Home',
            'icon': 'home'
        }
    },
    {
        'component': 'SubMenu',
        'props': {
            'key': '/sub-menu1',
            'title': 'Sub Menu 1'
        },
        'children': [
            {
                'component': 'ItemGroup',
                'props': {
                    'key': '/sub-menu1/item-group1',
                    'title': 'Menu Item Group 1-1'
                },
                'children': [
                    {
                        'component': 'Item',
                        'props': {
                            'key': '/sub-menu1/item-group1/item1',
                            'title': 'Menu Item 1-1-1'
                        }
                    },
                    {
                        'component': 'Item',
                        'props': {
                            'key': '/sub-menu1/item-group1/item2',
                            'title': 'Menu Item 1-1-2',
                            'disabled': True
                        }
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/sub-menu1/item-group1/sub-menu1',
                            'title': 'Sub Menu 1-1-3'
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/sub-menu1/item-group1/sub-menu1/item1',
                                    'title': 'Menu Item 1-1-3-1'
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/sub-menu1/item-group1/sub-menu1/item2',
                                    'title': 'Menu Item 1-1-3-2'
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

mode = 'vertical'  # Default is 'vertical' mode
```

**menuItemKeyToTitle:** *dict* type

　　Used to *set the corresponding component-type title content for specified menu items*, with the `key` of the menu item as the key and the component-type content as the value. This takes precedence over the `props.title` of the corresponding menu item in `menuItems`.

**mode:** *str* (default: `'vertical'`)

　　Used to set the display mode of the navigation menu. Available options are `'vertical'` (vertical mode), `'inline'` (inline mode), `'horizontal'` (horizontal mode).

**theme:** *str* (default: `'light'`)

　　Used to set the overall color theme mode. Available options are `'light'` (light mode) and `'dark'` (dark mode).

**currentKey:** *str*

　　Used to listen to or set the `key` value of the selected `Item` element.

**defaultSelectedKey:** *str*

　　Used to set the `key` value of the initially selected `Item` element.

**openKeys:** *list*

　　Used to listen to or set the `key` values of the `SubMenu` elements that are currently in the expanded state in the menu.

**defaultOpenKeys:** *list*

　　Used to set the `key` values of the `SubMenu` elements that are initially in the expanded state in the menu.

**renderCollapsedButton:** *bool* (default: `False`)

　　Used to determine whether to render the built-in collapse/expand trigger button for the menu.

**popupContainer:** *string* (default: `'body'`)

　　Used to set the reference container type for the floating elements associated with the current component. Available options are `'body'` (reference to the root of the page) and `'parent'` (reference to the parent container of the current element). When the component is inside a scrollable container, setting `popupContainer='parent'` can solve the issue of the floating layer not scrolling with the container.

**inlineCollapsed:** *bool* (default: `False`)

　　Used to set whether the current menu is in a collapsed state, only effective when `mode='inline'`.

**inlineIndent:** *int*, default `24`

　　Used to set the pixel width of submenu indentation, only effective when `mode='inline'`.

**persistence:** *bool*

　　Used to enable property persistence for the current component.

**persisted_props:** *list* (default: `['currentKey', 'openKeys']`)

　　Used to specify which properties of the current component should be persisted. Available options are `'currentKey'` and `'openKeys'`.

**persistence_type:** *string* (default: `'local'`)

　　Used to set the storage type for property persistence of the current component. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), and `'memory'` (in-memory temporary storage).