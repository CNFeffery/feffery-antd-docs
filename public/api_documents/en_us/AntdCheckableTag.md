- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- content (a list of or a singular dash component, string or number; optional):
    Component type, label content.

- checkedContent (a list of or a singular dash component, string or number; optional):
    Tag content in the selected state. Supports components.

- unCheckedContent (a list of or a singular dash component, string or number; optional):
    Tag content in the unselected state. Supports components.

- checked (boolean; default False):
    Monitor or set whether the tag is selected. Default: `False`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
