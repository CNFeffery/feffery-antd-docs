**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for forced re-rendering of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**locale:** *string*, default: `'zh-cn'`

　　Used to set the language for the functional text of the current component. Available options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**format:** *string*

　　Used to set the date parsing format for the current date picker. See [reference](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/) for details.

**size:** *string*, default: `'default'`

　　Used to set the size of the current component. Available options are `'default'` and `'large'`.

**value:** *string*

　　Used to listen to or set the currently selected value.

**defaultValue:** *string*

　　Used to listen to or set the initially selected value.

**persistence:** *bool*

　　Used to enable property persistence for the current component.

**persisted_props:** *list*, default: `['value']`

　　Used to set which properties of the current component should be persisted. Available option is `'value'`.

**persistence_type:** *string*, default: `'local'`

　　Used to set the storage type for property persistence of the current component. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), and `'memory'` (temporary memory cache).