- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Elements displayed as carousel slides. Supports components.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- arrows (boolean; default False):
    Whether to show arrows. Default: `False`.

- autoplay (dict; default False):
    Whether the carousel advances automatically. A dictionary enables additional settings. Default: `False`.

    `autoplay` is a boolean | dict with keys:

    - dotDuration (boolean; optional):
        Whether to show progress on carousel indicators.

- dotPosition (a value equal to: 'top', 'bottom', 'left', 'right'; default 'bottom'):
    Panel indicator placement. Supported values: `'top'`, `'bottom'`, `'left'`, `'right'`. Default: `'bottom'`.

- easing (string; default 'linear'):
    Animation timing, equivalent to CSS `animation-timing-function`. Default: 'linear'.

- effect (a value equal to: 'scrollx', 'fade'; default 'scrollx'):
    Transition effect: `'scrollx'` or `'fade'`. Default: 'scrollx'.

- autoplaySpeed (number; default 3000):
    Carousel interval in milliseconds. Default: `3000`.

- speed (number; default 500):
    Carousel transition duration in milliseconds. Default: `500`.

- pauseOnHover (boolean; default False):
    Whether to pause the carousel on hover. Default: `False`.

- infinite (boolean; default True):
    Whether the carousel loops infinitely. Default: `True`.

- lazyLoad (boolean; default False):
    Whether carousel items use lazy loading. Default: `False`.

- slidesToShow (number; default 1):
    Number of slides displayed at a time. Default: `1`.

- slidesToScroll (number; default 1):
    Number of slides advanced per transition. Default: `1`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
