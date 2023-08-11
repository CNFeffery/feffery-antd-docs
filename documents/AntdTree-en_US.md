**id:** *string* or *dict*

　　Used to set the unique ID information for the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for a forced redraw effect.

**style:** *dict*

　　Used to set the CSS style for the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**treeDataMode:** *string*, default: `'tree'`

　　Used to set the parsing mode for the `treeData` parameter. Options are `'tree'` (tree structure) and `'flat'` (flat structure).

**treeData:** `list[dict]`, required

　　Used to build the option structure for the tree selection.

　　When `treeDataMode='tree'`, the `treeData` parameter should follow the tree parsing mode, and each dictionary can have the following key-value pairs:

- **title:** *string*, required, used to set the title content of the current node.
- **key:** *string*, required, used to uniquely identify the current node.
- **disabled:** *bool*, default: `False`, used to set whether the current node is disabled.
- **icon:** *string*, used to set the prefix icon for the current node, same as the corresponding parameter in `AntdIcon`.
- **checkable:** *bool*, used to set whether the current node renders a checkbox.
- **disableCheckbox:** *bool*, used to set whether the checkbox of the current node is disabled.
- **selectable:** *bool*, used to set whether the current node can be selected.
- **style:** *dict*, used to set the CSS style for the current node.
- **className:** *string*, used to set the CSS class name for the current node.
- **tooltipProps:** *dict*, used to configure tooltip-related functionality for the current node, available key-value pairs include:
  - **title:** *string*, used to set the text content of the tooltip for the current node.
  - **placement:** *string*, used to set the position of the tooltip for the current node, options are `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`.
- **contextMenu:** `list[dict]`, used to define the options for the context menu of the current node, each dictionary can have the following key-value pairs:
  - **key:** *string*, used to set the unique ID for the current context menu item.
  - **label:** *string*, used to set the title content of the current context menu item.
  - **icon:** *string*, used to set the prefix icon for the current context menu item, same as the corresponding parameter in `AntdIcon`.

　　Here's an example of tree-like `treeData`:

```python
treeData = [
    {
        'key': 'Node 1',
        'title': 'Node 1',
        'children': [
            {
                'key': f'Node 1-{i}',
                'title': f'Node 1-{i}'
            }
            for i in range(1, 5)
        ]
    },
    {
        'key': 'Node 2',
        'title': 'Node 2'
    }
]
```

　　When `treeDataMode='flat'`, the `treeData` parameter should follow the flat parsing mode, and each dictionary can have the following key-value pairs:

- **title:** *string*,

 required, used to set the title content of the current node.
- **key:** *string*, required, used to uniquely identify the current node and establish the parent-child relationship.
- **disabled:** *bool*, default: `False`, used to set whether the current node is disabled.
- **icon:** *string*, used to set the prefix icon for the current node, same as the corresponding parameter in `AntdIcon`.
- **checkable:** *bool*, used to set whether the current node renders a checkbox.
- **disableCheckbox:** *bool*, used to set whether the checkbox of the current node is disabled.
- **selectable:** *bool*, used to set whether the current node can be selected.
- **style:** *dict*, used to set the CSS style for the current node.
- **className:** *string*, used to set the CSS class name for the current node.
- **tooltipProps:** *dict*, used to configure tooltip-related functionality for the current node, available key-value pairs include:
  - **title:** *string*, used to set the text content of the tooltip for the current node.
  - **placement:** *string*, used to set the position of the tooltip for the current node, options are `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`.
- **contextMenu:** `list[dict]`, used to define the options for the context menu of the current node, each dictionary can have the following key-value pairs:
  - **key:** *string*, used to set the unique ID for the current context menu item.
  - **label:** *string*, used to set the title content of the current context menu item.
  - **icon:** *string*, used to set the prefix icon for the current context menu item, same as the corresponding parameter in `AntdIcon`.
- **parent:** *string*, used to declare the parent node key for the current node and establish the parent-child relationship.

　　Here's an example of flat `treeData`:

```python
treeData = [
    {
        'title': '四川省',
        'key': '四川省'
    },
    {
        'title': '成都市',
        'key': '成都市',
        'parent': '四川省'
    },
    {
        'title': '广安市',
        'key': '广安市',
        'parent': '四川省'
    },
    {
        'title': '重庆市',
        'key': '重庆市'
    },
    {
        'title': '渝中区',
        'key': '渝中区',
        'parent': '重庆市'
    },
    {
        'title': '渝北区',
        'key': '渝北区',
        'parent': '重庆市'
    },
    {
        'title': '解放碑街道',
        'key': '解放碑街道',
        'parent': '渝中区'
    }
]
```

**showIcon:** *bool*, default: `False`

　　Used to set whether to render icons for tree node prefixes.

**selectable:** *bool*, default: `True`

　　Used to *set whether the tree nodes can be selected*.

**multiple:** *bool*, default: `False`

　　Used to *set whether multiple tree nodes can be selected*.

**checkable:** *bool*, default: `False`

　　Used to *set whether to add checkboxes to the tree nodes*.

**defaultExpandAll:** *bool*, default: `False`

　　Used to *set whether to expand all nodes on initialization*.

**expandedKeys:** `list[string]`

　　Used to *set or listen to the keys of nodes in the expanded state*.

**defaultExpandedKeys:** `list[string]`

　　Used to *set the keys of nodes in the expanded state on initialization*.

**defaultExpandParent:** *bool*, default: `False`

　　Used to *set whether the parent nodes of the initially expanded nodes should be automatically expanded as well*.

**selectedKeys:** `list[string]`

　　Used to *set or listen to the keys of nodes in the selected state*.

**defaultSelectedKeys:** `list[string]`

　　Used to *set the keys of nodes in the selected state on initialization*.

**checkedKeys:** `list[string]`

　　Used to *set or listen to the keys of nodes in the checked state*.

**defaultCheckedKeys:** `list[string]`

　　Used to *set the keys of nodes in the checked state on initialization*.

**halfCheckedKeys:** `list[string]`

　　Used to *listen to the keys of nodes in the half-checked state*.

**checkStrictly:** *bool*, default: `False`

　　Used to *set whether the checking behavior between nodes and their descendants is independent and not associated with each other*.

**showLine:** *bool* or *dict*, default: `{'showLeafIcon': False}`

　　Used to *set whether to show connecting lines*. When passing a *dict* as input, the available key-value pairs include:

- **showLeafIcon:** *bool*, used to *set whether to render prefix icons for leaf nodes*.

**height:** *int* or *float*

　　Used to *set the window pixel height in virtual scrolling mode*. If not set, virtual scrolling will not be enabled.

**draggable:** *bool*, default: `False`

　　When `treeDataMode="tree"`, used to *set whether to enable node dragging*. After each valid drag action, the new tree structure will be updated in the `treeData`.

**draggedNodeKey:** *string*

　　Used to *listen to the node key of each valid node drag action*.

**clickedContextMenu:** *dict*

　　Used to *listen to each valid right-click menu item click event*. It has the following key-value attributes:

- **nodeKey:** *string*, used to *listen to the key value of the tree node corresponding to the right-click menu item click event*.
- **menuKey:** *string*, used to *listen to the key value of the option corresponding to the right-click menu item click event*.
- **timestamp:** *int*, used to *listen to the timestamp of the right-click menu item click event*.

**persistence:** *bool*

　　Used to *set whether to enable property persistence for the current component*.

**persisted_props:** *list*, default: `['selectedKeys', 'checkedKeys', 'expandedKeys', 'halfCheckedKeys']`

　　Used to *set which properties of the current component to persist*. The available options are `'selectedKeys'`, `'checkedKeys'`, `'expanded

Keys'`, `'halfCheckedKeys'`.

**persistence_type:** *string*, default: `'local'`

　　Used to *set the storage type for property persistence of the current component*. The available options are `'local'` (browser local cache), `'session'` (current tab session cache), `'memory'` (temporary memory cache).