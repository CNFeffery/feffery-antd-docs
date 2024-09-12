Here is the translation of the provided text into English:

- id (string; optional):
    The unique id of the component.

- aria-* (string; optional):
    Wildcard for attributes in the `aria-*` format.

- cellClickEvent (dict; optional):
    Listen for the click event on the date cell.

    `cellClickEvent` is a dictionary with keys:

    - timestamp (number; optional):
        The timestamp of the event.

    - type (string; optional):
        The type of the panel being recorded.

- className (string | dict; optional):
    The current component's CSS class name, supports [dynamic CSS](/advanced-classname).

- customCells (list of dicts; optional):
    Custom display content for the corresponding month and date.

    `customCells` is a list of dictionaries with keys:

    - content (a list of or a singular dash component, string or number; optional):
        Custom content.

    - date (number; optional):
        The date value that the current item matches.

    - month (number; optional):
        The month value that the current item matches.

    - type (a value equal to: 'month', 'date'; required):
        Required, the type corresponding to the current item, options include `'month'`, `'date'`.

    - year (number; optional):
        The year value that the current item matches.

- data-* (string; optional):
    Wildcard for attributes in the `data-*` format.

- defaultValue (string; optional):
    The initial selected date value.

- format (string; default 'YYYY-MM-DD'):
    The format for displaying dates, [reference material](https://day.js.org/docs/en/display/format) 
    Default value: `'YYYY-MM-DD'`.

- key (string; optional):
    Update the `key` value of the current component to force a redraw of the component.

- loading_state (dict; optional)

    `loading_state` is a dictionary with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de'; default 'zh-cn'):
    The language of the component's text, options include `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German)
    Default value: `'zh-cn'`.

- name (string; optional):
    Used in conjunction with the `AntdForm` form batch value collection/control feature, serving as the field name for the current form item, with `id` as the default value.

- persisted_props (list of a value equal to: 'value's; default ['value']):
    The names of several properties that enable attribute persistence, with the option of `'value'`. Default value: `['value']`.

- persistence (boolean | string | number; optional):
    Whether to enable [property persistence](/prop-persistence).

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    The storage type for property persistence, options include `'local'` (local persistence), `'session'` (session persistence), `'memory'` (memory persistence)
    Default value: `'local'`.

- size (a value equal to: 'default', 'large'; default 'default'):
    The calendar size specification, options include `'default'`, `'large'`. Default value: `'default'`.

- style (dict; optional):
    The current component's CSS styles.

- value (string; optional):
    Listen for or set the current selected date value.
