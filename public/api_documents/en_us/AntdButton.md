
- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Updates the `key` value of the current component, which can force a redraw of the current component.

- children (a list of or a singular dash component, string or number; optional):
    Component type, the embedded element inside the button.

- style (dict; optional):
    The CSS style of the current component.

- className (string | dict; optional):
    The CSS class name of the current component, supports [dynamic CSS class names](/advanced-classname).

- styles (dict; optional):
    Fine-grained control over the CSS styles of child elements.

    `styles` is a dict with keys:

    - icon (dict; optional):
        The CSS style for the button icon element.

- classNames (dict; optional):
    Fine-grained control over the CSS class names of child elements.

    `classNames` is a dict with keys:

    - icon (string; optional):
        The CSS class name for the button icon element.

- loadingChildren (a list of or a singular dash component, string or number; optional):
    Component type, the embedded element displayed when the button is in a loading state.

- type (a value equal to: 'default', 'primary', 'dashed', 'link', 'text'; default 'default'):
    The type of button, with options `'default'`, `'primary'`, `'dashed'`, `'link'`, `'text'`.
    Default value: `'default'`.

- href (string; optional):
    The link address for the button to jump to when clicked.

- target (string; default '_blank'):
    The method of the link to jump when the button is clicked. Default value: `'_blank'`.

- autoInsertSpace (boolean; default True):
    Whether to insert a space between two Chinese characters in the button. Default value: `True`.

- block (boolean; default False):
    Whether the button is rendered as a block-level element (width fills the parent container). Default value: `False`.

- danger (boolean; default False):
    Whether the button presents a danger style. Default value: `False`.

- disabled (boolean; default False):
    Whether the button presents a disabled state. Default value: `False`.

- ghost (boolean; default False):
    Whether the button presents a transparent background state. Default value: `False`.

- shape (a value equal to: 'default', 'circle', 'round'; default 'default'):
    The shape of the button, with options `'default'`, `'circle'`, `'round'`. Default value: `'default'`.

- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):
    The size specification of the button, with options `'small'`, `'middle'`, `'large'`. Default value: `'middle'`.

- nClicks (number; default 0):
    The cumulative number of button clicks, used to monitor button click behavior. Default value: `0`.

- clickExecuteJsString (string; optional):
    The string of JavaScript code to be executed when the button is clicked.

- debounceWait (number; default 0):
    The debounce delay for the button click event listener, in milliseconds. Default value: `0`.

- icon (a list of or a singular dash component, string or number; optional):
    Component type, the prefix icon element embedded before the button.

- iconPosition (a value equal to: 'start', 'end'; default 'start'):
    The position of the button icon component, with options `'start'`, `'end'`. Default value: `'start'`.

- loading (boolean; optional):
    Whether the button presents a loading state. Default value: `False`.

- autoSpin (boolean; default False):
    Whether the current button automatically enters a loading state after each click. Default value: `False`.

- motionType (a value equal to: 'happy-work'; optional):
    The additional special interaction type of the button, with options `'happy-work'`.

- color (a value equal to: 'default', 'primary', 'danger'; optional):
    The color style of the button, with options `'default'`, `'primary'`, `'danger'`.

- variant (a value equal to: 'outlined', 'dashed', 'solid', 'filled', 'text', 'link'; optional):
    The variant type, with options `'outlined'`, `'dashed'`, `'solid'`, `'filled'`, `'text'`, `'link'`.

- title (string; optional):
    The native button title attribute.

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading.
