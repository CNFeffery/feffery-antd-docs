**id:** *string* or *dict* type

　　Used to set the unique ID information of the current component.

**key:** *string* type

　　Updates the `key` value of the current component, enabling forced re-rendering of the component.

**className:** *string* or *dict* type

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component* type

　　Used to pass in nested child elements.

**innerTextOrientation:** *string* type, default: `'center'`

　　Used to set the alignment of the inline content (passed through the `children` parameter). Available options are `'left'` (left-aligned), `'center'` (center-aligned), and `'right'` (right-aligned).

**isDashed:** *bool* type, default: `False`

　　Used to set whether to render the divider as dashed line.

**direction:** *string* type, default: `'horizontal'`

　　Used to set the direction of the divider. Available options are `'horizontal'` (horizontal) and `'vertical'` (vertical).

**fontSize:** *string* type

　　Used to set the font size of the inline content within the divider. Accepts a valid `font-size` value in CSS, such as `'16px'`.

**lineColor:** *string* type, default: `'lightgrey'`

　　Used to set the color of the divider. Accepts a valid color value in CSS.

**fontStyle:** *string* type, default: `'initial'`

　　Used to set the font style of the inline content within the divider. Accepts a valid `font-style` value in CSS, such as `'oblique'` for italic.

**fontWeight:** *string* type, default: `'initial'`

　　Used to set the font weight of the inline content within the divider. Accepts a valid `font-weight` value in CSS, such as `'bold'` for bold.

**fontFamily:** *string* type, default: `'initial'`

　　Used to set the font family of the inline content within the divider. Accepts a valid `font-family` value in CSS, such as `'KaiTi'` for KaiTi font.

**fontColor:** *string* type, default: `'#000000'`

　　Used to set the font color of the inline content. Accepts a valid `color` value in CSS, such as `'black'`.