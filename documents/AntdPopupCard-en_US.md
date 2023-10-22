**id:** *string* or *dict* type

　　 Used to set the *unique id information of the current component*.

**key:** *string* type

　　 Updates the `key` value of the current component to *force a redraw of the current component*.

**style:** *dict* type

　　 Used to set the *CSS style of the current component*.

**className:** *string* or *dict* type

　　 Used to set the *CSS class name of the current component*, supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　 Used to pass *nested child elements*.

**title:** *component type*

　　 Used to *set the title element of the current modal*.

**visible:** *bool* type, default is `True`

　　 Used to *set whether the current modal is in the visible state*.

**width:** *int* or *string* type

　　 Used to *set the width of the current modal*.

**transitionType:** *string* type, default is `'fade'`

　　 Used to *set the animation type for showing and hiding the current modal*, available options are `'none'`, `'fade'`, `'zoom'`, `'zoom-big'`, `'zoom-big-fast'`, `'slide-up'`, `'slide-down'`, `'slide-left'`, `'slide-right'`, `'move-up'`, `'move-down'`, `'move-left'`, `'move-right'`.

**closable:** *bool* type, default is `True`

　　 Used to *add a close button to the current modal*.

**closeIconType:** *string* type, default is `'default'`

　　 Used to *set the close button type of the current modal*, available options are `'default'`, `'outlined'`, `'two-tone'`.

**draggable:** *bool* type, default is `False`

　　 Used to *set whether the current modal can be freely dragged*.

**zIndex:** *int* type, default is `1000`

　　 Used to *set the z-index of the current modal*.

**bodyStyle:** *dict* type

　　 Used to *set the CSS style of the content area of the current modal*.

**dragClassName:** *string* or *dict*

　　 Used to set the *CSS class name for the draggable area*, supports [dynamic CSS](/advanced-classname).