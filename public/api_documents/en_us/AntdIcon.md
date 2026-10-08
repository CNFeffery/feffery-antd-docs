- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- mode (a value equal to: 'default', 'iconfont'; default 'default'):
    Icon source: `'default'` for built-in icons or `'iconfont'` for Alibaba Iconfont. Default: `'default'`.

- icon (string; optional):
    Built-in icon name when `mode='default'`, or custom source icon name when `mode='iconfont'`.

- scriptUrl (string | list of strings; optional):
    One or more Alibaba Iconfont sources created on iconfont.cn when `mode='iconfont'`.

- nClicks (number; default 0):
    Number of times the icon has been clicked, used to monitor icon click behavior. Default value: `0`.

- debounceWait (number; default 0):
    Debounce delay for the icon click event listener, in milliseconds. Default value: `0`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
