**id:** *string* or *dict*

　　Used to set the unique id information for the current component.

**key:** *string*

　　Updates the `key` value of the current component, which can force a re-render of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**locale:** *string* (default: `'zh-cn'`)

　　Used to set the language for the functional text of the current component, available options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**total:** *int*

　　Used to set the total number of records for inferring the number of pages.

**defaultCurrent:** *int* (default: `1`)

　　Used to set the initial page number to be displayed.

**defaultPageSize:** *int* (default: `10`)

　　Used to set the initial number of records per page.

**current:** *int*

　　Used to set or listen to the current page number.

**disabled:** *bool* (default: `False`)

　　Used to set whether the current component is disabled.

**hideOnSinglePage:** *bool* (default: `False`)

　　Used to automatically hide the pagination component when there is only one page.

**pageSize:** *int*

　　Used to set or listen to the number of records per page.

**pageSizeOptions:** *list[int]*

　　Used to set the options for the page size selector.

**showSizeChanger:** *bool* (default: `False`)

　　Used to render the page size selector.

**showQuickJumper:** *bool* (default: `False`)

　　Used to enable the quick jump feature.

**showLessItems:** *bool* (default: `False`)

　　Used to *determine whether to display fewer pagination buttons*.

**showTotalPrefix:** *str* (default: `'共 '`)

　　Used to set the prefix text for the total number of records.

**showTotalSuffix:** *str* (default: `' 条记录'`)

　　Used to set the suffix text for the total number of records.

**showTotal:** *bool* (default: `True`)

　　Used to set whether to display the total number of records.

**simple:** *bool* (default: `False`)

　　Used to enable the simple mode.

**size:** *str* (default: `'default'`)

　　Used to set the size of the current component, available options are `'default'` and `'small'`.

**persistence:** *bool*

　　Used to enable attribute persistence for the current component.

**persisted_props:** *list* (default: `['current', 'pageSize']`)

　　Used to set which properties of the current component to persist, available options are `'current'` and `'pageSize'`.

**persistence_type:** *string* (default: `'local'`)

　　Used to set the storage type for attribute persistence of the current component, available options are `'local'` (browser local storage), `'session'` (current tab session storage), and `'memory'` (temporary memory cache).