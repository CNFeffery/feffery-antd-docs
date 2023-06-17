**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for forced re-rendering of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass in nested child elements.

**offsetBottom:** *int*

　　Used to set the pixel threshold from the bottom of the window after which the affix component will be anchored when the user scrolls the page.

**offsetTop:** *int*

　　Used to set the pixel threshold from the top of the window after which the affix component will be anchored when the user scrolls the page.

**target:** *string*

　　Used to set the ID of the target container element for the affix component to listen to scroll events and perform anchoring. If not set, the root node of the page will be anchored.