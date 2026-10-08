- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- content (a list of or a singular dash component, string or number; optional):
    Component type, label content.

- icon (a list of or a singular dash component, string or number; optional):
    Tag prefix icon. Supports components.

- color (string; optional):
    Tag color, using a preset theme or any valid CSS color.

- href (string; optional):
    URL opened when the tag is clicked.

- target (string; default '_blank'):
    Link navigation behavior for the tag.

- bordered (boolean; default True):
    Whether to render borders. Default: `True`.

- closeIcon (boolean; default False):
    Whether to render a close button. Default: `False`.

- closeCounts (number; default 0):
    Cumulative number of clicks on the close button when `closeIcon=True`. Default: `0`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
