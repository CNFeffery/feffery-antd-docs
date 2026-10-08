- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- code (boolean; optional):
    Whether to render in code format.

- copyable (boolean; optional):
    Whether to enable the quick copy feature.

- strikethrough (boolean; optional):
    Whether to render in strikethrough format.

- disabled (boolean; optional):
    Whether to render in a disabled state.

- mark (boolean; optional):
    Whether to render in highlighted format.

- strong (boolean; optional):
    Whether to render in bold format.

- italic (boolean; optional):
    Whether to render in italic format.

- underline (boolean; optional):
    Whether to render in underline format.

- keyboard (boolean; optional):
    Whether to render in keyboard format.

- type (a value equal to: 'secondary', 'success', 'warning', 'danger'; optional):
    Set special state format for content, options include `'secondary'`, `'success'`, `'warning'`, `'danger'`.

- ellipsis (dict; default False):
    Content ellipsis settings. Set to `False` to disable ellipsis. Default: `False`.

    `ellipsis` is a boolean | dict with keys:

    - suffix (string; optional):
        Custom suffix for content after truncation.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
