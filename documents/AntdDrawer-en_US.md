**id:** *string* or *dict* type

　　Used to set the unique ID information of the current component.

**key:** *string* type

　　Updates the `key` value of the current component, which can force the current component to be redrawn.

**style:** *dict* type

　　Used to set the CSS style of the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component* type

　　Used to pass in nested child elements.

**visible:** *bool* type, default: `False`

　　Used to set or monitor the expansion status of the current drawer.

**title:** *component* type

　　Used to set the title content of the current drawer.

**placement:** *string* type, default: `'right'`

　　Used to set the expansion direction of the current drawer. Possible values are `'left'`, `'right'`, `'top'`, `'bottom'`.

**closable:** *bool* type, default: `True`

　　Used to set whether to render a close button for the current drawer.

**forceRender:** *bool* type, default: `False`

　　Used to set whether to pre-render internal elements when the drawer is initialized but closed.

**destroyOnClose:** *bool* type, default: `False`

　　Used to set whether to destroy internal elements after the drawer is closed.

**width:** *int*, *float*, or *string* type, default: `256`

　　When `placement` is `'left'` or `'right'`, used to set the width of the current drawer.

**height:** *int*, *float*, or *string* type, default: `256`

　　When `placement` is `'top'` or `'bottom'`, used to set the height of the current drawer.

**mask:** *bool* type, default: `True`

　　When the drawer is expanded, used to set whether to render a mask layer outside the drawer.

**maskClosable:** *bool* type, default: `True`

　　Used to set whether the expanded drawer can be closed by clicking on the mask layer.

**zIndex:** *int* type, default: `1000`

　　Used to set the z-index property of the current drawer.

**extra:** *component* type

　　Used to set additional action area elements for the current drawer.

**containerId:** *string* type

　　When the drawer needs to be displayed within a specific container, used to set the ID of the target container. Note that the `position` of the target container should be set to `relative`.