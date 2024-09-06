- children (a list of or a singular dash component, string or number; optional):
    Component type for nested elements.

- id (string; optional):
    Unique identifier for the component.

- aria-* (string; optional):
    Wildcard for attributes in the `aria-*` format.

- breakpoint (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'; optional):
    The responsive breakpoint at which the sidebar automatically collapses.

- className (string | dict; optional):
    CSS class name for the current component, supporting [dynamic CSS](/advanced-classname).

- collapsed (boolean; optional):
    Whether the sidebar is currently collapsed.

- collapsedWidth (number; default 80):
    The pixel width displayed when collapsed. If set to 0, it will additionally render a special trigger component. Default value: `80`.

- collapsible (boolean; default False):
    Whether the sidebar can be collapsed. Default value: `False`.

- data-* (string; optional):
    Wildcard for attributes in the `data-*` format.

- key (string; optional):
    Updates the `key` value of the current component to force a re-render.

- loading_state (dict; optional):
    The `loading_state` is a dictionary with the following keys:
    - component_name (string; optional):
        Holds the name of the component that is loading.
    - is_loading (boolean; optional):
        Determines whether the component is loading.
    - prop_name (string; optional):
        Holds which property is loading.

- reverseArrow (boolean; default False):
    Whether to reverse the direction of the collapse arrow, typically used when the Sider is on the right side. Default value: `False`.

- style (dict; optional):
    CSS styles for the current component.

- theme (a value equal to: 'light', 'dark'; default 'dark'):
    The theme of the component, with options `'light'` or `'dark'`. Default value: `'dark'`.

- trigger (a list of or a singular dash component, string or number; optional):
    If set to `None`, it will not render the built-in special trigger component.

- width (number | string; default 200):
    The pixel width of the sidebar. Default value: `200`.
