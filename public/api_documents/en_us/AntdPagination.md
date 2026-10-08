- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- align (a value equal to: 'start', 'center', 'end'; default 'start'):
    Component alignment setting. Supported values: `'start'`, `'center'`, `'end'`. Default: `'start'`.

- defaultCurrent (number; default 1):
    The current page number upon initialization. Default value: `1`.

- defaultPageSize (number; default 10):
    The number of items per page upon initialization. Default value: `10`.

- current (number; optional):
    Track or set current page number.

- disabled (boolean; default False):
    Whether to disable the functionality of the current component. Default value: `False`.

- hideOnSinglePage (boolean; default False):
    Whether to hide the pager when there is only one page. Default value: `False`.

- pageSize (number; optional):
    Listening to or setting the number of items per page.

- pageSizeOptions (list of numbers; optional):
    Options for switching the number of items per page.

- showSizeChanger (boolean; default False):
    Whether to render a page size switcher. Default value: `False`.

- showQuickJumper (boolean; default False):
    Whether to render quick jump control. Default: `False`.

- showTotalPrefix (string; optional):
    Prefix content for the total number of records description.

- showTotalSuffix (string; optional):
    Suffix content for the total number of records description.

- simple (boolean; default False):
    Whether to enable simple mode. Default value: `False`.

- size (a value equal to: 'default', 'small'; default 'default'):
    Component size. Supported values: `'default'`, `'small'`. Default: `'default'`.

- total (number; optional):
    Total number of records.

- showTotal (boolean; default True):
    Whether to render a description of the total number of records. Default value: `True`.

- showLessItems (boolean; default False):
    Whether to display fewer page jump buttons. Default value: `False`.

- batchPropsNames (list of strings; optional):
    List of property names to be included in batch property listening. Default value: `[]`.

- batchPropsValues (dict; optional):
    Batch listening for property values corresponding to the current batchPropsNames.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.

- persistence (boolean | string | number; optional):
    Whether to enable persistence for the current component.

- persisted_props (list of a value equal to: 'current', 'pageSize's; optional):
    Component properties whose values are persisted. Supported values: `'current'`, `'pageSize'`. Default: `['current', 'pageSize']`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Storage type for persisted properties. Default: `'local'`.
