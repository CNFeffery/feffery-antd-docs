- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- contentClassName (string | dict; optional):
    CSS class name for the content area. Supports [dynamic CSS classes](/advanced-classname).

- contentStyle (dict; optional):
    CSS styles for the content area.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- hideLabel (a list of or a singular dash component, string or number; optional):
    Collapse button label when expanded. Supports components.

- showLabel (a list of or a singular dash component, string or number; optional):
    Expand button label when collapsed. Supports components.

- labelPosition (a value equal to: 'left', 'right'; default 'left'):
    Position of the expand/collapse button. Supported values: `'left'`, `'right'`. Default: `'left'`.

- open (boolean; default False):
    Monitor or set the expanded state. Default: `False`.

- maxHeight (number; default 50):
    Maximum content height in pixels when collapsed. Default: `50`.

- transitionDuration (number; default 0.1):
    Duration of the expand/collapse transition in seconds. Default: `0.1`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
