**id:** *string* or *dict*

　　Used to set the *unique id information* of the current component.

**key:** *string*

　　Updates the `key` value of the current component to force a re-render.

**style:** *dict*

　　Used to set the *CSS style* of the current component.

**className:** *string* or *dict*

　　Used to set the *CSS class name* of the current component, supporting [dynamic CSS](/advanced-classname).

**children:** *component*

　　Used to pass *nested child elements*.

**title:** *component*

　　Used to *set the title content* of the current collapsible panel.

**isOpen:** *bool*, default is `True`

　　Used to *set or listen to the current collapsible panel's expansion state*.

**bordered:** *bool*, default is `True`

　　Used to *set whether to render the border of the current component*.

**showArrow:** *bool*, default is `True`

　　Used to *set whether to display the arrow*.

**ghost:** *bool*, default is `False`

　　Used to *enable transparent panel mode*.

**collapsible:** *string*

　　Used to *set the collapsible/expandable trigger strategy*. Options are `'header'` (only the header content triggers), `'disabled'` (disabled), `'icon'` (only the icon area triggers).

**forceRender:** *bool*, default is `False`

　　Used to *force rendering of internal child elements when the collapsible panel is not initially expanded*.

**persistence:** *bool*

　　Used to *enable attribute persistence for the current component*.

**persisted_props:** *list*, default is `['isOpen']`

　　Used to *set which properties of the current component to persist*. Options are `'isOpen'`.

**persistence_type:** *string*, default is `'local'`

　　Used to *set the storage type for attribute persistence of the current component*. Options are `'local'` (browser local storage), `'session'` (current tab session storage), `'memory'` (temporary memory cache).