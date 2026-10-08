- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- styles (dict; optional):
    Fine-grained CSS styles for child elements.

    `styles` is a dict with keys:

    - root (dict; optional):
        CSS styles for the root element.

    - image (dict; optional):
        CSS styles for the icon element.

    - description (dict; optional):
        CSS styles for the description element.

    - footer (dict; optional):
        CSS styles for the footer element.

- classNames (dict; optional):
    Fine-grained CSS class names for child elements.

    `classNames` is a dict with keys:

    - root (string; optional):
        CSS class name for the root element.

    - image (string; optional):
        CSS class name for the icon element.

    - description (string; optional):
        CSS class name for the description element.

    - footer (string; optional):
        CSS class name for the footer element.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- description (a list of or a singular dash component, string or number | boolean; optional):
    Description content.

- image (string | a value equal to: 'default', 'simple'; default 'default'):
    Status image URL, or a built-in image. Supported values: `'default'`, `'simple'`. Default: `'default'`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
