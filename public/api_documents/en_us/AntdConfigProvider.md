- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- algorithm (a value equal to: 'default', 'dark', 'compact' | list of a value equal to: 'default', 'dark', 'compact's; default 'default'):
    Theme algorithms for nested components. Multiple algorithms can be combined. Supported values: `'default'`, `'dark'`, `'compact'`. Default: `'default'`.

- cssVar (dict; optional):
    Whether to enable `CSS` variables. See https://ant-design.antgroup.com/docs/react/css-variables. Default: `False`.

    `cssVar` is a boolean | dict with keys:

    - prefix (string; optional)

    - key (string; optional)

- useOldTheme (a value equal to: 'default', 'dark'; optional):
    Use the theme styles from before version `0.3.x`. Supported values: `'default'`, `'dark'`.

- primaryColor (string; optional):
    Primary theme color.

- componentDisabled (boolean; optional):
    Whether to force all descendant components into the disabled state.

- componentSize (a value equal to: 'small', 'middle', 'large'; optional):
    Override descendant component sizes. `'default'` is an alias for `'middle'`. Supported values: `'small'`, `'middle'`, `'large'`.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; optional):
    Override descendant component languages: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'ru-ru'` (Russian), or `'fr-fr'` (French). This setting takes precedence over descendant components' own `locale` values. Custom content is not translated automatically.

- wavesDisabled (boolean; default False):
    Whether to disable the ripple effect on nested components. Default: `False`.

- token (dict; optional):
    `design token` settings.

    `token` is a dict with keys:

    - motion (boolean; optional):
        Whether animations are enabled. Default: `True`.

- componentsToken (dict; optional):
    Component-specific `design token` settings.

    `componentsToken` is a dict with strings as keys and values of
    type dict with keys:

    - algorithm (boolean; optional):
        Whether derived styles are calculated automatically. Default: `False`.

- compatibilityMode (boolean; default False):
    Whether to enable compatibility with `Chromium` version `88` and earlier. Default: `False`.

- enableLayer (boolean; default False):
    Whether to lower style priority using CSS layers. Default: `False`.
