- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- name (string; optional):
    Used with `AntdForm` for batch value collection/control, serving as the field name of the current form item, with `id` as the default value.

- enableBatchControl (boolean; default True):
    Controls whether the current component participates in the effective `AntdForm` batch value collection/control feature. Default: `True`.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- format (string; default 'YYYY-MM-DD'):
    The format for displaying dates, [reference material](https://day.js.org/docs/en/display/format) Default value: `'YYYY-MM-DD'`.

- size (a value equal to: 'default', 'large'; default 'default'):
    The calendar size specification, options include `'default'`, `'large'`. Default value: `'default'`.

- value (string; optional):
    Listen for or set the current selected date value.

- defaultValue (string; optional):
    The initial selected date value.

- customCells (list of dicts; optional):
    `customCells` is a list of dictionaries with keys:

    `customCells` is a list of dicts with keys:

    - type (a value equal to: 'month', 'date'; required):
        Required, the type corresponding to the current item, options include `'month'`, `'date'`.

    - year (number; optional):
        Year value for matching.

    - month (number; optional):
        Month value for matching.

    - date (number; optional):
        Day value for matching.

    - content (a list of or a singular dash component, string or number; optional):
        Custom content.

- cellClickEvent (dict; optional):
    Listen for the click event on the date cell.

    `cellClickEvent` is a dict with keys:

    - type (string; optional):
        The type of the panel being recorded.

    - timestamp (number; optional):
        The timestamp of the event.

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
