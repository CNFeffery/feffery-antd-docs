- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- text (string; default ''):
    Content to copy.

- format (a value equal to: 'text/plain', 'text/html'; default 'text/plain'):
    Clipboard content MIME type. Supported values: `'text/plain'`, `text/html`. Default: `'text/plain'`.

- tooltips (list of a list of or a singular dash component, string or numbers | boolean; optional):
    Copy tooltips, in the form `[复制前内容, 复制后内容]` (before and after copying). Set to `False` to disable tooltips.

- beforeIcon (a list of or a singular dash component, string or number; optional):
    Icon displayed before copying. Supports components.

- afterIcon (a list of or a singular dash component, string or number; optional):
    Icon displayed after copying. Supports components.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
