**id:** *string* or *dict* type

　　Used to set the unique ID information of the current component.

**key:** *string* type

　　Updates the `key` value of the current component, enabling the forced redraw of the current component.

**style:** *dict* type

　　Used to set the CSS style of the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**title:** *string* type

　　Used to set the title content of the dropdown menu trigger element.

**buttonMode:** *bool* type, default: `False`

　　Used to determine whether the dropdown menu trigger element should be rendered as a button.

**buttonProps:** *dict* type

　　Used to configure button-related parameters when the trigger element is rendered as a button. The available key-value pairs are:

- **size:** *string* type, default: `'middle'`, used to set the size specification of the trigger button. Options are `'small'`, `'middle'`, and `'large'`.
- **type:** *string* type, default: `'default'`, used to set the style of the trigger button. Options are `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`, and `'default'`.
- **danger:** *bool* type, default: `False`, used to set whether to render the button in a dangerous warning state.
- **style:** *dict* type, used to set the CSS style of the button.
- **className:** *string* type, used to set the CSS class name of the button.

**freePosition:** *bool* type, default: `False`

　　Used to force enable the free position mode.

**freePositionStyle:** *dict* type

　　When `freePosition=True`, used to adjust the position and other styles of the dropdown menu.

**freePositionClassName:** *string* type

　　When `freePosition=True`, used to set the CSS class name of the dropdown menu.

**clickedKey:** *string* type

　　Used to listen to the key value of the most recently clicked option in the dropdown menu.

**nClicks:** *int* type

　　Used to listen to the cumulative number of times all options in the dropdown menu are clicked. It can be used to assist in detecting repeated click events on menu items.

**menuItems:** `list[dict]` type

　　Used to define the structure of the dropdown menu options. Each element in the list is a dictionary with the following available key-value pairs:

- **title:** *string* type, used to set the title content of the current option.
- **href:** *string* type, used to set the link URL of the current option.
- **target:** *string* type, used to set the link target behavior of the current option.
- **disabled:** *bool* type, default: `False`, used to set whether the current option is disabled.
- **icon:** *string* type, same as the corresponding parameter in `AntdIcon`, used to set the prefix icon of the current option.
- **key:** *string* type, used to set the unique key value of the current option.
- **isDivider:** *bool* type, default: `False`, used to set whether the current option is a horizontal separator. Setting it to `True` will ignore other key-value pairs.

**arrow:** *bool* type, default: `False`

　　Used to determine whether to render a directional arrow for the expanded dropdown menu.

**disabled:** *bool* type, default: `False`

　　Used to set whether the current component is disabled.

**overlayClassName:** *string* or *dict* type

　　Used to set the class name of the dropdown menu container, supports [dynamic CSS](/advanced-classname).

**overlayStyle:** *string* type

　　Used to set the CSS style of the dropdown menu container.

**placement:** *string* type, default: `'bottomLeft'`

　　Used to set the direction of the dropdown menu. Options are `'bottomLeft'`, `'bottomCenter'`, `'bottomRight'`, `'topLeft'`, `'topCenter'`, and `'topRight'`.

**trigger:** *string* type, default: `'hover'`

　　Used to set the trigger method for expanding the dropdown menu. Options are `'hover'` and `'click'`.

**autoAdjustOverflow:** *bool* type, default: `True`

　　Used to determine whether the position of the dropdown menu should be automatically adjusted when it is obstructed.

**visible:** *bool* type, default: `False`

　　Used to set whether the dropdown menu is visible.

**popupContainer:** *string* type, default: `'body'`

　　Used to set the reference container type for the floating layer elements involved in the current component. Options are `'body'` (with the page root node as the reference) and `'parent'` (with the parent container of the current element as the reference). When the component is within a locally scrolling container, setting `popupContainer='parent'` can solve the problem of the floating layer not scrolling along.