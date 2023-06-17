**id:** *string* or *dict* type

　　Used to set the *unique id information of the current component*.

**key:** *string* type

　　Updates the `key` value of the current component to forcefully redraw the current component.

**style:** *dict* type

　　Used to set the *CSS style* of the current component.

**className:** *string* or *dict* type

　　Used to set the *CSS class name* of the current component, supports [dynamic CSS](/advanced-classname).

**locale:** *string* type, default: `'zh-cn'`

　　Used to set the *language for functional text of the current component*, available options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**treeDataMode:** *string* type, default: `'tree'`

　　Used to set the parsing mode for the `treeData` parameter, available options are `'tree'` (tree structure) and `'flat'` (flat structure).

**treeData:** `list[dict]` type, required

　　Used to *construct the option structure for tree selection*.

　　When `treeDataMode='tree'`, the `treeData` parameter needs to conform to the tree parsing mode. Each dictionary can have the following key-value pairs:

- **title:** *string* type, required, used to *set the title content of the current node*.
- **key:** *string* type, required, used to *uniquely identify the current node*.
- **value:** *int*, *float*, or *string* type, required, used to *set the value of the current node*.
- **disabled:** *bool* type, default: `False`, used to *set whether the current node is disabled*.
- **checkable:** *bool* type, used to *set whether to render a checkbox for the current node*.
- **disableCheckbox:** *bool* type, used to *set whether to disable the checkbox of the current node*.
- **selectable:** *bool* type, used to *set whether the current node can be selected*.
- **isLeaf:** *bool* type, used to *forcefully set the current node as a leaf node*.

　　Here is an example of tree `treeData`:

```python
treeData = [
    {
        'key': 'Node 1',
        'value': '1',
        'title': 'Node 1',
        'children': [
            {
                'key': f'Node 1-{i}',
                'value': f'1-{i}',
                'title': f'Node 1-{i}'
            }
            for i in range(1, 5)
        ]
    },
    {
        'key': 'Node 2',
        'value': '2',
        'title': 'Node 2'
    }
]
```

　　When `treeDataMode='flat'`, the `treeData` parameter needs to conform to the flat parsing mode. Each dictionary can have the following key-value pairs:

- **title:** *string* type, required, used to *set the title content of the current node*.
- **key:** *string* type, required, used to *uniquely identify the current node* and establish the relationship between parent and child nodes.

- **value:** *int*, *float*, or *string* type, required, used to *set the value of the current node*.
- **disabled:** *bool* type, default: `False`, used to *set whether the current node is disabled*.

- **checkable:** *bool* type, used to *set whether to render a checkbox for the current node*.
- **disableCheckbox:** *bool* type, used to *set whether to disable the checkbox of the current node*.
- **selectable:** *bool* type, used to *set whether the current node can be selected*.
- **isLeaf:** *bool* type, used to *set whether to force the current node as a leaf node*.
- **parent:** *string* type, used to *declare the parent node key value of the current node* and establish the relationship between parent and child nodes.

　　Here is an example of flat `treeData`:

```python
treeData = [
    {
        'key': 'Node 1',
        'value': '1',
        'title': 'Node 1'
    },
    *[
        {
            'key': f'Node 1-{i}',
            'value': f'1-{i}',
            'title': f'Node 1-{i}',
            'parent': 'Node 1'
        }
        for i in range(1, 6)
    ]
]
```

**disabled:** *bool* type, default: `False`

　　Used to set whether the current component is disabled.

**size:** *string* type, default: `'middle'`

　　Used to set the size of the current component. Available options are `'small'`, `'middle'`, and `'large'`.

**bordered:** *bool* type, default: `True`

　　Used to set whether to render the border.

**placeholder:** *string* type

　　Used to set the placeholder text for the empty input.

**placement:** *str* type, default: `'bottomLeft'`

　　Used to set the expansion direction of the dropdown menu. Available options are `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, and `'topRight'`.

**treeLine:** *bool* type, default: `False`

　　Used to set whether to render the connecting lines for the tree.

**value:** *int*, *float*, *string*, or *list* type

　　Used to listen to or set the currently selected value.

**defaultValue:** *int*, *float*, *string*, or *list* type

　　Used to listen to or set the initially selected value.

**maxTagCount:** *int* or *str* type

　　Used to set the maximum number of selected options displayed in the selection box in multi-select mode. It can also be set to `'responsive'` to enable responsive mode for adaptive adjustment.

**listHeight:** *int* type, default: `256`

　　Used to set the pixel height of the dropdown menu.

**multiple:** *bool* type, default: `False`

　　Used to set whether to enable multi-select mode.

**treeCheckable:** *bool* type, default: `False`

　　Used to set whether to add checkboxes to each node.

**treeDefaultExpandAll:** *bool* type, default: `False`

　　Used to set whether to expand all nodes on initialization.

**treeDefaultExpandedKeys:** *list* type

　　Used to set the keys of the nodes that are expanded by default on initialization.

**treeExpandedKeys:** *list* type

　　Used to listen to or set the keys of the currently expanded nodes.

**treeCheckStrictly:** *bool* type, default: `False`

　　Used to set whether to cancel the selection association between parent and child nodes.

**virtual:** *bool* type, default: `True`

　　Used to enable virtual scrolling to significantly improve rendering performance.

**status:** *string* type

　　Used to forcefully set the status of the component. Available options are `'error'` and `'warning'`.

**allowClear:** *bool* type, default: `True`

　　Used to set whether to allow users to clear selected options.

**treeNodeFilterProp:** *string* type, default: `'value'`

　　Used to set the target field for content search. Available options are `'title'` and `'value'`.

**treeNodeFilterMode:** *string* type, default: `'case-insensitive'`

　　Used to set the matching mode for input box search. Available options are `'case-insensitive'` (case-insensitive), `'case-sensitive'` (case-sensitive), and `'regex'` (regular expression).

**autoClearSearchValue:** *bool* type, default: `True`

　　Used to set whether to automatically clear the search content in the search box when new nodes are selected in multi-select mode.

**showCheckedStrategy:** *string* type, default: `'show-all'`

　　Used to set the display strategy for selected options

. Available options are `'show-all'` (display both parent and child nodes), `'show-parent'` (display only the parent node when all child nodes are selected), and `'show-child'` (display only the selected child nodes).

**dropdownBefore:** *component* type

　　Used to add additional custom content at the beginning of the dropdown menu.

**dropdownAfter:** *component* type

　　Used to add additional custom content at the end of the dropdown menu.

**readOnly:** *bool* type

　　Used to set whether to display in read-only mode.

**popupContainer:** *string* type, default: `'body'`

　　Used to set the reference container type for the elements involved in the floating layer of the current component. Available options are `'body'` (using the page root node as the reference) and `'parent'` (using the parent container of the current element as the reference). When the component is inside a scrollable container, setting `popupContainer='parent'` can solve the problem of the floating layer not scrolling with the container.

**persistence:** *bool* type

　　Used to enable property persistence for the current component.

**persisted_props:** *list* type, default: `['value']`

　　Used to set which properties of the current component are persisted. Available options are `'value'`.

**persistence_type:** *string* type, default: `'local'`

　　Used to set the storage type for property persistence of the current component. Available options are `'local'` (browser local cache), `'session'` (current tab session cache), and `'memory'` (temporary memory cache).