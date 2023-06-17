**id:** *string* or *dict* type

　　 Used to set the *unique ID information of the current component*.

**key:** *string* type

　　 Updates the `key` value of the current component, enabling the forced redraw of the current component.

**style:** *dict* type

　　 Used to set the *CSS style of the current component*.

**className:** *string* or *dict* type

　　 Used to set the *CSS class name of the current component*, supports [dynamic CSS](/advanced-classname).

**children:** *component* type

　　 Used to pass in the *trigger element for the popover confirmation box*, usually a button.

**locale:** *string* type, default is `'zh-cn'`

　　 Used to set the *language for the functional text of the current component*, available options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**title:** *component* type

　　 Used to *set the title content of the popover confirmation box*.

**disabled:** *bool* type, default is `False`

　　 Used to *set whether the current popover confirmation box is disabled*.

**placement:** *string* type, default is `'top'`

　　 Used to *set the expansion direction of the current popover confirmation box*, available options are `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`, `'leftTop'`, `'leftBottom'`, `'rightTop'`, `'rightBottom'`.

**mouseEnterDelay:** *int* or *float* type, default is `0.1`

　　 Used to *set the delay from mouse enter to the card display of the popover confirmation box*, in seconds.

**mouseLeaveDelay:** *int* or *float* type, default is `0.1`

　　 Used to *set the delay from mouse leave to the card disappearance of the popover confirmation box*, in seconds.

**overlayStyle:** *dict* type

　　 Used to *set the CSS style of the container of the popover confirmation box*.

**overlayInnerStyle:** *dict* type

　　 Used to *set the CSS style of the content area of the popover confirmation box*.

**okText:** *component* type

　　 Used to *set the label of the confirm button in the popover confirmation box*.

**okButtonProps:** *dict* type

　　 Used to *configure parameters related to the confirm button in the footer operation area*, available key-value pairs include:

- **size:** *string* type, used to *set the size specification of the confirm button*, available options are `'small'`, `'middle'`, `'large'`.
- **type:** *string* type, used to *set the style of the confirm button*, available options are `default`, `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`.
- **danger:** *bool* type, used to *render the confirm button in a dangerous state*.
- **disabled:** *bool* type, used to *disable the confirm button*.
- **shape:** *string* type, used to *set the shape of the confirm button*, available options are `'circle'`, `'round'`.

**cancelText:** *component* type

　　 Used to *set the label of the cancel button in the popover confirmation box*.

**cancelButtonProps:** *dict* type

　　 Used to *configure parameters related to the cancel button in the footer operation area*, available key-value pairs include:

- **size:** *string* type, used to *set the size specification of the cancel button*, available options are `'small'`, `'middle'`, `'large'`.
- **type:** *string* type, used to *set the style of the cancel button*, available options are `default`, `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`.
- **danger:** *bool* type, used to *render the cancel button in a dangerous state*.
- **disabled:** *bool* type, used to *disable the cancel button*.
- **shape:** *string* type, used to *set the shape of the cancel button*, available options are `'circle'`, `'round'`.

**confirmCounts:** *int* type, default is `0`

　　 Used to *listen for the accumulated number of clicks on the confirm button*.

**cancelCounts:** *int* type, default is `0`

　　 Used to *listen for the accumulated number of clicks on the cancel button*.

**trigger:** *string* or *list* type, default is `'hover'`

　　 Used to *set the display trigger behavior of the current popover card*, available options are `'hover'`, `'focus'`, `'click'`, and you can also pass a list of multiple behaviors to achieve multi-trigger behavior.

**popupContainer:** *string* type, default is `'body'`

　　 Used to *set the reference container type for the floating layer elements involved in the current component*, available options are `'body'` (referenced to the root node of the page) and `'parent'` (referenced to the parent container of the current element). When the component is within a locally scrolling container, setting `popupContainer='parent'` can solve the problem of the floating layer not scrolling with the content.