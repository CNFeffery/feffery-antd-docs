- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- message (a list of or a singular dash component, string or number; optional):
    Main notification message.

- description (a list of or a singular dash component, string or number; optional):
    Notification description.

- type (a value equal to: 'default', 'success', 'error', 'info', 'warning'; default 'default'):
    Notification type. Supported values: `'default'`, `'success'`, `'error'`, `'info'`, `'warning'`. Default: `'default'`.

- placement (a value equal to: 'top', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'; default 'topRight'):
    Notification placement on the screen. Supported values: `'top'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`. Default: `'topRight'`.

- top (number; default 24):
    Distance from the top in pixels for notifications appearing at the top. Default: `24`.

- bottom (number; default 24):
    Distance from the bottom in pixels for notifications appearing at the bottom. Default: `24`.

- duration (number; default 4.5):
    Seconds before the notification closes automatically. Set to `None` to keep it open. Default: `4.5`.

- showProgress (boolean; default False):
    Whether to show the automatic close progress bar. Default: `False`.

- pauseOnHover (boolean; default True):
    Whether to pause the progress countdown on mouse hover when `showProgress=True`. Default: `True`.

- closable (boolean; default True):
    Whether to show the close button. Default: `True`.

- closeButton (dict; optional):
    Lower-right close button settings. No close button by default.

    `closeButton` is a dict with keys:

    - content (string; optional):
        Button content.

    - style (dict; optional):
        Button CSS style.

    - className (string; optional):
        Button CSS class name.

    - type (a value equal to: 'default', 'primary', 'ghost', 'dashed', 'link', 'text'; optional):
        Button type, options include `'default'`, `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`. Default value: `'default'`.

    - danger (boolean; optional):
        Whether the button uses the danger state. Default: `False`.

- stack (dict; default False):
    Whether multiple notifications automatically collapse into a stack. Default: `False`.

    `stack` is a boolean | dict with keys:

    - threshold (number; optional)
