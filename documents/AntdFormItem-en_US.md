**id:** *string* or *dict* type

　　Used to set the unique ID information of the current component.

**key:** *string* type

　　Updates the `key` value of the current component, which allows for forcefully redrawing the current component.

**style:** *dict* type

　　Used to set the CSS style of the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass in nested child elements.

**required:** *bool* type, default: `False`

　　Used to set whether to add a required indicator to the label of the current form item.

**labelCol:** *dict* type

　　Used to configure the label width properties of the current form item. Available key-value pairs are:

- **span:** *int* type, same as the corresponding parameter in `AntdCol`, used to set the number of columns the label part occupies in the current form item.
- **offset:** *int* type, same as the corresponding parameter in `AntdCol`, used to set the number of columns the label part is shifted to the right.
- **flex:** An *integer* (int) or *string* (string) type, used to *configure the width of a section of the tag based on the flex property in CSS*.

**colon:** *bool* type, default: `True`

　　Used to set whether to add a colon after the label of the current form item.

**wrapperCol:** *dict* type

　　Used to configure the control width properties of the current form item. Available key-value pairs are:

- **span:** *int* type, same as the corresponding parameter in `AntdCol`, used to set the number of columns the control part occupies in the current form item.
- **offset:** *int* type, same as the corresponding parameter in `AntdCol`, used to set the number of columns the control part is shifted to the right.
- **flex:** An *integer* (int) or *string* (string) type, used to *configure the width of a form control element based on the flex property in CSS*.

**label:** *component type*

　　Used to set the label content of the current form item.

**labelAlign:** *string* type, default: `'right'`

　　Used to set the alignment of the label content for the current form item. Available options are `'left'` and `'right'`.

**tooltip:** *component type*

　　Used to set the content of the tooltip added after the label of the current form item.

**extra:** *component type*

　　Used to set the additional prompt information of the current form item.

**validateStatus:** *string* type

　　Used to set the validation status of the current form item. Available options are `'success'`, `'warning'`, `'error'`, and `'validating'`.

**help:** *component type*

　　Used to set the prompt message displayed when the validation status is triggered. It is used to provide feedback to the user with different validation states.

**hidden:** *bool* type, default: `False`

　　Used to set whether to hide the current form item.