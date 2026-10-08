- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- popupClassName (string; optional):
    CSS class name for the expanded menu.

- name (string; optional):
    Used with `AntdForm` for batch value collection/control, serving as the field name of the current form item, with `id` as the default value.

- enableBatchControl (boolean; default True):
    Controls whether the current component participates in the effective `AntdForm` batch value collection/control feature. Default: `True`.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- format (string; optional):
    Date/time display format, [reference](https://day.js.org/docs/en/display/format). Default: `'YYYY-MM-DD'`.

- picker (a value equal to: 'date', 'week', 'month', 'quarter', 'year'; default 'date'):
    Date selection granularity. Options: `'date'`, `'week'`, `'month'`, `'quarter'`, `'year'`. Default: `'date'`.

- firstDayOfWeek (number; optional):
    Custom index of the first day of the week.

- disabled (list of booleans; default [False, False]):
    Whether the start and end date inputs are disabled, respectively. Default: `[False, False]`.

- showTime (dict; default False):
    Time selection panel settings. Default: `False`.

    `showTime` is a boolean | dict with keys:

    - defaultValue (list of strings; optional):
        Initial selected time string for the time selection panel.

    - format (string; optional):
        Time format corresponding to `defaultValue`, [reference](https://day.js.org/docs/en/display/format). Default: `'HH:mm:ss'`.

- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):
    Current component size specification. Options are `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

- bordered (boolean; default True):
    Whether to show the border. When set to `True`, it is equivalent to `variant='outlined'`. Default: `True`.

- variant (a value equal to: 'outlined', 'borderless', 'filled', 'underlined'; optional):
    Variant type. Options are `'outlined'`, `'borderless'`, `'filled'`, `'underlined'`. Among them, `'outlined'` is equivalent to `bordered=True`, but with higher priority.

- placeholder (list of strings; optional):
    Placeholder text content for the input box.

- placement (a value equal to: 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'; default 'bottomLeft'):
    Direction in which the selection panel expands. Options are `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, `'topRight'` Default: `'bottomLeft'`.

- value (list of strings; optional):
    Listen to or set the selected value, corresponding to `format`.

- defaultValue (list of strings; optional):
    Initial selected value, corresponding to `format`.

- pickerValue (string | list of strings; optional):
    Listen to or set the panel’s displayed date, corresponding to `format`.

- disabledDatesStrategy (list of dicts; optional):
    `disabledDatesStrategy` is a list of dicts with keys:

    - mode (a value equal to: 'eq', 'ne', 'le', 'lt', 'ge', 'gt', 'in', 'not-in', 'in-enumerate-dates', 'not-in-enumerate-dates'; optional):
        Current strategy type. Options: `'eq'` (equal), `'ne'` (not equal), `'le'` (less than or equal), `'lt'` (less than), `'ge'` (greater than or equal), `'gt'` (greater than), `'in'` (in), `'not-in'` (not in), `'in-enumerate-dates'` (in list of date strings), `'not-in-enumerate-dates'` (not in list of date strings).

    - target (a value equal to: 'day', 'month', 'quarter', 'year', 'dayOfYear', 'dayOfWeek', 'specific-date'; optional):
        Strategy target. Options: `'dayOfYear'` (by day of year), `'dayOfWeek'` (by day of week), `'day'` (by day), `'month'` (by month), `'quarter'` (by quarter), `'year'` (by year), `'specific-date'` (specific date). For `'specific-date'`, the `value` must strictly follow the `'YYYY-MM-DD'` format.

    - value (number | string | list of numbers | list of strings; optional):
        The actual constraint value corresponding to the strategy type and target.

- open (boolean; optional):
    Monitor or set whether the date range selection panel is open.

- status (a value equal to: 'error', 'warning'; optional):
    Control the validation state. Options are `'error'`, `'warning'`.

- allowClear (boolean; default True):
    Whether to allow one-click clearing of selected values. Default: `True`.

- autoFocus (boolean; default False):
    Whether to automatically gain focus. Default: `False`.

- readOnly (boolean; optional):
    Whether to render as read-only. Default: `False`.

- extraFooter (a list of or a singular dash component, string or number; optional):
    Component type, extra footer content.

- presets (list of dicts; optional):
    `presets` is a list of dicts with keys:

    - label (a list of or a singular dash component, string or number; optional):
        Component type, label for the preset item.

    - value (list of strings; optional):
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
    Anchoring strategy for the related popup layer. Options are `'parent'`, `'body'`. Default: `'body'`.

- batchPropsNames (list of strings; optional):
    Property names to include in [batch property monitoring](/batch-props-values).

- batchPropsValues (dict; optional):
    Values of the properties specified by `batchPropsNames`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persisted_props (list of a value equal to: 'value's; optional):
    Several property names for which the persistence feature is enabled. Options are `'value'`. Default: `['value']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Type of persistent storage for properties. Options are `'local'` (local persistence), `'session'` (session persistence), `'memory'` (in-memory persistence) Default: `'local'`.
