- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- name (string; optional):
    Used with `AntdForm` for batch value collection/control, serving as the field name of the current form item, with `id` as the default value.

- enableBatchControl (boolean; default True):
    Controls whether the current component participates in the effective `AntdForm` batch value collection/control feature. Default: `True`.

- allowClear (boolean; default False):
    Whether to allow clearing the selected color. Default value: `False`.

- arrow (dict; optional):
    Arrow settings for the color picker panel. Default: `True`.

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
    Color mode: `'single'`, `'gradient'`, or a combination of modes. Default: `'single'`.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- disabledAlpha (boolean; default True):
    Whether to disable the transparency selection. Default value: `True`.

- open (boolean; optional):
    Listening to or setting the expansion state of the color selection panel.

- presets (list of dicts; optional):
    `presets` is a list of dicts with keys:

    - label (a list of or a singular dash component, string or number; optional):
        Component type, the label content of the current preset.

    - colors (list of strings; optional):
        An array of color values included in the current preset.

    - defaultOpen (boolean; optional):
        Whether the current preset is expanded by default. Default value: `True`.

- placement (a value equal to: 'top', 'topLeft', 'topRight', 'bottom', 'bottomLeft', 'bottomRight'; default 'bottomLeft'):
    Color panel placement. Supported values: `'top'`, `'topLeft'`, `'topRight'`, `'bottom'`, `'bottomLeft'`, `'bottomRight'`. Default: `'bottomLeft'`.

- showText (boolean; default False):
    Whether to display the color value text. Default value: `False`.

- size (a value equal to: 'large', 'middle', 'small'; default 'middle'):
    Set the size specification of the trigger control, options include `'large'`, `'middle'`, `'small'`. Default value: `'middle'`.

- trigger (a value equal to: 'hover', 'click'; default 'click'):
    The trigger method of the color selection panel, options include `'hover'`, `'click'`. Default value: `'click'`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
