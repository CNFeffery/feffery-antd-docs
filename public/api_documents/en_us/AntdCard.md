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

    - header (dict; optional):
        CSS styles for the card header.

    - title (dict; optional):
        CSS styles for the card title.

    - extra (dict; optional):
        CSS styles for the card's upper-right action area.

    - cover (dict; optional):
        CSS styles for the title cover.

    - body (dict; optional):
        CSS styles for the card body.

    - actions (dict; optional):
        CSS styles for the card footer action group.

- classNames (dict; optional):
    Fine-grained CSS class names for child elements.

    `classNames` is a dict with keys:

    - header (string; optional):
        CSS class name for the card header.

    - title (string; optional):
        CSS class name for the card title.

    - extra (string; optional):
        CSS class name for the card's upper-right action area.

    - cover (string; optional):
        CSS class name for the title cover.

    - body (string; optional):
        CSS class name for the card body.

    - actions (string; optional):
        CSS class name for the card footer action group.

- actions (a list of or a singular dash component, string or number; optional):
    Footer action area elements. Supports components.

- title (a list of or a singular dash component, string or number; optional):
    Title content. Supports components.

- extraLink (dict; optional):
    Additional upper-right card link settings.

    `extraLink` is a dict with keys:

    - content (string; optional):
        Link text.

    - href (string; optional):
        Link URL.

    - target (string; optional):
        Link navigation behavior.

    - className (string; optional):
        CSS class name for the link.

    - style (dict; optional):
        CSS styles for the link.

- extra (a list of or a singular dash component, string or number; optional):
    Additional upper-right card content. Supports components and takes precedence over `extraLink`.

- coverImg (dict; optional):
    Cover image settings.

    `coverImg` is a dict with keys:

    - src (string; optional):
        Image resource URL.

    - alt (string; optional):
        Image alternative text.

    - className (string; optional):
        CSS class name for the image.

    - style (dict; optional):
        CSS styles for the image.

- variant (a value equal to: 'outlined', 'borderless'; default 'outlined'):
    Card variant. Supported values: `'outlined'`, `'borderless'`. Default: `'outlined'`.

- hoverable (boolean; default False):
    Whether to show a special hover style. Default: `False`.

- size (a value equal to: 'default', 'small'; default 'default'):
    Card size. Supported values: `'default'`, `'small'`. Default: `'default'`.

- nClicks (number; default 0):
    Cumulative number of card clicks. Default: `0`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
