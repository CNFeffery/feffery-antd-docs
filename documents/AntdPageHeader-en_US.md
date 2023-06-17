**id:** *string* or *dict*

　　Used to set the unique id information for the current component.

**key:** *string*

　　Updates the `key` value of the current component, which can force a re-render of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component*

　　Used to pass in nested child elements.

**title:** *component*

　　Used to set the title content of the page header.

**subTitle:** *component*

　　Used to set the subtitle content of the page header.

**showBackIcon:** *bool* (default: `True`)

　　Used to set whether to display the back button.

**historyBackDisabled:** *bool* (default: `False`)

　　Used to disable the native browser page back function of the back button.

**backClicks:** *int* (default: `0`)

　　When `historyBackDisabled=True`, this parameter is used to record the number of times the back button in the page header is clicked.

**ghost:** *bool* (default: `True`)

　　Used to enable or disable transparent background mode.