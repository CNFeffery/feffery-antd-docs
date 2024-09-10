- id (string; optional):
    Unique identifier for the component.

- allowClick (boolean; default False):
    Whether the step can be switched by clicking. Default value: `False`.

- aria-* (string; optional):
    Wildcard for `aria-*` formatted attributes.

- className (string | dict; optional):
    The current component's CSS class name, supports [dynamic CSS class names](/advanced-classname).

- current (number; default 0):
    The current step number. Default value: `0`.

- data-* (string; optional):
    Wildcard for `data-*` formatted attributes.

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    The display direction of the step bar, options include `'horizontal'`, `'vertical'`. Default value: `'horizontal'`.

- key (string; optional):
    Update the `key` value of the current component to force a redraw of the component.

- labelPlacement (a value equal to: 'horizontal', 'vertical'; optional):
    The display direction of the label content, options include `'horizontal'`, `'vertical'`.

- loading_state (dict; optional):
    `loading_state` is a dictionary with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- percent (number; optional):
    The current step progress, the value should be between 0 and 100, suitable for a regular step bar.

- progressDot (boolean; default False):
    Whether to render as a dotted step bar. Default value: `False`.

- responsive (boolean; default True):
    Whether to automatically force vertical display when the page width is less than 532px. Default value: `True`.

- size (a value equal to: 'default', 'small'; default 'default'):
    The size specification of the step bar, options include `'default'`, `'small'`. Default value: `'default'`.

- status (a value equal to: 'wait', 'process', 'finish', 'error'; default 'process'):
    The status of the step bar, options include `'wait'`, `'process'`, `'finish'`, `'error'`.
    Default value: `'process'`.

- steps (list of dicts; required):
    Required, defines the data structure of the step content.

    `steps` is a list of dictionaries with keys:

    - description (a list of or a singular dash component, string or number; optional):
        The description content of the step.

    - disabled (boolean; optional):
        Whether the current step is disabled.

    - icon (a list of or a singular dash component, string or number; optional):
        Custom icon for the step.

    - status (a value equal to: 'wait', 'process', 'finish', 'error'; optional):
        Force the status of the current step, same as the status parameter.

    - subTitle (a list of or a singular dash component, string or number; optional):
        The sub-title of the step.

    - title (a list of or a singular dash component, string or number; required):
        The title of the step.

- style (dict; optional):
    The current component's CSS styles.

- type (a value equal to: 'default', 'navigation', 'inline'; default 'default'):
    The type of the step bar, options include `'default'`, `'navigation'`, `'inline'`. Default value: `'default'`.
