- id (string; optional):
    Unique identifier for the component.

- align (a value equal to: 'start', 'center', 'end'; default 'start'):
    Component alignment specification, with options `start`, `center`, `end`. Default value: `start`.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- batchPropsNames (list of strings; optional):
    List of property names to be included in batch property listening. Default value: `[]`.

- batchPropsValues (dict; optional):
    Batch listening for property values corresponding to the current batchPropsNames.

- className (string | dict; optional):
    Current component CSS class name, supporting [dynamic CSS](/advanced-classname).

- current (number; optional):
    Listening to or setting the current page number.

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- defaultCurrent (number; default 1):
    The current page number upon initialization. Default value: `1`.

- defaultPageSize (number; default 10):
    The number of items per page upon initialization. Default value: `10`.

- disabled (boolean; default False):
    Whether to disable the functionality of the current component. Default value: `False`.

- hideOnSinglePage (boolean; default False):
    Whether to hide the pager when there is only one page. Default value: `False`.

- key (string; optional):
    Update the `key` value of the current component to force a redraw of the current component.

- loading_state (dict; optional):
    `loading_state` is a dictionary with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de'; default 'zh-cn'):
    Component text language, with options `zh-cn` (Simplified Chinese), `en-us` (English), `de-de` (German).
    Default value: `zh-cn`.

- pageSize (number; optional):
    Listening to or setting the number of items per page.

- pageSizeOptions (list of numbers; optional):
    Options for switching the number of items per page.

- persisted_props (list of a value equal to: 'current', 'pageSize's; default ['current', 'pageSize']):
    Array of property values enabled for persistence in the current component, with options `current`, `pageSize`. Default value: `['current', 'pageSize']`.

- persistence (boolean | string | number; optional):
    Whether to enable persistence for the current component.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    The type of persistent storage for the current component's properties. Default value: `local`.

- showLessItems (boolean; default False):
    Whether to display fewer page jump buttons. Default value: `False`.

- showQuickJumper (boolean; default False):
    Whether to render a quick page jump control. Default value: `False`.

- showSizeChanger (boolean; default False):
    Whether to render a page size switcher. Default value: `False`.

- showTotal (boolean; default True):
    Whether to render a description of the total number of records. Default value: `True`.

- showTotalPrefix (string; optional):
    Prefix content for the total number of records description.

- showTotalSuffix (string; optional):
    Suffix content for the total number of records description.

- simple (boolean; default False):
    Whether to enable simple mode. Default value: `False`.

- size (a value equal to: 'default', 'small'; default 'default'):
    Component size specification, with options `default`, `small`. Default value: `default`.

- style (dict; optional):
    CSS styles for the current component.

- total (number; optional):
    Total number of records.
