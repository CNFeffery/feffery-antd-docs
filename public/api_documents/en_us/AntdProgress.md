- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- type (a value equal to: 'line', 'circle', 'dashboard'; default 'line'):
    Progress bar type. Supported values: `'line'`, `'circle'`, `'dashboard'`. Default: `'line'`.

- size (dict; default 'default'):
    Progress bar size: a preset size, a number for pixels, or a dictionary with separate width and height settings. Supported values: `'small'`, `'default'`, `'large'`. Default: `'default'`.

    `size` is a number | list of number | strings | a value equal to:
    'small', 'default' | dict with keys:

    - width (number; optional):
        Width in pixels.

    - height (number; optional):
        Height in pixels.

- percent (number; default 0):
    Progress value between `0` and `100`. A value of `100` shows the completed state by default. Default: `0`.

- success (dict; optional):
    Completed progress settings.

    `success` is a dict with keys:

    - percent (number; optional):
        Progress value marking completion, between `0` and `100`. Default: `100`.

    - strokeColor (dict; optional):
        Progress bar color for completed progress. Supports gradients.

        `strokeColor` is a string

      Or dict with keys:

        - from (string; optional):

            Gradient start color.

        - to (string; optional):

            Gradient end color.

- format (dict; optional):
    Progress tooltip settings.

    `format` is a dict with keys:

    - prefix (string; optional):
        Progress tooltip prefix. Default: `''`.

    - suffix (string; optional):
        Progress tooltip suffix. Default: `'%'`.

    - content (a list of or a singular dash component, string or number; optional):
        Override the displayed content. Supports components.

- status (a value equal to: 'success', 'exception', 'normal', 'active'; optional):
    Progress status. `'active'` only applies when `type='line'`. Supported values: `'success'`, `'exception'`, `'normal'`, `'active'`. Default: `'normal'`.

- showInfo (boolean; default True):
    Whether to show the numeric progress or status icon. Default: `True`.

- percentPosition (dict; optional):
    Numeric progress placement for `'line'` progress bars.

    `percentPosition` is a dict with keys:

    - align (a value equal to: 'start', 'center', 'end'; optional):
        Alignment. Options: `'start'`, `'center'`, `'end'`.

    - type (a value equal to: 'inner', 'outer'; optional):
        Position. Options: `'inner'`, `'outer'`.

- strokeColor (dict; optional):
    Progress bar color settings. Supports gradients.

    `strokeColor` is a string | list of strings | dict with keys:

    - from (string; optional):
        Gradient start color.

    - to (string; optional):
        Gradient end color. | dict with strings as keys and values of type string

- strokeLinecap (a value equal to: 'round', 'butt', 'square'; optional):
    Progress stroke line cap. Supported values: `'round'`, `'butt'`, `'square'`. Default: `'round'`.

- strokeWidth (number; optional):
    Progress stroke width as a percentage of the canvas width.

- trailColor (string; optional):
    Color of unfinished segments; no color by default.

- gapDegree (number; optional):
    Dashboard gap angle, between `0` and `295`. Only applies when `type='dashboard'`. Default: `75`.

- gapPosition (a value equal to: 'top', 'bottom', 'left', 'right'; default 'bottom'):
    Dashboard gap position. Only applies when `type='dashboard'`. Supported values: `'top'`, `'bottom'`, `'left'`, `'right'`. Default: `'bottom'`.

- steps (dict; optional):
    Number of progress segments. `'circle'` and `'dashboard'` support dictionary configuration for further settings.

    `steps` is a number | dict with keys:

    - count (number; optional):
        Number of segments.

    - gap (number; optional):
        Gap between segments in pixels.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
