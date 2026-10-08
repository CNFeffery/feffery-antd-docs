- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- steps (list of dicts; required):
    `steps` is a list of dictionaries with keys:

    `steps` is a list of dicts with keys:

    - title (a list of or a singular dash component, string or number; required):
        The title of the step.

    - subTitle (a list of or a singular dash component, string or number; optional):
        The sub-title of the step.

    - description (a list of or a singular dash component, string or number; optional):
        The description content of the step.

    - icon (a list of or a singular dash component, string or number; optional):
        Custom icon for the step.

    - disabled (boolean; optional):
        Whether the current step is disabled.

    - status (a value equal to: 'wait', 'process', 'finish', 'error'; optional):
        Force the status of the current step, same as the status parameter.

- current (number; default 0):
    The current step number. Default value: `0`.

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    The display direction of the step bar, options include `'horizontal'`, `'vertical'`. Default value: `'horizontal'`.

- labelPlacement (a value equal to: 'horizontal', 'vertical'; optional):
    The display direction of the label content, options include `'horizontal'`, `'vertical'`.

- progressDot (boolean; default False):
    Whether to render as a dotted step bar. Default value: `False`.

- size (a value equal to: 'default', 'small'; default 'default'):
    The size specification of the step bar, options include `'default'`, `'small'`. Default value: `'default'`.

- status (a value equal to: 'wait', 'process', 'finish', 'error'; default 'process'):
    The status of the step bar, options include `'wait'`, `'process'`, `'finish'`, `'error'`. Default value: `'process'`.

- type (a value equal to: 'default', 'navigation', 'inline'; default 'default'):
    The type of the step bar, options include `'default'`, `'navigation'`, `'inline'`. Default value: `'default'`.

- allowClick (boolean; default False):
    Whether the step can be switched by clicking. Default value: `False`.

- responsive (boolean; default True):
    Whether to automatically force vertical display when the page width is less than 532px. Default value: `True`.

- percent (number; optional):
    The current step progress, the value should be between 0 and 100, suitable for a regular step bar.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
