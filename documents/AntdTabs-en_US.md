**id:** String or dict type

　　Used to *set the unique ID information for the current component*.

**key:** String type

　　Updates the `key` value for the current component, which can force a redraw of the current component.

**style:** Dict type

　　Used to *set the CSS style for the current component*.

**className:** String or dict type

　　Used to *set the CSS class name for the current component*. Supports [dynamic CSS](/advanced-classname).

<font style="color: white; background: #fab005; border-radius: 6px; padding: 3px 8px;">Deprecated in 0.3.x</font> **children:** Component type

　　Used to pass *multiple nested AntdTabPane elements*.

**items:** List[dict] type

　　Used to *define each tab panel*. Each dictionary represents a tab panel, and available key-value parameters are:

- **label:** Component type, used to *set the title content of the current tab page*.
- **key:** String type, used to *set the unique identifier for the current tab page*.
- **children:** Component type, used to *set the nested child elements for the current tab page*.
- **disabled:** Boolean type, used to *set whether the current tab page is disabled*.
- **forceRender:** Boolean type, default is `False`, used to *set whether to forcefully render the elements inside the current tab page during initialization*.
- **closable:** Boolean type, used in `editable-card` mode to *set whether the current tab panel can be closed*.

**activeKey:** String type

　　Used to *set or listen to the currently active tab key value*.

**defaultActiveKey:** String type

　　Used to *set the key value of the initially active tab*.

**disabledTabKeys:** List[string] type, default is `[]`

　　Used to *set an array of tab key values that need to be disabled*.

**tabPosition:** String type, default is `'top'`

　　Used to *set the display position of the current tab page*. Available options are `'top'`, `'left'`, `'right'`, `'bottom'`.

**size:** String type, default is `'default'`

　　Used to *set the size specification of the current tab page*. Available options are `'small'`, `'default'`, `'large'`.

**type:** String type, default is `'line'`

　　Used to *set the rendering type of the current tab page*. Available options are `'line'`, `'card'`, `'editable-card'`.

**centered:** Boolean type, default is `False`

　　Used to *set whether to center align the tab bar*.

**tabBarGutter:** Int type

　　Used to *set the pixel spacing between tab bar options*.

**inkBarAnimated:** Boolean type, default is `True`

　　Used to *set whether to enable animation for tab page switching in the tab bar*.

**tabPaneAnimated:** Boolean type, default is `False`

　　Used to *set whether to enable animation for content area switching in the tab page*.

**latestDeletePane:** String type

　　Available when `type="editable-card"`. Used to *listen to the key value of the most recent tab page deleted*.

**tabBarLeftExtraContent:** Component type

　　Used to *set prefix content for the tab bar of the current tab page*.

**tabBarRightExtraContent:** Component type

　　Used to *set suffix content for the tab bar of the current

 tab page*.

**persistence:** Boolean type

　　Used to *set whether to enable property persistence for the current component*.

**persisted_props:** List type, default is `['activeKey']`

　　Used to *set which properties of the current component should be persisted*. Available options are `'activeKey'`.

**persistence_type:** String type, default is `'local'`

　　Used to *set the storage type for property persistence of the current component*. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), `'memory'` (temporary memory cache).