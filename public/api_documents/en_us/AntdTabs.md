- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- type (a value equal to: 'line', 'card', 'editable-card'; default 'line'):
    Tab type. Supported values: `'line'`, `'card'`, `'editable-card'`. Default: `'line'`.

- items (list of dicts; optional):
    Tab item definitions.

    `items` is a list of dicts with keys:

    - label (a list of or a singular dash component, string or number; optional):
        Tab title. Supports components.

    - key (string; optional):
        Unique tab ID.

    - children (a list of or a singular dash component, string or number; optional):
        Tab content elements. Supports components.

    - icon (a list of or a singular dash component, string or number; optional):
        Tab icon. Supports components.

    - closeIcon (boolean | a list of or a singular dash component, string or number; optional):
        Custom close button for `'editable-card'` tabs. Set to `None` or `False` to hide the default button.

    - destroyInactiveTabPane (boolean; optional):
        Whether to destroy tab content when the tab becomes hidden. Default: `False`.

    - disabled (boolean; optional):
        Whether this tab is disabled. Default: `False`.

    - forceRender (boolean; optional):
        Whether to render the tab content before its first activation. Default: `False`.

    - closable (boolean; optional):
        Whether this tab can be closed in `'editable-card'` mode. Default: `True`.

    - contextMenu (list of dicts; optional):
        Context menu settings for this tab's title.

        `contextMenu` is a list of dicts with keys:

        - key (string; optional):

            Unique context menu item ID.

        - label (string; optional):

            Context menu item title.

        - icon (string; optional):

            Context menu prefix icon. Uses the `AntdIcon` icon property when `iconRenderer` is `'AntdIcon'`, or a CSS class when it is `'fontawesome'`.

        - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):

            Renderer for the context menu item's prefix icon. Supported values: `'AntdIcon'`, `'fontawesome'`.

- itemKeys (list of strings; optional):
    Current tab `key` values in the same order as `items`.

- activeKey (string; optional):
    Monitor or set the active tab `key`.

- defaultActiveKey (string; optional):
    `key` of the initially active tab.

- disabledTabKeys (list of strings; optional):
    Array of disabled tab `key` values. Overrides the `disabled` settings in `items`.

- tabPosition (a value equal to: 'top', 'left', 'right', 'bottom'; default 'top'):
    Tab control placement. Supported values: `'top'`, `'left'`, `'right'`, `'bottom'`. Default: `'top'`.

- size (a value equal to: 'small', 'default', 'large'; default 'default'):
    Component size. Supported values: `'small'`, `'default'`, `'large'`. Default: 'default'.

- centered (boolean; default False):
    Whether to center the tab controls. Default: `False`.

- indicator (dict; optional):
    Indicator length and alignment settings.

    `indicator` is a dict with keys:

    - size (number; optional):
        Indicator width in pixels. A negative number subtracts pixels from the full tab width; matches the tab width by default.

    - align (a value equal to: 'start', 'center', 'end'; optional):
        Indicator alignment. Supported values: `'start'`, `'center'`, `'end'`.

- tabBarGutter (number; optional):
    Gap between tab cards in pixels.

- tabBarStyle (dict; optional):
    CSS styles for the tab card.

- inkBarAnimated (boolean; default True):
    Whether tab card transitions are animated. Default: `True`.

- tabPaneAnimated (boolean; default False):
    Whether tab content transitions are animated. Default: `False`.

- latestDeletePane (string; optional):
    `key` of the tab removed in the most recent deletion.

- tabCloseCounts (number; default 0):
    Cumulative number of tab close button clicks. Default: `0`.

- tabBarLeftExtraContent (a list of or a singular dash component, string or number; optional):
    Additional elements in the first position. Supports components.

- tabBarRightExtraContent (a list of or a singular dash component, string or number; optional):
    Additional elements in the second position. Supports components.

- tabCount (number; optional):
    Number of tabs.

- destroyInactiveTabPane (boolean; default False):
    Whether to destroy inactive tab content across all tabs.

- clickedContextMenu (dict; optional):
    Click events for tab title context menu items.

    `clickedContextMenu` is a dict with keys:

    - tabKey (string; optional):
        Tab `key` associated with the clicked context menu item.

    - menuKey (string; optional):
        `key` of the clicked context menu item.

    - timestamp (number; optional):
        Timestamp of the event.

- placeholder (a list of or a singular dash component, string or number; optional):
    Placeholder content when `items` is empty or has length `0`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'activeKey's; optional):
    Properties whose values are persisted. Supported values: `'activeKey'`. Default: `['activeKey']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
