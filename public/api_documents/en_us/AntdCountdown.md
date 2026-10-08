- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- format (string; optional):
    Date/time display format. See [reference](https://day.js.org/docs/en/display/format). For example, `HH:mm:ss` represents `时:分:秒` (hours:minutes:seconds).

- value (string; optional):
    Target deadline string, matching `valueFormat`.

- valueFormat (string; default 'YYYY-MM-DD hh:mm:ss'):
    Date/time parsing format for `value`. See [reference](https://day.js.org/docs/en/display/format). Default: `'YYYY-MM-DD hh:mm:ss'`.

- prefix (a list of or a singular dash component, string or number; optional):
    Value prefix. Supports components.

- suffix (a list of or a singular dash component, string or number; optional):
    Value suffix. Supports components.

- title (a list of or a singular dash component, string or number; optional):
    Title content. Supports components.

- titleTooltip (string; optional):
    Additional tooltip for the title.

- valueStyle (dict; optional):
    CSS styles for the displayed value.

- finishEvent (dict; optional):
    Countdown completion event.

    `finishEvent` is a dict with keys:

    - timestamp (number; optional):
        Event timestamp.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
