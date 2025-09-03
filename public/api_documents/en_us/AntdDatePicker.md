- id (string; optional):  
   Unique component id.

- key (string; optional):  
   Update the `key` value of the current component to force re-rendering of the component.

- className (string | dict; optional):  
   CSS class name of the current component, supports [dynamic css](/advanced-classname).

- popupClassName (string; optional):  
   CSS class name of the dropdown menu.

- name (string; optional):  
   Used with the `AntdForm` batch value collection/control function, serving as the field name of the current form item. Defaults to `id`.

- enableBatchControl (boolean; default True):  
   Controls whether the current component participates in the effective `AntdForm` batch value collection/control function. Default: `True`.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru'; default 'zh-cn'):  
   Language of the component text. Options: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'ru-ru'` (Russian).  
   Default: `'zh-cn'`.

- format (string; optional):  
   Date/time display format, [reference](https://day.js.org/docs/en/display/format).  
   Default: `'YYYY-MM-DD'`.

- picker (a value equal to: 'date', 'week', 'month', 'quarter', 'year'; default 'date'):  
   Date selection granularity. Options: `'date'`, `'week'`, `'month'`, `'quarter'`, `'year'`.  
   Default: `'date'`.

- firstDayOfWeek (number; optional):  
   Custom index of the first day of the week.

- disabled (boolean; default False):  
   Whether to disable the component. Default: `False`.

- showTime (dict; default False):  
   Configure parameters related to the time selection panel. Default: `False`.

  `showTime` is a boolean | dict with keys:

  - defaultValue (string; optional):  
     Initial selected time string for the time selection panel.

  - format (string; optional):  
     Time format corresponding to `defaultValue`, [reference](https://day.js.org/docs/en/display/format).  
     Default: `'HH:mm:ss'`.

- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):  
   Size specification of the component. Options: `'small'`, `'middle'`, `'large'`.  
   Default: `'middle'`.

- bordered (boolean; default True):  
   Whether to show a border. Equivalent to `variant='outlined'` when set to `True`. Default: `True`.

- variant (a value equal to: 'outlined', 'borderless', 'filled', 'underlined'; optional):  
   Variant type. Options: `'outlined'`, `'borderless'`, `'filled'`, `'underlined'`. `'outlined'` is equivalent to `bordered=True`, but takes higher priority.

- placeholder (string; optional):  
   Placeholder text in the input box.

- placement (a value equal to: 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'; default 'bottomLeft'):  
   Direction in which the panel expands. Options: `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, `'topRight'`.  
   Default: `'bottomLeft'`.

- value (string; optional):  
   Listen to or set the selected value, corresponding to `format`.

- defaultValue (string; optional):  
   Initial selected value, corresponding to `format`.

- pickerValue (string; optional):  
   Listen to or set the panel’s displayed date, corresponding to `format`.

- disabledDatesStrategy (list of dicts; optional):  
   Configure an array of disabled date strategies. Dates matching at least one rule will be disabled.

  `disabledDatesStrategy` is a list of dicts with keys:

  - mode (a value equal to: 'eq', 'ne', 'le', 'lt', 'ge', 'gt', 'in', 'not-in', 'in-enumerate-dates', 'not-in-enumerate-dates'; optional):  
     Current strategy type. Options: `'eq'` (equal), `'ne'` (not equal), `'le'` (less than or equal), `'lt'` (less than), `'ge'` (greater than or equal),  
     `'gt'` (greater than), `'in'` (in), `'not-in'` (not in), `'in-enumerate-dates'` (in list of date strings), `'not-in-enumerate-dates'` (not in list of date strings).

  - target (a value equal to: 'day', 'month', 'quarter', 'year', 'dayOfYear', 'dayOfWeek', 'specific-date'; optional):  
     Strategy target. Options: `'dayOfYear'` (by day of year), `'dayOfWeek'` (by day of week), `'day'` (by day), `'month'` (by month), `'quarter'` (by quarter), `'year'` (by year), `'specific-date'` (specific date).  
     For `'specific-date'`, the `value` must strictly follow the `'YYYY-MM-DD'` format.

  - value (number | string | list of numbers | list of strings; optional):  
     The actual constraint value corresponding to the strategy type and target.

- status (a value equal to: 'error', 'warning'; optional):  
   Validation status. Options: `'error'`, `'warning'`.

- allowClear (boolean; default True):  
   Whether to allow clearing the selected value with one click. Default: `True`.

- autoFocus (boolean; default False):  
   Whether to automatically focus. Default: `False`.

- readOnly (boolean; optional):  
   Whether to render as read-only. Default: `False`.

- extraFooter (a list of or a singular dash component, string or number; optional):  
   Component type, extra footer content.

- showToday (boolean; default True):  
   Whether to show the “Today” quick selection button. Default: `True`.

- presets (list of dicts; optional):  
   Configure a list of presets.

  `presets` is a list of dicts with keys:

  - label (a list of or a singular dash component, string or number; optional):  
     Component type, label for the preset item.

  - value (string; optional):  
     Value of the preset item, corresponding to `format`.

- clickedPreset (dict; optional):  
   Works with the `presets` parameter, listens for the most recent preset item click event information.

  `clickedPreset` is a dict with keys:

  - value (string | number; optional):  
     Value of the preset item.

  - timestamp (number; optional):  
     Timestamp of the event.

- needConfirm (boolean; default False):  
   Whether clicking a button is required to confirm selection. If `False`, losing focus means selection is made. Default: `False`.

- customCells (list of dicts; optional):  
   Customize cell styles for specific dates.

  `customCells` is a list of dicts with keys:

  - year (number; optional):  
     Year value for matching.

  - month (number; optional):  
     Month value for matching.

  - date (number; optional):  
     Day value for matching.

  - style (dict; optional):  
     Custom CSS style.

  - className (string; optional):  
     Custom CSS class name.

- prefix (a list of or a singular dash component, string or number; optional):  
   Component type, embedded prefix content.

- suffixIcon (a list of or a singular dash component, string or number; optional):  
   Custom suffix icon content for the selection box.

- popupContainer (a value equal to: 'parent', 'body'; default 'body'):  
   Anchoring strategy for the dropdown layer. Options: `'parent'`, `'body'`. Default: `'body'`.

- batchPropsNames (list of strings; optional):  
   List of property names to include in [batch property listening](/batch-props-values).

- batchPropsValues (dict; optional):  
   Listen to the values of properties specified in `batchPropsNames`.

- data-_ (string; optional):  
   Wildcard attribute in `data-_` format.

- aria-_ (string; optional):  
   Wildcard attribute in `aria-_` format.

- persistence (boolean | string | number; optional):  
   Whether to enable [property persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'value's; optional):  
   Properties enabled for persistence. Options: `'value'`.  
   Default: `['value']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):  
   Type of persistence storage. Options: `'local'` (local storage), `'session'` (session storage), `'memory'` (in-memory).  
   Default: `'local'`.
