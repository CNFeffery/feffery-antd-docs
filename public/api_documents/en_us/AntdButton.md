- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, the embedded element inside the button.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- styles (dict; optional):
    Fine-grained CSS styles for child elements.

    `styles` is a dict with keys:

    - icon (dict; optional):
        The CSS style for the button icon element.

- classNames (dict; optional):
    Fine-grained CSS class names for child elements.

    `classNames` is a dict with keys:

    - icon (string; optional):
        The CSS class name for the button icon element.

- loadingChildren (a list of or a singular dash component, string or number; optional):
    Component type, the embedded element displayed when the button is in a loading state.

- type (a value equal to: 'default', 'primary', 'dashed', 'link', 'text'; default 'default'):
    The type of button, with options `'default'`, `'primary'`, `'dashed'`, `'link'`, `'text'`. Default value: `'default'`.

- href (string; optional):
    URL to redirect to when the button is clicked.

- target (string; default '_blank'):
    Method of opening the link when the button is clicked. Default value: `'_blank'`.

- autoInsertSpace (boolean; default True):
    Whether to insert a space between two Chinese characters in the button. Default value: `True`.

- block (boolean; default False):
    Whether the button is rendered as a block-level element (width fills the parent container). Default value: `False`.

- danger (boolean; default False):
    Whether the button displays a danger style. Default value: `False`.

- disabled (boolean; default False):
    Whether the button presents a disabled state. Default value: `False`.

- ghost (boolean; default False):
    Whether the button presents a transparent background state. Default value: `False`.

- shape (a value equal to: 'default', 'circle', 'round'; default 'default'):
    The shape of the button, with options `'default'`, `'circle'`, `'round'`. Default value: `'default'`.

- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):
    Button size specification, options include `'small'`, `'middle'`, `'large'`. Default value: `'middle'`.

- nClicks (number; default 0):
    Number of times the button has been clicked, used to monitor button click behavior. Default value: `0`.

- clickExecuteJsString (string; optional):
    The string of JavaScript code to be executed when the button is clicked.

- debounceWait (number; default 0):
    The debounce delay for the button click event listener, in milliseconds. Default value: `0`.

- icon (a list of or a singular dash component, string or number; optional):
    Component type, prefix icon element nested within the button.

- iconPosition (a value equal to: 'start', 'end'; default 'start'):
    The position of the button icon component, with options `'start'`, `'end'`. Default value: `'start'`.

- loading (boolean; optional):
    Whether the button presents a loading state. Default value: `False`.

- autoSpin (boolean; default False):
    Whether the current button automatically enters a loading state after each click. Default value: `False`.

- motionType (a value equal to: 'happy-work'; optional):
    The additional special interaction type of the button, with options `'happy-work'`.

- color (a value equal to: 'default', 'primary', 'danger', 'blue', 'purple', 'cyan', 'green', 'magenta', 'pink', 'red', 'orange', 'yellow', 'volcano', 'geekblue', 'lime', 'gold'; optional):
    Button color scheme. Supports `'default'`, `'primary'`, `'danger'`, and built-in colors `'blue'`, `'purple'`, `'cyan'`, `'green'`, `'magenta'`, `'pink'`, `'red'`, `'orange'`, `'yellow'`, `'volcano'`, `'geekblue'`, `'lime'`, and `'gold'`.

- variant (a value equal to: 'outlined', 'dashed', 'solid', 'filled', 'text', 'link'; optional):
    The variant type, with options `'outlined'`, `'dashed'`, `'solid'`, `'filled'`, `'text'`, `'link'`.

- title (string; optional):
    The native button title attribute.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
