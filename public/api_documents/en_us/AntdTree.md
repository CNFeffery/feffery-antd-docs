- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- treeDataMode (a value equal to: 'tree', 'flat'; default 'tree'):
    Format of `treeData`: `'tree'` for nested data or `'flat'` for flat data. Default: `'tree'`.

- treeData (list; optional):
    Tree data structure, matching `treeDataMode`.

- treeNodeKeyToTitle (dict with strings as keys and values of type a list of or a singular dash component, string or number; optional):
    Component titles for specified tree nodes. Takes precedence over the corresponding `title` in `treeData`.

- showIcon (boolean; default False):
    Whether to render additional node icons. Default: `False`.

- selectable (boolean; default True):
    Whether nodes can be selected by clicking. Default: `True`.

- multiple (boolean; default False):
    Whether multiple nodes can be selected. Default: `False`.

- checkable (boolean; default False):
    Whether nodes can be checked. Default: `False`.

- defaultExpandAll (boolean; default False):
    Whether all nodes are initially expanded. Default: `False`.

- expandedKeys (list of strings; optional):
    Monitor or set the array of expanded node `key` values.

- defaultExpandedKeys (list of strings; optional):
    Initial array of expanded node `key` values.

- defaultExpandParent (boolean; default False):
    Whether to expand the parents of initially expanded nodes. Default: `False`.

- selectedKeys (list of strings; optional):
    Monitor or set the array of selected node `key` values.

- defaultSelectedKeys (list of strings; optional):
    Initial array of selected node `key` values.

- checkedKeys (list of strings; optional):
    Monitor or set the array of checked node `key` values.

- defaultCheckedKeys (list of strings; optional):
    Initial array of checked node `key` values.

- halfCheckedKeys (list of strings; optional):
    Monitor or set the array of half-checked node `key` values.

- checkStrictly (boolean; default False):
    Whether node selection is independent of descendant selection. Default: `False`.

- showLine (dict; default { showLeafIcon: False }):
    Whether to show connecting lines.

    `showLine` is a boolean | dict with keys:

    - showLeafIcon (boolean; optional):
        Whether to show prefix icons on leaf nodes.

- switcherIcon (a list of or a singular dash component, string or number; optional):
    Custom tree node expand/collapse icon. Supports components.

- height (number; optional):
    Maximum component height in pixels for virtual scrolling. Virtual scrolling is disabled if unset.

- draggable (boolean; default False):
    Whether nodes can be dragged. Default: `False`.

- showDragIcon (boolean; default True):
    Whether draggable nodes show a drag handle. Default: `True`.

- dragInSameLevel (boolean; default False):
    Whether dragging is restricted to nodes at the same level when `draggable=True`. Default: `False`.

- dragDisabledKeys (list of strings; optional):
    Array of node `key` values that cannot be dragged. Default: `[]`.

- dropDisabledKeys (list of strings; optional):
    Array of node `key` values that cannot accept dropped nodes. Default: `[]`.

- draggedNodeKey (string; optional):
    `key` of the most recently dragged node.

- clickedContextMenu (dict; optional):
    Click events for node context menu items.

    `clickedContextMenu` is a dict with keys:

    - nodeKey (string; optional):
        `key` of the node associated with the event.

    - menuKey (string; optional):
        `key` of the context menu item associated with the event.

    - timestamp (number; optional):
        Timestamp of the event.

- enableNodeFavorites (boolean; default False):
    Whether node favorites are enabled. Default: `False`.

- favoritedKeys (list of strings; optional):
    Monitor or set the array of favorite node `key` values.

- scrollTarget (dict; optional):
    Scroll to the specified node. Resets to null after each execution.

    `scrollTarget` is a dict with keys:

    - key (string; required):
        `key` of the target node to scroll to.

    - align (a value equal to: 'top', 'bottom', 'auto'; optional):
        Alignment of the scroll target node. Supported values: `'top'`, `'bottom'`, `'auto'`. Default: `'auto'`.

    - offset (number; optional):
        Scroll offset in pixels.

- searchKeyword (string | list of strings; optional):
    A search keyword, or an array of keywords, for quick tree search.

- caseSensitive (boolean; default True):
    Whether `searchKeyword` matching is case-sensitive. Default: `True`.

- highlightStyle (dict; default {    fontWeight: 'bold',    backgroundColor: 'transparent',    padding: 0,    color: '#ff5500',}):
    Highlight styles for matching text in quick tree search.

- nodeCheckedSuffix (a list of or a singular dash component, string or number; optional):
    Suffix element for checked nodes. Supports components.

- nodeUncheckedSuffix (a list of or a singular dash component, string or number; optional):
    Suffix element for unchecked nodes. Supports components.

- nodeCheckedStyle (dict; optional):
    CSS styles for checked nodes.

- nodeUncheckedStyle (dict; optional):
    CSS styles for unchecked nodes.

- enableAsyncLoad (boolean; default False):
    Whether to load children asynchronously. Nodes that have no `children` and do not set `isLeaf` to `True` can expand and trigger `loadingNode` updates. Default: `False`.

- loadingNode (dict; optional):
    Node expansion event that requests asynchronous data loading.

- batchPropsNames (list of strings; optional):
    Property names to include in [batch property monitoring](/batch-props-values).

- batchPropsValues (dict; optional):
    Values of the properties specified by `batchPropsNames`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'selectedKeys', 'checkedKeys', 'expandedKeys', 'halfCheckedKeys's; optional):
    Properties whose values are persisted. Supported values: `'selectedKeys'`, `'checkedKeys'`, `'expandedKeys'`, `'halfCheckedKeys'`. Default: `['selectedKeys', 'checkedKeys', 'expandedKeys', 'halfCheckedKeys']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
