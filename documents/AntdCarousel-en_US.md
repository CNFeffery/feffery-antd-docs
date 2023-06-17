**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component, enabling forced re-rendering of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass in nested child elements.

**autoplay:** *bool*, default: `False`

　　Used to enable automatic carousel rotation.

**dotPosition:** *string*, default: `'bottom'`

　　Used to set the position of the carousel indicator, options are `'top'`, `'bottom'`, `'left'`, and `'right'`.

**easing:** *string*, default: `'linear'`

　　Used to set the animation timing function for carousel transitions, same as the `animation-timing-function` property in CSS.

**effect:** *string*, default: `'scrollx'`

　　Used to set the carousel transition effect, options are `'scrollx'`, and `'fade'`.

**autoplaySpeed:** *int*, default: `3000`

　　Used to set the interval between carousel transitions, in milliseconds.

**speed:** *int*, default: `500`

　　Used to set the duration of the carousel transition animation, in milliseconds.

**pauseOnHover:** *bool*, default: `False`

　　Used to determine whether the carousel rotation pauses on mouse hover.