- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- steps (list of dicts; optional):
    Tour step definitions.

    `steps` is a list of dicts with keys:

    - targetId (string; optional):
        Target element ID for this step. Takes precedence over `targetSelector`.

    - targetSelector (string; optional):
        JavaScript code string locating the target element for this tour step.

    - arrow (dict; optional):
        Arrow settings for this tour step. Default: `True`.

        `arrow` is a boolean

      Or dict with keys:

        - pointAtCenter (boolean; optional):

            Whether the arrow points to the target's center.

    - cover (a list of or a singular dash component, string or number; optional):
        Cover content for this tour step. Supports components.

    - title (a list of or a singular dash component, string or number; optional):
        Title for this tour step. Supports components.

    - description (a list of or a singular dash component, string or number; optional):
        Description for this tour step. Supports components.

    - placement (a value equal to: 'center', 'left', 'leftTop', 'leftBottom', 'right', 'rightTop', 'rightBottom', 'top', 'topLeft', 'topRight', 'bottom', 'bottomLeft', 'bottomRight'; optional):
        Position of the tour popup relative to its target element. Supported values: `'center'`, `'left'`, `'leftTop'`, `'leftBottom'`, `'right'`, `'rightTop'`, `'rightBottom'`, `'top'`, `'topLeft'`, `'topRight'`, `'bottom'`, `'bottomLeft'`, `'bottomRight'`.

    - mask (dict; optional):
        Mask settings for this tour step. Default: `True`.

        `mask` is a boolean | dict with keys:

        - style (dict; optional):

            CSS styles for this step's mask.

        - color (string; optional):

            Mask color for this step.

    - type (a value equal to: 'default', 'primary'; optional):
        Tour step popup type. Supported values: `'default'`, `'primary'`. Default: `'default'`.

    - nextButtonProps (dict; optional):
        Next button settings for this tour step.

        `nextButtonProps` is a dict with keys:

        - children (a list of or a singular dash component, string or number; optional):
            Component type, the embedded element inside the button.

    - prevButtonProps (dict; optional):
        Previous button settings for this tour step.

        `prevButtonProps` is a dict with keys:

        - children (a list of or a singular dash component, string or number; optional):
            Component type, the embedded element inside the button.

- arrow (dict; default True):
    Shared tour popup arrow settings. Default: `True`.

    `arrow` is a boolean | dict with keys:

    - pointAtCenter (boolean; optional):
        Whether the arrow points to the target's center.

- placement (a value equal to: 'center', 'left', 'leftTop', 'leftBottom', 'right', 'rightTop', 'rightBottom', 'top', 'topLeft', 'topRight', 'bottom', 'bottomLeft', 'bottomRight'; default 'bottom'):
    Shared tour popup placement relative to the target element. Supported values: `'center'`, `'left'`, `'leftTop'`, `'leftBottom'`, `'right'`, `'rightTop'`, `'rightBottom'`, `'top'`, `'topLeft'`, `'topRight'`, `'bottom'`, `'bottomLeft'`, `'bottomRight'`. Default: `'bottom'`.

- mask (dict; default True):
    Shared tour popup mask settings. Default: `True`.

    `mask` is a boolean | dict with keys:

    - style (dict; optional):
        CSS styles for the mask.

    - color (string; optional):
        Mask color.

- type (a value equal to: 'default', 'primary'; default 'default'):
    Shared tour step popup type. Supported values: `'default'`, `'primary'`. Default: `'default'`.

- open (boolean; default False):
    Monitor or set whether the tour is open. Default: `False`.

- current (number; optional):
    Monitor or set the current tour step index.

- zIndex (number; default 1001):
    Tour z-index. Default: `1001`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
