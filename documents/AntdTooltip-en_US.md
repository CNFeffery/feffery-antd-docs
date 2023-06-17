**id:** *string* or *dict* type

　　Used to set the *unique ID information for the current component*.

**key:** *string* type

　　Updates the `key` value for the current component, which can force a redraw of the current component.

**style:** *dict* type

　　Used to set the *CSS style for the current component*.

**className:** *string* or *dict* type

　　Used to set the *CSS class name for the current component*. Supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass *the target element for anchoring the current tooltip*.

**title:** *component type*

　　Used to *set the content of the current tooltip*.

**placement:** *string* type, default: `'top'`

　　Used to set the *pop-up direction of the current tooltip*. Options include `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, and `'bottomRight'`.

**color:** *string* type

　　Used to *set the background color of the current tooltip*.

**mouseEnterDelay:** *int* or *float* type, default: `0.1`

　　Used to set the *delay in seconds from mouse enter to tooltip display*.

**mouseLeaveDelay:** *int* or *float* type, default: `0.1`

　　Used to set the *delay in seconds from mouse leave to tooltip disappearance*.

**overlayStyle:** *dict* type

　　Used to set the *CSS style for the tooltip container*.

**overlayInnerStyle:** *dict* type

　　Used to set the *CSS style for the tooltip content area*.

**trigger:** *string* or *list* type, default: `'hover'`

　　Used to set the *display trigger behavior of the current tooltip*. Options include `'hover'`, `'focus'`, `'click'`. It can also be a list of multiple behaviors for triggering.

**zIndex:** *int* type

　　Used to *set the z-index property for the current tooltip*.

**arrowPointAtCenter:** *bool* type, default: `False`

　　Used to *set whether the arrow attached to the tooltip points to the center of the anchor element*.

**open:** *bool* type, default: `False`

　　Used to *listen to or set whether the current tooltip is expanded*.

**permanent:** *bool* type, default: `False`

　　Used to *set whether to maintain the expansion state of the current tooltip consistent with the `open` parameter*. When set to `True`, the tooltip's expansion behavior will not be changed by the user's mouse enter or leave actions.

**popupContainer:** *string* type, default: `'body'`

　　Used to *set the reference container type for the floating layer elements involved in the current component*. Options include `'body'` (using the root node of the page as the reference) and `'parent'` (using the parent container of the current element as the reference). When the component is within a locally scrolling container, setting `popupContainer='parent'` can solve the issue of the floating layer not scrolling with the container.