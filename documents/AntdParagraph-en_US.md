**id:** *string* or *dict*

　　Used to set the unique id information for the current component.

**key:** *string*

　　Updates the `key` value of the current component, which can force a re-render of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component*

　　Used to pass in nested child elements.

**locale:** *string* (default: `'zh-cn'`)

　　Used to set the language for the functional text of the current component, available options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**code:** *bool* (default: `False`)

　　Used to render all content inside the paragraph in code style.

**copyable:** *bool* (default: `False`)

　　Used to add a quick copy function to the current paragraph.

**strikethrough:** *bool* (default: `False`)

　　Used to render the current paragraph in strikethrough mode.

**disabled:** *bool* (default: `False`)

　　Used to render the current paragraph in a disabled state.

**mark:** *bool* (default: `False`)

　　Used to highlight the current paragraph.

**strong:** *bool* (default: `False`)

　　Used to render the current paragraph in bold.

**italic:** *bool* (default: `False`)

　　Used to render the current paragraph in italics.

**underline:** *bool* (default: `False`)

　　Used to render the current paragraph with an underline.

**type:** *string*

　　Used to set the overall status type of the current paragraph. Essentially, it presets the color of the text within the paragraph. Available options are `'secondary'`, `'success'`, `'warning'`, and `'danger'`.

**ellipsis:** *bool* or *dict* type, default is `False`

　　Used for *configuring content ellipsis related functionality*. When passed as a dictionary type, the available key-value pair parameters are:

- **expandable:** *bool* type, used to *set whether it is expandable*.
- **rows:** *bool* type, used to *set the maximum number of content rows to display*.
- **suffix:** *string* type, used to *set the ellipsis content suffix*.
- **symbol:** *component type*, used to *customize the expand control*.