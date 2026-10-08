- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- duration (number; default 0.45):
    Duration of the back-to-top animation in seconds. Default: `0.45`.

- visibilityHeight (number; default 400):
    Scroll distance in pixels at which the back-to-top button appears. Default: `400`.

- containerId (string; optional):
    ID of the container whose scroll events are monitored.

- containerSelector (string; optional):
    JavaScript selector for the scroll event container. containerId takes precedence.

- nClicks (number; default 0):
    Cumulative number of back-to-top button clicks. Default: `0`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
