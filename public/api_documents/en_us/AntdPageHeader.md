- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- title (a list of or a singular dash component, string or number; optional):
    Component type, content for the page header title.

- subTitle (a list of or a singular dash component, string or number; optional):
    Component type, content for the page header subtitle.

- showBackIcon (boolean; default True):
    Whether to render the back button. Default value: `True`.

- historyBackDisabled (boolean; default False):
    Whether to disable the function of going back to the previous address by clicking the back button. Default value: `False`.

- backClicks (number; default 0):
    Number of times the back button has been clicked, used to monitor the behavior of back button clicks. Default value: `0`.

- ghost (boolean; default False):
    Whether to enable the transparent background mode. Default value: `False`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
