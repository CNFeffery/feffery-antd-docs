**id:** *string* or *dict*

   Used to set the unique ID information of the current component.

**key:** *string*

   Updates the `key` value of the current component, enabling forced re-rendering of the component.

**style:** *dict*

   Used to set the CSS style of the current component.

**className:** *string* or *dict*

   Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**locale:** *string*, default: `'zh-cn'`

   Used to set the language for the functional text of the current component. Available options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**optionsMode:** *string*, default: `'tree'`

   Used to set the parsing mode for the `options` parameter. Available options are `'tree'` (tree structure) and `'flat'` (flat structure).

**options:** `list[dict]`, required

   Used to construct the option structure for the cascading selection.

   When `optionsMode='tree'`, the `options` parameter needs to follow the tree parsing mode, and each dictionary can have the following key-value pairs:

   - **value:** *string*, *int*, or *float*, required. Used to set the value corresponding to the current node.
   - **label:** *string*, required. Used to set the label content of the current node.
   - **disabled:** *bool*, default: `False`. Used to set whether the current node is disabled.
   - **children:** *list*. Used to nest descendant tree structures.

   Here is an example of a tree structure for `options`:

   ```python
   options = [
       {
           'value': 'Node 1',
           'label': 'Node 1',
           'children': [
               {
                   'value': 'Node 1-1',
                   'label': 'Node 1-1'
               },
               {
                   'value': 'Node 1-2',
                   'label': 'Node 1-2',
                   'children': [
                       {
                           'value': 'Node 1-2-1',
                           'label': 'Node 1-2-1'
                       },
                       {
                           'value': 'Node 1-2-2',
                           'label': 'Node 1-2-2'
                       }
                   ]
               }
           ]
       },
       {
           'value': 'Node 2',
           'label': 'Node 2',
           'children': [
               {
                   'value': 'Node 2-1',
                   'label': 'Node 2-1'
               },
               {
                   'value': 'Node 2-2',
                   'label': 'Node 2-2'
               }
           ]
       }
   ]
   ```

   When `optionsMode='flat'`, the `options` parameter needs to follow the flat parsing mode, and each dictionary can have the following key-value pairs:

   - **value:** *string*, *int*, or *float*, required. Used to set the value corresponding to the current node.
   - **label:** *string*, required. Used to set the label content of the current node.
   - **disabled:** *bool*, default: `False`. Used to set whether the current node is disabled.
   - **key:** *string*. Used to uniquely identify the current node and establish the relationship between parent and child nodes.
   - **parent:** *string*. Used to declare the key value of the parent node of the current node and establish the relationship between parent and child nodes.

   Here is an example of a flat `options` structure:

```python
options = [
    {
        'value': '1',
        'label': 'Node 1',
        'key': '1'
    },
    *[
        {
            'value': f'1-{i}',
            'label': f'Node 1-{i}',
            'key': f'1-{i}',
            'parent': '1'
        }
        for i in range(1, 4)
    ],
    {
        'value': '2',
        'label': 'Node 2',
        'key': '2'
    },
    {
        'value': '2-1',
        'label': 'Node 2-1',
        'key': '2-1',
        'parent': '2'
    },
    {
        'value': '2-2',
        'label': 'Node 2-2',
        'key': '2-2',
        'parent': '2'
    },
    *[
        {
            'value': f'2-2-{i}',
            'label': f'Node 2-2-{i}',
            'key': f'2-2-{i}',
            'parent': '2-2'
        }
        for i in range(1, 4)
    ],
]
```

**disabled:** *bool*, default: `False`

   Used to set whether the current component is disabled.

**changeOnSelect:** *bool*, default: `False`

   Used to set whether the value is updated when any node is selected. When `changeOnSelect=False`, the value is only updated when a leaf node is selected.

**size:** *string*, default: `'middle'`

   Used to set the size of the current component. Available options are `'small'`, `'middle'`, and `'large'`.

**bordered:** *bool*, default: `True`

   Used to set whether to render the border.

**placeholder:** *string*

   Used to set the placeholder text for the blank input.

**placement:** *str*, default: `'bottomLeft'`

   Used to set the direction of the dropdown menu. Available options are `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, and `'topRight'`.

**value:** *list*

   Used to listen to or set the currently selected value.

**defaultValue:** *list*

   Used to listen to or set the initially selected value.

**maxTagCount:** *int* or *str*

   Used to set the maximum number of selected options displayed in the selection box in multi-select mode. It can also be set to `'responsive'` to enable responsive mode for adaptive adjustment.

**multiple:** *bool*, default: `False`

   Used to enable multiple selection mode.

**expandTrigger:** *str*, default: `'click'`

   Used to set the trigger mode for expanding the dropdown menu. Available options are `'hover'` and `'click'`.

**status:** *string*

   Used to forcibly set the status of the component. Available options are `'error'` and `'warning'`.

**allowClear:** *bool*, default: `True`

   Used to set whether the user is allowed to clear the selected options.

**showCheckedStrategy:** *string*, default: `'show-parent'`

   Used to set the display strategy for selected options. Available options are `'show-parent'` (only show the parent node when all child nodes are selected) and `'show-child'` (only show the selected child nodes).

**readOnly:** *bool*

   Used to set whether to display in read-only mode.

**popupContainer:** *string*, default: `'body'`

   Used to set the reference container type for the floating layer elements related to the current component. Available options are `'body'` (referenced to the root node of the page) and `'parent'` (referenced to the parent container of the current element). When the component is inside a scrollable container, setting `popupContainer='parent'` can solve the issue of the floating layer not scrolling along.

**persistence:** *bool*

   Used to enable property persistence for the current component.

**persisted_props:** *list*, default: `['value']`

   Used to set which properties of the current component are persisted. Available options are `'value'`.

**persistence_type:** *string*, default: `'local'`

   Used to set the storage type for property persistence of the current component. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), and `'memory'` (temporary memory cache).