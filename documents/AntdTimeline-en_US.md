**id:** String or dict type

　　Used to *set the unique ID information for the current component*.

**key:** String type

　　Updates the `key` value for the current component, which can force a redraw of the current component.

**style:** Dict type

　　Used to *set the CSS style for the current component*.

**className:** String or dict type

　　Used to *set the CSS class name for the current component*. Supports [dynamic CSS](/advanced-classname).

**items:** `list[dict]` type, required

　　Used to *define the nodes of the timeline*. Each dictionary element can have the following key-value parameters:

- **content:** Component type, used to *set the main content of the current node*.
- **color:** String type, used to *set the color of the icon for the current node*. Available status colors include: `'blue'` (indicating in progress or default state), `'green'` (indicating completed), `'red'` (indicating warning or error state), `'grey'` (indicating incomplete or invalid state).
- **icon:** Component type, used to *customize the icon for the current node*.
- **label:** Component type, used to *set the label content of the current node*.

**mode:** String type, default is `'right'`

　　Used to *set the overall display mode of the timeline*. This is reflected in the relative position of the node label and content. Options include `'left'`, `'alternate'`, and `'right'`.

**pending:** Component type

　　Used to *add a "loading" node at the end of the timeline and set the label content*. By default, this node is not added.

**pendingDot:** Component type

　　Used to *customize the icon for the "loading" node at the end of the timeline*.

**reverse:** Boolean type, default is `False`

　　Used to *set whether to reverse the display order of the timeline nodes*. `False` indicates top-down display order.