**id:** *string* or *dict* type

　　Used to set the unique id information for the current component.

**key:** *string* type

　　Updates the `key` value of the current component to force a re-rendering effect.

**style:** *dict* type

　　Used to set the CSS style for the current component.

**className:** *string* type

　　Used to set the CSS class name for the current component.

**locale:** *string* type, default: `'zh-cn'`

　　Used to set the language for the functional text of the current component. Available options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**columns:** `list[dict]` type

　　Used to define the fields and related functional parameters to be displayed for the current table. Each dictionary represents one field, and the available key-value parameters are:

- **title:** *component type*, required. Used to set the title content of the current field.
- **dataIndex:** *string* type, required. Used to set the unique id information of the current field, which corresponds to key-value pairs within each record in the `data`.
- **group:** *string* or *list* type, used to *assign grouping information to the current field* for rendering multi-level headers.
- **renderOptions:** *dict* type. Used to set the configuration parameters related to the re-rendering mode for the current field. The available key-value parameters are:
  - **renderType:** *string* type. Used to set the desired re-rendering mode type for the current field. Available options are `'link'` (link mode), `'ellipsis'` (long content truncation mode), `'copyable'` (copyable mode), `'ellipsis-copyable'` (long content truncation + copyable mode), `'tags'` (tag mode), `'status-badge'` (status badge mode), `'image'` (image mode), `'custom-format'` (custom format mode), `'corner-mark'` (corner mark mode), `'row-merge'` (row-spanning merged cell mode), `'dropdown-links'` (dropdown link menu mode), `'image-avatar'` (image avatar mode), `'mini-line'` (mini line chart mode), `'mini-bar'` (mini bar chart mode), `'mini-progress'` (mini progress chart mode), `'mini-ring-progress'` (mini ring progress chart mode), `'mini-area'` (mini area chart mode), `'button'` (button mode), `'checkbox'` (checkbox mode), `'switch'` (switch mode), `'dropdown'` (dropdown menu mode), `'select'` (select mode).
  - **renderLinkText:** *string* type. When `renderType="link"`, used to set the text content for the links rendered for the current field.
  - **renderButtonPopConfirmProps:** *dict* type. When `renderType="button"` and a popover confirmation box needs to be added to the button rendered for the current field, used to set the configuration parameters related to the popover confirmation. The available key-value parameters are:
    - **title:** *string* type. Used to set the title text for the popover confirmation box.
    - **okText:** *string* type. Used to set the text for the confirm button of the popover confirmation box.
    - **cancelText:** *string* type. Used to set the text for the cancel button of the popover confirmation box.
  - **tooltipCustomContent:** *string* type. When `renderType` is `'mini-line'`, `'mini-area'`, or `'

mini-bar'`, used to set a JavaScript function string for custom formatting the tooltip in the mini charts.
  - **progressOneHundredPercentColor:** *string* type. When `renderType` is `'mini-progress'` or `'mini-ring-progress'`, used to set the fill color when the progress reaches 1. The default value is <font color="#52c41a">'#52c41a'</font>.
  - **ringProgressFontSize:** *int* type. When `renderType="mini-ring-progress"`, used to set the font size of the percentage text.
  - **dropdownProps:** *dict* type. When `renderType="dropdown-links"`, used to set the configuration parameters related to the dropdown link menu for the current field. The available key-value parameters are:
    - **title:** *string* type. Used to set the text content for the anchor of the dropdown link menu for the current field.
    - **arrow:** *bool* type. Used to set whether to display the connecting arrow for the dropdown link menu for the current field.
    - **disabled:** *bool* type, default: `False`. Used to set whether to disable all dropdown link menus under the current field.
    - **overlayClassName:** *string* type. Used to set the CSS class name for the dropdown menu container of the current field.
    - **overlayStyle:** *string* type. Used to set the CSS style for the dropdown menu container of the current field.
    - **placement:** *string* type. Used to set the popup position for the dropdown link menu of the current field. Available options are `'bottomLeft'`, `'bottomCenter'`, `'bottomRight'`, `'topLeft'`, `'topCenter'`, `'topRight'`.
- **fixed:** *string* type. Used to freeze the current field in a fixed position. Available options are `'left'`, `'right'`.
- **editable:** *bool* type, default: `False`. Used to set whether the current field is editable.
- **editOptions:** *dict* type. Used to configure the parameters related to the edit mode for the current field. The available key-value parameters are:
  - **mode:** *string* type, default: `'default'`. Used to set the input box type in the editable mode of the current field. Available options are `'default'`, `'text-area'`.
  - **autoSize:** *bool* or *dict* type, default: `False`. Used to enable the auto-sizing feature for the input box in the text area input mode. When passing a dictionary, the available key-value parameters are:
    - **minRows:** *int* type. Used to set the minimum number of rows.
    - **maxRows:** *int* type. Used to set the maximum number of rows.
  - **maxLength:** *int* type. Used to set the maximum number of characters allowed in the input box. There is no limit by default.
  - **placeholder:** *string* type, Used to *set the placeholder text displayed in input mode when the cell content is empty.*
- **align:** *string* type. Used to set the horizontal alignment of the content of the current field. Available options are `'left'`, `'center'`, `'right'`.
- **width:** *int* or *string* type. Used to set the width of the current field.
- **hidden:** *bool* type, default: `False`. Used to set whether the current field should be hidden.
- **filterResetToDefaultFilteredValue:** *bool* type, used to determine whether the filter menu corresponding to the current field should be reset to the default selected items set by the `defaultFilteredValues` parameter after resetting.

**data:** Type *list*

　　Used to *set the source data for the current table*. Each element is a dictionary that corresponds to the `dataIndex` information of each field in the `columns`. Additionally, you can set key-value pairs with `key` as the unique identifier for the current row record (if `key` is not set, `AntdTable` will automatically generate an incremental number as the `key`). The format of the field values in each record in `data` depends on whether the corresponding field has enabled re-rendering and the specific type of re-rendering mode enabled. The input value formats accepted by different re-rendering modes are as follows:

- **Normal mode (no re-rendering enabled):** Type *int*, *float*, or *string*
- **Link mode:** Type *dict*. Available key-value parameters include:
- **content:** Type *string*. Used to *set the text content of the rendered link for the current record*. Takes precedence over `renderLinkText`.
  - **href:** Type *string*. Used to *set the URL of the rendered link for the current record*.
  - **target:** Type *string*. Default is `'_blank'`. Used to *set the target behavior of the rendered link for the current record*.
  - **disabled:** Type *bool*. Default is `False`. Used to *disable the rendered link for the current record*.
- **Ellipsis mode (long content with ellipsis):** Type *int*, *float*, or *string*
- **Copyable mode:** Type *int*, *float*, or *string*
- **Ellipsis-copyable mode (long content with ellipsis and copyable):** Type *int*, *float*, or *string*
- **Tags mode:** Type *dict* or *list[dict]*. A single *dict* represents a single tag, while a list of *dict* represents multiple tags. Each dictionary can have the following key-value parameters:

  - **color:** Type *string*. Used to *set the background color of the current tag*.
  - **tag:** Type *string*. Used to *set the text content of the current tag*.
- **Status badge mode:** Type *dict*. Available key-value parameters include:

  - **status:** Type *string*. Used to *set the status of the current status badge*. Options are `'success'`, `'processing'`, `'default'`, `'error'`, `'warning'`.
  - **text:** Type *int*, *float*, or *string*. Used to *set the suffix text content of the current status badge*.
- **Image mode:** Type *dict*. Available key-value parameters include:

  - **src:** Type *string*. Used to *set the URL address of the current image*.
  - **height:** Type *int*, *float*, or *string*. Used to *set the height of the current image*.
  - **preview:** Type *bool*. Default is `True`. Used to *enable interactive preview functionality for the current image*.
- **Custom format mode:** Type *int*, *float*, or *string*
- **Corner mark mode:** Type *dict*. Available key-value parameters include:

  - **placement:** Type *string*. Used to *set the position of the corner mark in the current cell*. Options are `'top-left'`, `'top-right'`, `'bottom-left'`, `'bottom-right'`.
  - **color:** Type *string*. Default is <font color="#1890ff">'#1890ff'</font>. Used to *set the color of the corner mark*.
  - **content:** Type *int*, *float*, or *string*. Used to *set the content of the current cell*.
  - **offsetX:** Type *int* or *float*. Used to *set the horizontal pixel offset for the corner mark in the current cell*.
  - **offsetY:** Type *int* or *float*. Used to *set the vertical pixel offset for the corner mark in the current cell*.
  - **hide:** Type *bool*. Default is `False`. Used to *hide the corner mark in the current cell*.
- **Row merge mode:** Type *dict*. Available key-value parameters include:

  - **content:** Type *int*, *float*, or *string*. Used to *set the content of the current cell*.
  - **rowSpan:** Type *int*. Used to *set the number of cells vertically spanned by the current cell*. `1` means no merging.
- **Dropdown links mode:** Type *list[dict]*. Each dictionary is used to define a link item in the current dropdown menu. Available key-value parameters include:

  - **title:** Type *string*. Used to *set the title text of the current link item*.
  - **href:** Type *string*. Used to *set the link address of the current link item*.
  - **disabled:** Type *bool*. Default is `False`. Used to *disable the current link item*.
  - **icon:** Type *string*. Used to *set the prefix icon of the current link item*, same as the corresponding parameter in `AntdIcon`.
  - **iconRenderer:** A *string* type, defaulting to `'AntdIcon'`, is used to determine the *rendering method for setting prefix icons for the current link item*. Available options include `'AntdIcon'` (built-in icons) and `'fontawesome'` (rendered based on CSS class names).
  - **isDivider:** Type *bool*. Used to *indicate whether the current link item acts as a divider*.
- **Image avatar mode:** Type *dict*. Available key-value parameters include:
- **src:** Type *string*. Used to *set the URL address of the image avatar*.
  - **size:** Type *int*, *string*, or *dict*. Used to *set the size of the avatar*. When an *int* is provided, it sets the pixel size of the avatar. When a *string* is provided, it selects from predefined sizes, including `'small'`, `'default'`, and `'large'`. When a *dict* is provided, it sets the pixel sizes of the avatar for different responsive breakpoints, with available breakpoints being `'xs'`, `'sm'`, `'md'`, `'lg'`, `'xl'`, and `'xxl'`.
  - **shape:** Type *string*, default is `'circle'`. Used to *set the shape of the avatar*. Available options are `'circle'` and `'square'`.
- **Mini line chart mode:** Type `list[int]` or `list[float]`.
- **Mini bar chart mode:** Type `list[int]` or `list[float]`.
- **Mini area chart mode:** Type `list[int]` or `list[float]`.
- **Mini progress chart mode:** Type *float* or *int*. The value should be between `0` and `1`.
- **Mini ring progress chart mode:** Type *float* or *int*. The value should be between `0` and `1`.
- **Button mode:** Type *dict* or `list[dict]`. A single *dict* represents a single button, and a list of multiple *dicts* represents multiple buttons. Available key-value parameters for each dictionary include:
  - **disabled:** Type *bool*, default is `False`. Used to *set whether the current button is disabled*.
  - **type:** Type *string*. Used to *set the type of the current button*. Available options are `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`, and `'default'`.
  - **danger:** Type *bool*, default is `False`. Used to *render the current button as a dangerous state*.
  - **style:** Type *dict*. Used to *set the CSS style of the current button*.
  - **content:** Type *string*. Used to *set the text content of the current button*.
  - **href:** Type *string*. Used to *set the URL of the current button*.
  - **target:** Type *string*, default is `'_blank'`. Used to *set the target behavior when the current button has a link*.
  - **icon:** Type *string*. Used to *set the prefix icon of the current button*, same as the corresponding parameter in `AntdIcon`.
  - **iconRenderer:** A *string* type, defaulting to `'AntdIcon'`, is used to specify the *rendering method for the prefix icon of the current button*. Available options include `'AntdIcon'` (built-in icons) and `'fontawesome'` (rendered based on CSS class names).
  - **custom:** Type *any*. Used to *store auxiliary information*.
- **Checkbox mode:** Type *dict*. Available key-value parameters include:
  - **checked:** Type *bool*. Used to *set whether the checkbox is checked*.
  - **disabled:** Type *bool*, default is `False`. Used to *set whether the checkbox is disabled*.
  - **label:** Type *string*. Used to *set the label text content for the checkbox*.
  - **custom:** Type *any*. Used to *store auxiliary information*.
- **Switch mode:** Type *dict*. Available key-value parameters include:
  - **checked:** Type *bool*. Used to *set whether the switch is in the on state*.
  - **disabled:** Type *bool*, default is `False`. Used to *set whether the switch is disabled*.


  - **checkedChildren:** Type *string*. Used to *set the label text for the on state of the switch*.
  - **unCheckedChildren:** Type *string*. Used to *set the label text for the off state of the switch*.
  - **custom:** Type *any*. Used to *store auxiliary information*.
- **Dropdown mode:** Type `list[dict]`. Each dictionary is used to define a menu item in the current dropdown menu. Available key-value parameters for each dictionary include:
  - **title:** Type *string*. Used to *set the title text of the current menu item*.
  - **disabled:** Type *bool*, default is `False`. Used to *set whether the current menu item is disabled*.
  - **icon:** Type *string*. Used to *set the prefix icon of the current menu item*, same as the corresponding parameter in `AntdIcon`.
  - **iconRenderer:** A *string* type, defaulting to `'AntdIcon'`, is used to determine the *rendering method for setting prefix icons for the current menu item*. Available options include `'AntdIcon'` (built-in icons) and `'fontawesome'` (rendered based on CSS class names).
  - **isDivider:** Type *bool*. Used to *set whether the current menu item acts as a divider*.
  - **custom:** Type *any*. Used to *store auxiliary information*.
- **Select mode:** Type *dict*. Available key-value parameters include:
  - **className:** Type *string*. Used to *set the CSS class name for the current select*.
  - **style:** Type *dict*. Used to *set the CSS style for the current select*.
  - **options:** Type `list[dict]`. Used to *set the options for the select*, where each dictionary has the following key-value parameters:
    - **label:** Type *string*. Used to *set the title content of the current option*.
    - **value:** Type *string*, *int*, or *float*. Used to *set the value of the current option*.
  - **listHeight:** Type *int*, default is `256`. Used to *set the maximum pixel height of the expanded layer of the select*.
  - **mode:** Type *string*. Used to *set the selection mode*. If not set, it defaults to single selection. Available options are `'multiple'` (multiple selection mode) and `'tags'` (free input mode).
  - **disabled:** Type *bool*. Used to *set whether the select is disabled*.
  - **size:** Type *string*, default is `'middle'`. Used to *set the size specification of the select*. Available options are `'small'`, `'middle'`, and `'large'`.
  - **bordered:** Type *bool*, default is `True`. Used to *set whether to render the border*.
  - **placeholder:** Type *string*. Used to *set the placeholder text when no option is selected*.
  - **placement:** Type *string*, default is `'bottomLeft'`. Used to *set the expansion direction of the select*. Available options are `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, and `'topRight'`.
  - **value:** Type *string*, *int*, or *float*. Used to *set the selected value of the select*.
  - **maxTagCount:** Type *int* or *string*. Used to *set the maximum number of selected items displayed in the selection box* in multiple selection mode. It can also be set to `'responsive'` to enable responsive mode for adaptive adjustment.
  - **optionFilterProp:** Type *string*. Used to *set the matching field for searching content to each option*. Available options are `'value'` and `'label'`.
  - **allowClear:** Type *bool*. Used to *set whether to allow the user to clear the selected option*.

**bordered:** *bool* type, default is `False`

　　Used to *determine whether to add border lines to all cells.*

**maxHeight:** *int* type

　　Used to *set the maximum pixel height of the current table area*. When the total height of the content exceeds a single page, a vertical scroll bar will be automatically rendered. The default is unlimited.

**maxWidth:** *int* type

　　Used to *set the maximum pixel width of the current table area*. When the table width exceeds this limit, a horizontal scroll bar will be automatically rendered. The default is unlimited.

**size:** *string* type, default is `'default'`

　　Used to *set the size specification of the current table*. Options include `'small'`, `'default'`, and `'large'`. This setting may be overridden by special cell rendering modes, such as editable cells.

---

**rowSelectionType:** *string* type

　　Used to *set the row selection mode for the current table*. Options include `'checkbox'` (multiple selection) and `'radio'` (single selection). If not set, row selection functionality will not be enabled by default.

**selectedRowKeys:** *list* type

　　Used to *set or monitor the list of selected row keys*.

**rowSelectionWidth:** *int* or *string* type, default is `32`

　　Used to *set the width of the column containing the row selection checkbox*.

**selectedRows:** *list[dict]* type

　　Used to *monitor the list of selected row records*.

**selectedRowsSyncWithData:** *bool* type, default is `False`

　　When set to `True`, the corresponding row record information in `selectedRows` will be synchronized after each update of the `data` data source.

**sticky:** *bool* type, default is `False`

　　Used to *enable sticky table headers*.

**titlePopoverInfo:** *dict* type

　　Used to *configure the tooltip information displayed next to each field name*. The key is the corresponding `dataIndex` of the field, and the value is a dictionary with the following key-value pairs:

- **title:** *component* type, used to *set the title content of the tooltip*.

- **content:** *component* type, used to *set the content of the tooltip*.

- **placement:** *string* type, default is `'bottom'`, used to *set the position of the tooltip*. Options include `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`, `'leftTop'`, `'leftBottom'`, `'rightTop'`, `'rightBottom'`.

- **overlayStyle:** *dict* type, used to *set the CSS style of the tooltip*.

**columnsFormatConstraint:** *dict* type

　　Used to *configure the input content format validation for fields with editable cell functionality*. The key is the corresponding `dataIndex` of the field, and the value is a dictionary with the following key-value pairs:

- **rule:** *string* type, used to *set the regular expression for the valid input format of the field*.
- **content:** *string* type, used to *set the message displayed when the user input format fails validation*.

**sortOptions:** *dict* type

　　Used to *configure the field sorting functionality*. Available key-value pairs include:

- **sortDataIndexes:** *list[dict]* type, used to *set the `dataIndex` values of the fields that need sorting functionality*.
- **multiple:** *bool* or *string* type, default is `False`, used to *enable multiple-field sorting*. When set to `True`, the order of fields in `sortDataIndexes` will determine the priority of combined sorting; when set to `'auto'`, the priority of combined sorting will be determined by the order in which users click on the sorting fields.

**sorter:** *dict* type

　　Used to *monitor the sorting status of each field after the most recent sorting operation*.

**filterOptions:** *dict* type

　　Used to *configure the field filtering functionality*. The key is the corresponding `dataIndex` of the field, and the value is a dictionary with the following key-value pairs:

- **filterMode:** *string* type, default is `'checkbox'`, used to *set the filtering functionality type for the current field*, with options including `'checkbox'`, `'keyword'`, and `'tree'`.
- **filterCustomItems:** *list* type. When `filterMode` is `'checkbox'`, it is used to *manually set the values of filter options*.
- **filterCustomTreeItems:** *list* type, used when `filterMode` is `'tree'` to *configure the tree-like filter menu structure*.
- **filterMultiple:** *bool* type, default is `True`. When `filterMode` is `'checkbox'`, it is used to *set whether multiple selections are allowed*.
- **filterSearch:** *bool* type, default is `False`. When `filterMode` is `'checkbox'`, it is used to *enable the search box*.

**defaultFilteredValues:** *dict*

　　Used to *set the initial default selected filter values for various fields*.

**filter:** *dict* type

　　Used to *monitor the filter values of each field after the most recent filtering operation*.

**hiddenRowKeys:** *list[string]* type, default is `[]`

　　Used to *set the array of row record keys that need to be hidden*. It is mainly used to achieve more advanced field value filtering effects by linking with other condition filtering components.

**pagination:** *dict* or *bool* type

　　Used to *configure the pagination functionality of the table*. Setting it to `False` will disable pagination. When passing it as a *dict* type, the available key-value pairs are:

- **position:** *string* type, default is `'bottomRight'`, used to *set the position of the pagination control relative to the table area*. Options include `'topLeft'`, `'topCenter'`, `'topRight'`, `'bottomLeft'`, `'bottomCenter'`, and `'bottomRight'`.
- **pageSize:** *int* type, used to *set the number of rows per page*.
- **current:** *int* type, used to *set or monitor the current page number of the pagination*.
- **showSizeChanger:** *bool* type, used to *set whether to enable the function of changing the number of rows per page*.
- **pageSizeOptions:** *list[int]* type, used to *set the options for changing the number of rows per page*.
- **showTitle:** *bool* type, used to *set whether to display additional explanatory text with the pagination control*.
- **showQuickJumper:** *bool* type, used to *set whether to enable the function of quickly jumping to a specific page*.
- **showLessItems:** *bool* type, used to *determine whether to display fewer pagination buttons*.
- **showTotalPrefix:** *string* type, used to *set the content displayed before the total number of records in the additional explanatory text*.
- **showTotalSuffix:** *string* type, used to *set the content displayed after the total number of records in the additional explanatory text*.
- **hideOnSinglePage:** *bool* type, used to *set whether to automatically hide the pagination control when the total number of records in the table is less than one page*.
- **simple:** *bool* type, used to *set whether to enable the simple mode*.
- **disabled:** *bool* type, used to *set whether to disable the pagination control*.
- **size:** *string* type, used to *set the size specification of the pagination control*. Options include `'default'` and `'small'`.
- **total:** *int* type, used when `mode="server-side"`, to *manually set the total number of records in the table*.

**recentlyChangedRow:** *dict* type

　　Used to *monitor the row record dictionary that has changed after the most recent editable cell operation*.

**recentlyChangedColumn:** *string*

　　Used to *track the field corresponding to the cell that has changed after the most recent editable cell operation.*

**summaryRowContents:** `list[dict]` type

　　Used to *configure the functionality related to summary rows*. Each dictionary element collectively forms the summary row of the current table in order. The available key-value parameters are:

- **content:** Component type, used to *set the content of the corresponding summary row*.
- **colSpan:** Integer type, default is `1`, used to *set the number of fields spanned by the current summary row*.
- **align:** String type, default is `'left'`, used to *set the alignment of the content in the current summary row*. Possible values are `'left'`, `'center'`, and `'right'`.

**summaryRowFixed:** Boolean type, default is `False`

　　Used to *determine whether the current summary row is fixed at the bottom*.

**conditionalStyleFuncs:** *dict* type

　　Used to *configure the JavaScript function strings for handling custom styles for each field*. The keys are the corresponding `dataIndex` of the field, and the values are strings. Note that this feature cannot be used simultaneously with cell editing.

**expandedRowKeyToContent:** `list[dict]` type

　　Used to *configure expandable content for corresponding rows*. Each dictionary element is used to define the expandable content for the corresponding row. The available key-value parameters are:

- **key:** String type, used to *set the key value of the expandable content for the current row*.
- **content:** Component type, used to *set the content of the expandable row*.

**defaultExpandedRowKeys:** `list[string]` type

　　Used to *set the row record key values that are initially in the expanded state when the table is initialized*.

**expandedRowWidth:** Integer or string type

　　Used to *set the width of the column containing the row expansion control in the current table*.

**expandRowByClick:** Boolean type, default is `False`

　　Used to *determine whether the expandable content of the current table can be triggered by clicking anywhere on the corresponding row*.

**enableCellClickListenColumns:** `list[string]` type

　　Used to *set the `dataIndex` information of the fields that enable the cell click event listener in the current table*. Enabling this feature will affect the normal use of various rendering modes. Please use with caution.

**recentlyCellClickColumn:** String type

　　When `enableCellClickListenColumns` is valid, it is used to *listen to the `dataIndex` information of the field corresponding to the most recent cell click event*.

**recentlyCellClickRecord:** *dict* type

　　When `enableCellClickListenColumns` is valid, it is used to *listen to the row record dictionary corresponding to the most recent cell click event*.

**nClicksCell:** Integer type, default is `0`

　　When `enableCellClickListenColumns` is valid, it is used to *track the cumulative number of clicks on the relevant cells in the current table*.

**recentlyCellDoubleClickColumn:** String type

　　When `enableCellClickListenColumns` is valid, it is used to *listen to the `dataIndex` information of the field corresponding to the most recent cell double-click event*.

**recentlyCellDoubleClickRecord:** Dict type

　　When `enableCellClickListenColumns` is valid, it is used to *listen to the row record dictionary corresponding to the most recent cell double-click event*.

**nDoubleClicksCell:** Integer type, default is `0`

　　When `enableCellClickListenColumns` is valid, it is used to *track the cumulative number of double-clicks on the relevant cells in the current table*.

**enableHoverListen:** Boolean type, default is `False`

　　Used to *determine whether to enable the row mouse hover event listener*. Note that enabling this feature will affect the normal use of various rendering modes. Please use with caution.

**recentlyMouseEnterColumnDataIndex:** String type

　　When `enableHoverListen=True`, it is used to *listen to the `dataIndex` information of the field corresponding to the most recent column mouse enter event*.

**recentlyMouseEnterRowKey:** Integer or string type

　　When `enableHoverListen=True`, it is used to *listen to the row record key corresponding to the most recent row mouse enter event*.

**recentlyMouseEnterRow:** Dict type

　　When `enableHoverListen=True`, it is used to *listen to the row record dictionary corresponding to the most recent mouse enter event*.

**emptyContent:** Component type

　　Used to *customize the prompt message when the current table data record is empty*.

**containerId:** String type

　　Used to *set the reference container ID for various floating elements in the current table*, in order to solve issues such as floating elements within a local container not following scroll.

**cellUpdateOptimize:** Boolean type, default is `False`

　　Used to *determine whether to enable cell content rendering optimization and acceleration for the current table*. When enabled, if the source data for a cell, identified by the row `key` and column `dataIndex`, remains unchanged when `data` is updated, the cell will not be redrawn, reducing the page refresh overhead. However, this may cause some content refresh issues.

**mode:** String type, default is `'client-side'`

　　Used to *set the table data rendering mode*. Possible values are `'client-side'` (client-side rendering) and `'server-side'` (server-side rendering).

---

**miniChartHeight:** Integer type, default is `30`

　　Used to *set the pixel height for all mini-chart mode related cells in the current table*.

**miniChartAnimation:** Boolean type, default is `False`

　　Used to *determine whether to enable the initialization animation effect for mini-chart mode related cells in the current table*.

**nClicksButton:** Integer type, default is `0`

　　Used to *track the cumulative number of clicks on the buttons in the fields of the current table*.

**clickedContent:** String type

　　Used to *track the content of the most recent button mode related click event*.

**clickedCustom:** *int*, *float*, *string*, *list*, or *dict* type

　　Used to *listen to the custom field information of the button associated with the most recent button mode click event*.

**recentlyButtonClickedDataIndex:** String type

　　Used to *track the `dataIndex` information of the field corresponding to the most recent button mode related click event*.

**recentlyButtonClickedRow:** Dict type

　　Used to *track the row record dictionary corresponding to the most recent button mode related click event*.

**customFormatFuncs:** Dict type

　　Used to *set the corresponding JavaScript function strings for custom format mode fields in the current table*. The keys are the `dataIndex` of the respective fields, and the values are strings.

**recentlyCheckedLabel:** String type

　　Used to *track the label content of the most recent checkbox mode related check event*.

**recentlyCheckedDataIndex:** String type

　　Used to *track the `dataIndex` information of the field corresponding to the most recent checkbox mode related check event*.

**recentlyCheckedStatus:** Boolean type

　　Used to *track the status of the checkbox in the most recent checkbox mode related check event*.

**recentlyCheckedRow:** Dict type

　　Used to *track the row record dictionary corresponding to the most recent checkbox mode related check event*.

**recentlySwitchDataIndex:** String type

　　Used to *track the `dataIndex` information of the field corresponding to the most recent switch mode related event*.

**recentlySwitchStatus:** Boolean type

　　Used to *track the status of the switch in the most recent switch mode related event*.

**recentlySwitchRow:** Dict type

　　Used to *track the row record dictionary corresponding to the most recent switch mode related event*.

**nClicksDropdownItem:** Integer type, default is `0`

　　Used to *track the cumulative number of clicks on the options in the dropdown menu mode related fields of the current table*.

**recentlyClickedDropdownItemTitle:** String type

　　Used to *track the title content of the most recent dropdown menu mode option click event*.

**recentlyDropdownItemClickedDataIndex:** String type

　　Used to *track the `dataIndex` information of the field corresponding to the most recent dropdown menu mode option click event*.

**recentlyDropdownItemClickedRow:** Dict type

　　Used to *track the row record dictionary corresponding to the most recent dropdown menu mode option click event*.

**recentlySelectDataIndex:** String type

　　Used to *track the `dataIndex` information of the field corresponding to the most recent dropdown select mode value update event*.

**recentlySelectValue:** String, Integer, Float, or List type

　　Used to *track the latest value status in the most recent dropdown select mode value update event*.

**recentlySelectRow:** Dict type

　　Used to *track the row record dictionary corresponding to the most recent dropdown select mode value update event*.