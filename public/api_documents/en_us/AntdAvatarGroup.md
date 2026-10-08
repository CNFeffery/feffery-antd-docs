- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    `AntdAvatar` components in the group.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- max (dict; optional):
    Maximum display count settings.

    `max` is a dict with keys:

    - count (number; optional):
        Maximum number of visible avatars; unrestricted by default.

    - style (dict; optional):
        CSS styles for the overflow avatar.

    - popover (dict; optional):
        Popup settings.

        `popover` is a dict with keys:

        - placement (a value equal to: 'top', 'bottom', 'right'; optional):
            Placement of the popover containing avatars beyond `maxCount`. Supported values: `'top'`, `'bottom'`, `'right'`. Default: `'top'`.

        - trigger (a value equal to: 'hover', 'click'; optional):
            Trigger for the popover containing avatars beyond `maxCount`. Supported values: `'hover'`, `'click'`. Default: `'hover'`.

- size (dict; default 'default'):
    Shared avatar size. Use a number for pixels or a preset size; supports responsive breakpoints. Supported values: `'large'`, `'small'`, `'default'`. Default: `'default'`.

    `size` is a number | a value equal to: 'large', 'small', 'default'
    | dict with keys:

    - xs (number; optional)

    - sm (number; optional)

    - md (number; optional)

    - lg (number; optional)

    - xl (number; optional)

    - xxl (number; optional)

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
