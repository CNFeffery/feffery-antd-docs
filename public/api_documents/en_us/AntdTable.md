- id (string; optional):
  Unique id of the component.

- key (string; optional):
  Update the `key` value of the current component to force re-rendering.

- className (string; optional):
  CSS class name of the component.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru'; default 'zh-cn'):
  Language for component text. Options: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'ru-ru'` (Russian).
  Default: `'zh-cn'`.

- containerId (string; optional):
  When the table is rendered in a scrollable container, specify the container id to avoid abnormal behavior of expanded rows when scrolling.

- columns (list of dicts; optional):
  Configure column definitions.

  `columns` is a list of dicts with keys:

  - title (a list of or a singular dash component, string or number; required):
    Required. Current column title.

  - dataIndex (string; required):
    Required. Unique identifier of the column.

  - group (string | list of strings; optional):
    Group information of the column, used for rendering multi-level headers.

  - renderOptions (dict; optional):
    Configure [re-render mode](/AntdTable-rerender) parameters.

    `renderOptions` is a dict with keys:

    - renderType (a value equal to: 'link', 'ellipsis', 'copyable', 'ellipsis-copyable', 'tags', 'status-badge', 'image', 'custom-format', 'corner-mark', 'row-merge', 'dropdown', 'dropdown-links', 'image-avatar', 'mini-line', 'mini-bar', 'mini-progress', 'mini-ring-progress', 'mini-area', 'button', 'checkbox', 'switch', 'select'; optional):
      Re-render type. Options: `'link'`, `'ellipsis'`, `'copyable'`, `'ellipsis-copyable'`, `'tags'`, `'status-badge'`, `'image'`,
      `'custom-format'`, `'corner-mark'`, `'row-merge'`, `'dropdown'`, `'dropdown-links'`, `'image-avatar'`,
      `'mini-line'`, `'mini-bar'`, `'mini-progress'`, `'mini-ring-progress'`, `'mini-area'`,
      `'button'`, `'checkbox'`, `'switch'`, `'select'`.

    - renderLinkText (string; optional):
      When `renderType='link'`, set link text content.

    - renderButtonSplit (boolean; optional):
      When `renderType='button'`, whether to add dividers between multiple buttons.

    - renderButtonPopConfirmProps (dict; optional):
      When `renderType='button'`, configure confirmation popup parameters.

      `renderButtonPopConfirmProps` is a dict with keys:

      - title (string; optional):
        Confirmation popup title.

      - okText (string; optional):
        Confirmation button text.

      - cancelText (string; optional):
        Cancel button text.

    - miniChartColor (string; optional):
      For `renderType='mini-line'`, `'mini-area'`, `'mini-bar'`, set chart color.

    - tooltipCustomContent (string; optional):
      For `renderType='mini-line'`, `'mini-area'`, `'mini-bar'`, JavaScript function string for tooltip content.

    - progressOneHundredPercentColor (string; optional):
      For `renderType='mini-progress'`, `'mini-ring-progress'`, fill color when progress reaches 100%.

    - progressShowPercent (boolean; optional):
      For `renderType='mini-progress'`, whether to show percent text.
      Default: `False`.

    - progressPercentPrecision (number; optional):
      For `renderType='mini-progress'`, number of decimal places for percent text. Default keeps original precision.

    - progressPercentPosition (dict; optional):
      For `renderType='mini-progress'`, position of percent text.

      `progressPercentPosition` is a dict with keys:

      - align (a value equal to: 'start', 'center', 'end'; optional):
        Alignment. Options: `'start'`, `'center'`, `'end'`.

      - type (a value equal to: 'inner', 'outer'; optional):
        Position. Options: `'inner'`, `'outer'`.

    - progressStrokeLinecap (a value equal to: 'square', 'round'; optional):
      For `renderType='mini-progress'`, progress bar cap style. Options: `'square'`, `'round'`.
      Default: `'square'`.

    - progressSize (number; optional):
      For `renderType='mini-progress'`, set pixel size.

    - progressColor (dict; optional):
      For `renderType='mini-progress'`, progress bar color. Supports gradient with keys `'from'`, `'to'`.

      `progressColor` is a string

      Or dict with keys:

  - from (string; optional):
    Gradient start color.

  - to (string; optional):
    Gradient end color.

    - ringProgressFontSize (number; optional):
      For `renderType='mini-ring-progress'`, font size of percent text.

    - dropdownProps (dict; optional):
      For `renderType='dropdown'`, `'dropdown-links'`, configure dropdown menu parameters.

      `dropdownProps` is a dict with keys:

      - title (string; optional):
        Dropdown anchor title.

      - arrow (boolean; optional):
        Whether to show arrow. Default: `False`.

      - disabled (boolean; optional):
        Whether to disable dropdown globally. Lower priority than per-item settings.

      - overlayClassName (string; optional):
        CSS class name of dropdown container.

      - overlayStyle (dict; optional):
        CSS style of dropdown container.

      - placement (a value equal to: 'bottomLeft', 'bottomCenter', 'bottomRight', 'topLeft', 'topCenter', 'topRight'; optional):
        Dropdown placement. Options: `'bottomLeft'`, `'bottomCenter'`, `'bottomRight'`, `'topLeft'`, `'topCenter'`, `'topRight'`.

  - fixed (a value equal to: 'left', 'right' | boolean; optional):
    Column fixed direction. Options: `'left'`, `'right'`. `True` = `'left'`.

  - editable (boolean; optional):
    Whether the column is editable. Default: `False`.

  - editOptions (dict; optional):
    Configure editable input box parameters.

    `editOptions` is a dict with keys:

    - mode (a value equal to: 'default', 'text-area'; optional):
      Input mode. Options: `'default'`, `'text-area'`. Default: `'default'`.

    - autoSize (dict; optional):
      When `mode='textarea'`, configure auto resize. Same as `AntdInput`.
      Default: `False`.

      `autoSize` is a boolean

      Or dict with keys:

  - minRows (number; optional)

  - maxRows (number; optional)

    - maxLength (number; optional):
      Max characters in editable input. Default: unlimited.

    - placeholder (string; optional):
      Placeholder text when empty.

    - disabledKeys (list of strings; optional):
      List of row `key` values to disable input.

  - align (a value equal to: 'left', 'center', 'right'; optional):
    Column alignment. Options: `'left'`, `'center'`, `'right'`. Default: `'center'`.

  - headerAlign (a value equal to: 'left', 'center', 'right'; optional):
    Header alignment. Follows column alignment by default. Options: `'left'`, `'center'`, `'right'`.
    Default: `'center'`.

  - width (number | string; optional):
    Column width.

  - minWidth (number | string; optional):
    Minimum width. Only effective when `tableLayout="auto"`.

  - hidden (boolean; optional):
    Whether to hide the column. Default: `False`.

  - className (string; optional):
    Column CSS class name.

  - defaultSortOrder (a value equal to: 'ascend', 'descend'; optional):
    Default sort order when initializing. Options: `'ascend'`, `'descend'`.

  - filterResetToDefaultFilteredValue (boolean; optional):
    If default filter values are set via `defaultFilteredValues`, whether reset restores them.
    Default: `False`.

- showHeader (boolean; default True):
  Whether to display table header. Default: `True`.

- rowHoverable (boolean; default True):
  Whether rows have hover effect. Default: `True`.

- tableLayout (a value equal to: 'auto', 'fixed'; optional):
  When column widths are not set, control width allocation. Options: `'auto'`, `'fixed'`.

- data (list of dicts; optional):
  Define table data source, corresponding to `columns`.

  `data` is a list of dicts with strings as keys and values of type
  list of boolean | number | string | dict | lists | a list of or a
  singular dash component, string or number | string | number |
  boolean | dict with keys:

  - content (string; optional):
    For `'link'` mode, link text content. Overrides `renderLinkText` in column config.

  - href (string; optional):
    For `'link'` mode, link address.

  - target (string; optional):
    For `'link'` mode, link target. Default: `'_blank'`.

  - disabled (boolean; optional):
    For `'link'` mode, whether the link is disabled. Default: `False`.

    Or list of numbers | dict with keys:

  - color (string; optional):
    For `'tags'` mode, tag color.

  - tag (string | number; optional):
    For `'tags'` mode, tag content. | list of dicts with keys:

  - color (string; optional):
    For `'tags'` mode, tag color.

  - tag (string | number; optional):
    For `'tags'` mode, tag content. | dict with keys:

  - disabled (boolean; optional):
    For `'button'` mode, same as parameter in `AntdButton`.

  - type (a value equal to: 'primary', 'ghost', 'dashed', 'link', 'text', 'default'; optional):
    For `'button'` mode, same as parameter in `AntdButton`.

    - color (a value equal to: 'default', 'primary', 'danger', 'blue', 'purple', 'cyan', 'green', 'magenta', 'pink', 'red', 'orange', 'yellow', 'volcano', 'geekblue', 'lime', 'gold'; optional):
      For `'button'` mode, same as parameter in `AntdButton`.

    - variant (a value equal to: 'outlined', 'dashed', 'solid', 'filled', 'text', 'link'; optional):
      For `'button'` mode, same as parameter in `AntdButton`.

    - danger (boolean; optional):
      For `'button'` mode, same as parameter in `AntdButton`.

    - style (dict; optional):
      For `'button'` mode, same as parameter in `AntdButton`.

    - content (string; optional):
      For `'button'` mode, button text content.

    - href (string; optional):
      For `'button'` mode, same as parameter in `AntdButton`.

    - target (string; optional):
      For `'button'` mode, same as parameter in `AntdButton`.

    - popConfirmProps (dict; optional):
      For `'button'` mode, configure confirmation popup parameters for the button (higher priority).

      `popConfirmProps` is a dict with keys:

      - title (string; optional):
        Confirmation popup title.

      - okText (string; optional):
        Confirmation button text.

      - cancelText (string; optional):
        Cancel button text.

    - icon (string; optional):
      For `'button'` mode, button prefix icon type. If `iconRenderer='AntdIcon'`, same as `AntdIcon`; if `iconRenderer='fontawesome'`, CSS class name.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
      For `'button'` mode, rendering method for button prefix icon.

    - tooltip (dict; optional):
      For `'button'` mode, add tooltip.

      `tooltip` is a dict with keys:

      - title (string; optional):
        Tooltip text.

      - placement (a value equal to: 'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'; optional):
        Tooltip placement. Default: `'top'`.

    - custom (boolean | number | string | dict | list; optional):
      For `'button'` mode, extra information.

    - status (a value equal to: 'success', 'processing', 'default', 'error', 'warning'; optional):
      For `'status-badge'` mode, badge status.

    - text (string | number; optional):
      For `'status-badge'` mode, badge text.

    - src (string; optional):
      For `'image'` mode, image URL.

    - height (string | number; optional):
      For `'image'` mode, image height.

    - preview (boolean; optional):
      For `'image'` mode, whether image is previewable. Default: `True`.

    - placement (a value equal to: 'top-left', 'top-right', 'bottom-left', 'bottom-right'; optional):
      For `'corner-mark'` mode, badge position.

    - color (string; optional):
      For `'corner-mark'` mode, badge color. Default: `'#1890ff'`.

    - content (number | string; optional):
      For `'corner-mark'` mode, cell value.

    - offsetX (number; optional):
      For `'corner-mark'` mode, horizontal offset.

    - offsetY (number; optional):
      For `'corner-mark'` mode, vertical offset.

    - hide (boolean; optional):
      For `'corner-mark'` mode, whether to hide. Default: `False`.

    - checked (boolean; optional):
      For `'checkbox'` mode, checked status.

    - disabled (boolean; optional):
      For `'checkbox'` mode, disabled state.

    - label (string; optional):
      For `'checkbox'` mode, label text.

    - custom (boolean | number | string | dict | list; optional):
      For `'checkbox'` mode, extra information.

    - checked (boolean; optional):
      For `'switch'` mode, switch state.

    - disabled (boolean; optional):
      For `'switch'` mode, disabled state.

    - checkedChildren (string; optional):
      For `'switch'` mode, text when on.

    - unCheckedChildren (string; optional):
      For `'switch'` mode, text when off.

    - custom (boolean | number | string | dict | list; optional):
      For `'switch'` mode, extra information.

    - content (number | string; optional):
      For `'row-merge'` mode, cell value.

    - rowSpan (number; optional):
      For `'row-merge'` mode, number of merged cells.

    - title (string; optional):
      For `'dropdown'` mode, dropdown item text.

    - disabled (boolean; optional):
      For `'dropdown'` mode, whether dropdown item is disabled.

    - icon (string; optional):
      For `'dropdown'` mode, button prefix icon type.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
      For `'dropdown'` mode, icon rendering method.

    - custom (boolean | number | string | dict | list; optional):
      For `'dropdown'` mode, extra information.

    - isDivider (boolean; optional):
      For `'dropdown'` mode, whether item is divider. Default: `False`.

    - title (string; optional):
      For `'dropdown-links'` mode, dropdown item text.

    - href (string; optional):
      For `'dropdown-links'` mode, link URL.

    - disabled (boolean; optional):
      For `'dropdown-links'` mode, disabled.

    - icon (string; optional):
      For `'dropdown-links'` mode, icon type.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
      For `'dropdown-links'` mode, icon rendering method.

    - isDivider (boolean; optional):
      For `'dropdown-links'` mode, whether divider. Default: `False`.

    - src (string; optional):
      For `'image-avatar'` mode, avatar image URL.

    - size (dict; optional):
      For `'image-avatar'` mode, avatar size. Number = px, string = preset size (`'small'`, `'default'`, `'large'`). Supports responsive. Default: `'default'`.

      `size` is a number | 'large' | 'small' | 'default' | dict with keys: xs, sm, md, lg, xl, xxl.

    - shape (a value equal to: 'circle', 'square'; optional):
      For `'image-avatar'` mode, avatar shape. Default: `'circle'`.

    - className (string; optional):
      For `'select'` mode, CSS class name.

    - style (dict; optional):
      For `'select'` mode, CSS style. Default width: `'100%'`.

    - options (list of dicts; optional):
      For `'select'` mode, dropdown options.

      `options` is a list of dicts with keys:

      - label (string; optional):
        Option text.

      - value (string | number; optional):
        Option value.

    - listHeight (number; optional):
      For `'select'` mode, dropdown menu height. Default: `256`.

    - mode (a value equal to: 'multiple', 'tags'; optional):
      For `'select'` mode, selection mode. Default: single.

    - disabled (boolean; optional):
      For `'select'` mode, disabled state.

    - size (a value equal to: 'small', 'middle', 'large'; optional):
      For `'select'` mode, size. Default: `'middle'`.

    - bordered (boolean; optional):
      For `'select'` mode, whether bordered. Default: `True`.

    - placeholder (string; optional):
      For `'select'` mode, placeholder text.

    - placement (a value equal to: 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'; optional):
      For `'select'` mode, dropdown placement. Default: `'bottomLeft'`.

    - value (string | number | list of string | numbers; optional):
      For `'select'` mode, selected value(s).

    - maxTagCount (number | 'responsive'; optional):
      For `'select'` mode, max number of tags shown. Default: `5`.

    - optionFilterProp (a value equal to: 'value', 'label'; optional):
      For `'select'` mode, search target field. Default: `'value'`.

    - allowClear (boolean; optional):
      For `'select'` mode, allow clearing. Default: `True`.

- bordered (boolean; default False):
  Whether to render table borders. Default: `False`.

- maxHeight (number | string; optional):
  Maximum table height in pixels. When actual height exceeds this, a vertical scrollbar is rendered.

- maxWidth (number | string | boolean; optional):
  Maximum table width. When actual width exceeds this, a horizontal scrollbar is rendered.

- scrollToFirstRowOnChange (boolean; default True):
  After pagination, sorting, or filtering triggers table change, whether to scroll to the top. Default: `True`.

- size (a value equal to: 'small', 'middle', 'large'; default 'middle'):
  Table cell size. Options: `'small'`, `'middle'`, `'large'`.

- rowSelectionType (a value equal to: 'checkbox', 'radio'; optional):
  Row selection mode. Options: `'checkbox'` (multi-select), `'radio'` (single-select). Default: disabled.

- selectedRowKeys (list of string | numbers; optional):
  Track selected row `key` values.

- selectedRows (list; optional):
  Track selected row records.

- rowSelectionWidth (string | number; default 32):
  Width of row selection column. Default: `32`.

- rowSelectionCheckStrictly (boolean; optional):
  For nested rows, whether selection of parent and child rows are independent. Default: `True`.

- rowSelectionIgnoreRowKeys (list of string | numbers; optional):
  Specify row `key` values that cannot be selected.

- selectedRowsSyncWithData (boolean; default False):
  When data source `data` updates, whether to sync `selectedRows` based on current `selectedRowKeys`.
  Default: `False`.

- sticky (dict; default False):
  Configure sticky header. Default: `False`.

  `sticky` is a boolean | dict with keys:

  - offsetHeader (number; optional):
    Vertical offset for sticky header.

  - offsetScroll (number; optional):
    Vertical offset for bottom scrollbar in sticky header.

- enableHoverListen (boolean; default False):
  Enable row mouse enter/leave event listening. May affect other features. Default: `False`.

- recentlyMouseEnterColumnDataIndex (string; optional):
  When `enableHoverListen=True`, track `dataIndex` of most recently hovered column.

- recentlyMouseEnterRowKey (string | number; optional):
  When `enableHoverListen=True`, track `key` of most recently hovered row.

- recentlyMouseEnterRow (dict; optional):
  When `enableHoverListen=True`, track record of most recently hovered row.

- titlePopoverInfo (dict; optional):
  Configure extra popover info for column titles.

  `titlePopoverInfo` is a dict with strings as keys and values of type dict with keys:

  - title (string; optional):
    Popover title.

  - content (string; optional):
    Popover content.

  - placement (a value equal to: 'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight', 'leftTop', 'leftBottom', 'rightTop', 'rightBottom'; optional):
    Popover placement. Options: `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`, `'leftTop'`, `'leftBottom'`, `'rightTop'`, `'rightBottom'`.
    Default: `'bottom'`.

  - overlayStyle (dict; optional):
    CSS style for popover overlay.

- columnsFormatConstraint (dict; optional):
  For editable fields, configure regex-based input validation rules.

  `columnsFormatConstraint` is a dict with strings as keys and values of type dict with keys:

  - rule (string; optional):
    Regular expression to validate input format.

  - content (string; optional):
    Message shown when validation fails.

- sortOptions (dict; optional):
  Configure sorting features.

  `sortOptions` is a dict with keys:

  - sortDataIndexes (list of strings; optional):
    Columns (`dataIndex`) involved in sorting. Order of array defines priority (high to low).

  - multiple (boolean | 'auto'; optional):
    Enable multi-column sorting. `'auto'` = auto multi-sort based on click order.
    Default: `False`.

  - forceCompareModes (dict with strings as keys and values of type 'number' | 'custom'; optional):
    Force sorting mode per column. Options: `'number'` (numeric), `'custom'` (custom).

  - customOrders (dict with strings as keys and values of type list; optional):
    When `forceCompareModes='custom'`, define custom sort order for column values.

- showSorterTooltip (boolean; default True):
  For sortable columns, whether to show tooltip on hover. Default: `True`.

- showSorterTooltipTarget (a value equal to: 'full-header', 'sorter-icon'; default 'full-header'):
  Tooltip hover target. Options: `'full-header'`, `'sorter-icon'`.
  Default: `'full-header'`.

- filterOptions (dict; optional):
  Configure filtering features.

  `filterOptions` is a dict with strings as keys and values of type dict with keys:

  - filterMode (a value equal to: 'checkbox', 'keyword', 'tree'; optional):
    Filter mode. Options: `'checkbox'`, `'keyword'`, `'tree'`. `'tree'` mode requires `filterCustomTreeItems`.
    Default: `'checkbox'`.

  - filterCustomItems (list | boolean | number | string | dict | list; optional):
    For `'checkbox'` mode, define custom filter items.

  - filterCustomTreeItems (list of dicts; optional):
    For `'tree'` mode, define custom tree structure.

  - filterMultiple (boolean; optional):
    For `'checkbox'` mode, whether multi-select is enabled. Default: `True`.

  - filterSearch (boolean; optional):
    For `'checkbox'` mode, whether search box is enabled. Default: `False`.

- defaultFilteredValues (dict with strings as keys and values of type list; optional):
  Default filter values for fields.

- pagination (dict; optional):
  Configure pagination. Set `False` to disable.

  `pagination` is a dict with keys:

  - position (a value equal to: 'topLeft', 'topCenter', 'topRight', 'bottomLeft', 'bottomCenter', 'bottomRight'; optional):
    Pagination component placement. Default: `'bottomRight'`.

  - pageSize (number; optional):
    Track or set max rows per page.

  - current (number; optional):
    Track or set current page number.

  - showSizeChanger (boolean; optional):
    Show pageSize switcher. Default: `True` if total rows > 50.

  - pageSizeOptions (list of numbers; optional):
    Options for pageSize switcher.

  - showTitle (boolean; optional):
    Whether to show native browser tooltip on page number hover. Default: `True`.

  - showQuickJumper (boolean; optional):
    Whether to render quick jump control. Default: `False`.

  - showTotalPrefix (string; optional):
    Prefix text for total records description.

  - showTotalSuffix (string; optional):
    Suffix text for total records description.

  - hideOnSinglePage (boolean; optional):
    Hide pagination if rows < one page. Default: `False`.

  - simple (boolean; optional):
    Enable simple mode. Default: `False`.

  - disabled (boolean; optional):
    Disable pagination controls. Default: `False`.

  - size (a value equal to: 'default', 'small'; optional):
    Pagination control size. Default: `'default'`.

  - total (number; optional):
    Manually set total rows, usually with [server-side mode](/AntdTable-server-side-mode).

  - showLessItems (boolean; optional):
    Prefer fewer jump items. Default: `False`.

- currentData (list; optional):
  Track table data after edits.

- recentlyChangedRow (dict; optional):
  Track row most recently edited.

- recentlyChangedColumn (string; optional):
  Track `dataIndex` of most recently edited column.

- sorter (dict; optional):
  Track sort behavior.

  `sorter` is a dict with keys:

  - columns (list of strings; optional):
    Track sorted columns (`dataIndex`).

  - orders (list of a value equal to: 'ascend', 'descend'; optional):
    Track sort order. `'ascend'` = ascending, `'descend'` = descending.

- filter (dict; optional):
  Track filter behavior.

- mode (a value equal to: 'client-side', 'server-side'; default 'client-side'):
  Data load mode. Options: `'client-side'` (client), `'server-side'` (server). Server mode fits large datasets. Default: `'client-side'`.

- summaryRowContents (list of dicts; optional):
  Configure summary row contents.

  `summaryRowContents` is a list of dicts with keys:

  - content (a list of or a singular dash component, string or number; optional):
    Component, summary cell content.

  - colSpan (number; optional):
    Number of columns spanned by cell. Default: `1`.

  - align (a value equal to: 'left', 'center', 'right'; optional):
    Column alignment. Options: `'left'`, `'center'`, `'right'`.

- summaryRowBlankColumns (number; default 0):
  Number of blank columns per summary row. For use with row selection, etc. Default: `0`.

- summaryRowFixed (boolean | a value equal to: 'top', 'bottom'; default False):
  Whether to fix summary row. Options: `'top'`, `'bottom'`. Default: `False`.

- conditionalStyleFuncs (dict with strings as keys and values of type string; optional):
  Configure conditional formatting JavaScript functions per column.

- expandedRowKeyToContent (list of dicts; optional):
  Configure expanded row content. Key = row `key`, value = expanded content.

  `expandedRowKeyToContent` is a list of dicts with keys:

  - key (string | number; required)

  - content (a list of or a singular dash component, string or number; optional)

- expandedRowWidth (string | number; optional):
  Width of expanded row control column.

- expandRowByClick (boolean; default False):
  Allow expanding row by clicking directly. Default: `False`.

- defaultExpandedRowKeys (list of strings; optional):
  Keys of rows expanded by default.

- expandedRowKeys (list of strings; optional):
  Track or set expanded row keys.

- enableCellClickListenColumns (list of strings; optional):
  Enable cell click/double-click/right-click event listening. Default: `False`.

- recentlyCellClickColumn (string; optional):
  When enabled, track `dataIndex` of most recent cell click.

- recentlyCellClickRecord (dict; optional):
  When enabled, track record of most recent cell click.

- nClicksCell (number; default 0):
  When enabled, track cumulative number of cell clicks. Default: `0`.

- cellClickEvent (dict; optional):
  When enabled, track details of most recent cell click.

  `cellClickEvent` is a dict with keys:

  - pageX (number; optional):
    X coordinate relative to page top-left.

  - pageY (number; optional):
    Y coordinate relative to page top-left.

  - clientX (number; optional):
    X coordinate relative to browser window.

  - clientY (number; optional):
    Y coordinate relative to browser window.

  - screenX (number; optional):
    X coordinate relative to screen.

  - screenY (number; optional):
    Y coordinate relative to screen.

  - timestamp (number; optional):
    Event timestamp.

- recentlyCellDoubleClickColumn (string; optional):
  Track `dataIndex` of most recent cell double-click.

- recentlyCellDoubleClickRecord (dict; optional):
  Track record of most recent cell double-click.

- nDoubleClicksCell (number; default 0):
  Track cumulative cell double-clicks. Default: `0`.

- cellDoubleClickEvent (dict; optional):
  Track details of most recent cell double-click.

  `cellDoubleClickEvent` is a dict with keys:

  - pageX (number; optional):
    X coordinate relative to page.

  - pageY (number; optional):
    Y coordinate relative to page.

  - clientX (number; optional):
    X coordinate relative to window.

  - clientY (number; optional):
    Y coordinate relative to window.

  - screenX (number; optional):
    X coordinate relative to screen.

  - screenY (number; optional):
    Y coordinate relative to screen.

  - timestamp (number; optional):
    Event timestamp.

- recentlyContextMenuClickColumn (string; optional):
  Track `dataIndex` of most recent cell right-click.

- recentlyContextMenuClickRecord (dict; optional):
  Track record of most recent cell right-click.

- nContextMenuClicksCell (number; default 0):
  Track cumulative cell right-clicks. Default: `0`.

- cellContextMenuClickEvent (dict; optional):
  Track details of most recent cell right-click.

  `cellContextMenuClickEvent` is a dict with keys:

  - pageX (number; optional):
    X coordinate relative to page.

  - pageY (number; optional):
    Y coordinate relative to page.

  - clientX (number; optional):
    X coordinate relative to window.

  - clientY (number; optional):
    Y coordinate relative to window.

  - screenX (number; optional):
    X coordinate relative to screen.

  - screenY (number; optional):
    Y coordinate relative to screen.

  - timestamp (number; optional):
    Event timestamp.

- emptyContent (a list of or a singular dash component, string or number; optional):
  Component for custom empty-state content.

- cellUpdateOptimize (boolean; default False):
  Strictly optimize cell rendering based on data. Default: `False`.

- miniChartHeight (number; default 30):
  Set height for mini-chart cells. Default: `30`.

- miniChartAnimation (boolean; default False):
  Enable animation for mini-chart cells. Default: `False`.

- recentlyButtonClickedRow (dict; optional):
  For `'button'` mode, track row of most recent button click.

- nClicksButton (number; default 0):
  For `'button'` mode, track cumulative button clicks. Default: `0`.

- clickedContent (string; optional):
  For `'button'` mode, track text of most recent button click.

- clickedCustom (boolean | number | string | dict | list; optional):
  For `'button'` mode, track `custom` field of most recent button click.

- recentlyButtonClickedDataIndex (string; optional):
  For `'button'` mode, track `dataIndex` of most recent button click.

- customFormatFuncs (dict with strings as keys and values of type string; optional):
  For `'custom-format'` mode, key = `dataIndex`, value = JavaScript pre-processing function.

- recentlyCheckedRow (dict; optional):
  For `'checkbox'` mode, track row of most recent check.

- recentlyCheckedLabel (string; optional):
  For `'checkbox'` mode, track label of most recent check.

- recentlyCheckedDataIndex (string; optional):
  For `'checkbox'` mode, track `dataIndex` of most recent check.

- recentlyCheckedStatus (boolean; optional):
  For `'checkbox'` mode, track status of most recent check.

- recentlySwitchRow (dict; optional):
  For `'switch'` mode, track row of most recent toggle.

- recentlySwitchDataIndex (string; optional):
  For `'switch'` mode, track `dataIndex` of most recent toggle.

- recentlySwitchStatus (boolean; optional):
  For `'switch'` mode, track status of most recent toggle.

- nClicksDropdownItem (number; default 0):
  For `'dropdown'` mode, track cumulative dropdown item clicks.

- recentlyClickedDropdownItemTitle (string; optional):
  For `'dropdown'` mode, track `title` of most recent item clicked.

- recentlyDropdownItemClickedDataIndex (string; optional):
  For `'dropdown'` mode, track `dataIndex` of most recent item clicked.

- recentlyDropdownItemClickedRow (dict; optional):
  For `'dropdown'` mode, track row of most recent item clicked.

- recentlySelectRow (dict; optional):
  For `'select'` mode, track row of most recent value update.

- recentlySelectDataIndex (string; optional):
  For `'select'` mode, track `dataIndex` of most recent value update.

- recentlySelectValue (number | string | list of number | strings; optional):
  For `'select'` mode, track value(s) of most recent update.

- hiddenRowKeys (list of strings; optional):
  Row `key` values to hide. Default: `[]`.

- dataDeepCompare (boolean; optional):
  On re-render, whether to deep compare `data` for optimization. Default: `False`.

- virtual (boolean; default False):
  Enable virtual scrolling. Default: `False`.

- title (a list of or a singular dash component, string or number; optional):
  Component for table title.

- footer (a list of or a singular dash component, string or number; optional):
  Component for table footer.

- loading (boolean; default False):
  Whether to show loading state. Default: `False`.

- rowClassName (dict; optional):
  CSS class for rows. Supports defining JavaScript function via `func`.

  `rowClassName` is a string | dict with keys:

  - func (string; optional):
    JavaScript function string.

- data-_ (string; optional):
  Wildcard for `data-_` attributes.

- aria-\* (string; optional):
