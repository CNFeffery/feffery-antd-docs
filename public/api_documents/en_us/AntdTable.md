- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string; optional):
    CSS class name of the component.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- containerId (string; optional):
    When the table is rendered in a scrollable container, specify the container id to avoid abnormal behavior of expanded rows when scrolling.

- columns (list of dicts; optional):
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
            Re-render type. Options: `'link'`, `'ellipsis'`, `'copyable'`, `'ellipsis-copyable'`, `'tags'`, `'status-badge'`, `'image'`, `'custom-format'`, `'corner-mark'`, `'row-merge'`, `'dropdown'`, `'dropdown-links'`, `'image-avatar'`, `'mini-line'`, `'mini-bar'`, `'mini-progress'`, `'mini-ring-progress'`, `'mini-area'`, `'button'`, `'checkbox'`, `'switch'`, `'select'`.

        - renderLinkText (string; optional):
            When `renderType='link'`, set link text content.

        - likeDccLink (boolean; optional):
            Whether links use `dcc.Link` when `renderType` is `'link'` or `'button'`. Default: `False`.

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
            Chart color when `renderType` is `'mini-line'`, `'mini-area'`, or `'mini-bar'`.

        - tooltipCustomContent (string; optional):
            Tooltip renderer supplied as a `javascript` function string when `renderType` is `'mini-line'`, `'mini-area'`, or `'mini-bar'`.

        - progressOneHundredPercentColor (string; optional):
            Completed progress fill color when `renderType` is `'mini-progress'` or `'mini-ring-progress'`.

        - progressShowPercent (boolean; optional):
            Whether to show the numeric progress for `'mini-progress'` `renderType`. Default: `False`.

        - progressPercentPrecision (number; optional):
            Decimal places of the numeric progress for `'mini-progress'` `renderType`. Preserves the original precision by default.

        - progressPercentPosition (dict; optional):
            Position of the numeric progress for `'mini-progress'` `renderType`.

            `progressPercentPosition` is a dict with keys:

            - align (a value equal to: 'start', 'center', 'end'; optional):
                Alignment. Options: `'start'`, `'center'`, `'end'`.

            - type (a value equal to: 'inner', 'outer'; optional):
                Position. Options: `'inner'`, `'outer'`.

        - progressStrokeLinecap (a value equal to: 'square', 'round'; optional):
            Progress bar shape for `'mini-progress'` `renderType`. Supported values: `'square'`, `'round'`. Default: `'square'`.

        - progressSize (number; optional):
            Progress bar size in pixels for `'mini-progress'` `renderType`.

        - progressColor (dict; optional):
            Progress bar color for `'mini-progress'` `renderType`. Use `'from'` and `'to'` for a gradient.

            `progressColor` is a string

          Or dict with keys:

    - from (string; optional):
        Gradient start color.

    - to (string; optional):
        Gradient end color.

        - ringProgressFontSize (number; optional):
            For `renderType='mini-ring-progress'`, font size of percent text.

        - dropdownProps (dict; optional):
            Dropdown settings for `'dropdown'` or `'dropdown-links'` `renderType`.

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
            Automatic textarea height settings when `mode='textarea'`, as in `AntdInput`. Default: `False`.

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
        Header alignment. Follows column alignment by default. Options: `'left'`, `'center'`, `'right'`. Default: `'center'`.

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
        If default filter values are set via `defaultFilteredValues`, whether reset restores them. Default: `False`.

- showHeader (boolean; default True):
    Whether to display table header. Default: `True`.

- rowHoverable (boolean; default True):
    Whether rows have hover effect. Default: `True`.

- tableLayout (a value equal to: 'auto', 'fixed'; optional):
    Column width allocation when fields in `columns` have no `width`. Supported values: `'auto'`, `'fixed'`.

- data (list of dicts; optional):
    Table data source, corresponding to `columns`.

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
        Whether the link is disabled in `'link'` mode. Default: `False`.

      Or list of numbers | dict with keys:

    - color (string; optional):
        For `'tags'` mode, tag color.

    - tag (string | number; optional):
        For `'tags'` mode, tag content. | dict with keys:

    - tooltip (dict; optional):
        Additional tag tooltip in `'tags'` mode.

        `tooltip` is a dict with keys:

        - title (string; optional):
            Tooltip content.

        - placement (a value equal to: 'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'; optional):
            Tooltip placement. Supported values: `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`, `'leftTop'`, `'leftBottom'`, `'rightTop'`, `'rightBottom'`. Default: `'top'`. | list of dicts with keys:

    - color (string; optional):
        For `'tags'` mode, tag color.

    - tag (string | number; optional):
        For `'tags'` mode, tag content. | dict with keys:

    - tooltip (dict; optional):
        Additional tag tooltip in `'tags'` mode.

        `tooltip` is a dict with keys:

        - title (string; optional):
            Tooltip content.

        - placement (a value equal to: 'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'; optional):
            Tooltip placement. Supported values: `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`, `'leftTop'`, `'leftBottom'`, `'rightTop'`, `'rightBottom'`. Default: `'top'`. | dict with keys:

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
        Button content in `'button'` mode.

    - href (string; optional):
        For `'button'` mode, same as parameter in `AntdButton`.

    - target (string; optional):
        For `'button'` mode, same as parameter in `AntdButton`.

    - popConfirmProps (dict; optional):
        Higher-priority confirmation popup settings for the button in `'button'` mode.

        `popConfirmProps` is a dict with keys:

        - title (string; optional):
            Confirmation popup title.

        - okText (string; optional):
            Confirmation button text.

        - cancelText (string; optional):
            Cancel button text.

    - icon (string; optional):
        Button prefix icon in `'button'` mode. Uses the `AntdIcon` icon property when `iconRenderer` is `'AntdIcon'`, or a CSS class when it is `'fontawesome'`.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
        Button prefix icon renderer in `'button'` mode. Supported values: `'AntdIcon'`, `'fontawesome'`.

    - tooltip (dict; optional):
        Additional button tooltip in `'button'` mode.

        `tooltip` is a dict with keys:

        - title (string; optional):
            Tooltip content.

        - placement (a value equal to: 'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'; optional):
            Tooltip placement. Supported values: `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`, `'leftTop'`, `'leftBottom'`, `'rightTop'`, `'rightBottom'`. Default: `'top'`.

    - custom (boolean | number | string | dict | list; optional):
        Additional information in `'button'` mode. | list of dicts with keys:

    - disabled (boolean; optional):
        For `'button'` mode, same as parameter in `AntdButton`.

    - type (a value equal to: 'primary', 'ghost', 'dashed', 'link', 'text', 'default'; optional):
        For `'button'` mode, same as parameter in `AntdButton`.

    - danger (boolean; optional):
        For `'button'` mode, same as parameter in `AntdButton`.

    - style (dict; optional):
        For `'button'` mode, same as parameter in `AntdButton`.

    - content (string; optional):
        Button content in `'button'` mode.

    - href (string; optional):
        For `'button'` mode, same as parameter in `AntdButton`.

    - target (string; optional):
        For `'button'` mode, same as parameter in `AntdButton`.

    - icon (string; optional):
        Button prefix icon in `'button'` mode. Uses the `AntdIcon` icon property when `iconRenderer` is `'AntdIcon'`, or a CSS class when it is `'fontawesome'`.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
        Button prefix icon renderer in `'button'` mode. Supported values: `'AntdIcon'`, `'fontawesome'`.

    - custom (boolean | number | string | dict | list; optional):
        Additional information in `'button'` mode. | dict with keys:

    - status (a value equal to: 'success', 'processing', 'default', 'error', 'warning'; optional):
        Badge status in `'status-badge'` mode. Supported values: `'success'`, `'processing'`, `'default'`, `'error'`, `'warning'`.

    - text (string | number; optional):
        Status badge label in `'status-badge'` mode. | dict with keys:

    - src (string; optional):
        Image URL in `'image'` mode.

    - height (string | number; optional):
        Image height in `'image'` mode.

    - preview (boolean; optional):
        Whether interactive image preview is allowed in `'image'` mode. Default: `True`. | dict with keys:

    - placement (a value equal to: 'top-left', 'top-right', 'bottom-left', 'bottom-right'; optional):
        Corner mark placement in `'corner-mark'` mode. Supported values: `'top-left'`, `'top-right'`, `'bottom-left'`, `'bottom-right'`.

    - color (string; optional):
        Corner mark color in `'corner-mark'` mode. Default: `'#1890ff'`.

    - content (number | string; optional):
        Cell value content in `'corner-mark'` mode.

    - offsetX (number; optional):
        Horizontal corner mark offset in pixels in `'corner-mark'` mode.

    - offsetY (number; optional):
        Vertical corner mark offset in pixels in `'corner-mark'` mode.

    - hide (boolean; optional):
        Whether to hide the corner mark in `'corner-mark'` mode. Default: `False`. | dict with keys:

    - checked (boolean; optional):
        Checkbox state in `'checkbox'` mode.

    - disabled (boolean; optional):
        Whether the checkbox is disabled in `'checkbox'` mode.

    - label (string; optional):
        Checkbox label in `'checkbox'` mode.

    - custom (boolean | number | string | dict | list; optional):
        Additional information in `'checkbox'` mode. | dict with keys:

    - checked (boolean; optional):
        Current switch state in `'switch'` mode.

    - disabled (boolean; optional):
        Whether the switch is disabled in `'switch'` mode.

    - checkedChildren (string; optional):
        On-state label in `'switch'` mode.

    - unCheckedChildren (string; optional):
        Off-state label in `'switch'` mode.

    - custom (boolean | number | string | dict | list; optional):
        Additional information in `'switch'` mode. | dict with keys:

    - content (number | string; optional):
        Cell value content in `'row-merge'` mode.

    - rowSpan (number; optional):
        Number of following cells merged with the current cell in `'row-merge'` mode. | list of dicts with keys:

    - title (string; optional):
        Dropdown menu item anchor content in `'dropdown'` mode.

    - disabled (boolean; optional):
        Whether the menu item is disabled in `'dropdown'` mode.

    - icon (string; optional):
        Button prefix icon in `'dropdown'` mode. Uses the `AntdIcon` icon property when `iconRenderer` is `'AntdIcon'`, or a CSS class when it is `'fontawesome'`.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
        Button prefix icon renderer in `'dropdown'` mode. Supported values: `'AntdIcon'`, `'fontawesome'`.

    - custom (boolean | number | string | dict | list; optional):
        Additional information in `'dropdown'` mode.

    - isDivider (boolean; optional):
        Whether the item is a divider in `'dropdown'` mode. Default: `False`. | list of dicts with keys:

    - title (string; optional):
        Dropdown menu item anchor content in `'dropdown-links'` mode.

    - href (string; optional):
        Dropdown menu item URL in `'dropdown-links'` mode.

    - disabled (boolean; optional):
        Whether the menu item is disabled in `'dropdown-links'` mode.

    - icon (string; optional):
        Button prefix icon in `'dropdown-links'` mode. Uses the `AntdIcon` icon property when `iconRenderer` is `'AntdIcon'`, or a CSS class when it is `'fontawesome'`.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
        Button prefix icon renderer in `'dropdown-links'` mode. Supported values: `'AntdIcon'`, `'fontawesome'`.

    - isDivider (boolean; optional):
        Whether the item is a divider in `'dropdown-links'` mode. Default: `False`. | dict with keys:

    - src (string; optional):
        Avatar image URL in `'image-avatar'` mode.

    - size (dict; optional):
        Avatar size in `'image-avatar'` mode. Use a number for pixels or a preset size; supports responsive settings. Supported values: `'small'`, `'default'`, `'large'`. Default: `'default'`.

        `size` is a number | a value equal to: 'large', 'small',
        'default' | dict with keys:

        - xs (number; optional)

        - sm (number; optional)

        - md (number; optional)

        - lg (number; optional)

        - xl (number; optional)

        - xxl (number; optional)

    - shape (a value equal to: 'circle', 'square'; optional):
        Avatar shape in `'image-avatar'` mode. Supported values: `'circle'`, `'square'`. Default: `'circle'`. | dict with keys:

    - className (string; optional):
        CSS class name for the selection input in `'select'` mode.

    - style (dict; optional):
        CSS styles for the selection input in `'select'` mode. `width` defaults to `'100%'`.

    - options (list of dicts; optional):
        Selection options in `'select'` mode.

        `options` is a list of dicts with keys:

        - label (string; optional):

            Option title.

        - value (string | number; optional):

            The value of the current option.

    - listHeight (number; optional):
        Dropdown menu height in pixels in `'select'` mode. Default: `256`.

    - mode (a value equal to: 'multiple', 'tags'; optional):
        Selection mode in `'select'` mode: `'multiple'` or `'tags'`; single selection by default.

    - disabled (boolean; optional):
        Whether the selection input is disabled in `'select'` mode.

    - size (a value equal to: 'small', 'middle', 'large'; optional):
        Selection input size in `'select'` mode. Supported values: `'small'`, `'middle'`, `'large'`. Default: `'middle'`.

    - bordered (boolean; optional):
        Whether the selection input has a border in `'select'` mode. Default: `True`.

    - placeholder (string; optional):
        Selection input placeholder in `'select'` mode.

    - placement (a value equal to: 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'; optional):
        Dropdown placement in `'select'` mode. Supported values: `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, `'topRight'`. Default: `'bottomLeft'`.

    - value (string | number | list of string | numbers; optional):
        Selected value in `'select'` mode.

    - maxTagCount (number | a value equal to: 'responsive'; optional):
        Maximum visible selected options in `'select'` mode. Additional selections are hidden. Default: `5`.

    - optionFilterProp (a value equal to: 'value', 'label'; optional):
        Search target field in `'select'` mode. Supported values: `'value'`, `'label'`. Default: `'value'`.

    - allowClear (boolean; optional):
        Whether selected values can be cleared quickly in `'select'` mode. Default: `True`.

    - showSearch (boolean; optional):
        Whether searching is enabled in `'select'` mode. | dict

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
    When data source `data` updates, whether to sync `selectedRows` based on current `selectedRowKeys`. Default: `False`.

- sticky (dict; default False):
    Sticky table header settings. Default: `False`.

    `sticky` is a boolean | dict with keys:

    - belowSelector (string | list of strings; optional):
        Selector for the sticky header's target element. The active sticky header attaches below that element.

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

    `titlePopoverInfo` is a dict with strings as keys and values of
    type dict with keys:

    - title (string; optional):
        Popover title.

    - content (string; optional):
        Popover content.

    - placement (a value equal to: 'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight', 'leftTop', 'leftBottom', 'rightTop', 'rightBottom'; optional):
        Popover placement. Options: `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`, `'leftTop'`, `'leftBottom'`, `'rightTop'`, `'rightBottom'`. Default: `'bottom'`.

    - overlayStyle (dict; optional):
        CSS style for popover overlay.

- columnsFormatConstraint (dict; optional):
    For editable fields, configure regex-based input validation rules.

    `columnsFormatConstraint` is a dict with strings as keys and
    values of type dict with keys:

    - rule (string; optional):
        Regular expression to validate input format.

    - content (string; optional):
        Message shown when validation fails.

- sortOptions (dict; optional):
    Configure sorting features.

    `sortOptions` is a dict with keys:

    - sortDataIndexes (list of strings; optional):
        Columns (`dataIndex`) involved in sorting. Order of array defines priority (high to low).

    - multiple (boolean | a value equal to: 'auto'; optional):
        Enable multi-column sorting. `'auto'` = auto multi-sort based on click order. Default: `False`.

    - forceCompareModes (dict with strings as keys and values of type a value equal to: 'number', 'custom'; optional):
        Force sorting mode per column. Options: `'number'` (numeric), `'custom'` (custom).

    - customOrders (dict with strings as keys and values of type list; optional):
        Custom element order used for sorting a field when `forceCompareModes` is `'custom'`.

- showSorterTooltip (boolean; default True):
    For sortable columns, whether to show tooltip on hover. Default: `True`.

- showSorterTooltipTarget (a value equal to: 'full-header', 'sorter-icon'; default 'full-header'):
    Tooltip hover target. Options: `'full-header'`, `'sorter-icon'`. Default: `'full-header'`.

- filterOptions (dict; optional):
    Configure filtering features.

    `filterOptions` is a dict with strings as keys and values of type
    dict with keys:

    - filterMode (a value equal to: 'checkbox', 'keyword', 'tree'; optional):
        Filter mode. `'tree'` requires `'filterCustomTreeItems'` to define the custom tree menu. Supported values: `'checkbox'`, `'keyword'`, `'tree'`. Default: `'checkbox'`.

    - filterCustomItems (list | boolean | number | string | dict | list; optional):
        Custom filter menu items when `filterMode` is `'checkbox'`.

    - filterCustomTreeItems (list of dicts; optional):
        Custom tree menu structure when `filterMode` is `'tree'`.

    - filterMultiple (boolean; optional):
        Whether multiple selections are allowed when `filterMode` is `'checkbox'`. Default: `True`.

    - filterSearch (boolean; optional):
        Whether to show a search input when `filterMode` is `'checkbox'`. Default: `False`.

- defaultFilteredValues (dict with strings as keys and values of type list; optional):
    Default filter values for fields.

- pagination (dict; optional):
    Configure pagination. Set `False` to disable.

    `pagination` is a dict with keys:

    - position (a value equal to: 'topLeft', 'topCenter', 'topRight', 'bottomLeft', 'bottomCenter', 'bottomRight'; optional):
        Position of the pagination controls. Supported values: `'topLeft'`, `'topCenter'`, `'topRight'`, `'bottomLeft'`, `'bottomCenter'`, `'bottomRight'`. Default: `'bottomRight'`.

    - pageSize (number; optional):
        Track or set max rows per page.

    - current (number; optional):
        Track or set current page number.

    - showSizeChanger (boolean; optional):
        Whether to show the `pageSize` selector. Defaults to `True` when the table has more than 50 records.

    - pageSizeOptions (list of numbers; optional):
        Available options for the `pageSize` selector.

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
        Size of the pagination controls. Supported values: `'small'`, `'default'`. Default: `'default'`.

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

    - orders (list of a value equal to: 'ascend', 'descend's; optional):
        Track sort order. `'ascend'` = ascending, `'descend'` = descending.

- filter (dict; optional):
    Track filter behavior.

- mode (a value equal to: 'client-side', 'server-side'; default 'client-side'):
    Table data loading mode: `'client-side'` or `'server-side'`. Server-side mode is intended for large datasets; see [server-side data loading](/AntdTable-server-side-mode). Default: `'client-side'`.

- summaryRowContents (list of dicts; optional):
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
    `javascript` function strings for conditional rendering of each field.

- expandedRowKeyToContent (list of dicts; optional):
    Expanded row content, keyed by each row's `key` value.

    `expandedRowKeyToContent` is a list of dicts with keys:

    - key (string | number; required)

    - content (a list of or a singular dash component, string or number; optional)

- expandedRowWidth (string | number; optional):
    Width of expanded row control column.

- expandRowByClick (boolean; default False):
    Allow expanding row by clicking directly. Default: `False`.

- defaultExpandedRowKeys (list of strings; optional):
    Initial `key` values of expanded rows.

- expandedRowKeys (list of strings; optional):
    Monitor or set expanded row `key` values.

- enableCellClickListenColumns (list of strings; optional):
    Enable cell click/double-click/right-click event listening. Default: `False`.

- recentlyCellClickColumn (string; optional):
    `dataIndex` of the most recently clicked cell when `enableCellClickListenColumns=True`.

- recentlyCellClickRecord (dict; optional):
    Row data for the most recently clicked cell when `enableCellClickListenColumns=True`.

- nClicksCell (number; default 0):
    Cumulative cell click count when `enableCellClickListenColumns=True`. Default: `0`.

- cellClickEvent (dict; optional):
    Details of the most recent cell click when `enableCellClickListenColumns=True`.

    `cellClickEvent` is a dict with keys:

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

- recentlyCellDoubleClickColumn (string; optional):
    `dataIndex` of the most recently double-clicked cell when `enableCellClickListenColumns=True`.

- recentlyCellDoubleClickRecord (dict; optional):
    Row data for the most recently double-clicked cell when `enableCellClickListenColumns=True`.

- nDoubleClicksCell (number; default 0):
    Cumulative cell double-click count when `enableCellClickListenColumns=True`. Default: `0`.

- cellDoubleClickEvent (dict; optional):
    Details of the most recent cell double-click when `enableCellClickListenColumns=True`.

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
    `dataIndex` of the most recently right-clicked cell when `enableCellClickListenColumns=True`.

- recentlyContextMenuClickRecord (dict; optional):
    Row data for the most recently right-clicked cell when `enableCellClickListenColumns=True`.

- nContextMenuClicksCell (number; default 0):
    Cumulative cell right-click count when `enableCellClickListenColumns=True`. Default: `0`.

- cellContextMenuClickEvent (dict; optional):
    Details of the most recent cell right-click when `enableCellClickListenColumns=True`.

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
    `'custom'` field of the most recently clicked button item in the table's `'button'` rendering mode.

- recentlyButtonClickedDataIndex (string; optional):
    For `'button'` mode, track `dataIndex` of most recent button click.

- customFormatFuncs (dict with strings as keys and values of type string; optional):
    Preprocessing `javascript` function strings for `'custom-format'` rendering, keyed by field `dataIndex`.

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
    For `'switch'` mode, track status of most recent toggle.

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
    Table row CSS class name. Use `func` to define a dynamic `javascript` function.

    `rowClassName` is a string | dict with keys:

    - func (string; optional):
        `javascript` function supplied as a string.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
