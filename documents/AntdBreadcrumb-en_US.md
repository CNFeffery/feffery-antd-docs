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

**items:** `list[dict]`

　　Used to define the breadcrumb structure. Each dictionary element in the list corresponds to a different level of the breadcrumb hierarchy. The available key-value pairs are:

- **title:** *string* type, used to set the text content of the current node.
- **href:** *string* type, used to set the URL link for the current node.
- **target:** *string*, used to set the behavior of the link for the current node.
- **icon:** *string* type, same as the corresponding parameter in `AntdIcon`, used to set the prefix icon for the breadcrumb.
- **menuItems:** `list[dict]` type, used to render a dropdown menu for the current node. Each dictionary element in the list corresponds to an option in the dropdown menu. The available key-value pairs are:
  - **title:** *string* type, used to set the text content of the current option.
  - **href:** *string* type, used to set the URL link for the current option.
  - **target:** *string* type, used to set the link behavior for the current option.
  - **disabled:** *bool* type, default: `False`, used to determine whether the current option is disabled.
  - **icon:** *string* type, same as the corresponding parameter in `AntdIcon`, used to set the prefix icon for the current option.

**separator:** *component type*, default: `'/'`

　　Used to customize the separator between different levels of the breadcrumb.