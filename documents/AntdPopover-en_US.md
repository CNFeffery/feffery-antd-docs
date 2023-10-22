**id:** *string* or *dict* type

　　 Used to set the *unique id information of the current component*.

**key:** *string* type

　　 Updates the `key` value of the current component to *force a redraw of the current component*.

**style:** *dict* type

　　 Used to set the *CSS style of the current component*.

**className:** *string* or *dict* type

　　 Used to set the *CSS class name of the current component*, supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　 Used to pass *the target element that the current popover card anchors to*.

**title:** *component type*

　　 Used to *set the title element of the current popover card*.

**content:** *component type*

　　 Used to *set the content element of the current popover card*.

**placement:** *string* type, default is `'top'`

　　 Used to *set the pop-up direction of the current popover card*, available options are `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`, `'leftTop'`, `'leftBottom'`, `'rightTop'`, `'rightBottom'`.

**color:** *string* type

　　 Used to *set the background color of the current popover card*.

**mouseEnterDelay:** *int* or *float* type, default is `0.1`

　　 Used to *set the delay from mouse entering to displaying the popover card*, in seconds.

**mouseLeaveDelay:** *int* or *float* type, default is `0.1`

　　 Used to *set the delay from mouse leaving to hiding the popover card*, in seconds.

**overlayStyle:** *dict* type

　　 Used to *set the CSS style of the container of the current popover card*.

**overlayInnerStyle:** *dict* type

　　 Used to *set the CSS style of the content area of the current popover card*.

**trigger:** *string* or *list* type, default is `'hover'`

　　 Used to *set the display trigger behavior of the current popover card*, available options are `'hover'`, `'focus'`, `'click'`, and you can also pass a list of multiple behaviors to achieve multi-trigger behavior.

**zIndex:** *int* type

　　 Used to *set the z-index property of the current popover card*.

**arrowPointAtCenter:** *bool* type, default is `False`

　　 Used to *set whether the arrow attached to the current popover card points to the center of the anchor element*.

**open:** *bool*, default is `False`

　　 Used to *set or monitor whether the bubble card is open.*

**popupContainer:** *string* type, default is `'body'`

　　 Used to *set the reference container type for the floating layer elements involved in the current component*, available options are `'body'` (referenced to the root node of the page) and `'parent'` (referenced to the parent container of the current element). When the component is within a locally scrolling container, setting `popupContainer='parent'` can solve the problem of the floating layer not scrolling with the content.