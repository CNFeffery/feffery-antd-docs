- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- breakpoints (list of numbers; required):
    Required. Segment breakpoint array to monitor or set.

- colors (list of strings; required):
    Required. Segment colors; the array length must be one less than the length of `breakpoints`.

- controls (boolean; default True):
    Whether segment numeric inputs show increment/decrement buttons. Default: `True`.

- keyboard (boolean; default True):
    Whether the up/down arrow keys adjust segment numeric inputs. Default: `True`.

- min (number; optional):
    Minimum numeric value allowed in each segment's input; unrestricted by default.

- max (number; optional):
    Maximum numeric value allowed in each segment's input; unrestricted by default.

- step (number; default 0.01):
    Step size for each segment's numeric input. Default: `0.01`.

- precision (number; default 2):
    Decimal precision for each segment's numeric input. Default: `2`.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):
    Current component size specification. Options are `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

- bordered (boolean; default True):
    Whether to show the border. When set to `True`, it is equivalent to `variant='outlined'`. Default: `True`.

- variant (a value equal to: 'outlined', 'borderless', 'filled', 'underlined'; optional):
    Variant type. Options are `'outlined'`, `'borderless'`, `'filled'`, `'underlined'`. Among them, `'outlined'` is equivalent to `bordered=True`, but with higher priority.

- placeholder (string; optional):
    Placeholder text for each segment's numeric input.

- readOnly (boolean; optional):
    Whether to render as read-only. Default: `False`.

- pureLegend (boolean; default False):
    Whether to render only the legend. Default: `False`.

- inputNumberStyle (dict; optional):
    Shared CSS styles for the segment numeric inputs.

- colorBlockStyle (dict; optional):
    CSS styles for the color block.

- colorBlockPosition (a value equal to: 'left', 'right'; default 'right'):
    Color block placement. Supported values: `'left'`, `'right'`. Default: `'right'`.

- colorBlockClickEvent (dict; optional):
    Segment color block click event.

    `colorBlockClickEvent` is a dict with keys:

    - color (string; optional):
        Color of the clicked color block.

    - range (list of numbers; optional):
        Range represented by the clicked color block.

    - timestamp (number; optional):
        Event timestamp.

- pureLegendLabelStyle (dict; optional):
    Shared CSS styles for segment values when `pureLegend=True`.

- batchPropsNames (list of strings; optional):
    Property names to include in [batch property monitoring](/batch-props-values).

- batchPropsValues (dict; optional):
    Values of the properties specified by `batchPropsNames`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
