- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Nested description items. Supports components.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- styles (dict; optional):
    Fine-grained CSS styles for child elements.

    `styles` is a dict with keys:

    - root (dict; optional):
        CSS styles for the root element.

    - header (dict; optional):
        CSS styles for the header element.

    - title (dict; optional):
        CSS styles for the title element.

    - extra (dict; optional):
        CSS styles for the additional content.

    - label (dict; optional):
        CSS styles for the label element.

    - content (dict; optional):
        CSS styles for the body element.

- classNames (dict; optional):
    Fine-grained CSS class names for child elements.

    `classNames` is a dict with keys:

    - root (string; optional):
        CSS class name for the root element.

    - header (string; optional):
        CSS class name for the header element.

    - title (string; optional):
        CSS class name for the title element.

    - extra (string; optional):
        CSS class name for the additional content.

    - label (string; optional):
        CSS class name for the label element.

    - content (string; optional):
        CSS class name for the body element.

- items (list of dicts; optional):
    Description list item definitions. Takes precedence over `children`.

    `items` is a list of dicts with keys:

    - label (a list of or a singular dash component, string or number; optional):
        Child item title. Supports components.

    - span (number | a value equal to: 'filled'; optional):
        Width units occupied by this item. Set to `'filled'` to fill the remaining space in the row. Default: `1`.

    - children (a list of or a singular dash component, string or number; optional):
        Child item content. Supports components.

    - style (dict; optional):
        CSS styles for the child item.

    - className (string; optional):
        CSS class name for the child item.

- title (a list of or a singular dash component, string or number; optional):
    Title content. Supports components.

- column (dict; default 3):
    Number of description fields per row. Supports responsive settings. Default: `3`.

    `column` is a number | dict with keys:

    - xxl (number; optional)

    - xl (number; optional)

    - lg (number; optional)

    - md (number; optional)

    - sm (number; optional)

    - xs (number; optional)

- bordered (boolean; default False):
    Whether to show a border. Default: `False`.

- size (a value equal to: 'small', 'default', 'large'; default 'default'):
    Overall size. Supported values: `'small'`, `'default'`, `'large'`. Default: `'default'`.

- layout (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    Layout direction. Supported values: `'horizontal'`, `'vertical'`. Default: `'horizontal'`.

- extra (a list of or a singular dash component, string or number; optional):
    Upper-right action area elements. Supports components.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
