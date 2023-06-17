**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for forced re-rendering of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**linkDict:** `list[dict]`, required

　　Defines the hierarchical structure of the current anchor points. Each dictionary represents a node, and nesting can be done using the `children` parameter. Available key-value parameters include:

- **title:** *string*, used to set the title text of the current node.
- **href:** *string*, used to set the website URL corresponding to the current node.
- **target:** *string*, used to set the link behavior of the current node.
- **children:** `list[dict]`, used to further nest nodes.

**align:** *string*, default: `'right'`

　　Used to set the layout position of the anchor component, with options `'left'`, `'right'`.

**containerId:** *string*

　　Used to set the ID of the reference local container for the anchor.

**targetOffset:** *int* or *float*

　　Used to set the offset distance after clicking the anchor to switch to the target element.

**affix:** *bool*, default: `True`

　　Used to enable or disable the affix mode for the anchor.

**bounds:** *int*, default: `5`

　　Used to set the pixel margin outside the anchor area.

**offsetTop:** *int* or *float*

　　Used to set the pixel threshold for triggering the anchoring effect of the anchor.

**clickedLink:** *dict*

　　Used to listen for click events in the anchor.