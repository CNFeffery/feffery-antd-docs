**id:** *string* or *dict* type

　　 Used to set the unique ID information of the current component.

**key:** *string* type

　　 Updates the `key` value of the current component, enabling the forced redraw of the current component.

**style:** *dict* type

　　 Used to set the CSS style of the current component.

**className:** *string* or *dict* type

　　 Used to set the CSS class name of the current component, supporting [dynamic CSS](/advanced-classname).

**children:** *component type*

　　 Used to pass in nested child elements.

**format:** *string* type

　　 Used to set the date and time format template for the countdown content of the current countdown component. See [reference documentation](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/) for details.

**value:** *string* type

　　 Used to set the target deadline date and time as a date and time string.

**valueFormat:** *string* type, default: `'YYYY-MM-DD hh:mm:ss'`

　　 Used to set the reference format for parsing the date and time of the `value`. See [reference documentation](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/) for details.

**prefix:** *component type*

　　 Used to add prefix content to the numerical information.

**suffix:** *component type*

　　 Used to add suffix content to the numerical information.

**title:** *component type*

　　 Used to set the title content.

**titleTooltip:** *string* type

　　 Used to set the tooltip content for the title suffix.

**valueStyle:** *dict* type

　　 Used to set the CSS style of the numerical information.