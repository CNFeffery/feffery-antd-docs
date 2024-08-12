import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    row_select_radio,  # noqa: F401
    row_select_checkbox,  # noqa: F401
    row_select_callbacks,  # noqa: F401
    row_select_sync_data,  # noqa: F401
    sticky,  # noqa: F401
    title_popover_info,  # noqa: F401
    columns_format_constraint,  # noqa: F401
    text_area_editable,  # noqa: F401
    sort_single,  # noqa: F401
    sort_multiple,  # noqa: F401
    sort_multiple_dynamic,  # noqa: F401
    sort_tooltip,  # noqa: F401
    sort_callbacks,  # noqa: F401
    filter_checkbox,  # noqa: F401
    filter_default_filtered_values,  # noqa: F401
    filter_keyword,  # noqa: F401
    filter_callbacks,  # noqa: F401
    pagination_placement,  # noqa: F401
    pagination_page_size,  # noqa: F401
    pagination_page_size_options,  # noqa: F401
    pagination_show_quick_jumper,  # noqa: F401
    pagination_show_less_items,  # noqa: F401
    pagination_hide_on_single_page,  # noqa: F401
    pagination_simple,  # noqa: F401
    pagination_disabled,  # noqa: F401
    pagination_false,  # noqa: F401
    summary_basic,  # noqa: F401
    summary_fixed_bottom,  # noqa: F401
    summary_fixed_top,  # noqa: F401
    conditional_style,  # noqa: F401
    expand_basic,  # noqa: F401
    expand_default,  # noqa: F401
    expand_by_click,  # noqa: F401
    listen_cell_click,  # noqa: F401
    listen_mouse_enter,  # noqa: F401
    custom_empty_content,  # noqa: F401
    container_id,  # noqa: F401
    nested_data,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'row_select_radio',
        'title': '行选择：单选模式',
        'description': fac.AntdParagraph('单选型行选择功能。'),
    },
    {
        'path': 'row_select_checkbox',
        'title': '行选择：多选模式',
        'description': fac.AntdParagraph('多选型行选择功能。'),
    },
    {
        'path': 'row_select_callbacks',
        'title': '行选择：回调监听',
        'description': fac.AntdParagraph('在回调函数中监听行选择相关事件。'),
    },
    {
        'path': 'row_select_sync_data',
        'title': '行选择：同步数据变化',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('selectedRowsSyncWithData=True', code=True),
                '后，针对表格数据源的更新会根据当前的',
                fac.AntdText('selectedRowKeys', code=True),
                '状态，对',
                fac.AntdText('selectedRows', code=True),
                '信息进行同步刷新（使用此项功能时请确保原始输入数据源各行记录手动设置了键值对key）。',
            ]
        ),
    },
    {
        'path': 'sticky',
        'title': '粘性表头',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('sticky=True', code=True),
                '后，针对高度超过视口高度的表格，将在浏览表格时自动进行恰当的表头吸顶。',
            ]
        ),
    },
    {
        'path': 'title_popover_info',
        'title': '字段标题添加额外信息',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('titlePopoverInfo', code=True),
                '为对应字段快捷添加额外说明信息。',
            ]
        ),
    },
    {
        'path': 'columns_format_constraint',
        'title': '编辑模式格式校验',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('columnsFormatConstraint', code=True),
                '为对应字段配合单元格编辑模式下的内容校验正则表达式规则。',
            ]
        ),
    },
    {
        'path': 'text_area_editable',
        'title': '文本域编辑模式',
        'description': fac.AntdParagraph(
            [
                '文本域编辑模式下，',
                fac.AntdText('enter', keyboard=True),
                '键的按下将不会退出当前输入框，而是会进行换行。',
            ]
        ),
    },
    {
        'path': 'sort_single',
        'title': '字段排序：单字段',
        'description': fac.AntdParagraph('基于单个字段进行排序。'),
    },
    {
        'path': 'sort_multiple',
        'title': '字段排序：多字段组合',
        'description': fac.AntdParagraph(
            '基于多个字段的固定顺序进行组合排序。'
        ),
    },
    {
        'path': 'sort_multiple_dynamic',
        'title': '字段排序：多字段动态组合',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('"multiple": "auto"', code=True),
                '后，多字段组合排序的字段优先级顺序将动态遵循用户的排序点击顺序。',
            ]
        ),
    },
    {
        'path': 'sort_tooltip',
        'title': '字段排序：额外信息提示',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('showSorterTooltip', code=True),
                '、',
                fac.AntdText('showSorterTooltipTarget', code=True),
                '控制可排序字段表头的额外信息提示。',
            ]
        ),
    },
    {
        'path': 'sort_callbacks',
        'title': '字段排序：回调监听',
        'description': fac.AntdParagraph('通过回调函数监听排序事件。'),
    },
    {
        'path': 'filter_checkbox',
        'title': '字段筛选：勾选模式',
        'description': fac.AntdParagraph('通过勾选选项进行字段筛选。'),
    },
    {
        'path': 'filter_default_filtered_values',
        'title': '行选择：默认选中项',
        'description': fac.AntdParagraph('为字段筛选功能设置默认选中项。'),
    },
    {
        'path': 'filter_keyword',
        'title': '字段筛选：搜索模式',
        'description': fac.AntdParagraph('通过关键词搜索进行字段筛选。'),
    },
    {
        'path': 'pagination_placement',
        'title': '分页：控件位置',
        'description': fac.AntdParagraph('分页控件的不同显示位置。'),
    },
    {
        'path': 'pagination_page_size',
        'title': '分页：每页记录数',
        'description': fac.AntdParagraph('控制每页显示的最大记录数量。'),
    },
    {
        'path': 'pagination_page_size_options',
        'title': '分页：允许用户调整每页记录数',
        'description': fac.AntdParagraph(
            '渲染控件供用户调整每页显示的最大记录数量。'
        ),
    },
    {
        'path': 'pagination_show_quick_jumper',
        'title': '分页：开启快捷跳页功能',
        'description': fac.AntdParagraph(
            '渲染控件供用户输入页码进行快捷跳页。'
        ),
    },
    {
        'path': 'pagination_show_less_items',
        'title': '分页：显示较少的跳页按钮',
        'description': fac.AntdParagraph('优先显示数量更少的跳页按钮。'),
    },
    {
        'path': 'pagination_hide_on_single_page',
        'title': '分页：单页自动隐藏控件',
        'description': fac.AntdParagraph('单页数据时自动隐藏分页相关控件。'),
    },
    {
        'path': 'pagination_simple',
        'title': '分页：简洁模式',
        'description': fac.AntdParagraph('渲染简洁风格的分页控件。'),
    },
    {
        'path': 'pagination_disabled',
        'title': '分页：禁用状态',
        'description': fac.AntdParagraph('以禁用状态显示分页控件。'),
    },
    {
        'path': 'pagination_false',
        'title': '分页：关闭分页功能',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('pagination=False', code=True),
                '关闭分页功能。',
            ]
        ),
    },
    {
        'path': 'summary_basic',
        'title': '总结栏：基础使用',
        'description': fac.AntdParagraph('在表格底部渲染总结栏。'),
    },
    {
        'path': 'summary_fixed_bottom',
        'title': '总结栏：固定在底部',
        'description': fac.AntdParagraph('将总结栏固定在表格底部。'),
    },
    {
        'path': 'summary_fixed_top',
        'title': '总结栏：固定在顶部',
        'description': fac.AntdParagraph('将总结栏固定在表格顶部。'),
    },
    {
        'path': 'conditional_style',
        'title': '单元格条件样式',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('conditionalStyleFuncs', code=True),
                '对指定字段进行单元格条件样式渲染规则控制。',
            ]
        ),
    },
    {
        'path': 'expand_basic',
        'title': '行展开：基础使用',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('expandedRowKeyToContent', code=True),
                '为指定行渲染行展开内容。',
            ]
        ),
    },
    {
        'path': 'expand_default',
        'title': '行展开：初始化展开行',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('defaultExpandedRowKeys', code=True),
                '控制初始化需要处于展开状态的行展开内容。',
            ]
        ),
    },
    {
        'path': 'expand_by_click',
        'title': '行展开：点击整行触发展开',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('expandRowByClick=True', code=True),
                '后，点击整行即可触发行展开。',
            ]
        ),
    },
    {
        'path': 'listen_cell_click',
        'title': '监听单元格点击事件',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('enableCellClickListenColumns', code=True),
                '设置需要启用单元格点击事件监听的字段。',
            ]
        ),
    },
    {
        'path': 'listen_mouse_enter',
        'title': '监听鼠标移入事件',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('enableHoverListen=True', code=True),
                '后开启表格内部鼠标移入事件监听。',
            ]
        ),
    },
    {
        'path': 'custom_empty_content',
        'title': '自定义空内容',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('emptyContent', code=True),
                '自定义空数据提示内容。',
            ]
        ),
    },
    {
        'path': 'container_id',
        'title': '局部容器内悬浮层显示矫正',
        'description': fac.AntdParagraph(
            [
                '与表格部分功能有关的悬浮层控件，譬如字段筛选对应的下拉菜单等，默认是以页面根节点为滚动事件参考容器，因此当表格置于局部容器内时，已展开的悬浮层控件会不跟随局部容器滑轮滚动事件移动，这种情况下可以设置参数',
                fac.AntdText('containerId="局部容器id"', code=True),
                '来进行优化。',
            ]
        ),
    },
    {
        'path': 'nested_data',
        'title': '行数据嵌套',
        'description': fac.AntdParagraph(
            [
                '在定义参数',
                fac.AntdText('data', code=True),
                '时可通过键值对属性',
                fac.AntdText('children', code=True),
                '向下嵌套展示行记录。',
            ]
        ),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
