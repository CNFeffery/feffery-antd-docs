**id:** *string* or *dict* type

　　 Used to set the *unique id information of the current component*.

**key:** *string* type

　　 Updates the `key` value of the current component to *force a redraw of the current component*.

**style:** *dict* type

　　 Used to set the *CSS style of the current component*.

**className:** *string* or *dict* type

　　 Used to set the *CSS class name of the current component*, supports [dynamic CSS](/advanced-classname).

**type:** *string* type, default is `'line'`

　　 Used to *set the type of the progress bar*, available options are `'line'`, `'circle'`, `'dashboard'`.

**size:** *string* type, default is `'default'`

　　 Used to *set the size specification of the progress bar*, available options are `'default'`, `'small'`.

**percent:** *int* or *float* type, default is `0`

　　 Used to *set the corresponding percentage of the progress bar*, the value should be between 0 and 100.

**success:** *dict*

　　 Used for configuring parameters related to the success state. The available key-value pairs are:

- **percent:** *int*, used to customize the percentage corresponding to the success state.
- **strokeColor:** *string* or *dict*, used to set the color for the success state. When passing a dictionary type, it is used to configure a gradient color. The available key-value pairs are:
  - **from:** *string*, used to set the starting color.
  - **to:** *string*, used to set the ending color.

**format:** *dict* type

　　 Used to *configure the percentage text content*, available key-value parameters are:

- **prefix:** *string* type, default is `''`, used to *set the prefix text of the percentage text*.
- **suffix:** *string* type, default is `'%'`, used to *set the suffix text of the percentage text*.
- **content:** *component type*, used to *force override the original percentage text content*.

**status:** *string* type

　　 Used to *force set the status of the progress bar*, available options are `'success'`, `'exception'`, `'normal'`, `'active'`, where `'active'` is only available for `'line'` type progress bar.

**showInfo:** *bool* type, default is `True`

　　 Used to *set whether to display the progress value or status icon*.

**strokeColor:** *string* or *dict* type

　　 Used to *set the color of the progress bar*, when passed as a *dict*, it can set gradient color, available key-value parameters are:

- **from:** *string* type, used to *set the starting color of the progress bar*.
- **to:** *string* type, used to *set the ending color of the progress bar*.

**strokeLinecap:** *string* type, default is `'round'`

　　 Used to *set the line cap style of the progress bar*, same as the `stroke-linecap` property in CSS, available options are `'round'`, `'butt'`, `'square'`.

**strokeWidth:** *int* type

　　 Used to *set the pixel line width of the progress bar*.

**trailColor:** *string* type

　　 Used to *set the color of the unfinished part of the progress bar*, default is no color.

**width:** *int* type, default is `132`

　　 Available when `type` is `'circle'` or `'dashboard'`, used to *set the canvas width in pixels*.

**gapDegree:** *int* type, default is `75`

　　 Available when `type` is `'dashboard'`, used to *set the gap angle of the dashboard progress bar*, the value should be between 0 and 295.

**gapPosition:** *string* type, default is `'bottom'`

　　 Available when `type` is `'dashboard'`, used to *set the position of the gap in the dashboard*, available options are `'left'`, `'top'`, `'right'`, `'bottom'`.

**steps:** *int* type

　　 Available when `type` is `'line'`, used to *set the number of segments in the segmented progress bar*.



