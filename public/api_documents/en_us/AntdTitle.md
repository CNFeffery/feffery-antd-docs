- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- id (string; optional):
    Unique ID for the component.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- className (string | dict; optional):
    CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

- code (boolean; optional):
    Whether to render in code format.

- copyable (boolean; optional):
    Whether to enable the quick copy feature.

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- disabled (boolean; optional):
    Whether to render in a disabled state.

- italic (boolean; optional):
    Whether to render in italic format.

- key (string; optional):
    Update the `key` value for the current component, which can force a redraw of the current component.

- keyboard (boolean; optional):
    Whether to render in keyboard format.

- level (number; default 1):
    Heading level, options include `1`, `2`, `3`, `4`, `5`. Default value: `1`.

- loading_state (dict; optional):
    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de'; default 'zh-cn'):
    Component text language, options include `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German).
    Default value: `'zh-cn'`.

- mark (boolean; optional):
    Whether to render in highlighted format.

- strikethrough (boolean; optional):
    Whether to render in strikethrough format.

- strong (boolean; optional):
    Whether to render in bold format.

- style (dict; optional):
    CSS styles for the current component.

- type (a value equal to: 'secondary', 'success', 'warning', 'danger'; optional):
    Set special state format for content, options include `'secondary'`, `'success'`, `'warning'`, `'danger'`.

- underline (boolean; optional):
    Whether to render in underline format.
