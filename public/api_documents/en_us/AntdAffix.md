- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- offsetBottom (number; optional):
    Distance from the viewport bottom, in pixels, at which affixing starts.

- offsetTop (number; default 0):
    Distance from the viewport top, in pixels, at which affixing starts. Default: `0`.

- target (string; optional):
    ID of the container whose scroll events are monitored.

- affixed (boolean; optional):
    Whether the target is currently affixed.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
