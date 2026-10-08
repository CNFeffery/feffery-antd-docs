- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- styles (dict; optional):
    Fine-grained CSS styles for child elements.

    `styles` is a dict with keys:

    - label (dict; optional):
        CSS styles for the label element.

    - content (dict; optional):
        CSS styles for the body element.

- classNames (dict; optional):
    Fine-grained CSS class names for child elements.

    `classNames` is a dict with keys:

    - label (string; optional):
        CSS class name for the label element.

    - content (string; optional):
        CSS class name for the body element.

- label (a list of or a singular dash component, string or number; optional):
    Title content. Supports components.

- span (number; default 1):
    Number of width units occupied. Default: `1`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
