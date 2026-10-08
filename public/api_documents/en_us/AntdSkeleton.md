- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- loading (boolean; default False):
    Whether the component is loading.

- active (boolean; default False):
    Whether to show animation. Default: `False`.

- delay (number; default 0):
    Delay in milliseconds before showing the loading indicator. Default: `0`.

- avatar (dict; default False):
    Avatar placeholder settings. Set to `False` to hide the avatar. Default: `False`.

    `avatar` is a boolean | dict with keys:

    - active (boolean; optional):
        Whether the avatar placeholder is animated. Default: `False`.

    - shape (a value equal to: 'circle', 'square'; optional):
        Avatar placeholder shape. Supported values: `'circle'`, `'square'`.

    - size (number | a value equal to: 'large', 'small', 'default'; optional):
        Avatar placeholder size. Use a number for pixels or a preset size. Supported values: `'large'`, `'small'`, `'default'`. Default: `'default'`.

- paragraph (dict; default True):
    Paragraph placeholder settings. Set to `False` to hide it. Default: `True`.

    `paragraph` is a boolean | dict with keys:

    - rows (number; optional):
        Number of paragraph placeholder rows.

    - width (number | string | list of number | strings; optional):
        Paragraph placeholder width. An *int* or *string* sets the last row width; a *list* sets widths for individual rows.

- title (dict; default True):
    Whether to show the title placeholder. Default: `True`.

    `title` is a boolean | dict with keys:

    - width (number | string; optional):
        Width of the title placeholder.

- round (boolean; default False):
    Whether paragraph and title placeholders have rounded corners. Default: `False`.

- debug (boolean; default False):
    Whether debug mode logs `prop` information to the developer console on each animation load. Default: `False`.

- listenPropsMode (a value equal to: 'default', 'exclude', 'include'; default 'default'):
    Monitoring mode. Supported values: `'default'`, `'exclude'`, `'include'`. Default: `'default'`.

- excludeProps (list of strings; optional):
    Callback targets excluded from monitoring when `listenPropsMode='exclude'`, in the form `['组件id1.组件属性1', '组件id2.组件属性2', ...]` (component ID and property name pairs).

- includeProps (list of strings; optional):
    Callback targets included in monitoring when `listenPropsMode='include'`, in the form `['组件id1.组件属性1', '组件id2.组件属性2', ...]` (component ID and property name pairs).

- manual (boolean; default False):
    Whether loading is controlled manually through `loading`, independently of callbacks involving child elements. Default: `False`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
