- children (a list of or a singular dash component, string or number; optional):
    Component type, for nested elements.

- id (string; optional):
    Unique identifier for the component.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- className (string | dict; optional):
    Current component's CSS class name, supports [dynamic CSS](/advanced-classname).

- code (boolean; optional):
    Whether to render in code format.

- copyable (boolean; optional):
    Whether to enable the quick copy feature.

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- disabled (boolean; optional):
    Whether to render in a disabled state.

- ellipsis (dict; default False):
    Configuration for content truncation features, set to `False` to disable. Default value: `False`.

    `ellipsis` can be a boolean or a dict with keys:

    - suffix (string; optional):
        Custom suffix for content after truncation.

- italic (boolean; optional):
    Whether to render in italic format.

- key (string; optional):
    Update the `key` value of the current component to force a redraw of the component.

- keyboard (boolean; optional):
    Whether to render in keyboard format.

- loading_state (dict; optional):
    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is in a loading state.

    - prop_name (string; optional):
        Holds which property is currently loading.

- locale (a value equal to: 'zh-cn', 'en-us'; default 'zh-cn'):
    Component's text language, options include `'zh-cn'`, `'en-us'`. Default value: `'zh-cn'`.

- mark (boolean; optional):
    Whether to render in highlighted format.

- strikethrough (boolean; optional):
    Whether to render with a strikethrough.

- strong (boolean; optional):
    Whether to render in bold format.

- style (dict; optional):
    CSS styles for the current component.

- type (a value equal to: 'secondary', 'success', 'warning', 'danger'; optional):
    Set the special state of the content, options include `'secondary'`, `'success'`, `'warning'`, `'danger'`.

- underline (boolean; optional):
    Whether to render with an underline.
