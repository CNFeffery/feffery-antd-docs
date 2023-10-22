**id:** String or dict type

　　Used to *set the unique ID information for the current component*.

**key:** String type

　　Updates the `key` value for the current component, which can force a redraw of the current component.

**style:** Dict type

　　Used to *set the CSS style for the current component*.

**className:** String or dict type

　　Used to *set the CSS class name for the current component*. Supports [dynamic CSS](/advanced-classname).

**children:** Component type

　　Used to pass *nested child elements*.

**locale:** String type, default is `'zh-cn'`

　　Used to *set the language for the functional text of the current component*. Options include `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**code:** Boolean type, default is `False`

　　Used to *render the text content with a code style*.

**copyable:** Boolean type, default is `False`

　　Used to *add the ability to copy the text content*.

**strikethrough:** Boolean type, default is `False`

　　Used to *render the text content with a strikethrough style*.

**disabled:** Boolean type, default is `False`

　　Used to *render the text content as disabled*.

**mark:** Boolean type, default is `False`

　　Used to *highlight the text content with a yellow background*.

**strong:** Boolean type, default is `False`

　　Used to *render the text content in bold*.

**italic:** Boolean type, default is `False`

　　Used to *render the text content in italic*.

**underline:** Boolean type, default is `False`

　　Used to *render the text content with an underline*.

**keyboard:** Boolean type, default is `False`

　　Used to *render the text content with a keyboard key style*.

**type:** String type

　　Used to *set the overall state type of the text content*. Essentially, it presets the color of the text content. Options include `'secondary'`, `'success'`, `'warning'`, and `'danger'`. The default value is `None`, which means no state.

**ellipsis:** *bool* or *dict* type, default is `False`

　　Used to *enable content ellipsis functionality*. When passed as a dictionary type, the available key-value pair parameter is:

- **suffix:** *string* type, used to *set an additional suffix for ellipsized content*.