**id:** *string* or *dict* type

　　Used to set the *unique ID information for the current component*.

**key:** *string* type

　　Updates the `key` value for the current component, which can force a redraw of the current component.

**style:** *dict* type

　　Used to set the *CSS style for the current component*.

**className:** *string* or *dict* type

　　Used to set the *CSS class name for the current component*. Supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass *nested child elements*.

**locale:** *string* type, default: `'zh-cn'`

　　Used to set the language for the functional text of the current component. Options include `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**level:** *int* type, default: `1`

　　Used to set the heading level. Options are integers from 1 to 5, corresponding to different heading levels from `<h1>` to `<h5>`.

**code:** *bool* type, default: `False`

　　Used to set whether to render the heading content in code style.

**copyable:** *bool* type, default: `False`

　　Used to add the shortcut copy function to the heading content.

**strikethrough:** *bool* type, default: `False`

　　Used to render the heading content with a strikethrough style.

**disabled:** *bool* type, default: `False`

　　Used to render the heading content in a disabled state.

**mark:** *bool* type, default: `False`

　　Used to highlight the heading content with a yellow background.

**strong:** *bool* type, default: `False`

　　Used to render the heading content in bold.

**italic:** *bool* type, default: `False`

　　Used to render the heading content in italics.

**underline:** *bool* type, default: `False`

　　Used to render the heading content with an underline.

**keyboard:** *bool* type, default: `False`

　　Used to render the heading content in a keyboard key style.

**type:** *string* type

　　Used to set the overall status type of the heading content, essentially providing predefined colors for the heading content. Options include `'secondary'`, `'success'`, `'warning'`, and `'danger'`. The default is `None`, indicating no specific status.