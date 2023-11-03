**id:** *string* or *dict*

　　Used to set the unique ID information for the current component.

**key:** *string*

　　Updates the `key` value for the current component, enabling forced rendering of the component.

**style:** *dict*

　　Used to set the CSS styles for the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name for the current component, supporting [dynamic CSS](/advanced-classname).

**locale:** *string*, default: `'zh-cn'`

　　Sets the language for the functional text of the current component. Options include `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**format:** *string*

　　Sets the date parsing format for the current date picker. Refer to the [documentation](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/) for specific formatting options.

**picker:** *string*, default: `'date'`

　　Sets the granularity of the date selection. Options include `'date'`, `'week'`, `'month'`, `'quarter'`, and `'year'`.

**firstDayOfWeek:** *int*

　　Customizes the first day of the week. For example, `1` represents Monday.

**disabled:** *bool*, default: `False`

　　Sets whether the current component is disabled.

**showTime:** *bool* or *dict*, default: `False`

　　Enables additional time selection functionality. When passing a *dict* as input, it automatically sets the default selected time value after the user clicks to select a date. Available key-value pairs for the *dict* include:

　　- **defaultValue:** *string*, sets the time string.
　　- **format:** *string*, default: `'HH:mm:ss'`, sets the time parsing format corresponding to `showTime.defaultValue`. Refer to the [documentation](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/) for specific formatting options.

**size:** *string*, default: `'middle'`

　　Sets the size specification for the current component. Options include `'small'`, `'middle'`, and `'large'`.

**bordered:** *bool*, default: `True`

　　Sets whether to render a border.

**placeholder:** *string*

　　Sets the placeholder text for blank inputs.

**placement:** *str*, default: `'bottomLeft'`

　　Sets the direction of the dropdown menu. Options include `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, and `'topRight'`.

**value:** *string*

　　Listens to or sets the currently selected value.

**defaultValue:** *string*

　　Listens to or sets the initially selected value.

**defaultPickerValue:** *string*

　　Sets the date position where the date selection panel stays when initialized.

**disabledDatesStrategy:** `list[dict]`

　　Customizes the strategy for disabling dates. Each dictionary represents a single strategy, and dates that satisfy at least one strategy will be disabled. Available key-value pairs for each strategy include:

  - **mode:** *str*, defines the strategy type. Options include `'eq'` (equal to), `'ne'` (not equal to), `'le'` (less than or equal to), `'lt'` (less than), `'ge'` (greater than or equal to), `'gt'` (greater than), `'in'` (in), `'not in'` (not in), `'in-enumerate-dates'` (in date string enumeration array), and `'not-in-enumerate-dates'` (not in date string enumeration array).
  - **target:** *str*, defines the constraint target for the strategy. Options include `'day'` (by day), `'month'` (by month), `'quarter'` (by quarter), `'year'` (by year), `'dayOfYear'` (by day of the year), `'dayOfWeek'` (by day of the week), and `'specific-date'` (specific date).
  - **value:** *int*, *string*, `list[int]`, or `list[str]`, defines the constraint value for the strategy. Strategies with `'in'` require a list-type input.

**status:** *string*

　　Forces the component's status. Options include `'error'` and `'warning'`.

**allowClear:** *bool*, default: `True`

　　Sets whether to allow users to clear the selected option.

**autoFocus:** *bool* type, default: `False`

　　Used to set whether to automatically focus.

**readOnly:** *bool*

　　Sets whether to display the component in read-only mode.

**showToday:** *bool*, Default: `True`

　　Used to *determine whether to render the "Today" shortcut button.*

**extraFooter:** *Component*

　　Used to *set additional elements at the bottom of the selection panel.*

**popupContainer:** *string*, default: `'body'`

　　Sets the reference container type for the floating elements associated with the current component. Options include `'body'` (root node of the page) and `'parent'` (parent container of the current element). When the component is inside a scrollable container, setting `popupContainer='parent'` resolves the issue of the floating panel not scrolling along.

**persistence:** *bool*

　　Sets whether to enable property persistence for the current component.

**persisted_props:** *list*, default: `['value']`

　　Sets which properties of the current component should be persisted. Options include `'value'`.

**persistence_type:** *string*, default: `'local'`

　　Sets the storage type for property persistence of the current component. Options include `'local'` (browser local cache), `'session'` (current tab session cache), and `'memory'` (temporary memory cache).