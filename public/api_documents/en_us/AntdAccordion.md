- id (string; optional):
  Component unique id.

- key (string; optional):
  Update the `key` value of the current component to force a re-render of the component.

- className (string | dict; optional):
  CSS class name of the current component, supports [dynamic css](/advanced-classname).

- styles (dict; optional):
  Fine-grained control of child element CSS styles.

  `styles` is a dict with keys:

  - header (dict; optional):
    CSS styles for the header element.

  - body (dict; optional):
    CSS styles for the body element.

- classNames (dict; optional):
  Fine-grained control of child element CSS class names.

  `classNames` is a dict with keys:

  - header (string; optional):
    CSS class name for the header element.

  - body (string; optional):
    CSS class name for the body element.

- items (list of dicts; optional):
  Define accordion sub-items.

  `items` is a list of dicts with keys:

  - children (a list of or a singular dash component, string or number; optional):
    Inner elements of the current sub-item.

  - className (string | dict; optional):
    CSS class name of the current sub-item, supports [dynamic css](/advanced-classname).

  - style (dict; optional):
    CSS styles of the current sub-item.

  - key (string | number; required):
    Required, unique key value of the current sub-item.

  - collapsible (a value equal to: 'header', 'disabled', 'icon'; optional):
    Collapse trigger method of the current sub-item. Options are `'header'`, `'disabled'`, `'icon'`.

  - title (a list of or a singular dash component, string or number; optional):
    Title element of the current sub-item.

  - extra (a list of or a singular dash component, string or number; optional):
    Extra element at the top right corner of the current sub-item.

  - showArrow (boolean; optional):
    Whether to display the arrow icon of the current accordion item. Default: `True`.

  - forceRender (boolean; optional):
    Whether to force render inner elements. Default: `False`.

- accordion (boolean; default True):
  Whether to enable accordion mode. Default: `True`.

- activeKey (string | list of strings | number | list of numbers; optional):
  Listen to or set the key value of the accordion item currently expanded.

- defaultActiveKey (string | list of strings | number | list of numbers; optional):
  Set the key value of the accordion item initially expanded.

- bordered (boolean; default True):
  Whether to render borders. Default: `True`.

- size (a value equal to: 'large', 'middle', 'small'; default 'middle'):
  Component size specification. Options are `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

- collapsible (a value equal to: 'header', 'disabled', 'icon'; optional):
  Set the collapse trigger method for all sub-items. Options are `'header'`, `'disabled'`, `'icon'`.

- expandIconPosition (a value equal to: 'left', 'right'; default 'left'):
  Set the position of the collapse icon. Options are `'left'`, `'right'`.

- ghost (boolean; default False):
  Whether to enable transparent borderless mode. Default: `False`.

- data-_ (string; optional):
  Wildcard attributes in `data-_` format.

- aria-_ (string; optional):
  Wildcard attributes in `aria-_` format.
