- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- collapsed (boolean; optional):
    Whether the sidebar is currently collapsed.

- collapsedWidth (number; default 80):
    The pixel width displayed when collapsed. If set to 0, it will additionally render a special trigger component. Default value: `80`.

- collapsible (boolean; default False):
    Whether the sidebar can be collapsed. Default value: `False`.

- reverseArrow (boolean; default False):
    Whether to reverse the direction of the collapse arrow, typically used when the Sider is on the right side. Default value: `False`.

- theme (a value equal to: 'light', 'dark'; default 'dark'):
    The theme of the component, with options `'light'` or `'dark'`. Default value: `'dark'`.

- width (number | string; default 200):
    The pixel width of the sidebar. Default value: `200`.

- trigger (a list of or a singular dash component, string or number; optional):
    If set to `None`, it will not render the built-in special trigger component.

- breakpoint (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'; optional):
    The responsive breakpoint at which the sidebar automatically collapses.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
