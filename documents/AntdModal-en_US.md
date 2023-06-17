**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component to force a redraw of the component.

**style:** *dict*

　　Used to set the CSS styles of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component. Supports [dynamic CSS](/advanced-classname).

**children:** *component*

　　Used to pass in nested child elements.

**locale:** *string* (default: `'zh-cn'`)

　　Used to set the language for the functional text of the current component. Options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**visible:** *bool* (default: `False`)

　　Used to set or monitor the visibility of the current dialog.

**title:** *component*

　　Used to set the title content of the current dialog.

**renderFooter:** *bool* (default: `False`)

　　Used to set whether to render the footer button operation area.

**okText:** *component*

　　Used to set the content of the confirmation button in the current dialog.

**okButtonProps:** *dict*

　　Used to configure parameters related to the confirmation button in the footer operation area. Available key-value pairs include:

- **size:** *string* - Used to set the size specification of the confirmation button. Options are `'small'`, `'middle'`, `'large'`.
- **type:** *string* - Used to set the style of the confirmation button. Options are `'default'`, `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`.
- **danger:** *bool* - Used to set whether to render the confirmation button in a dangerous state.
- **disabled:** *bool* - Used to set whether the confirmation button is disabled.
- **shape:** *string* - Used to set the shape of the confirmation button. Options are `'circle'`, `'round'`.

**cancelText:** *component*

　　Used to set the content of the cancel button in the current dialog.

**cancelButtonProps:** *dict*

　　Used to configure parameters related to the cancel button in the footer operation area. Available key-value pairs include:

- **size:** *string* - Used to set the size specification of the cancel button. Options are `'small'`, `'middle'`, `'large'`.
- **type:** *string* - Used to set the style of the cancel button. Options are `'default'`, `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`.
- **danger:** *bool* - Used to set whether to render the cancel button in a dangerous state.
- **disabled:** *bool* - Used to set whether the cancel button is disabled.
- **shape:** *string* - Used to set the shape of the cancel button. Options are `'circle'`, `'round'`.

**width:** *int* or *string* (default: `520`)

　　Used to set the width of the current dialog.

**centered:** *bool* (default: `False`)

　　Used to vertically center the current dialog.

**keyboard:** *bool* (default: `True`)

　　Used to enable closing the current dialog with the ESC key.

**closable:** *bool* (default: `True`)

　　Used to render a close button for the current dialog.

**mask:** *bool* (default: `True`)

　　Used to render the background mask.

**maskClosable:** *bool* (default: `True`)

　　Used to allow closing the dialog by clicking on the mask.

**okClickClose:** *bool* (default: `True`)

　　Used to automatically close the dialog after clicking the confirmation button.

**zIndex:** *int* (default: `1000`)

　　Used to set the z-index property of the current dialog.

**maskStyle:** *dict*

　　Used to set the CSS style of the mask.

**bodyStyle:** *dict*

　　Used to set the CSS style of the main body area of the dialog.

**okCounts:** *int* (default: `0`)

　　Used to track the cumulative number of clicks on the confirmation button in the current dialog.

**cancelCounts:** *int* (default: `0`)

　　Used to track the cumulative number of clicks on the cancel button in the current dialog.

**closeCounts:** *int* (default: `0`)

　　Used to track the cumulative number of times the current dialog has been closed.

**confirmAutoSpin:** *bool* (default: `False`)

　　Used to automatically activate the loading state of the confirmation button in the current dialog after clicking.

**loadingOkText:** *component*

　　Used to set the content displayed on the confirmation button when it is in the loading state in the current dialog.

**confirmLoading:** *bool* (default: `False`)

　　Used to manually set whether the confirmation button in the current dialog is in the loading state.

**transitionType:** *string* (default: `'zoom'`)

　　Used to set the animation type for showing and hiding the current dialog. Available options are `'none'`, `'fade'`, `'zoom'`, `'zoom-big'`, `'zoom-big-fast'`, `'slide-up'`, `'slide-down'`, `'slide-left'`, `'slide-right'`, `'move-up'`, `'move-down'`, `'move-left'`, `'move-right'`.



