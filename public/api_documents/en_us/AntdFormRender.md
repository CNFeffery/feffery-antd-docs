An AntdFormRender component.


    Keyword arguments:

    - id (string; optional):
        Unique identifier for the component.

    - className (string | dict; optional):
        CSS class name of the component.

    - key (string; optional):
        Unique key used to force a component refresh.

    - schema (dict; required):
        Required. The form schema.

        `schema` is a dict with keys:

        - type (a value equal to: 'object'; optional):
            Must be set to `type: 'object'`.

        - displayType (a value equal to: 'column', 'row', 'inline'; optional):
            Form label layout: `'column'`, `'row'`, or `'inline'`. Default: `'column'`.

        - column (number; optional):
            Number of form columns in a row. Default: `3`.

        - labelWidth (number; optional):
            Width of form item labels.

        - maxWidth (number; optional):
            Maximum width of form item controls.

        - labelCol (number; optional):
            Number of grid columns occupied by form labels.

        - fieldCol (number; optional):
            Number of grid columns occupied by form controls.

        - properties (dict; optional):
            Form control definitions.

            `properties` is a dict with strings as keys and values of type
            dict with keys:

            - type (a value equal to: 'string', 'number', 'boolean', 'array', 'range', 'html', 'block'; optional):

                Field type: `'string'`, `'number'`, `'boolean'`, `'array'`, `'range'`, `'html'`, or `'block'`.

            - title (string; optional):

                Label of the form field.

            - labelWidth (number

                  Or string; optional):

                Width of form item labels.

            - maxWidth (number

          Or string; optional):

                Maximum width of form item controls.

            - labelCol (number | string; optional):

                Number of grid columns occupied by form labels.

            - fieldCol (number | string; optional):

                Number of grid columns occupied by form controls.

            - cellSpan (number | string; optional):

                Display a form item across columns. Use with `lableWidth` to align it with other items; configuring the item's `labelCol` and `fieldCol` can also improve alignment.

            - span (number | string; optional):

                Form item width in a grid of 24 columns. Use `span` to specify how many columns it occupies.

            - widget (a value equal to: 'input', 'inputNumber', 'select', 'multiSelect', 'radio', 'checkboxes', 'textArea', 'checkbox', 'switch', 'rate', 'slider', 'datePicker', 'dateRange', 'timePicker', 'timeRange', 'cascader', 'treeSelect', 'color', 'imageInput', 'urlInput', 'html'; optional):

                Name of the control to render.

            - placeholder (string | list of strings; optional):

                Input placeholder text.

            - description (string; optional):

                Subtitle description.

            - tooltip (dict; optional):

                Tooltip content. Supports HTML and an Ant Design tooltip configuration object for additional settings.

                `tooltip` is a string | dict with keys:

                - title (boolean | number | string | dict | list; optional):

                    Text to display.

                - placement (a value equal to: 'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'; optional):

                    Tooltip placement: `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`,

                    、'topRight'、'bottomLeft'、'bottomRight'、'leftTop'、'leftBottom'

                    `'rightTop'`, or `'rightBottom'`. Default: `'top'`.

                - color (string; optional):

                    Background color.

                - mouseEnterDelay (number; optional):

                    Delay in seconds before showing the tooltip after mouse entry. Default: `0.1`.

                - mouseLeaveDelay (number; optional):

                    Delay in seconds before hiding the tooltip after mouse exit. Default: `0.1`.

                - overlayClassName (string | dict; optional):

                    CSS class of the tooltip card.

                - overlayStyle (dict; optional):

                    Style of the tooltip card.

                - overlayInnerStyle (dict; optional):

                    Style of the tooltip content area.

                - trigger (a value equal to: 'hover', 'focus', 'click' | list of a value equal to: 'hover', 'focus', 'click's; optional):

                    Trigger: `'hover'`, `'focus'`, `'click'`, or a list of these values. Default: `'hover'`.

                - zIndex (number; optional):

                    Tooltip overlay z-index.

                - arrow (a value equal to: 'show', 'hide', 'center'; optional):

                    Arrow visibility and whether the arrow points to the target center. Default: `'show'`.

                - fresh (boolean; optional):

                    Whether to always refresh tooltip content. Default: `False`.

                    Tooltips normally cache content while closed; enabling this option keeps content updated.

                - open (boolean; optional):

                    Observe or control tooltip visibility. Default: `False`.

                - autoAdjustOverflow (boolean; optional):

                    Whether to adjust the tooltip placement automatically when obscured. Default: `True`.

                - defaultOpen (boolean; optional):

                    Initial visibility. Default: `False`.

                - destroyTooltipOnHide (boolean; optional):

                    Whether to destroy the tooltip when hidden. Default: `False`.

            - extra (string; optional):

                Additional help text shown directly below the control. Supports HTML.

            - required (boolean | string; optional):

                Whether the field is required. Default: `False`.

            - min (number | string; optional):

                Minimum string length for `string`, minimum value for `number`, or minimum array length for `array`.

            - max (number | string; optional):

                Maximum string length for `string`, maximum value for `number`, or maximum array length for `array`.

            - format (a value equal to: 'image', 'textarea', 'color', 'email', 'url', 'dateTime', 'date', 'time', 'upload'; optional):

                How to handle the configured field type.

            - rules (list of dicts; optional):

                Validation rules for the form control.

                `rules` is a list of dicts with keys:

                - defaultField (dict; optional):

                    Validation rules for array elements. Only applies when `type` is `'array'`.

                - enum (boolean | number | string | dict | list; optional):

                    Whether the value matches an enumeration. Requires `type: 'enum'`.

                - fields (boolean | number | string | dict | list; optional):

                    Validation rules for child fields. Only applies when `type` is `'array'` or `'object'`.

                - len (number; optional):

                    Exact string length for `string`, exact value for `number`, or exact array length for `array`.

                - max (number; optional):

                    Requires `type`. Maximum string length for `string`, maximum value for `number`, or maximum array length for `array`.

                - message (string; optional):

                    Validation error message. Generated from a template when omitted.

                - min (number; optional):

                    Requires `type`. Minimum string length for `string`, minimum value for `number`, or minimum array length for `array`.

                - pattern (string; optional):

                    Regular expression to match.

                - required (boolean; optional):

                    Whether the field is required.

                - type (a value equal to: 'string', 'number', 'boolean', 'method', 'regexp', 'integer', 'float', 'array', 'object', 'enum', 'date', 'url', 'hex', 'email', 'any'; optional):

                    Value type, such as `string`, `number`, `boolean`, `url`, or `email`.

                - validateTrigger (a value equal to: 'onChange', 'onBlur', 'onFocus'; optional):

                    Validation trigger: `'onChange'`, `'onBlur'`, or `'onFocus'`. Default: `'onChange'`.

                - validator (string; optional):

                    Custom validator, provided as a JavaScript function string.

                - warningOnly (boolean; optional):

                    Issue a warning without blocking form submission.

                - whitespace (boolean; optional):

                    Reject values containing only whitespace. Only applies when `type` is `'string'`.

            - hidden (boolean | string; optional):

                Whether to hide the field. Default: `False`.

            - disabled (boolean | string; optional):

                Whether to disable the field. Default: `False`.

            - readOnly (boolean | string; optional):

                Whether to enable read-only mode. Default: `False`.

            - readOnlyWidget (string; optional):

                Name of the component used to render read-only content.

            - dependencies (list of strings; optional):

                Dependent form fields. Changes to these fields trigger this field to re-render, supporting linked form controls.

            - className (string; optional):

                Custom CSS class for the control.

            - reserveLabel (boolean | string; optional):

                When `title` is omitted, set `reserveLabel` to

                `True` to reserve `labelWidth` space and align the input with other controls.

            - props (dict; optional):

                Additional control properties. For Ant Design controls, these are the corresponding Ant Design component properties. | dict with keys:

            - type (a value equal to: 'object'; optional):

                Must be set to `type: 'object'`.

            - title (string; optional):

                Title text.

            - widget (a value equal to: 'collapse', 'card', 'lineTitle', 'subInline'; optional):

                Nested component: `'collapse'`, `'card'`, `'lineTitle'`, or `'subInline'`. Default: `'card'`.

            - properties (dict; optional):

                Collection of form fields.

            - column (number | string; optional):

                Number of form columns in a row. Default: `3`.

            - description (string; optional):

                Subtitle description.

            - tooltip (dict; optional):

                Tooltip content. Supports HTML and an Ant Design tooltip configuration object for additional settings.

                `tooltip` is a string | dict with keys:

                - title (boolean | number | string | dict | list; optional):

                    Text to display.

                - placement (a value equal to: 'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'; optional):

                    Tooltip placement: `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`,

                    、'topRight'、'bottomLeft'、'bottomRight'、'leftTop'、'leftBottom'

                    `'rightTop'`, or `'rightBottom'`. Default: `'top'`.

                - color (string; optional):

                    Background color.

                - mouseEnterDelay (number; optional):

                    Delay in seconds before showing the tooltip after mouse entry. Default: `0.1`.

                - mouseLeaveDelay (number; optional):

                    Delay in seconds before hiding the tooltip after mouse exit. Default: `0.1`.

                - overlayClassName (string | dict; optional):

                    CSS class of the tooltip card.

                - overlayStyle (dict; optional):

                    Style of the tooltip card.

                - overlayInnerStyle (dict; optional):

                    Style of the tooltip content area.

                - trigger (a value equal to: 'hover', 'focus', 'click' | list of a value equal to: 'hover', 'focus', 'click's; optional):

                    Trigger: `'hover'`, `'focus'`, `'click'`, or a list of these values. Default: `'hover'`.

                - zIndex (number; optional):

                    Tooltip overlay z-index.

                - arrow (a value equal to: 'show', 'hide', 'center'; optional):

                    Arrow visibility and whether the arrow points to the target center. Default: `'show'`.

                - fresh (boolean; optional):

                    Whether to always refresh tooltip content. Default: `False`.

                    Tooltips normally cache content while closed; enabling this option keeps content updated.

                - open (boolean; optional):

                    Observe or control tooltip visibility. Default: `False`.

                - autoAdjustOverflow (boolean; optional):

                    Whether to adjust the tooltip placement automatically when obscured. Default: `True`.

                - defaultOpen (boolean; optional):

                    Initial visibility. Default: `False`.

                - destroyTooltipOnHide (boolean; optional):

                    Whether to destroy the tooltip when hidden. Default: `False`.

            - props (dict; optional):

                Additional properties forwarded to the nested component. | dict with keys:

            - type (a value equal to: 'array'; optional):

                Must be set to `type: 'array'`.

            - title (string; optional):

                Title text.

            - widget (a value equal to: 'cardList', 'simpleList', 'tableList', 'drawerList', 'virtualList'; optional):

                List component: `'cardList'`, `'simpleList'`, `'tableList'`, `'drawerList'`, or `'virtualList'`. Default: `'cardList'`.

            - max (number | string; optional):

                Maximum list length.

            - min (number | string; optional):

                Minimum list length.

            - props (dict; optional):

                List control settings.

                `props` is a dict with keys:

                - addBtnProps (dict; optional):

                    Add button properties. See Ant Design Button props.

                - delConfirmProps (dict; optional):

                    Delete confirmation popup properties. See Ant Design Popconfirm props.

                - actionColumnProps (dict; optional):

                    Action column properties for `tableList`, `drawerList`, and `virtualList`. See Ant Design

                    Table `ColumnType`. Use `colHeaderText` in place of `title`.

                - hideAdd (boolean; optional):

                    Whether to hide the add button.

                - hideCopy (boolean; optional):

                    Whether to hide the copy button.

                - hideMove (boolean; optional):

                    Whether to hide the move button.

                - hideDelete (boolean; optional):

                    Whether to hide the delete button.

            - items (dict; optional):

                Dynamic item configuration; may contain a nested control.

    - displayType (a value equal to: 'column', 'row', 'inline'; default 'column'):
        Form layout: place labels and controls in a column or a row, or use natural inline flow. Options: `'column'`, `'row'`, `'inline'`. Default: `'column'`.

    - labelAlign (a value equal to: 'left', 'right'; default 'right'):
        Label text alignment: `'left'` or `'right'`. Default: `'right'`.

    - lableWidth (number; optional):
        Fixed width of form labels.

    - maxWidth (number; optional):
        Maximum width of form item controls.

    - labelCol (number; optional):
        Number of grid columns occupied by form labels.

    - fieldCol (number; optional):
        Number of grid columns occupied by form controls.

    - colon (boolean; default True):
        Whether to show a colon after labels. Default: `True`.

    - globalConfig (dict; optional):
        Global form configuration.

        `globalConfig` is a dict with keys:

        - mustacheDisabled (boolean; optional):
            Whether to disable expressions.

        - listOperate (dict; optional):
            List form settings.

            `listOperate` is a dict with keys:

            - btnType (a value equal to: 'icon', 'text'; optional):
                Style of list operation buttons.

            - hideMove (boolean; optional):
                Whether to hide the move button.

    - watch (dict with strings as keys and values of type string; optional):
        Watch changes in form data. Values must be JavaScript function strings.

    - removeHiddenData (boolean; default True):
        Whether to remove hidden field data on submission. Default: `True`.

    - readOnly (boolean; default False):
        Whether to enable read-only mode, typically used for text previews. Default: `False`.

    - column (number; default 1):
        Number of form columns in each row.

    - disabled (boolean; default False):
        Whether to disable all form items. Default: `False`.

    - scrollToFirstError (boolean; default False):
        Whether to scroll to the first invalid field after a failed submission. Default: `False`.

    - locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-CN'):
        Display language. The docstring describes support for `'zh-CN'` and `'en-US'`, with default `'zh-CN'`.

    - footer (dict; optional):
        Footer action area settings.

        `footer` is a boolean | dict with keys:

        - submit (dict; optional):
            Submit button settings.

            `submit` is a dict with keys:

            - text (string; optional):
                Button text.

            - hide (boolean; optional):
                Whether to show the button.

            - btnProps (dict; optional):
                Additional button properties. See Ant Design Button props.

        - reset (dict; optional):
            Reset button settings.

            `reset` is a dict with keys:

            - text (string; optional):
                Button text.

            - hide (boolean; optional):
                Whether to show the button.

            - btnProps (dict; optional):
                Additional button properties. See Ant Design Button props. | a list of or a singular dash component, string or number

    - configProvider (dict; optional):
        Ant Design ConfigProvider settings.

    - validateMessages (dict; optional):
        Default validation messages.

        `validateMessages` is a dict with keys:

        - default (string; optional)

        - required (string; optional)

        - whitespace (string; optional)

        - date (dict; optional)

            `date` is a dict with keys:

            - format (string; optional)

            - parse (string; optional)

            - invalid (string; optional)

        - types (dict; optional)

            `types` is a dict with keys:

            - string (string; optional)

            - method (string; optional)

            - array (string; optional)

            - object (string; optional)

            - number (string; optional)

            - date (string; optional)

            - boolean (string; optional)

            - integer (string; optional)

            - float (string; optional)

            - regexp (string; optional)

            - email (string; optional)

            - url (string; optional)

            - hex (string; optional)

        - string (dict; optional)

            `string` is a dict with keys:

            - len (string; optional)

            - min (string; optional)

            - max (string; optional)

            - range (string; optional)

        - number (dict; optional)

            `number` is a dict with keys:

            - len (string; optional)

            - min (string; optional)

            - max (string; optional)

            - range (string; optional)

        - array (dict; optional)

            `array` is a dict with keys:

            - len (string; optional)

            - min (string; optional)

            - max (string; optional)

            - range (string; optional)

        - pattern (dict; optional)

            `pattern` is a dict with keys:

            - mismatch (string; optional)

    - values (dict; optional):
        Set or observe form data.

    - validateStatuses (boolean; optional):
        Observe form validation results.

    - submitForm (boolean; optional):
        Collect validation results manually for submission. Set to `True` in a callback; resets automatically to `False`.

    - submitFormClicks (number; default 0):
        Auxiliary counter for observing form submissions.

    - resetForm (boolean; optional):
        Reset form item validation states. This does not reset the values of wrapped controls; reset those values through callbacks. Set to `True` in a callback; resets automatically to `False`.

    - resetFormClicks (number; default 0):
        Auxiliary counter for observing form resets.

    - loading_state (dict; optional)

        `loading_state` is a dict with keys:

        - is_loading (boolean; optional):
            Determines if the component is loading or not.

        - prop_name (string; optional):
            Holds which property is loading.

        - component_name (string; optional):
            Holds the name of the component that is loading.