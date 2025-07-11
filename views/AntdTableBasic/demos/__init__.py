from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    percentage_column_width,  # noqa: F401
    numeric_column_width,  # noqa: F401
    css_column_width,  # noqa: F401
    max_height_usage,  # noqa: F401
    scroll_to_first_row_on_change,  # noqa: F401
    max_width_usage,  # noqa: F401
    fixed_columns,  # noqa: F401
    bordered,  # noqa: F401
    column_content_align,  # noqa: F401
    column_header_align,  # noqa: F401
    editable,  # noqa: F401
    editable_disabled_keys,  # noqa: F401
    nested_editable,  # noqa: F401
    listen_edit_event,  # noqa: F401
    sizes,  # noqa: F401
    group_columns,  # noqa: F401
    loading,  # noqa: F401
    row_class_name,  # noqa: F401
    dynamic_row_class_name,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '基础数据表格。',
    },
    {
        'path': 'percentage_column_width',
        'title': '百分比列宽',
        'description': '使用百分比形式控制列宽。',
        'group': '列宽控制',
    },
    {
        'path': 'numeric_column_width',
        'title': '数值型列宽',
        'description': '默认情况下，为各字段设置数值型列宽后，会自动计算转换为比例，作为各个字段的百分比列宽。',
        'group': '列宽控制',
    },
    {
        'path': 'css_column_width',
        'title': 'css控制列宽',
        'description': '基于**CSS**实现更为灵活的列宽控制。',
        'group': '列宽控制',
    },
    {
        'path': 'max_height_usage',
        'title': 'maxHeight的使用',
        'description': '设置参数`maxHeight`后，当表格实际像素高度超出`maxHeight`所设定值时，会自动渲染垂直滚动条。',
    },
    {
        'path': 'scroll_to_first_row_on_change',
        'title': 'scrollToFirstRowOnChange的使用',
        'description': '设置参数`scrollToFirstRowOnChange=False`后，翻页等操作后表格将不会自动滚回当页第一行。',
    },
    {
        'path': 'max_width_usage',
        'title': 'maxWidth的使用',
        'description': '设置参数`maxWidth`后，当表格实际像素宽度超出`maxWidth`所设定值时，会自动渲染水平滚动条。',
    },
    {
        'path': 'fixed_columns',
        'title': '冻结部分列',
        'description': '在参数`columns`中控制字段的`fixed`以实现冻结部分列的功能。',
    },
    {
        'path': 'bordered',
        'title': '添加边框线',
        'description': '设置参数`bordered=True`为表格添加边框线。',
    },
    {
        'path': 'column_content_align',
        'title': '字段内容对齐方式',
        'description': '在参数`columns`中控制字段的`align`以控制字段内容对齐方式。',
    },
    {
        'path': 'column_header_align',
        'title': '字段标题对齐方式',
        'description': '在参数`columns`中控制字段的`headerAlign`以控制字段标题对齐方式。',
    },
    {
        'path': 'editable',
        'title': '可编辑单元格',
        'description': '在参数`columns`中控制字段的`editable`以开启字段单元格可编辑功能。',
        'group': '可编辑',
    },
    {
        'path': 'editable_disabled_keys',
        'title': '禁用部分单元格不可编辑',
        'description': '为各数据记录行妥善设置唯一识别`key`后，可禁用部分单元格不可编辑。',
        'group': '可编辑',
    },
    {
        'path': 'nested_editable',
        'title': '嵌套可编辑单元格',
        'description': '为各数据记录行妥善设置唯一识别`key`后，嵌套数据结构下同样支持字段单元格可编辑功能。',
        'group': '可编辑',
    },
    {
        'path': 'listen_edit_event',
        'title': '监听单元格编辑事件',
        'description': '在回调函数中监听属性`recentlyChangedRow`、`recentlyChangedColumn`获知最近一次单元格编辑事件相关信息。',
        'group': '可编辑',
    },
    {
        'path': 'sizes',
        'title': '表格尺寸规格',
        'description': '设置参数`size`控制表格尺寸规格。',
    },
    {
        'path': 'group_columns',
        'title': '多层表头',
        'description': '在参数`columns`中控制字段的`group`以渲染具有相应多层表头的表格。',
    },
    {
        'path': 'loading',
        'title': '自带的加载中效果',
        'description': '通过参数`loading`控制是否开启表格自带的加载中效果。',
    },
    {
        'path': 'row_class_name',
        'title': '自定义行样式',
        'description': '通过参数`rowClassName`添加额外行样式。',
    },
    {
        'path': 'dynamic_row_class_name',
        'title': '动态控制自定义行样式',
        'description': '参数`rowClassName`支持基于动态`javascript`函数的行自定义css类控制。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
