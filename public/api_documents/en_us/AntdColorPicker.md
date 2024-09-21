- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the `key` value of the current component to force a redraw of the component.

- style (dict; optional):
    CSS styles for the current component.

- className (string | dict; optional):
    CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de'; default 'zh-cn'):
    Language of the component's text, options include `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German).
    Default value: `'zh-cn'`.

- name (string; optional):
    Used in conjunction with the `AntdForm` form for batch value collection/control, serving as the field name for the current form item, with `id` as the default value.

- allowClear (boolean; default False):
    Whether to allow clearing the selected color. Default value: `False`.

- arrow (dict; optional):
    Configure additional arrows for the color selection panel. Default value: `True`.

    `arrow` is a boolean | dict with keys:

    - pointAtCenter (boolean; optional):
        Whether the arrow points to the center of the panel. Default value: `False`.

- defaultValue (string; optional):
    The initial input value.

- value (string; optional):
    Listening to or setting the selected color value. Default value: `'#1677FF'`.

- format (a value equal to: 'rgb', 'hex', 'hsb'; default 'hex'):
    Listening to or setting the color format, options include `'rgb'`, `'hex'`, `'hsb'`. Default value: `'hex'`.

- mode (a value equal to: 'single', 'gradient' | list of a value equal to: 'single', 'gradient's; default 'single'):
    The selector mode, used to configure single color and gradient, options include `'single'`, `'gradient'`, supports single or multiple option combinations.
    Default value: `single`.

- disabled (boolean; default False):
    Whether to disable the current component. Default value: `False`.

- disabledAlpha (boolean; default True):
    Whether to disable the transparency selection. Default value: `True`.

- open (boolean; optional):
    Listening to or setting the expansion state of the color selection panel.

- presets (list of dicts; optional):
    Configure preset color selection options.

    `presets` is a list of dicts with keys:

    - colors (list of strings; optional):
        An array of color values included in the current preset.

    - defaultOpen (boolean; optional):
        Whether the current preset is expanded by default. Default value: `True`.

    - label (a list of or a singular dash component, string or number; optional):
        Component type, the label content of the current preset.

- placement (a value equal to: 'top', 'topLeft', 'topRight', 'bottom', 'bottomLeft', 'bottomRight'; default 'bottomLeft'):
    The expansion direction of the color selection panel, options include `'top'`, `'topLeft'`, `'topRight'`, `'bottom'`, `'bottomLeft'`, `'bottomRight'`.
    Default value: `'bottomRight'`.

- showText (boolean; default False):
    Whether to display the color value text. Default value: `False`.

- size (a value equal to: 'large', 'middle', 'small'; default 'middle'):
    Set the size specification of the trigger control, options include `'large'`, `'middle'`, `'small'`. Default value: `'middle'`.

- trigger (a value equal to: 'hover', 'click'; default 'click'):
    The trigger method of the color selection panel, options include `'hover'`, `'click'`. Default value: `'click'`.

- data-* (string; optional):
    `data-*` format attribute wildcard.

- aria-* (string; optional):
    `aria-*` format attribute wildcard.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.
