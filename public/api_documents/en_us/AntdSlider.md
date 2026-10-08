- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- styles (dict; optional):
    Fine-grained CSS styles for child elements.

    `styles` is a dict with keys:

    - root (dict; optional):
        CSS styles for the root element.

    - track (dict; optional):
        CSS styles for an individual track between handles in range mode.

    - tracks (dict; optional):
        CSS styles for all selected tracks in range mode.

    - rail (dict; optional):
        CSS styles for the slider rail.

    - handle (dict; optional):
        CSS styles for the slider handle.

- classNames (dict; optional):
    Fine-grained CSS class names for child elements.

    `classNames` is a dict with keys:

    - root (string; optional):
        CSS class name for the root element.

    - track (string; optional):
        CSS class name for an individual track between handles in range mode.

    - tracks (string; optional):
        CSS class name for all selected tracks in range mode.

    - rail (string; optional):
        CSS class name for the slider rail.

    - handle (string; optional):
        CSS class name for the slider handle.

- name (string; optional):
    Used with `AntdForm` for batch value collection/control, serving as the field name of the current form item, with `id` as the default value.

- enableBatchControl (boolean; default True):
    Controls whether the current component participates in the effective `AntdForm` batch value collection/control feature. Default: `True`.

- vertical (boolean; default False):
    Whether to display the slider vertically. Default: `False`.

- range (dict; default False):
    Whether to use range selection mode.

    `range` is a boolean | dict with keys:

    - editable (boolean; optional):
        Whether slider nodes can be added and removed dynamically. Default: `False`.

    - minCount (number; optional):
        Minimum number of slider nodes when dynamic node editing is enabled. Default: `0`.

    - maxCount (number; optional):
        Maximum number of slider nodes when dynamic node editing is enabled.

- min (number; default 0):
    Minimum slider value. Default: `0`.

- max (number; default 100):
    Maximum slider value. Default: `100`.

- step (number; default 1):
    Slider step size.

- marks (dict with strings as keys and values of type a list of or a singular dash component, string or number; optional):
    Tick marks for specific values.

- tooltipVisible (boolean; optional):
    Slider value tooltip visibility: `True` always shows it; `False` always hides it.

- tooltipPrefix (string; default ''):
    Prefix for the slider value tooltip.

- tooltipSuffix (string; default ''):
    Suffix for the slider value tooltip.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- value (number | list of numbers; optional):
    Listen to or set the selected value(s).

- defaultValue (number | list of numbers; optional):
    Initial selected value(s).

- autoFocus (boolean; default False):
    Whether the slider receives focus automatically when mounted. Default: `False`.

- popupContainer (a value equal to: 'parent', 'body'; default 'body'):
    Anchoring strategy for the related popup layer. Options are `'parent'`, `'body'`. Default: `'body'`.

- readOnly (boolean; default False):
    Whether to render as read-only. Default: `False`.

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
