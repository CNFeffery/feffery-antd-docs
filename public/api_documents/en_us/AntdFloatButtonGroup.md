- children (a list of or a singular dash component, string or number; optional):
  Component type, embedded element within the button.
- id (string; optional):
  Unique identifier for the component.
- className (string | dict; optional):
  CSS class name for the current component, supports [dynamic CSS](/advanced-classname).
- description (a list of or a singular dash component, string or number; optional):
  Description content
- icon (a list of or a singular dash component, string or number; optional):
  Component type, prefix icon element nested within the button.
- key (string; optional):
  Updating the `key` value of the current component can force a redraw of the component.
- loading_state (dict; optional)

  `loading_state` is a dict with keys:

  - component_name (string; optional):
    Holds the name of the component that is loading.
  - is_loading (boolean; optional):
    Determines if the component is loading or not.
  - prop_name (string; optional):
    Holds which property is loading.
- open (boolean; optional):
  Set or listen to the open state of the current component.
- shape (a value equal to: 'circle', 'square'; default 'circle'):
  Shape of the button, options include `'circle'`, `'square'`. Default value: `'circle'`.
- style (dict; optional):
  CSS styles for the current component.
- tooltip (a list of or a singular dash component, string or number; optional):
  Component type, additional tooltip content for the button.
- trigger (a value equal to: 'click', 'hover'; optional):
  The trigger method for menu expansion mode. options include `'click'` , `'hover'`.
- type (a value equal to: 'default', 'primary'; default 'default'):
  Type of the button, options include `'default'`, `'primary'`. Default value: `'default'`.
