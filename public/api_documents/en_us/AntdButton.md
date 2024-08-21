- children (a list of or a singular dash component, string or number; optional):
  Component type, embedded element within the button.
- id (string; optional):
  Unique identifier for the component.
- aria-* (string; optional):
  Wildcard for attributes in the `aria-*` format.
- autoInsertSpace (boolean; default True):
  Whether to insert a space between two Chinese characters in the button. Default value: `True`.
- autoSpin (boolean; default False):
  Whether the current button automatically enters a loading state after each click. Default value: `False`.
- block (boolean; default False):
  Whether the button is rendered as a block-level element (width fills the parent container). Default value: `False`.
- className (string | dict; optional):
  CSS class name for the current component, supports [dynamic CSS](/advanced-classname).
- classNames (dict; optional):
  Detailed control over the CSS class names of child elements.
  `classNames` is a dict with keys:
  - icon (string; optional):
    CSS class name for the button icon element.
- clickExecuteJsString (string; optional):
  The string of JavaScript code to be executed when the button is clicked.
- danger (boolean; default False):
  Whether the button displays a dangerous style. Default value: `False`.
- data-* (string; optional):
  Wildcard for attributes in the `data-*` format.
- debounceWait (number; default 0):
  Debounce delay for the button click event listener, in milliseconds. Default value: `0`.
- disabled (boolean; default False):
  Whether the button displays a disabled state. Default value: `False`.
- ghost (boolean; default False):
  Whether the button displays a transparent background state. Default value: `False`.
- href (string; optional):
  The link address for the button to jump to when clicked.
- icon (a list of or a singular dash component, string or number; optional):
  Component type, the prefix icon element embedded before the button.
- iconPosition (a value equal to: 'start', 'end'; default 'start'):
  The position of the button icon component, options include `'start'`, `'end'`. Default value: `'start'`.
- key (string; optional):
  Update the `key` value of the current component to force a redraw of the component.
- loading (boolean; optional):
  Whether the button displays a loading state. Default value: `False`.
- loadingChildren (a list of or a singular dash component, string or number; optional):
  Component type, the embedded element displayed in the button's loading state.
- loading_state (dict; optional)
  `loading_state` is a dict with keys:
  - component_name (string; optional):
    Holds the name of the component that is loading.
  - is_loading (boolean; optional):
    Determines if the component is loading or not.
  - prop_name (string; optional):
    Holds which property is loading.
- motionType (a value equal to: 'happy-work'; optional):
  The special interaction type for the button, options include `'happy-work'`.
- nClicks (number; default 0):
  The cumulative number of button clicks, used to monitor button click behavior. Default value: `0`.
- shape (a value equal to: 'default', 'circle', 'round'; default 'default'):
  The shape of the button, options include `'default'`, `'circle'`, `'round'`. Default value: `'default'`.
- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):
  The size specification of the button, options include `'small'`, `'middle'`, `'large'`. Default value: `'middle'`.
- style (dict; optional):
  CSS styles for the current component.
- styles (dict; optional):
  Detailed control over the CSS styles of child elements.
  `styles` is a dict with keys:
  - icon (dict; optional):
    CSS styles for the button icon element.
- target (string; default '_blank'):
  The way the button link is opened when clicked. Default value: `'_blank'`.
- title (string; optional):
  The native button title attribute.
- type (a value equal to: 'default', 'primary', 'dashed', 'link', 'text'; default 'default'):
  The type of the button, options include `'default'`, `'primary'`, `'dashed'`, `'link'`, `'text'`.
  Default value: `'default'`.
