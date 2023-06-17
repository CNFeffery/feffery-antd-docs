**id:** *string* or *dict*

　　Used to set the unique ID information for the current component.

**key:** *string*

　　Updates the `key` value for the current component, which can force a redraw of the current component.

**style:** *dict*

　　Used to set the CSS style for the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**locale:** *string*, default: `'zh-cn'`

　　Used to set the language for the functional text of the current component. Options include `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**format:** *string*

　　Used to set the date parsing format for the current date range picker. See [reference documentation](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/) for details.

**picker:** *string*, default: `'date'`

　　Used to set the granularity of the date range selection. Options include `'date'`, `'week'`, `'month'`, `'quarter'`, and `'year'`.

**firstDayOfWeek:** *int*

　　Used to customize the first day of the week, where `1` represents Monday.

**disabled:** `list[bool]`, default: `[False, False]`

　　Used to individually disable the start and end date selection of the current date range selection component. The format is `[disable start date, disable end date]`.

**showTime:** *bool* or *dict*, default: `False`

　　Used to enable the additional time selection feature. When passing a *dict* input, it will automatically set the default selected time value when the time selection feature is enabled. The default time value will be automatically selected after the user clicks to select the date. The available key-value parameters are:

- **defaultValue:** `list[string]`, used to set the time strings corresponding to the start and end dates.
- **format:** *string*, default: `'HH:mm:ss'`, used to set the time parsing format corresponding to `showTime.defaultValue`. See [reference documentation](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/) for details.

**size:** *string*, default: `'middle'`

　　Used to set the size specification of the current component. Options include `'small'`, `'middle'`, and `'large'`.

**bordered:** *bool*, default: `True`

　　Used to render the border.

**placeholder:** *list*

　　Used to set the placeholder text for blank inputs. The format is `[placeholder for start date, placeholder for end date]`.

**placement:** *str*, default: `'bottomLeft'`

　　Used to set the direction of the dropdown menu. Options include `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, and `'topRight'`.

**value:** *list*

　　Used to listen to or set the currently selected values.

**defaultValue:** *list*

　　Used to listen to or set the initially selected values.

**defaultPickerValue:** *string*

　　Used to set the initial date position for the date range selection panel.

**disabledDatesStrategy:** `list[dict]`

　　Used to customize the date disabling strategy. Each dictionary represents a single strategy, and dates that meet at least one strategy will be disabled. The available key-value parameters are:

- **mode:** *str*, used to define the current strategy type. Options include `'eq'` (equals), `'ne'` (notequals), `'le'` (less than or equal to), `'lt'` (less than), `'ge'` (greater than or equal to), `'gt'` (greater than), `'in'` (in), `'not in'` (not in), `'in-enumerate-dates'` (in enumerated date strings array), and `'not-in-enumerate-dates'` (not in enumerated date strings array).

  - **target:** *str*, used to define the constraint target for the current strategy. Options include `'day'` (by day), `'month'` (by month), `'quarter'` (by quarter), `'year'` (by year), `'dayOfYear'` (by day of the year), `'dayOfWeek'` (by day of the week), and `'specific-date'` (specific date).
  - **value:** *int*, *string*, `list[int]`, or `list[str]`, used to define the constraint value corresponding to the current strategy. Strategies with `'in'` require a list-type input.

  **open:** *bool*

  　　Used to set or listen to the expand/collapse state of the component's overlay.

  **status:** *string*

  　　Forces the component's status. Options include `'error'` and `'warning'`.

  **allowClear:** *bool*, default: `True`

  　　Sets whether to allow the user to clear the selected option.

  **readOnly:** *bool*

  　　Sets whether to display the component in read-only mode.

  **popupContainer:** *string*, default: `'body'`

  　　Sets the reference container type for the floating layer elements associated with the current component. Options include `'body'` (page root node) and `'parent'` (parent container of the current element). When the component is inside a scrollable container, setting `popupContainer='parent'` can solve the issue of the floating layer not scrolling along.

  **persistence:** *bool*

  　　Sets whether to enable property persistence for the current component.

  **persisted_props:** *list*, default: `['value']`

  　　Sets which properties of the current component to persist. Options include `'value'`.

  **persistence_type:** *string*, default: `'local'`

  　　Sets the storage type for property persistence of the current component. Options include `'local'` (browser local cache), `'session'` (current tab session cache), and `'memory'` (temporary memory cache).