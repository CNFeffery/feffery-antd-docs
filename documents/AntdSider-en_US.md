**id：** *string* or *dict* type

　　Used to set the unique id information for the current component.

**key：** *string* type

　　Updates the `key` value of the current component to force a re-rendering effect.

**style：** *dict* type

　　Used to set the CSS style for the current component.

**railStyle：** *dict* type

　　Used to set the CSS style for the slider rail.

**className：** *string* or *dict* type

　　Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**children：** *component type*

　　Used to pass in nested child elements.

**collapsed：** *bool* type, default to `False`

　　Used to set whether the current sidebar area is collapsed.

**defaultCollapsed：** *bool* type, default to `False`

　　Used to set whether the sidebar is initially collapsed when it is loaded.

**collapsedWidth：** *int* type, default to `80`

　　Used to set the pixel width of the sidebar in the collapsed state. When set to `0`, a special toggle button for the collapsed state is rendered to avoid the inability to trigger the expand operation after collapsing.

**collapsible：** *bool* type, default to `False`

　　Used to set whether the current sidebar is collapsible.

**reverseArrow：** *bool* type, default to `False`

　　Used to set whether to horizontally flip the arrow direction of the collapse trigger area. This is usually necessary when `AntdSider` is positioned on the right side of the page.

**theme：** *string* type, default to `'dark'`

　　Used to set the theme style. Optional values are `'dark'` and `'light'`.

**width：** *int* or *string* type, default to `200`

　　Used to set the width of the current sidebar.

**trigger：**

　　When it is necessary to hide the built-in sidebar collapse trigger element and customize the collapse trigger element through a callback, please set `trigger=None`.

**breakpoint：** *string* type

　　When the sidebar needs to implement responsive automatic collapse/expand functionality, it is used to set the breakpoint. Optional values are `'xs'`, `'sm'`, `'md'`, `'lg'`, `'xl'`, `'xxl'`.