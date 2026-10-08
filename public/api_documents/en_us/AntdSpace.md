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

    - item (dict; optional):
        CSS style for the child item container element.

- classNames (dict; optional):
    Fine-grained control over the CSS classes of child elements.

    `classNames` is a dict with keys:

    - item (string; optional):
        CSS class for the child item container element.

- align (a value equal to: 'start', 'end', 'center', 'baseline'; optional):
    Alignment of the elements. Supported values: `'start'`, `'end'`, `'center'`, `'baseline'`.

- direction (a value equal to: 'vertical', 'horizontal'; default 'horizontal'):
    Direction of arrangement, options include `'vertical'`, `'horizontal'`. Default value: `'horizontal'`.

- size (a value equal to: 'small', 'middle', 'large' | number; default 'small'):
    Gap between child elements. Use a preset size or a number for pixels. Supported values: `'small'`, `'middle'`, `'large'`. Default: `'small'`.

- addSplitLine (boolean; default False):
    Whether to add a separator line. Default value: `False`.

- customSplit (a list of or a singular dash component, string or number; optional):
    Custom separator line element.

- wrap (boolean; default False):
    Whether child elements automatically wrap to the next line, only effective when `direction='horizontal'`. Default value: `False`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
