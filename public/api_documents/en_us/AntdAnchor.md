- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- linkDict (optional):
    Hierarchical data structure for the directory.

- direction (a value equal to: 'vertical', 'horizontal'; default 'vertical'):
    Navigation direction. Subdirectories are not supported in `'horizontal'` mode. Supported values: `'vertical'`, `'horizontal'`. Default: `'vertical'`.

- align (a value equal to: 'left', 'right'; default 'right'):
    Anchor placement. Supported values: `'left'`, `'right'`. Default: `'right'`.

- containerId (string; optional):
    The ID of the target container for the anchor point.

- targetOffset (number; optional):
    The offset for the anchor point. Default is the same as the parameter offsetTop.

- affix (boolean; default True):
    Whether to enable the affix mode. Default value: `True`.

- bounds (number; default 5):
    The pixel margin for the anchor point. Default value: `5`.

- offsetTop (number; optional):
    Sets the specified pixel offset from the top of the window to trigger the anchoring effect.

- replace (boolean; default False):
    When `True`, browser back/forward navigation does not jump to the anchor. Default: `False`.

- currentAnchor (string; optional):
    Override the currently highlighted anchor link.

- clickedLink (dict; optional):
    Listens for click events on the anchor point node.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
