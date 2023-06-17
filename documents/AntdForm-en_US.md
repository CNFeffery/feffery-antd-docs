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

**layout:** *string* type, default: `'horizontal'`

　　Used to set the form layout mode, available options are `'horizontal'`, `'vertical'`, and `'inline'`.

**labelCol:** *dict* type

　　Used to set the column width-related properties for the labels of each form item in the form as a whole. The specific parameters are the same as the corresponding parameters in `AntdFormItem`. This has a lower priority than individually setting `labelCol` in `AntdFormItem`.

**wrapperCol:** *dict* type

　　Used to set the column width-related properties for the controls of each form item in the form as a whole. The specific parameters are the same as the corresponding parameters in `AntdFormItem`. This has a lower priority than individually setting `wrapperCol` in `AntdFormItem`.

**colon:** *bool* type, default: `True`

　　Used to set whether to add a colon suffix to the labels of all form items below it. Only applicable when `layout='horizontal'`.

**labelAlign:** *string* type, default: `'right'`

　　Used to set the alignment of the label contents for all form items below it. Available options are `'left'` and `'right'`.